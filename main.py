import csv
file_csv='paises.csv'
def mostrar_menu(paises):
    while True:
        print("\n====== SISTEMA DE PAISES ======")
        print("1. Gestión de Países (ABM)")
        print("2. Reportes")
        print("3. Salir")
        
        try:
            opcion=int(input("Ingrese una opción: "))
        except ValueError:
            print("Error, debe ingresar un número.")
            continue
        match opcion:
            case 1:
                menu_ABM(paises)
            case 2:
                menu_reportes(paises)
            case 3:
                print("Saliendo ...")
                break
            case _:
                print("Opción inválida.")
            

def menu_ABM():
    while True:
        print("======== GESTIÓN DE PAISES ========")
        print("1. Agregar Pais")
        print("2. Buscar Pais")
        print("3. Mostrar Paises")
        print("4. Actualizar Paises")
        print("5. Eliminar Pais")
        print("6. Volver")
        
        try:
            opcion=int(input("Ingrese una opcion: "))
        except ValueError:
            print("Error, debe ingersar un número.")
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
                break
            case _:
                print("Opción inválida.")

def menu_reportes(paises):
    while True:
        print("\n------ REPORTES ------")
        print("1. Filtrar por continente")
        print("2. Filtrar por población")
        print("3. Filtrar por superficie")
        print("4. Ordenar por nombre")
        print("5. Ordenar por superficie")
        print("6. Ordenar por población")
        print("7. Estadísticas")
        print("8. Volver")
        
        try:
            opcion=int(input("Ingersa una opción: "))
        except ValueError:
            print("Error, debe ingresar un número.")
            continue
        
        match opcion:
            case 1:
                filtrar_continente()
            case 2:
                filtrar_poblacion()
            case 3:
                filtrar_superficie()
            case 4:
                ordenar_nombre()
            case 5:
                ordenar_superficie()
            case 6:
                ordenar_poblacion()
            case 7:
                estadisticas()
            case 8:
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
            if poblacion<=0:
                print("Error, debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Error, debías ingresar un numero.")

    while True:
        try:
            superficie=int(input("Ingresa la superficie: "))
            if superficie<=0:
                print("Error, valores invalidos.")
                continue
            break
        except ValueError:
            print("Error, debe ingresar un numero.")

                
    continente=input("Ingrese el continente en el que se encuentra: ").strip().title()    

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

    with open(file_csv,"a",encoding="utf-8") as archivo:
        archivo.write(f"\n{nombre},{poblacion},{superficie},{continente}\n")

def mostrar_paises(paises):
    if not paises:
        print("No hay paises cargados")
        return
    print("======== Lista de Paises ========")
    for pais in paises:
        print(f"Nombre: {pais['NombreDelPais']} - Poblacion: {pais['Poblacion']}  - Superficie: {pais['Superficie']}  - Continente: {pais['Continente']}")
        
def actualizar_pais(paises):
    print("======== Actualizar Pais ========")

    try:
        nombre = input("Ingerse el nombre: ").strip().title()
        encontrado = False

        for pais in paises:
            if pais['NombreDelPais'] == nombre:
                encontrado = True
                print("Pais encontrado. Deje en blanco si no desea modificar un campo.")

                nuevo_nombre = input("Nuevo nombre: ").strip().title()
                nueva_poblacion = input("Nueva Poblacion: ").strip()
                nueva_superficie = input("Nueva Superficie: ").strip()
                nuevo_continente = input("Nuevo Continente: ").strip().title()

                if nuevo_nombre != "":
                    pais['NombreDelPais'] = nuevo_nombre

                if nueva_poblacion != "":
                    pais['Poblacion'] = int(nueva_poblacion)

                if nueva_superficie != "":
                    pais['Superficie'] = int(nueva_superficie)

                if nuevo_continente != "":
                    pais['Continente'] = nuevo_continente

                print("Pais actualizado correctamente.")
                break

        if not encontrado:
            print("Error, el pais no existe.")
            return

        with open(file_csv, "w", encoding="utf-8") as archivo:
            archivo.write("Nombre,Poblacion,Superficie,Continente\n")
            for p in paises:
                archivo.write(f"{p['NombreDelPais']},{p['Poblacion']},{p['Superficie']},{p['Continente']}\n")

    except Exception as e:
        print(f"Error inesperado: {type(e).__name__}")

