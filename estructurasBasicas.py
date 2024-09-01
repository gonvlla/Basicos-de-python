import math 
from math import sqrt
import random
import datetime
import misModulos
#Hello world

print("Hola Mundo")

#Tipos de datos en python

nom = "Gon Villalba"
edad = 21
altura = 1.80
estaAfeitado = True

#Asignacion multiple

a = b = 200
print(nom)
print(a)

#Aritmeticos

suma = 10 + 20
resta = 20 - 10
mult = 10 * 4
div = 10 / 4
divEntera = 10 // 4
mod = 10 % 2
pot = 2 ** 2    

#De comparacion (Retorna true)d

igual = 10==10 #True
distinto = 10 != 20 #True
mayorQue = 10 > 20 #False
menorQue  = 10 < 5 #False
mayorIgual = 10 >= 10 #True
menorIgual = 10 <= 4 #False

#Logicos

compAnd = (4>1) and (4>2)
compOr = (4>1) or (4>5)
compNot = not(4>1)

#Estructuras condicionales
nota = 10
edad = 17
if edad > 18:
    print("Eres mayor!")
else:
    print("Eres menor!")
if nota < 60:
    print("Desaprobado :(")
elif  nota >  60 and nota <80:
    print("Estas regular :)")
else:
    print("Estas promocionado :DD")
    
#Bucles
    
frutas = ["Manzana","Bananas","Peras"]
for fruta in frutas:
    if(fruta == "Manzana"):
        continue #Saltar la iteracion y seguir con el bucle
        #pass no hace nada, solo para cuando se desee implementar
    print(fruta)


#while repite bucle mientras la condicion sea verdadera

cont = 0
while cont < 5:
    print(cont)
    #Instruccion break
    if cont == 2:
        break
    cont +=1

#Listas
    
misPersonas = ["Gonzalo","Maria","Carlos"]
print(misPersonas[0]) #Imprimira Gonzalo
print(misPersonas[1]) #Imprimira Maria
print(misPersonas[2]) #Imprimira Carlos

#Funciones con las listas

misPersonas.append("Jose") #Agrega al final
misPersonas.insert(0,"Alejandra") #Necesita como parametro el indice para ubicarla
misPersonas.remove("Maria") #Remueve maria
misPersonas.sort() #Las ordena
misPersonas.reverse() #Da vuelta la lista
personaActual = misPersonas.pop(1) #Saca la persona con el indice 1

#Listas de comprension
numeros = [1,2,3,4,5]
cuadrados = [x**2 for x in numeros if x%2  == 0] #Contiene los cuadrados de los numeros pares

#Una tupla es una estructura de datos inmutable y ordenada que permite almacenar una colección de elementos. 
#Los elementos de una tupla se encierran entre paréntesis (),
# separados por comas.

miTupla = (3,4)
print(miTupla[0]) #Imprime 3
print(miTupla[1]) #Imprime 4

#Funciones de las tuplas
miTupla.count(3) #Cant de veces q se repite el elemento
miTupla.index(3) #Devuelve el indice del valor pasado por parametros
len(miTupla) #Retorna el size de la tupla

#Diccionarios (clave valor)
miDiccionario = {"Nombre": "Maria","Edad":21,"Ciudad":"Parana"}

#Para utilizar el valor, se accede mediante la clave
print(miDiccionario["Nombre"])
print(miDiccionario["Edad"])
print(miDiccionario["Ciudad"])

#Funciones de los diccionarios
print(miDiccionario.keys())  #Imprime todas las claves de el diccionario
print(miDiccionario.values()) #Imprime todos los valores del diccionario
print(miDiccionario.items())  #Imprime todas las clave/valor del diccionario
miDiccionario.update({"Profesion": "Barista"})

#Conjuntos

#Creacion y operaciones basicas

#Funcion set
misNumeros = set([1,2,3,4,5])

#Estos admiten operaciones como la union, interseccion y la diferencia simetrica

c1 = {1,2,3}
c2 = {2,3,4}
unionDeUnConjunto = c1 | c2

print(unionDeUnConjunto)
inteseccionDeUnConjunto = c1 & c2
print(inteseccionDeUnConjunto)
diferenciaSimetrica = c1 - c2
print(diferenciaSimetrica)

#Metodos de un conjunto

miConjunto = {"Villalba","Reyser","Torres"}

miConjunto.add("Ferreyra") #Agrega un elemnto al conjunto

miConjunto.remove("Ferreyra") #Remueve un elemento

miConjunto.discard("Perez") #Elimina el elemnto SI esta, sino no hace nada

miConjunto.clear() #Elimina todos los elementos del conjunto

#Funciones

def saludo():
    print("Hola mundo :D")

saludo()

#Funciones con parametros

def saludoConParametro(nombre):
    print(f"Hola, {nombre} !")

saludoConParametro("Maria")

#Funciones con retorno
def conRetorno(a, b):
    return a + b

print(conRetorno(10,4))

#Funciones lambda

cuadrado = lambda x: x**2
#Es una funcion pequenia de una linea, sin definir comunmente usadas en funciones pequenias   
print(cuadrado(5))

#Documentacion (docstrings)

def area_rectangulo(altura,  base):
    """
        Calcula el área de un rectángulo.


    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.


    Returns:
        float: El área del rectángulo.
    """
    return base * altura

print(area_rectangulo(1.33,2.22))

#Funciones con numeros variables de elementos

def sumaVariable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(sumaVariable(1,33,44)) #Imprime 78
print(sumaVariable(2,2,6)) #Imprime 10

#Manejo de excepciones

"""
    El bloque try contiene el código que puede generar una excepción. 
    Si ocurre una excepción dentro del bloque try
    , el flujo de ejecución se transfiere al bloque except correspondiente.
"""

try:
    result = 10/0
    print(result)
except ZeroDivisionError:
    print("Error, division por cero")
except ValueError:
    print("Error: invalido")
"""
    El bloque except especifica el tipo de excepción que se desea capturar y manejar. 
    Puedes tener múltiples bloques except para manejar diferentes tipos de excepciones.
"""
try:
    #Codigo que puede generar un error
    archivo = open("archivo.txt","r") #Lectura
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    archivo.close() #Cerrar de todas formas el archivo 
"""
    El bloque finally es opcional y se ejecuta siempre, independientemente de si ocurrió una excepción o no. 
    Se utiliza comúnmente para realizar tareas de limpieza o liberación de recursos.
"""
#Entrada y salida de datos

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

print("Hola " + nombre + "!") #Concatenarlos
print(nombre + "tiene: " + edad + "anios! ")

#Asignar tipos en caso de requerirlos

altura = float(input("Ingrese su altura"))

if altura >  1.70:
    print("Mide + de 1.70cm!")
else:
    print("Mide - de 1.70cm!")

print(f"{nombre} tiene: {edad} anios y mide: {altura}")

#Archivos: r (lectura), w(escritura), a(anexar)

#Lectura
archivo = open("prueba.txt","r")
contenido = archivo.read()
print(contenido)
archivo.close()

#Escritura
file = open("archivo.txt","w")
file.write("Hola mundo! :D")
file.close()

#With para apertura y cierre automatico
with open("datos.txt","r") as arch:
    contenido = arch.read()
    print(contenido)

#Modulos: las cabeceras que traen funciones
resultado = math.sqrt(25) #Raiz de 25
print(resultado)

numAleatorio = random.randint(1,10)
print(numAleatorio) #Random entre 1 y 10

fechaActual = datetime.datetime.now() 
print(fechaActual) #Fecha actual

#Importacion de los modulos

print(misModulos.suma(10,20))
print(misModulos.mult(10,2))

