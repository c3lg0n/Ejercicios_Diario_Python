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
    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u" or caracter == "A" or caracter == "E" or caracter == "I" or caracter == "O" or caracter == "U":
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

#Ejercicio 11
#La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.

def max_in_list(lst):
    alto = 0
    for i in lst:
        if i > alto:
            alto = i
    return alto

#print(max_in_list((1,2,41,2,7,6,0)))

#Ejercicio 12
#Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.

def mas_larga(lst):
    larga = ""
    for word in lst:
        if longitud(word) > longitud(larga):
            larga = word
    return larga

#print(mas_larga(("hola", "celis", "miercoles", "mañana")))

#Ejercicio 13
#Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.

def filtrar_palabras(lst, n):
    filtradas = []
    for word in lst:
        if longitud(word) > n:
            filtradas.append(word)
    return filtradas

#print(filtrar_palabras(("hola","uno","yo","tres"), 12))

#Ejercicio 14
#Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.

def evaluar_cadena():
    cadena = input("Ingrese el texto: ")
    mayus = 0
    for caracter in cadena:
        if caracter.isupper():
            mayus += 1
    return mayus

#print(evaluar_cadena())

#Ejercicio 15
#Construir un pequeño programa que convierta números binarios en enteros.

def binToDec(binario):
    binario = inversa(str(binario))
    exp = 0
    result = 0
    for i in binario:
        i = int(i)
        result = result + (i * (2 ** exp))
        exp += 1
    return result

#print(binToDec(1101110011100101100))

#Ejercicio 16
#Escribir un pequeño programa donde:
#- Se ingresa el año en curso.
#- Se ingresa el nombre y el año de nacimiento de tres personas.
#- Se calcula cuántos años cumplirán durante el año en curso.
#- Se imprime en pantalla.

def edad():
    actual = int(input("Ingresa el año actual: "))
    conteo = 0
    while conteo < 3:
        nombre = input("Escribe tu nombre: ")
        nacimiento = int(input("Escribe tu año de nacimiento: "))
        edad = actual - nacimiento
        print(nombre, ", cumplirás este año ", edad, " años.")
        conteo += 1
#edad()

#Ejercicio 17
#Definir una tupla con 10 edades de personas. Imprimir la cantidad de personas con edades superiores a 20. Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

def edades():
    conteo = 1
    edads = []
    while conteo <= 10:
        ingreso = input("Ingresa edad {0}:\n".format(conteo))
        edads.insert(conteo - 1, str(ingreso))
        conteo += 1
    edads = tuple(edads)
    mayor_edad = 0
    for i in edads:
        if int(i) > 20:
            mayor_edad += 1
    return mayor_edad

#print(edades())

#Ejercicio 18
#Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a. También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)

def lstNm():
    seguir = "S"
    lista = []
    while seguir == "S":
        entrada = input("Ingrese un nombre:\n")
        lista.append(entrada)
        seguir = input("¿Desea ingresa otro nombre?(S/N): ")
    return lista

def concurrencia(lista):
    letra = input("Elija la letra a buscar: ").upper()
    igual = 0
    for i in lista:
        if i[0].upper() == letra:
            igual += 1
    return igual

#print(concurrencia(lstNm()))

#Ejercicio 19
#Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales. Se puede hacer que el usuario sea quien elija la palabra.

def contar_vocales(palabra):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for letra in palabra:
        if letra == "a" or letra == "A":
            a += 1
        elif letra == "e" or letra == "E":
            e += 1
        elif letra == "i" or letra == "I":
            i += 1
        elif letra == "o" or letra == "O":
            o += 1
        elif letra == "u" or letra == "U":
            u += 1
    if a > 0:
        print("Hay {0} 'a'".format(a))
    if e > 0:
        print("Hay {0} 'e'".format(e))
    if i > 0:
        print("Hay {0} 'i'".format(i))
    if o > 0:
        print("Hay {0} 'o'".format(o))
    if u > 0:
        print("Hay {0} 'u'".format(u))

#contar_vocales(input("Escriba una palabra:\n"))

#Ejercicio 20
#Escriba una función es_bisiesto() que determine si un año determinado es un año bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400

def es_bisiesto(year):
    año = int(year)
    if año % 100 == 0:
        if año % 400 == 0:
            print(año, "es año bisiesto!!!")
        else:
            print(año, "no es año bisiesto!!!")
    elif año % 4 == 0:
        print(año, "es año bisiesto.")
    else:
        print(año, "no es año bisiesto!!!")

es_bisiesto(2000)
