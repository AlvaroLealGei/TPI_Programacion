import csv

def cargar_csv(nombre_archivo):
    paises=[]

    with open(nombre_archivo,"r", encoding="utf-8") as archivo:
        lector=csv.reader(archivo, delimiter=",")

        encabezado=next(lector)

        for linea in lector:
            nombre, poblacion, superficie, continente = linea

            pais={
                "NombreDelPais": nombre,
                "Poblacion": int(poblacion),
                "Superficie": int(superficie),
                "Continente": continente
            }
            paises.append(pais)
    return paises
        
def buscar_pais(paises, nombre):
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
        
    try:
        poblacion=int(input("Ingresa la poblacion: "))
        superficie=int(input("Ingresa la superficie: "))
    except ValueError:
        print("Error, debías ingresar un numero.")
        return

    if poblacion<=0 or superficie<=0:
        print("Error, valores invalidos.")
        return

    continente=input("Ingrese el continente en el que se encuentra: ")      

    while not continente.replace(" ","").isalpha():
        print("Error. Solo se permiten letras.")
        continente=input("Ingrese el continente en el que se encuentra: ")      
            
    pais={
            "NombreDelPais":nombre,
            "Poblacion": poblacion,
            "Superficie": superficie,
            "Continente": continente
        }
    paises.append(pais)

    with open("paises.csv","a",encoding="utf-8") as archivo:
        archivo.write(f"\n{nombre},{poblacion},{superficie},{continente}\n")

def actualizar_pais(paises,nombre):

    encontrado=False

    for pais in paises:
        if pais["NombreDelPais"]==nombre:
            try:
                nuevo_pob=int(input("Nueva poblacion: "))
                nuevo_sup=int(input("Nueva Superficie: "))
                if nuevo_pob <=0 or nuevo_sup<=0:
                    print("Error, el numero debe ser mayor a 0.")
                    return
            except ValueError:
                print("Error, debe ingresar numeros unicamente.")
                return
            pais["Poblacion"]=nuevo_pob
            pais["Superficie"]=nuevo_sup
                
            encontrado=True
            break
    if not encontrado:
            print("Pais no encontrado.")
            return

    with open("paises.csv","w", encoding="utf-8") as archivo:
        archivo.write("NombreDelPais, Poblacion, Superficie, Continente\n")

        for p in paises:
            archivo.write(f"{p['NombreDelPais']},{p['Poblacion']},{p['Superficie']},{p['Continente']}\n")

def eliminar_pais(paises, nombre):
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

