print("Ejercicio 1.1 \n")
def clasificar_calificacion(calificacion):
    if 9 <= calificacion <= 10:
        return "A"
    elif 8 <= calificacion < 9:
        return "B"
    elif 7 <= calificacion < 8:
        return "C"
    elif 6 <= calificacion < 7:
        return "D"
    elif 0 <= calificacion < 6:
        return "F"
    else:
        return "Valor desconocido"

def main():
    try:
        calificacion = float(input("Ingrese una calificación entre 0 y 10: "))
        
        if 0 <= calificacion <= 10:
            resultado = clasificar_calificacion(calificacion)
            print(f"La calificación {calificacion} es equivalente a una: {resultado}")
        else:
            print("El valor ingresado está fuera del rango permitido.")
    except ValueError:
        print("Error: Ingrese un número válido.")

if __name__ == "__main__":
    main()
#------------------------------------
print("\nEjercicio 1.2 \n")
def main():
    try:
        numero1 = int(input("Proporciona el numero1: "))
        numero2 = int(input("Proporciona el numero2: "))

        if numero1 > numero2:
            print(f"El numero mayor es: {numero1}")
        elif numero2 > numero1:
            print(f"El numero mayor es: {numero2}")
        else:
            print("Los números son iguales.")
    except ValueError:
        print("Error: Ingrese valores enteros válidos.")

if __name__ == "__main__":
    main()
#------------------------------------
print("\nEjercicio 1.3 \n")
print("Números divisibles por 3 del 0 al 10:")
for i in range(11): 
    if i % 3 == 0:
        print(i)

#------------------------------------
print("\nEjercicio 2.1 \n")
print("\n") 
def max(num1, num2):
    """Devuelve el mayor de dos números."""
    if num1 > num2:
        return num1
    else:
        return num2

numero1 = int(input("Ingresa el primer número "))
numero2 = int(input("Ingresa el segundo número "))
print(f"El número máximo entre {numero1} y {numero2} es: {max(numero1, numero2)}")
#------------------------------------
print("\nEjercicio 2.2 \n")
def max_de_tres(num1, num2, num3):
    """Devuelve el mayor de tres números."""
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
numero1 = int(input("Ingresa el primer número "))
numero2 = int(input("Ingresa el segundo número "))
numero3 = int(input("Ingresa el tercernúmero "))

print(f"El número máximo entre {numero1}, {numero2} y {numero3} es: {max_de_tres(numero1, numero2, numero3)}")
#------------------------------------
print("\nEjercicio 2.3 \n")

def longitud(elemento):
    """Calcula la longitud de una lista o cadena dada."""
    contador = 0
    for _ in elemento:
        contador += 1
    return contador
cadena_ejemplo = input("Proporciona una cadena ")
lista_ejemplo = [1, 2, 3, 4, 5]
print(f"Longitud de la cadena '{cadena_ejemplo}': {longitud(cadena_ejemplo)}")
print(f"Longitud de la lista {lista_ejemplo}: {longitud(lista_ejemplo)}")

#------------------------------------
print("\nEjercicio 2.4 \n")
def es_vocal(caracter):
    vocales = 'aeiouAEIOU'
    return caracter in vocales
letra_test = input("Proporciona una letra ")
if es_vocal(letra_test):
    print("Es vocal")
else:
    print("No es vocal")
#------------------------------------
print("\nEjercicio 2.5 \n")
def sum(lista):
    """Devuelve la suma de todos los números en la lista."""
    resultado = 0
    for num in lista:
        resultado += num
    return resultado

def multip(lista):
    """Devuelve el producto de todos los números en la lista."""
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado
li = [1, 2, 3, 4]
print("La lista es", li)
print("La suma es:")
print(sum(li))
print("La multiplicación da:")
print(multip(li)) 
#------------------------------------
print("\nEjercicio 2.6 \n")
def inversa(cadena):
    """Devuelve la cadena invertida."""
    return cadena[::-1]
cadena_test = input("Proporciona una cadena ")
print(inversa(cadena_test))
#------------------------------------
print("\nEjercicio 2.7 \n")
def superposicion(lista1, lista2):
    """Devuelve True si las dos listas tienen al menos un elemento en común."""
    for elem1 in lista1:
        for elem2 in lista2:
            if elem1 == elem2:
                return True
    return False
print("Las listas son:")
li = [1, 2, 3]
lo = [3, 4, 5]
la = [4, 5, 6]
print("li", li, "lo", lo, "la", la)
print("Entre li y lo:")
print(superposicion(li, lo))
print("Entre li y la:")
print(superposicion(li, la))
#------------------------------------
print("\nEjercicio 2.8 \n")
def generar_n_caracteres(n, caracter):
    """Devuelve el caracter multiplicado por n."""
    return caracter * n
