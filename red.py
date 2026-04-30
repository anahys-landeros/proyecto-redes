import os

def limpiar():
    os.system('clear' if os.name == 'posix' else 'cls')

def menu():
    campus = ["zona core", "campus uno", "campus matriz", "sector outsourcing"]
    while True:
        limpiar()
        print("--- GESTION DE REDES AVANZADAS I ---")
        print("1. Ver dispositivos (Leer Archivo)")
        print("2. Registrar nuevo dispositivo")
        print("3. Salir")
        
        opt = input("\nSeleccione una opcion: ")
        
        if opt == "1":
            limpiar()
            for i, c in enumerate(campus, 1): print(f"{i}. {c}")
            sel = int(input("\nVer campus numero: ")) - 1
            archivo = campus[sel] + ".txt"
            limpiar()
            if os.path.exists(archivo):
                with open(archivo, "r") as f: print(f.read())
            else:
                print("Archivo vacio.")
            input("\nPresione Enter para volver...")
            
        elif opt == "2":
            limpiar()
            for i, c in enumerate(campus, 1): print(f"{i}. {c}")
            sel = int(input("\nAsignar a campus numero: ")) - 1
            archivo = campus[sel] + ".txt"
            
            print(f"\n--- Registro en {campus[sel]} ---")
            nombre = input("Nombre Equipo: ")
            ip = input("Direccion IP: ")
            vlan = input("VLAN: ")
            
            print("\nCapas: 1. Core | 2. Distribucion | 3. Acceso")
            capa_opt = input("Capa: ")
            capas = {"1":"Core", "2":"Distribucion", "3":"Acceso"}
            capa = capas.get(capa_opt, "Acceso")

            with open(archivo, "a") as f:
                f.write(f"\nEquipo: {nombre} | IP: {ip} | VLAN: {vlan} | Capa: {capa}\n")
                f.write("-" * 30 + "\n")
            print("\n¡Guardado con exito!")
            input("\nPresione Enter...")
            
        elif opt == "3":
            break

if __name__ == "__main__":
    menu()

