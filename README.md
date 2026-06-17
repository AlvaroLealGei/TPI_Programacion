🌍 Sistema de Gestion de Paises



Sistema de consola desarrollado en Python que permite administrar un registro de paises con sus datos geograficos y demograficos, almacenados en un archivo CSV.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 DESCRIPCION

El programa carga un archivo paises.csv al iniciarse y ofrece dos modulos principales:

🗂  Gestion de Paises (ABM): permite agregar, buscar, mostrar, actualizar y eliminar paises.
📊  Reportes: permite filtrar y ordenar paises por distintos criterios, y visualizar estadisticas generales.

Todos los cambios realizados desde el ABM se persisten automaticamente en el archivo CSV.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 ESTRUCTURA DEL PROYECTO

/
├── main.py        archivo principal del programa
├── paises.csv     base de datos en formato CSV
└── README.md      este archivo

Formato del archivo paises.csv:

NombreDelPais,Poblacion,Superficie,Continente
Argentina,45000000,2780400,America
Brasil,215000000,8515767,America
Francia,68000000,643801,Europa

⚠  El encabezado debe respetar exactamente esos nombres de columna.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

▶  INSTRUCCIONES DE USO

Requisitos:

* Python 3.10 o superior (se utiliza match/case)
* Modulo csv (incluido en la biblioteca estandar de Python)

Ejecucion:
python main.py

Al iniciar, el programa carga automaticamente el archivo paises.csv ubicado en el mismo directorio.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🧭 NAVEGACION DEL MENU

Menu principal:

====== SISTEMA DE PAISES ======

1. Gestion de Paises (ABM)
2. Reportes
3. Salir

Submenu — Gestion de Paises (ABM):

======== GESTION DE PAISES ========

1. Agregar Pais
2. Buscar Pais
3. Mostrar Paises
4. Actualizar Paises
5. Eliminar Pais
6. Volver

Submenu — Reportes:

\------ REPORTES ------

1. Filtrar por continente
2. Filtrar por poblacion
3. Filtrar por superficie
4. Ordenar por nombre
5. Ordenar por superficie
6. Ordenar por poblacion
7. Estadisticas
8. Volver



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 EJEMPLOS DE ENTRADAS Y SALIDAS



➕ Agregar un pais

Entrada:
Ingresa el nombre del pais: Japon
Ingresa la poblacion: 125000000
Ingresa la superficie: 377975
Ingrese el continente en el que se encuentra: Asia

Salida:
(el pais se agrega a la lista en memoria y al CSV)



🔍 Buscar un pais

Entrada:
Ingrese el nombre: argentina

Salida:
Pais encontrado:
Nombre: Argentina - Poblacion: 45000000 - Superficie: 2780400 - Continente: America

Entrada (pais inexistente):
Ingrese el nombre: Pangea

Salida:
Error, el pais no ha sido ingresado.



📋 Mostrar todos los paises

Salida:
======== Lista de Paises ========
Nombre: Argentina - Poblacion: 45000000  - Superficie: 2780400  - Continente: America
Nombre: Brasil    - Poblacion: 215000000 - Superficie: 8515767  - Continente: America
Nombre: Francia   - Poblacion: 68000000  - Superficie: 643801   - Continente: Europa



✏  Actualizar un pais

Entrada:
Ingerse el nombre: Francia
Nuevo nombre:              (vacio, no se modifica)
Nueva Poblacion: 69000000
Nueva Superficie:          (vacio, no se modifica)
Nuevo Continente:          (vacio, no se modifica)

Salida:
Pais actualizado correctamente.



🗑  Eliminar un pais

Entrada:
Ingrese el nombre del pais: Francia

Salida:
Pais eliminado correctamente.



🌎 Filtrar por continente

Entrada:
Ingresa el continente para filtrar los paises:
America

Salida:
argentina
brasil



📊 Filtrar por poblacion

Entrada:
Ingresa el minimo del rango: 10000000
Ingresa el maximo del rango: 100000000

Salida:
PAISES SEGUN POBLACION | MIN: 10000000 - MAX: 100000000
Argentina | POBLACION: 45000000 PERSONAS
Francia   | POBLACION: 68000000 PERSONAS



📐 Filtrar por superficie

Entrada:
Ingresa el minimo del rango: 500000
Ingresa el maximo del rango: 5000000

Salida:
PAISES SEGUN SUPERFICIE | MIN: 500000 - MAX: 5000000 KM
PAIS N°1: Argentina | SUPERFICIE: 2780400 KM
PAIS N°2: Francia   | SUPERFICIE: 643801 KM



🔤 Ordenar por nombre

Salida:
NOMBRES DE PAISES ORDENADOS ALFABETICAMENTE:
PAIS: Argentina
PAIS: Brasil
PAIS: Francia
PAIS: Japon



📈 Ordenar por superficie

Entrada:
A - Menor a Mayor
B - Mayor a Menor

> b

Salida:
PAIS: Brasil    | SUPERFICIE: 8515767 km
PAIS: Argentina | SUPERFICIE: 2780400 km
PAIS: Francia   | SUPERFICIE: 643801 km
PAIS: Japon     | SUPERFICIE: 377975 km



📉 Estadisticas

## Salida:

PAIS CON MAYOR POBLACION: Brasil | 215000000 personas
PAIS CON MENOR POBLACION: Japon  | 125000000 personas
---

Suma total de poblacion: 453000000 personas
Suma total de superficie: 12317943 KM
---

CANTIDAD DE PAISES POR CONTINENTE:
AMERICA - 2 paises
EUROPA  - 1 paises
ASIA    - 1 paises



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠  CONSIDERACIONES

* El campo nombre solo acepta letras (sin numeros ni simbolos).
* Los campos poblacion y superficie deben ser numeros enteros positivos mayores a 0.
* El campo continente solo acepta letras.
* Al actualizar, dejar un campo en blanco conserva el valor original.
* La funcion limpieza\_tildes permite comparar continentes ignorando tildes (America = America).
* El archivo CSV se reescribe completamente tras cada operacion de actualizacion o eliminacion.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👥 INTEGRANTES DEL EQUIPO

Integrante 1   ->   Alvaro Leal Gei
Integrante 2   ->   Nicolas Compagnucci



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📄 LICENCIA

TRABAJO INTEGRADOR - PROGRAMACION\_I - UTN San Nicolas