def eliminar_pais(paises):
    print("======== Eliminar Pais ========")
    nombre=input("Ingrese el nombre del pais: ").strip().title()
    encontrado=False
    for pais in paises:
        if pais['NombreDelPais']== nombre:
            paises.remove(pais)
            encontrado=True
            print("Pais eliminado correctamente.")
            break
    if not encontrado:
        print("Error, el pais no existe.")
        return
    with open(file_csv,"w",encoding="utf-8") as archivo:
        archivo.write("NombreDelPais,Poblacion,Superficie,Continente\n")
        for p in paises:
            archivo.write(f"{p['NombreDelPais']},{p['Poblacion']},{p['Superficie']},{p['Continente']}\n")

def filtrar_continente():
    # Maneja errores de tipo de dato no válido
    try:
        # Solicita al usuario ingresar un continente
        print("Ingresa el continente para filtrar los paises: ")
        # Lee la entrada del usuario y elimina espacios al inicio y al final
        continente = input().strip()
        # Guarda una copia del continente ingresado
        aux = continente
        # Elimina los espacios internos para validar que solo tenga letras
        continente = continente.replace(" ", "")
        # Repite mientras el continente contenga números o símbolos
        while not continente.isalpha():
            # Informa al usuario que el continente no puede contener números ni símbolos
            print("ERROR: El continente no puede contener números, ni simbolos")
            # Lee nuevamente la entrada del usuario
            continente = input().strip()
            # Guarda la nueva entrada en la variable auxiliar
            aux = continente
            # Elimina espacios internos para volver a validar
            continente.replace(" ", "")
        # Restaura el continente con espacios originales para comparar con el CSV
        continente = aux
        # Abre el archivo CSV en modo lectura con codificación UTF-8
        with open(file_csv, 'r', encoding='utf-8') as archivo:
            # Bandera para saber si se encontró el continente en los datos
            existencia = False
            # Lee todas las filas del CSV y las convierte en una lista de diccionarios
            filas = list(csv.DictReader(archivo))
            # Contador para saber en qué iteración del loop estamos
            i = 1
            # Recorre cada fila del archivo CSV
            for fila in filas:
                # Obtiene el continente de la fila, lo convierte a minúsculas y elimina tildes
                continente_registrado = limpieza_tildes(fila['Continente'].lower())
                # Compara el continente ingresado con el continente de la fila actual
                if (continente.lower() == continente_registrado):
                    # Imprime el nombre del país en minúsculas si coincide el continente
                    print(fila['NombreDelPais'].lower())
                    # Marca que se encontró al menos un país del continente ingresado
                    existencia = True
                # Si es la última fila y no se encontró ningún país del continente
                elif(len(filas) == i and existencia == False):
                    # Informa al usuario que el continente no existe en la base de datos
                    print("El continente ingresado no se encuentra registrado en la base de datos.")
                # Incrementa el contador de iteraciones
                i += 1
    # Captura errores de tipo de dato no válido
    except ValueError as e:
        print("ERROR: Tipo de dato no valido")
    # Captura cualquier otro error inesperado
    except:
        print("Error identificado verificar el codigo desarrollado en la funcionalidad")

