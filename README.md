> **Avertissement / Disclaimer:**
> 
> **Nous ne cautionnons ni n'encourageons aucune activité malveillante** ou action illégale. Toute utilisation de ce projet à des fins non autorisées, nuisibles ou illégales est strictement interdite. Nous déclinons toute responsabilité quant aux dommages ou conséquences résultant d'un usage inapproprié.  
> Utilisez ce projet à vos propres risques.
>  
> **We do not condone or encourage any form of malicious activity** or illegal actions. Any use of this project for unauthorized, harmful, or illegal purposes is strictly prohibited. We disclaim any responsibility for damages or consequences resulting from misuse.  
> Use this project at your own risk.

# 📦 POO_ServeurC2_2025_26_Dogan-Alkin_Trichon-Anthony

## 📝 Description du projet

Ce projet est un serveur C2 (Command & Control) développé en Python, permettant de gérer plusieurs machines cibles à distance.  
L'objectif est que la machine cible déclenche le script client (`client.py`), lequel se connecte automatiquement au serveur C2.  
Depuis le serveur, il est possible de sélectionner une cible connectée et d'exécuter des commandes sur celle-ci.

## 📦 Dépendances

Comme il s'agit de scripts Python, il est absolument nécessaire d'avoir Python installé aussi bien côté client que côté serveur.  
Assurez-vous que Python (3.x recommandé) soit disponible sur toutes les machines impliquées dans le projet.

## 🗂️ Structure du projet

```
# Coté client (Logiciel à envoyer à la cible) :
client_class.py
client.py

# Coté serveur (Logiciel serveur) :
server_class.py
server.py
```

## 🚀 Comment l'utiliser ?

> **Pour qu'une machine cible se connecte au serveur, il faut exécuter le script `client.py` sur la machine cible.**
> 
> **Attention : pour que `client.py` et `server.py` fonctionnent correctement, il est nécessaire que les fichiers de classe (`client_class.py` et `server_class.py`) soient présents dans le même répertoire.**

Lorsque vous lancez le serveur avec la commande :

```bash
python server.py
```

Vous verrez apparaître le menu principal du serveur C2 :

![Menu du serveur C2](https://github.com/user-attachments/assets/52e42903-9bca-4538-857c-888e06a64c62)

**Description des options du menu :**

1. **Lister les cibles**  
   Affiche la liste des machines cibles actuellement connectées au serveur.

2. **Sélectionner une cible**  
   Permet de choisir une cible parmi celles connectées pour envoyer des commandes à distance.  
   **Pour revenir au menu principal, il suffit d'utiliser la commande** `back` dans le prompt cible.

3. **Quitter**  
   Ferme proprement le serveur C2.

## 🛠️ Fonctionnalités avancées

Le logiciel client installe automatiquement l'outil **nmap** sur la machine cible (via apt).  
Cela permet ensuite de lancer des scans réseau depuis le serveur, directement sur le réseau de la cible.  
Ainsi, vous pouvez exécuter des commandes nmap à distance pour explorer ou auditer le réseau local de la machine cible.
