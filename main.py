import csv
def mostrar_menu():
    while True:
        print("====== Menu =====")
        print("1. Agregar Pais")
        print("2. Buscar Pais")
        print("3. Mostrar Paises")
        print("4. Actualizar Paises")
        print("5. Eliminar Pais")
        print("6. Salir")

        try:
            opcion=int(input("Ingrese una opcion: "))
        except ValueError:
            print("Error, debe ingresar un numero.")
            continue
        match opcion:
            case 1:
                agregar_pais(paises)
            case 2:
               
                buscar_pais(paises)
            case 3:
                mostrar_paises(paises)
            case 4:
                actualizar_pais(paises)
            case 5:
                eliminar_pais(paises)
            case 6:
                print("Saliendo...")
                break
            case _:
                print("Opción inválida.")

def cargar_csv(nombre_archivo):
    paises=[]

    with open(nombre_archivo,"r", encoding="utf-8") as archivo:
        lector=csv.reader(archivo, delimiter=",")

        encabezado=next(lector)

        for linea in lector:

            if len(linea)!=4:
                continue

            nombre, poblacion, superficie, continente = linea
            

            pais={
                "NombreDelPais": nombre,
                "Poblacion": int(poblacion),
                "Superficie": int(superficie),
                "Continente": continente
            }
            paises.append(pais)
    return paises

def mostrar_paises(paises):
    if len(paises)==0:
        print("No se han cargado paises.")
        return
    for p in paises:
        print(f"Nombre: {p['NombreDelPais']} - Poblacion: {p['Poblacion']} - Superficie: {p['Superficie']} - Continente: {p['Continente']}")
        
def buscar_pais(paises):
    print("======== Buscar Pais ========")
    nombre=input("Ingrese el nombre: ").strip().title()

    encontrado=False

    for pais in paises:
        if pais["NombreDelPais"]==nombre:
            print(f"Pais encontrado:")
            print(f"Nombre: {pais['NombreDelPais']} - Poblacion: {pais['Poblacion']} - Superficie: {pais['Superficie']} - Continente: {pais['Continente']}")
            encontrado=True
            break

    if not encontrado:
        print("Error, el pais no ha sido ingresado.")
        
def agregar_pais(paises):

    
    nombre=input("Ingresa el nombre del pais: ").strip().title()
    while not nombre.replace(" ","").isalpha():
        print("Error. Solo se permiten letras")
        nombre=input("Ingresa el nombre del pais: ").strip().title()

    for pais in paises:
        if pais["NombreDelPais"]==nombre:
            print(f"El pais ya existe")
            return
        
    while True:
        try:
            poblacion=int(input("Ingresa la poblacion: "))
            if poblacion <= 0:
                print("Error, debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Error, debías ingresar un numero.")

    while True:
        try:
            superficie=int(input("Ingresa la superficie: "))
            if superficie<=0:
                print("Error, debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Error, debías ingresar un numero.")

    

    continente=input("Ingrese el continente en el que se encuentra: ").strip().title()    

    while not continente.replace(" ","").isalpha():
        print("Error. Solo se permiten letras.")
        continente=input("Ingrese el continente en el que se encuentra: ").strip().title()     
            
    pais={
            "NombreDelPais":nombre,
            "Poblacion": poblacion,
            "Superficie": superficie,
            "Continente": continente
        }
    paises.append(pais)
    print("Pais agregado correctamente.")

    with open("paises.csv","a",encoding="utf-8") as archivo:
        archivo.write(f"{nombre},{poblacion},{superficie},{continente}\n")

def actualizar_pais(paises):
    print("======== Actualizar Pais ========")
    nombre=input("Ingrese el nombre del pais: ").strip().title()

    encontrado=False

    for pais in paises:
        if pais["NombreDelPais"]==nombre:
            while True:
                try:
                    nuevo_pob=int(input("Nueva poblacion: "))
                    if nuevo_pob <=0:
                        print("Error, el numero debe ser mayor a 0.")
                        continue
                    break

                except ValueError:
                    print("Error, debe ingresar unicamente números.")
            
            
                
            while True:

                try:
                    nuevo_sup=int(input("Nueva Superficie: "))
                    if nuevo_sup<=0:
                        print("Error, el numero debe ser mayor a 0.")
                        continue
                    break
                    
                except ValueError:
                    print("Error, debe ingresar numeros unicamente.")
            
            while True:
                nuevo_cont=input("Nuevo Continente: ").strip().title()
                if nuevo_cont.replace(" ","").isalpha():
                    break
                else:
                    print("Error, solo se permiten letras.")


            pais["Poblacion"]=nuevo_pob
            pais["Superficie"]=nuevo_sup
            pais["Continente"]=nuevo_cont

            print("Pais actualizado correctamente.")

                
                    
            encontrado=True
            break
    if not encontrado:
            print("Pais no encontrado.")
            return

    with open("paises.csv","w", encoding="utf-8") as archivo:
        archivo.write("NombreDelPais, Poblacion, Superficie, Continente\n")

        for p in paises:
            archivo.write(f"{p['NombreDelPais']},{p['Poblacion']},{p['Superficie']},{p['Continente']}\n")

def eliminar_pais(paises):

    print("======== Eliminar Pais ========")
    nombre=input("Ingrese el nombre: ").strip().title()
    encontrado=False

    for pais in paises:
        if pais["NombreDelPais"] == nombre:
            paises.remove(pais)
            encontrado=True
            break
    if not encontrado:
        print("Pais no encontrado.")
        return
    with open("paises.csv","w",encoding="utf-8") as archivo:
        archivo.write("NombreDelPais,Poblacion,Superficie,Continente\n")

        for p in paises:
            archivo.write(f"{p['NombreDelPais']},{p['Poblacion']},{p['Superficie']},{p['Continente']}\n")
    print("Pais eliminado correctamente.")        

#Principal
paises = cargar_csv("paises.csv")
#n=input("Ingrese una opcion: ")
mostrar_menu()