def filtrar_poblacion():
    # Maneja errores de tipo de dato no válido y otros errores inesperados
    try:
        # Abre el archivo CSV en modo lectura con codificación UTF-8
        with open(file_csv, 'r', encoding='utf-8') as archivo:
            # Define una función interna para obtener la población máxima del archivo
            def obtener_max(archivo):
                # Inicializa el máximo en cero
                maximo = 0
                # Recorre cada fila del archivo
                for dato in archivo:
                    # Si la población del dato actual supera el máximo registrado, lo actualiza
                    if (maximo < int(dato['Poblacion'])):
                        maximo = int(dato['Poblacion'])
                # Devuelve el valor máximo de población encontrado
                return maximo
            # Lee todas las filas del CSV y las convierte en una lista de diccionarios
            archivo = list(csv.DictReader(archivo))
            # Obtiene la población máxima registrada en el archivo
            rango_maximo = obtener_max(archivo)
            # Solicita al usuario que establezca un rango de población
            print("Establece un rango para filtrar paises por su población")
            # Solicita el valor mínimo del rango
            print("Ingresa el minimo del rango: ")
            # Lee la entrada del usuario y elimina espacios al inicio y al final
            min = input().strip()
            # Repite mientras el valor ingresado no sea un número positivo
            while not min.isdigit():
                # Informa al usuario que solo puede ingresar números positivos o cero
                print("ERROR: Solo puedes ingresar numeros positivos o iguales a cero")
                # Lee nuevamente la entrada del usuario
                min = input().strip()
            # Convierte el mínimo a entero
            min = int(min)
            # Repite mientras el mínimo sea mayor o igual al máximo de población registrada
            while min >= rango_maximo:
                # Informa al usuario que el mínimo no puede superar o igualar el máximo registrado
                print("ERROR: El minimo ingresado no puede superar o igualar el maximo de población registrada")
                # Solicita al usuario que ingrese un número más bajo
                print("Ingresa un número mas bajo")
                # Lee nuevamente la entrada del usuario
                min = input().strip()
                # Repite mientras el valor ingresado no sea un número positivo
                while not min.isdigit():
                    # Informa al usuario que solo puede ingresar números positivos o cero
                    print("ERROR: Solo puedes ingresar numeros positivos o iguales a cero")
                    # Lee nuevamente la entrada del usuario
                    min = input().strip()
                # Convierte el mínimo a entero
                min = int(min)
            # Solicita el valor máximo del rango
            print("Ingresa el maximo del rango")
            # Lee la entrada del usuario y elimina espacios al inicio y al final
            max = input().strip()
            # Repite mientras el valor ingresado no sea un número positivo
            while not max.isdigit():
                # Informa al usuario que solo puede ingresar números positivos o cero
                print("ERROR: Solo puedes ingresar numeros positivos o iguales a cero")
                # Lee nuevamente la entrada del usuario
                max = input().strip()
            # Convierte el máximo a entero
            max = int(max)
            # Repite mientras el máximo sea igual, menor al mínimo, o mayor al máximo registrado
            while max == min or max < min or max > rango_maximo:
                # Informa al usuario que el máximo debe ser mayor y distinto al mínimo
                print("ERROR: El maximo debe ser mayor al minimo y distinto al minimo")
                # Lee nuevamente la entrada del usuario
                max = input().strip()
                # Repite mientras el valor ingresado no sea un número positivo
                while not max.isdigit():
                    # Informa al usuario que solo puede ingresar números positivos o cero
                    print("ERROR: Solo puedes ingresar numeros positivos o iguales a cero")
                    # Lee nuevamente la entrada del usuario
                    max = input().strip()
                # Convierte el máximo a entero
                max = int(max)
            # Muestra el encabezado con el rango ingresado
            print(f"PAISES SEGUN POBLACION | MIN: {min} - MAX: {max}")
            # Contador para saber en qué iteración del loop estamos
            i = 1
            # Bandera para saber si se encontró algún país dentro del rango
            filtro = False
            # Recorre cada fila del archivo CSV
            for dato in archivo:
                # Verifica si la población del país está dentro del rango ingresado
                if(int(dato['Poblacion']) >= min and int(dato['Poblacion']) <= max):
                    # Marca que se encontró al menos un país dentro del rango
                    filtro = True
                    # Muestra el nombre del país y su población
                    print(f"{dato['NombreDelPais']} | POBLACION: {int(dato['Poblacion'])} PERSONAS")
                # Si es la última fila y no se encontró ningún país dentro del rango
                if (i == len(archivo) and filtro == False):
                    # Informa al usuario que no hay países dentro del rango ingresado
                    print("No se encuentran paises dentro del rango ingresado")
                # Incrementa el contador de iteraciones
                i += 1
    # Captura errores de tipo de dato no válido
    except ValueError as e:
        print("ERROR: Tipo de dato no valido")
    # Captura cualquier otro error inesperado
    except:
        print("Error identificado verificar el codigo desarrollado en la funcionalidad")

