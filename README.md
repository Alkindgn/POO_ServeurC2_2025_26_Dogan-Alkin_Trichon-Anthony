# POO_ServeurC2_2025_26_Dogan-Alkin_Trichon-Anthony

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