caracter = input("Dame el caracter: ")
numero = int(input("¿Cuantaas veces lo quieres repetido? "))
print(generar_n_caracteres(numero, caracter))
#------------------------------------
# Ej 2.9
def procedimiento(li):
    for num in li:
        print(num, "*" * num )
print("\nEjercicio 2.9 \n")
li = [4,6,9,2]
print("La lista es", li)
procedimiento(li)
def max_in_list(lo):
    x = sorted(lo, reverse=True)
    max_num = x[0]
    return max_num

lo = [5, 65, 44, 99, 32]

print("\n", "\nEjercicio 2.10 \n")
print("La lista es ", lo)
print("El numero más grande es :",max_in_list(lo), "\n")
#------------------------------------
def mas_larga(le):
    larga = ""
    maxlo = 0
    for cad in le:
        cont = 0
        for letra in cad:
            cont +=1
        if cont > maxlo:
            maxlo = cont
            larga = cad
    return larga

le = ["casa", "huevo", "frijoles", "yamal"]
print("\nEjercicio 2.11 \n")
print("La palabra más larga en", le , "es ", mas_larga(le), "\n")
#------------------------------------
def filtra_palabrras(la,n):
    li_fil = []
    for cad in la:
        if len(cad) > n:
            li_fil.append(cad)
    return li_fil
le = ["casa", "huevo", "frijoles", "yamal"]
print("\nEjercicio 2.12 \n")
print(filtra_palabrras(le,5), "\n")

def mayus(cad):
    cont = 0
    for letra in cad:
        if letra.isupper():
            cont +=1
    return cont
cad = "HuEvOs"
print("\nEjercicio 2.13 \n")
print(mayus(cad), "\n")
#------------------------------------
def ente_to_bin(n):
    binario = ""
    while n >= 1:
        if n % 2 == 0:
            binario = "0" +binario
        else:
            binario = "1" + binario
        n = n//2
    return binario
print("\nEjercicio 2.14 \n")
z = 1024
print(ente_to_bin(z), "\n")
#------------------------------------
print("\nEjercicio 2.15 \n")
edades = (18, 22, 25, 30, 15, 21, 27, 19, 20, 23)
print ("Las edades son", edades)
cantidad_mayores_a_20 = sum(1 for edad in edades if edad > 20)

print(f"La cantidad de personas con edades superiores a 20 es: {cantidad_mayores_a_20}")

def contar_mayores_20(edades):
    """Cuenta cuántas edades ingresadas son mayores a 20."""
    return sum(1 for edad in edades if edad > 20)

try:
    edades_usuario = []
    for i in range(10):
        edad = int(input(f"Ingrese la edad {i + 1}: "))
        edades_usuario.append(edad)
    
    cantidad_mayores_a_20 = contar_mayores_20(edades_usuario)
    
    print(f"La cantidad de personas con edades superiores a 20 es: {cantidad_mayores_a_20}")
except ValueError:
    print("Por favor, ingrese un número válido para la edad.")
#------------------------------------
print("\nEjercicio 2.16 \n")
nombres = ["Ana", "Juan", "Maria", "Carlos", "Luisa", "Carolina", "Luis", "Lolo"]
print("Los nombres son", nombres)
letra = input("Ingrese la letra para contar nombres que comienzan con esa letra: ")

cantidad = sum(1 for nombre in nombres if nombre.lower().startswith(letra.lower()))

print(f"La cantidad de nombres que comienzan con la letra '{letra}' es: {cantidad}")

#------------------------------------
print("\nEjercicio 2.17 \n")
def contar_vocales(palabra):
    """Cuenta la cantidad de veces que aparece cada vocal en la palabra."""
    vocales = ['a', 'e', 'i', 'o', 'u']
    resultado = {vocal: palabra.lower().count(vocal) for vocal in vocales}
    return resultado

palabra_usuario = input("Ingrese una palabra para contar las vocales: ")

print(contar_vocales(palabra_usuario))


#------------------------------------
print("\nEjercicio 2.18 \n")
def es_bisiesto(anio):
    """Determina si un año es bisiesto o no."""
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

anio_usuario = int(input("Ingrese un año para determinar si es bisiesto: "))

if es_bisiesto(anio_usuario):
    print(f"{anio_usuario} es un año bisiesto.")
else:
    print(f"{anio_usuario} no es un año bisiesto.")