def filtrar_superficie():
    # Maneja cualquier error inesperado
    try:
        # Abre el archivo CSV en modo lectura con codificación UTF-8
        with open(file_csv, 'r', encoding='utf-8') as archivo:
            # Lee todas las filas del CSV y las convierte en una lista de diccionarios
            filas = list(csv.DictReader(archivo))
            # Obtiene el diccionario completo de la fila con la mayor superficie
            rango_maximo = max(filas, key=lambda x: int(x['Superficie']))
            # Guarda el diccionario de la fila con mayor superficie para mostrar datos luego
            fila_maxima = rango_maximo
            # Extrae únicamente el valor numérico de la superficie máxima
            rango_maximo = int(rango_maximo['Superficie'])
            # Muestra la superficie máxima registrada
            print(rango_maximo)
            # Solicita al usuario que establezca un rango de superficie
            print("Establece un rango para filtrar paises según superficie")
            # Solicita el valor mínimo del rango
            print("Ingresa el minimo del rango: ")
            # Lee la entrada del usuario y elimina espacios al inicio y al final
            minimo = input().strip()
            # Repite mientras el valor ingresado no sea un número positivo
            while not minimo.isdigit():
                # Informa al usuario que solo puede ingresar números positivos o cero
                print("ERROR: Solo puedes ingresar numeros positivos o iguales a cero")
                # Lee nuevamente la entrada del usuario
                minimo = input().strip()
            # Convierte el mínimo a entero
            minimo = int(minimo)
            # Repite mientras el mínimo sea mayor o igual a la superficie máxima registrada
            while minimo >= rango_maximo:
                # Informa al usuario cuál es el país con mayor superficie registrada
                print(f"El pais con mayor superficie registrada es de {fila_maxima['NombreDelPais']} - {fila_maxima['Superficie']} km")
                # Solicita al usuario que ingrese un valor más bajo
                print("Vuelve a ingresar un valor")
                # Lee nuevamente la entrada del usuario
                minimo = input().strip()
                # Repite mientras el valor ingresado no sea un número positivo
                while not minimo.isdigit():
                    # Informa al usuario que solo puede ingresar números positivos o cero
                    print("ERROR: Solo puedes ingresar numeros positivos o iguales a cero")
                    # Lee nuevamente la entrada del usuario
                    minimo = input().strip()
                # Convierte el mínimo a entero
                minimo = int(minimo)
            # Solicita el valor máximo del rango
            print("Ingresa el maximo del rango: ")
            # Lee la entrada del usuario y elimina espacios al inicio y al final
            maximo = input().strip()
            # Repite mientras el valor ingresado no sea un número positivo
            while not maximo.isdigit():
                # Informa al usuario que solo puede ingresar números positivos o cero
                print("ERROR: Solo puedes ingresar numeros positivos o iguales a cero")
                # Lee nuevamente la entrada del usuario
                maximo = input().strip()
            # Convierte el máximo a entero
            maximo = int(maximo)
            # Repite mientras el máximo sea igual o menor al mínimo
            while maximo == minimo or maximo < minimo:
                # Informa al usuario que el máximo debe ser mayor y distinto al mínimo
                print("ERROR: El maximo debe ser mayor al minimo y distinto al minimo ingresado")
                # Lee nuevamente la entrada del usuario
                maximo = input().strip()
                # Repite mientras el valor ingresado no sea un número positivo
                while not maximo.isdigit():
                    # Informa al usuario que solo puede ingresar números positivos o cero
                    print("ERROR: Solo puedes ingresar numeros positivos o iguales a cero")
                    # Lee nuevamente la entrada del usuario
                    maximo = input().strip()
                # Convierte el máximo a entero
                maximo = int(maximo)
            # Muestra el encabezado con el rango ingresado
            print(f"PAISES SEGUN SUPERFICIE | MIN: {minimo} - MAX: {maximo} KM")
            # Ordena los países de mayor a menor superficie
            paises_ordenados = sorted(filas, key=lambda x: int(x['Superficie']), reverse=True)
            # Contador para numerar los países en la salida
            i = 1
            # Bandera para saber si se encontró algún país dentro del rango
            filtro = False
            # Recorre cada país ordenado por superficie
            for pais in paises_ordenados:
                # Verifica si la superficie del país está dentro del rango ingresado
                if(int(pais['Superficie']) >= minimo and int(pais['Superficie']) <= maximo):
                    # Marca que se encontró al menos un país dentro del rango
                    filtro = True
                    # Muestra el número, nombre y superficie del país
                    print(f"PAIS N°{i}: {pais['NombreDelPais']} | SUPERFICIE: {int(pais['Superficie'])} KM")
                # Si es la última fila y no se encontró ningún país dentro del rango
                if (i == len(paises_ordenados) and filtro == False):
                    # Informa al usuario que no hay países dentro del rango ingresado
                    print("No se encuentran paises dentro del rango ingresado")
                # Incrementa el contador de iteraciones
                i += 1
    # Captura cualquier error inesperado
    except:
        print("Error encontrado verifica el desarrollo del codigo")

