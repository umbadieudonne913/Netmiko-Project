from netmiko import ConnectHandler
from tabulate import tabulate

# Paramètres de connexion (remplace par tes credentials Quick Access)
cisco1 = {
    "device_type": "cisco_xr",   # type correct pour IOS XR
    "host": "sandbox-iosxr-1.cisco.com",
    "username": "20uk550",       # ton username
    "password": "Q9r-OL6mb8_hI9",# ton password
    "port": 22,
}

def main():
    print("\n" + "="*70)
    print("   PROJET DEVNET - AUTOMATISATION NETMIKO ")
    print("="*70 + "\n")

    # Connexion au routeur
    net_connect = ConnectHandler(**cisco1)

    # 1. Infos du routeur
    print("[1] Informations du routeur (Nom, OS, Modèle)\n")
    version_info = net_connect.send_command("show version")
    print(version_info)
    print("\n" + "-"*70 + "\n")

    # 2 & 3. Interfaces UP/DOWN
    print("[2] Interfaces UP / [3] Interfaces DOWN\n")
    interfaces = net_connect.send_command("show ip interface brief")

    up_list, down_list = [], []

    for line in interfaces.splitlines():
        if line.startswith("Interface") or line.strip() == "":
            continue  # ignorer l'entête
        parts = line.split()
        if len(parts) >= 5:
            iface, ip, status, protocol, vrf = parts[0], parts[1], parts[2], parts[3], parts[4]
            if status.lower() == "up" and protocol.lower() == "up":
                up_list.append([iface, ip, status, protocol, vrf])
            else:
                down_list.append([iface, ip, status, protocol, vrf])

    print("Interfaces UP")
    print(tabulate(up_list, headers=["Interface", "IP-Address", "Status", "Protocol", "VRF"]))
    print("\n Interfaces DOWN")
    print(tabulate(down_list, headers=["Interface", "IP-Address", "Status", "Protocol", "VRF"]))
    print("\n" + "-"*70 + "\n")

    # 4. Nombre d’interfaces FastEthernet et GigabitEthernet
    fast_count = sum(1 for line in interfaces.splitlines() if "FastEthernet" in line)
    gig_count = sum(1 for line in interfaces.splitlines() if "GigabitEthernet" in line)

    print("[4] Statistiques des interfaces")
    print(f" Nombre d'interfaces FastEthernet : {fast_count}")
    print(f" Nombre d'interfaces GigabitEthernet : {gig_count}")
    print("\n" + "-"*70 + "\n")

    # 5. Table de routage
    print("[5] Table de routage (show ip route)\n")
    routes = net_connect.send_command("show ip route")
    print(routes)
    print("\n" + "="*70)
    print("Fin du rapport Netmiko - Projet DevNet")
    print("="*70 + "\n")

    # Déconnexion
    net_connect.disconnect()

if __name__ == "__main__":
    main()
