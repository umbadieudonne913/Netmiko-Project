<<<<<<< HEAD:README
# Projet DevNet – Automatisation réseau avec Netmiko

## 👤 Auteurs
* **Travail réalisé par** : Dieudonné UMBA  et Sharon-rose MUKUNDI 
* **Filière** : DevOps et Sécurité informatique
* **Promotion** : Master 2
* **Année académique** : 2025 – 2026
  
## Description
Ce projet DevNet consiste à développer un programme en **Python** permettant de se connecter à un **routeur Cisco** via **SSH**, en utilisant la librairie **Netmiko**, afin d’exécuter des commandes réseau et d’afficher automatiquement des informations importantes sur le routeur.

Le projet est réalisé dans un cadre **académique et pédagogique**, pour introduire les concepts de base de l’**automatisation réseau** et du **NetDevOps**.

---
## 🧰 Technologies utilisées
- **Python 3**
- **Netmiko**
- **Tabulate**
- **Cisco IOS XR**
- **Cisco DevNet Sandbox**
- **SSH**
---
## 🖧 Environnement réseau
- Équipement : Routeur Cisco
- Système : IOS XR
- Accès : Cisco DevNet Sandbox
- Méthode de connexion : SSH
---
## 📂 Structure du projet
```text
Netmiko-Project/
│
├── devnet_netmiko_router.py   # Script Python principal (Netmiko)
├── screenshots/              # Captures d’écran des résultats d’exécution
│   └── *.png
├── README.md                 # Documentation du projet
```
--- 
## Test
Le programme permet de :

1. Afficher le **nom du routeur**, la **version du système d’exploitation (OS)** et le **modèle du routeur**  
   ➜ Commandes utilisées :  
   - `show running-config`  
   - `show version`
➜ Voici le resultat :
![Texte alternatif](screenshots/router_Info_ok.png) 
---

2. Afficher la **liste des interfaces actives (UP)**  
   ➜ Commande : `show ip interface brief`
➜ Voici le resultat :
![Texte alternatif](screenshots/interfaces_up_down_ok.png) 
---

3. Afficher la **liste des interfaces inactives (DOWN)**  
   ➜ Commande : `show ip interface brief`
➜ Voici le resultat : 
![Texte alternatif](screenshots/interfaces_up_down_ok.png) 
---

4. Afficher le **nombre d’interfaces FastEthernet** et **GigabitEthernet**  
   ➜ Commande : `show ip interface brief`
➜ Voici le resultat :
![Texte alternatif](screenshots/statistiques_Interfaces_ok.png) 
---

5. Afficher la **liste des réseaux accessibles via le routeur**  
   ➜ Commande : `show ip route`
   ➜ Voici le resultat :
![Texte alternatif](screenshots/table_routage_ok.png) 
---
## Conclusion