def ordenar_nombre():
    # Maneja cualquier error inesperado
    try:
        # Abre el archivo CSV en modo lectura con codificación UTF-8
        with open(file_csv, 'r', encoding='utf-8') as archivo:
            # Lee todas las filas del CSV y las convierte en una lista de diccionarios
            archivo = list(csv.DictReader(archivo))
            # Inicializa la lista donde se almacenarán los nombres de los países
            nombres = []
            # Recorre cada elemento del archivo
            for elemento in archivo:
                # Muestra el nombre original del país
                print(elemento['NombreDelPais'])
                # Elimina las tildes del nombre para poder ordenarlo correctamente
                nombre = validacion_tildes(elemento['NombreDelPais'])
                # Muestra el nombre sin tildes
                print(nombre)
                # Agrega el nombre sin tildes a la lista
                nombres.append(nombre)
            # Ordena la lista de nombres alfabéticamente
            nombres = sorted(nombres)
            # Muestra el encabezado de la lista ordenada
            print("NOMBRES DE PAISES ORDENADOS ALFABETICAMENTE: ")
            # Recorre cada nombre ordenado
            for nombre in nombres:
                # Muestra el nombre del país
                print(f"PAIS: {nombre}")
    # Captura cualquier error inesperado
    except:
        print("Error identificado verificar el codigo desarrollado en la funcionalidad")

def ordenar_superficie():
    # Maneja cualquier error inesperado
    try:
        # Solicita al usuario el criterio de ordenamiento
        print("Ingresa el criterio por el cual quieras ordenar las superficies")
        # Muestra la opción para ordenar de menor a mayor
        print("A - Menor a Mayor")
        # Muestra la opción para ordenar de mayor a menor
        print("B - Mayor a Menor")
        # Lee la entrada del usuario, elimina espacios y convierte a minúsculas
        eleccion = input().strip().lower()
        # Repite mientras la elección no sea 'a' o 'b'
        while not eleccion.isalpha() or (eleccion != 'a' and eleccion != 'b'):
            # Informa al usuario que solo puede ingresar 'A' o 'B'
            print("Solo debes ingresar 'A' o 'B' como eleccion")
            # Lee nuevamente la entrada del usuario
            eleccion = input().strip().lower()
        # Abre el archivo CSV en modo lectura con codificación UTF-8
        with open(file_csv, 'r', encoding='utf-8') as archivo:
            # Lee todas las filas del CSV y las convierte en una lista de diccionarios
            filas = list(csv.DictReader(archivo))
            # Si el usuario eligió ordenar de menor a mayor
            if (eleccion == 'a'):
                # Ordena las filas por superficie de menor a mayor
                filas_ordenadas = sorted(filas, key=lambda x: int(x['Superficie']))
            # Si el usuario eligió ordenar de mayor a menor
            elif (eleccion == 'b'):
                # Ordena las filas por superficie de mayor a menor
                filas_ordenadas = sorted(filas, key=lambda x: int(x['Superficie']), reverse=True)
            # Recorre cada fila ordenada
            for fila in filas_ordenadas:
                # Muestra el nombre del país y su superficie
                print(f"PAIS: {fila['NombreDelPais']} | SUPERFICIE: {fila['Superficie']} km")
    # Captura cualquier error inesperado
    except:
        print("Error identificado verificar el codigo desarrollado en la funcionalidad")

