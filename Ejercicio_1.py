#Ejercicio 1
#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

def max(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2

#uno = input('Ingresa primer número: ')
#dos = input('Ingresa segundo número: ')

#print(max(uno, dos))

#Ejercicio 2
#  Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
def max_de_tres(uno, dos, tres):
    if uno >= dos and uno >= tres:
        return uno
    elif dos >= tres:
        return dos
    else:
        return tres

#uno = input('Ingresa primer número: ')
#dos = input('Ingresa segundoz número: ')
#tres = input('Ingresa tercer número: ')

#Ejercicio 3
#Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

def longitud(variable):
    l = 0
    for i in variable:
        l += 1
    return l

#variable = {1, 2, 3, 4, 5}
#print(longitud(variable))

#Ejercicio 4
#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def aeiou(caracter):
    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u" caracter == "A" caracter == "E" caracter == "I" caracter == "O" caracter == "U":
        return True
    else:
        return False

#print(aeiou("ae"))

#Ejercicio 5
#Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def suman(arg):
    suma = 0
    for i in arg:
        suma = suma + i
    return suma

def multi(arg):
    multip = 1
    for i in arg:
        multip = multip * i
    return multip

#print(multi([1,2,3,4,5]))

#Ejercicio 6
#Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa(string):
    pal_inv = ""
    for car in string:
        pal_inv = car + pal_inv
    return pal_inv

#print(inversa("aloha"))

#Ejercicio 7
#Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

def es_palindromo(palabra):
    if palabra == inversa(palabra):
        return True
    else:
        return False

#print(es_palindromo("radar"))

#Ejercicio 8
#Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

def superposicion(list1, list2):
    igual = False
    for i in list1:
        for j in list2:
            if i == j:
                igual = True
    return igual

#print(superposicion(("a",2,3), ("b",4,3)))

#Ejercicio 9
#Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generar_n_caracteres(n, c):
    return n * str(c)

#print(generar_n_caracteres(5, "x"))

#Ejercicio 10
#Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla.

def procedimiento(lista):
    for num in lista:
        print(num * "*")

#procedimiento((1,4,2,6))
