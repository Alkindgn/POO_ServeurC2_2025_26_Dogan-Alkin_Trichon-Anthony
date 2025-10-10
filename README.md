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

Lorsque vous lancez le serveur avec la commande :

```bash
python server.py
```

Vous verrez apparaître le menu principal du serveur C2 :

![Menu du serveur C2](<img width="542" height="156" alt="image" src="https://github.com/user-attachments/assets/52e42903-9bca-4538-857c-888e06a64c62" />
)

**Description des options du menu :**

1. **Lister les cibles**  
   Affiche la liste des machines cibles actuellement connectées au serveur.

2. **Sélectionner une cible**  
   Permet de choisir une cible parmi celles connectées pour envoyer des commandes à distance.

3. **Quitter**  
   Ferme proprement le serveur C2.

Choisissez l'option souhaitée en entrant le numéro correspondant.

_(Ajoutez ici les étapes ou instructions complémentaires pour utiliser le projet selon vos besoins)_