def ordenar_poblacion():
    # Maneja cualquier error inesperado
    try:
        # Abre el archivo CSV en modo lectura con codificación UTF-8
        with open(file_csv, 'r', encoding='utf-8') as archivo:
            # Lee todas las filas del CSV y las convierte en una lista de diccionarios
            filas = list(csv.DictReader(archivo))
            # Ordena las filas por población de menor a mayor
            filas_ordenadas = sorted(filas, key=lambda x: int(x['Poblacion']))
            # Recorre cada fila ordenada
            for fila in filas_ordenadas:
                # Muestra el nombre del país y su población
                print(f"PAIS: {fila['NombreDelPais']} | POBLACIÓN: {fila['Poblacion']} personas")
    # Captura cualquier error inesperado
    except:
        print("Error identificado verifica el codigo desarrollado")

def estadisticas():
    # Maneja cualquier error inesperado
    try:
        # Abre el archivo CSV en modo lectura con codificación UTF-8
        with open(file_csv, 'r', encoding='utf-8') as archivo:
            # Define una función interna para sumar la población total de todos los países
            def promedio_poblacion(lista):
                # Inicializa el acumulador en cero
                promedio = 0
                # Recorre cada dato de la lista
                for dato in lista:
                    # Suma la población de cada país al acumulador
                    promedio = promedio + int(dato['Poblacion'])
                # Devuelve la suma total de la población
                return promedio
            # Define una función interna para sumar la superficie total de todos los países
            def promedio_superficie(lista):
                # Inicializa el acumulador en cero
                promedio = 0
                # Recorre cada dato de la lista
                for dato in lista:
                    # Suma la superficie de cada país al acumulador
                    promedio = promedio + int(dato['Superficie'])
                # Devuelve la suma total de la superficie
                return promedio
            # Define una función interna para obtener una lista de continentes sin repetidos
            def registro_continentes(lista):
                # Inicializa la lista de continentes vacía
                continentes = []
                # Recorre cada dato de la lista
                for dato in lista:
                    # Si el continente del dato no está en la lista, lo agrega
                    if (dato['Continente'] not in continentes):
                        continentes.append(dato['Continente'])
                # Devuelve la lista de continentes únicos
                return continentes
            # Define una función interna para contar cuántos países hay por continente
            def contar_paises(lista, continentes):
                # Recorre cada continente registrado
                for continente in continentes:
                    # Inicializa el contador de países para este continente
                    i = 0
                    # Recorre cada dato de la lista
                    for dato in lista:
                        # Si el país pertenece al continente actual, incrementa el contador
                        if (continente == dato['Continente']):
                            i += 1
                    # Muestra el nombre del continente y la cantidad de países
                    print(f"{continente.upper()} - {i} paises")
            # Lee todas las filas del CSV y las convierte en una lista de diccionarios
            filas = list(csv.DictReader(archivo))
            # Obtiene el diccionario completo del país con mayor población
            fila_maxima = max(filas, key=lambda x: int(x['Poblacion']))
            # Muestra separador visual
            print("------------------------------------------------------------------------------------------------------------")
            # Muestra el país con mayor población y su valor
            print(f"PAIS CON MAYOR POBLACION: {fila_maxima['NombreDelPais']} | {fila_maxima['Poblacion']} personas")
            # Obtiene el diccionario completo del país con menor población
            fila_minima = min(filas, key=lambda x: int(x['Poblacion']))
            # Muestra el país con menor población y su valor
            print(f"PAIS CON MENOR POBLACION: {fila_minima['NombreDelPais']} | {fila_minima['Poblacion']} personas")
            # Muestra separador visual
            print("------------------------------------------------------------------------------------------------------------")
            # Calcula la suma total de la población de todos los países
            p_promedio = promedio_poblacion(filas)
            # Muestra la suma total de población
            print(f"El promedio de la población entre los paises registrados es de: {p_promedio} personas")
            # Muestra separador visual
            print("------------------------------------------------------------------------------------------------------------")
            # Calcula la suma total de la superficie de todos los países
            s_promedio = promedio_superficie(filas)
            # Muestra la suma total de superficie
            print(f"El promedio de superficie de los paises registrados es de: {s_promedio} KM")
            # Muestra separador visual
            print("------------------------------------------------------------------------------------------------------------")
            # Muestra el encabezado de la sección de países por continente
            print("CANTIDAD DE PAISES POR CONTINENTE:")
            # Obtiene la lista de continentes únicos registrados
            continentes = registro_continentes(filas)
            # Muestra la cantidad de países por cada continente
            contar_paises(filas, continentes)
    # Captura cualquier error inesperado
    except:
        print("Se presento un error, verifica el desarrollo del código")

