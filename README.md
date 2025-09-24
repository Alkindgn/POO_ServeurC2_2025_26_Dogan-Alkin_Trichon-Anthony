# POO_ServeurC2_2025_26_Dogan-Alkin_Trichon-Anthony

# Disclaimer

This project is intended solely for educational purposes. It is designed to help users learn about cybersecurity, programming, and related topics. By using this software, you agree to do so within the confines of the law and with full responsibility for your actions.

<div style="color:red">**We do not condone or encourage any form of malicious activity** or illegal actions. Any use of this project for unauthorized, harmful, or illegal purposes is strictly prohibited. We disclaim any responsibility for damages or consequences resulting from misuse.</div>

Use this project at your own risk.



Le code illustre des concepts : connexion réseau, réception/traitement de commandes, gestion du répertoire courant, tentative d’installation d’un paquet (nmap)

Prérequis
Une machine de laboratoire isolée (VM ou réseau fermé).
Python 3.x installé


Comportement attendu (haut-niveau)

Le client tente de se connecter à un serveur d’écoute configuré.
Il accepte des commandes simples depuis le serveur — uniquement à des fins de démonstration dans un labo.
Il conserve un cwd persistant pour l’exécution des commandes.
Il contient une routine d’installation de nmap (adaptée à Debian/Ubuntu) 


Détection (pour les défenseurs)
Si vous souhaitez vous entraîner à détecter ce type d’activité dans un cadre défensif :
Surveiller les connexions réseau sortantes inhabituelles (ports non standards, IPs externes).
Rechercher les processus Python persistants exécutant des connexions réseau.
Vérifier les logs sudo et apt pour installations inattendues.
Utiliser des EDR/IDS dans les environnements de production.
