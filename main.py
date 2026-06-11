import csv

def main():
    print("Hola mundo")

if __name__ == "__main__":
    main()

ARCHIVO = 'paises.csv'


def filtrar_continente():
    def validacion_tildes(texto):
        try:
            a = ord('a')
            b = ord('e')
            c = ord('i')
            d = ord('o')
            e = ord('u') 
            UNICODE_VOCALES = [a, b, c, d, e]
            letras = []
            letra_tilde = ""
            for letra in texto:
                letras.append(letra)
            for letra in letras:
                letra_tilde = letra
                decimal = letra.encode("ascii")
            return texto
        except UnicodeEncodeError as e:
            unicode_tilde = ord(letra_tilde)
            for unicode in UNICODE_VOCALES:
                suma = unicode + unicode_tilde
                if (suma == 322):
                    letra = 'a'
                    texto = texto.replace(letra_tilde, letra)
                    return texto
                elif (suma == 334):
                    letra = 'e'
                    texto = texto.replace(letra_tilde, letra)
                    return texto
                elif (suma == 342):
                    letra = 'i'
                    texto = texto.replace(letra_tilde, letra)
                    return texto
                elif (suma == 354):
                    letra = 'o'
                    texto = texto.replace(letra_tilde, letra)
                    return texto
                elif (suma == 367):
                    letra = 'u'
                    texto = texto.replace(letra_tilde, letra)
                    return texto
    print("Ingresa el continente para filtrar los paises: ")
    continente = input().strip()
    aux = continente
    continente = continente.replace(" ", "")
    while not continente.isalpha():
        print("ERROR: El continente no puede contener números, ni simbolos")
        continente = input().strip()
        aux = continente
        continente.replace(" ", "")
    continente = aux
    continente = validacion_tildes(continente)
    with open(ARCHIVO, 'r', encoding='utf-8') as archivo:
        existencia = False
        reader = list(csv.DictReader(archivo))
        i = 1
        for fila in reader:
            continente_registrado = validacion_tildes(fila['Continente'].lower())
            if (continente.lower() == continente_registrado):
                print(fila['NombreDelPais'].lower())
                existencia = True
            elif(len(reader) == i and existencia == False):
                print("El continente ingresado no se encuentra registrado en la base de datos.")
            i += 1

filtrar_continente()
        