def limpieza_tildes(texto):
        # Maneja el caso en que una letra no pueda codificarse en ASCII (tiene tilde)
        try:
            # Obtiene el valor decimal del carácter 'a'
            a = ord('a')
            # Obtiene el valor decimal del carácter 'e'
            b = ord('e')
            # Obtiene el valor decimal del carácter 'i'
            c = ord('i')
            # Obtiene el valor decimal del carácter 'o'
            d = ord('o')
            # Obtiene el valor decimal del carácter 'u'
            e = ord('u')
            # Crea una lista con los valores decimales de las vocales sin tilde
            UNICODE_VOCALES = [a, b, c, d, e]
            # Inicializa la lista donde se almacenarán las letras del texto
            letras = []
            # Inicializa la variable que guardará la letra con tilde detectada
            letra_tilde = ""
            # Recorre cada letra del texto
            for letra in texto:
                # Agrega cada letra a la lista
                letras.append(letra)
            # Recorre cada letra de la lista
            for letra in letras:
                # Guarda la letra actual como posible letra con tilde
                letra_tilde = letra
                # Intenta codificar la letra en ASCII para detectar si tiene tilde
                decimal = letra.encode("ascii")
            # Si todas las letras pudieron codificarse en ASCII, devuelve el texto sin cambios
            return texto
        # Si una letra no puede codificarse en ASCII, es porque tiene tilde
        except UnicodeEncodeError as e:
            # Obtiene el valor Unicode de la letra con tilde detectada
            unicode_tilde = ord(letra_tilde)
            # Recorre cada vocal sin tilde para identificar cuál es la versión sin tilde
            for unicode in UNICODE_VOCALES:
                # Suma el valor Unicode de la vocal y el de la letra con tilde
                suma = unicode + unicode_tilde
                # Verifica si la letra con tilde corresponde a la 'á'
                if (suma == 322 and unicode == 47):
                    # Asigna 'a' como reemplazo
                    letra = 'a'
                    # Reemplaza la letra con tilde por la vocal sin tilde en el texto
                    texto = texto.replace(letra_tilde, letra)
                    # Devuelve el texto con la tilde eliminada
                    return texto
                # Verifica si la letra con tilde corresponde a la 'é'
                elif (suma == 334 and unicode == 101):
                    # Asigna 'e' como reemplazo
                    letra = 'e'
                    # Reemplaza la letra con tilde por la vocal sin tilde en el texto
                    texto = texto.replace(letra_tilde, letra)
                    # Devuelve el texto con la tilde eliminada
                    return texto
                # Verifica si la letra con tilde corresponde a la 'í'
                elif (suma == 342 and unicode == 105):
                    # Asigna 'i' como reemplazo
                    letra = 'i'
                    # Reemplaza la letra con tilde por la vocal sin tilde en el texto
                    texto = texto.replace(letra_tilde, letra)
                    # Devuelve el texto con la tilde eliminada
                    return texto
                # Verifica si la letra con tilde corresponde a la 'ó'
                elif (suma == 354 and unicode == 111):
                    # Asigna 'o' como reemplazo
                    letra = 'o'
                    # Reemplaza la letra con tilde por la vocal sin tilde en el texto
                    texto = texto.replace(letra_tilde, letra)
                    # Devuelve el texto con la tilde eliminada
                    return texto
                # Verifica si la letra con tilde corresponde a la 'ú'
                elif (suma == 367 and unicode == 117):
                    # Asigna 'u' como reemplazo
                    letra = 'u'
                    # Reemplaza la letra con tilde por la vocal sin tilde en el texto
                    texto = texto.replace(letra_tilde, letra)
                    # Devuelve el texto con la tilde eliminada
                    return texto
                

#Principal
paises = cargar_csv("paises.csv")

mostrar_menu(paises)



