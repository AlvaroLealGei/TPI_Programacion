import csv

# Punto de entrada principal del programa (no se usa funcionalmente)
def main():
    print("Hola mundo")

# Solo ejecuta main() si el script se corre directamente, no si se importa
if __name__ == "__main__":
    main()

# Nombre del archivo CSV que contiene los datos de países
ARCHIVO = 'paises.csv'


def filtrar_continente():
    # Función anidada que recibe un texto y elimina tildes de vocales
    def validacion_tildes(texto):
        # Intenta codificar cada letra en ASCII para detectar tildes
        try:
            # Obtiene el code point Unicode de cada vocal sin tilde
            a = ord('a')
            b = ord('e')
            c = ord('i')
            d = ord('o')
            e = ord('u')
            # Lista con los code points de las vocales sin tilde
            UNICODE_VOCALES = [a, b, c, d, e]
            # Lista auxiliar para almacenar cada carácter del texto
            letras = []
            # Variable que guarda la última letra procesada antes del error
            letra_tilde = ""
            # Recorre el texto y agrega cada carácter a la lista
            for letra in texto:
                letras.append(letra)
            # Itera la lista de letras intentando codificar cada una en ASCII
            for letra in letras:
                # Guarda la letra actual por si falla el encode en la siguiente línea
                letra_tilde = letra
                # Intenta convertir la letra a bytes ASCII; falla si tiene tilde
                decimal = letra.encode("ascii")
            # Si ninguna letra falló, retorna el texto original sin modificaciones
            return texto
        # Captura el error cuando una letra no puede codificarse en ASCII (tiene tilde)
        except UnicodeEncodeError as e:
            # Obtiene el code point Unicode de la letra con tilde
            unicode_tilde = ord(letra_tilde)
            # Recorre los code points de las vocales sin tilde para identificar cuál corresponde
            for unicode in UNICODE_VOCALES:
                # Suma el code point de la vocal sin tilde con el de la vocal con tilde
                suma = unicode + unicode_tilde
                # Si la suma corresponde a 'a' + 'á', reemplaza la tilde y retorna
                if (suma == 322):
                    letra = 'a'
                    texto = texto.replace(letra_tilde, letra)
                    return texto
                # Si la suma corresponde a 'e' + 'é', reemplaza la tilde y retorna
                elif (suma == 334):
                    letra = 'e'
                    texto = texto.replace(letra_tilde, letra)
                    return texto
                # Si la suma corresponde a 'i' + 'í', reemplaza la tilde y retorna
                elif (suma == 342):
                    letra = 'i'
                    texto = texto.replace(letra_tilde, letra)
                    return texto
                # Si la suma corresponde a 'o' + 'ó', reemplaza la tilde y retorna
                elif (suma == 354):
                    letra = 'o'
                    texto = texto.replace(letra_tilde, letra)
                    return texto
                # Si la suma corresponde a 'u' + 'ú', reemplaza la tilde y retorna
                elif (suma == 367):
                    letra = 'u'
                    texto = texto.replace(letra_tilde, letra)
                    return texto

    # Solicita al usuario que ingrese el nombre del continente
    print("Ingresa el continente para filtrar los paises: ")
    # Lee el input del usuario y elimina espacios al inicio y al final
    continente = input().strip()
    # Guarda una copia del input original con espacios para usar luego
    aux = continente
    # Elimina los espacios internos para validar que solo contenga letras
    continente = continente.replace(" ", "")
    # Repite la solicitud mientras el input contenga números o símbolos
    while not continente.isalpha():
        print("ERROR: El continente no puede contener números, ni simbolos")
        # Vuelve a leer el input del usuario
        continente = input().strip()
        # Guarda la copia del nuevo input
        aux = continente
        # Intenta eliminar espacios pero no reasigna, por lo que no tiene efecto
        continente.replace(" ", "")
    # Restaura el valor con espacios para usar el nombre completo del continente
    continente = aux
    # Aplica la función de validación para eliminar tildes del continente ingresado
    continente = validacion_tildes(continente)
    # Abre el archivo CSV en modo lectura con codificación UTF-8
    with open(ARCHIVO, 'r', encoding='utf-8') as archivo:
        # Bandera para saber si se encontró al menos un país del continente
        existencia = False
        # Lee todas las filas del CSV como lista de diccionarios
        reader = list(csv.DictReader(archivo))
        # Contador para saber en qué posición de la lista se está iterando
        i = 1
        # Recorre cada fila del archivo
        for fila in reader:
            # Obtiene el continente del registro actual en minúsculas y sin tildes
            continente_registrado = validacion_tildes(fila['Continente'].lower())
            # Compara el continente ingresado con el del registro actual
            if (continente.lower() == continente_registrado):
                # Si coinciden, imprime el nombre del país en minúsculas
                print(fila['NombreDelPais'].lower())
                # Marca que se encontró al menos un resultado
                existencia = True
            # Si es la última fila y no se encontró ningún país, informa al usuario
            elif(len(reader) == i and existencia == False):
                print("El pais ingresado no se encuentra registrado en la base de datos.")
            # Incrementa el contador de posición
            i += 1

# Llama a la función principal para ejecutar el programa
filtrar_continente()


