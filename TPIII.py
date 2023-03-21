#Problema 1
num = int(input("Ingrese una variable: "))
print(f"El valor absoluto de {num} es {abs(num)}")

#Problema 2
nombre = input("Ingrese su nombre: ")
print(f"El nombre {nombre} tiene {len(nombre)}")

#Problema 3
base = int(input("Ingrese una base: "))
exponente = int(input("Ingrese un exponente: "))
print(str(base ** exponente))

#Problema 4 y 5
base = int(input("Ingrese la base del rectangulo: "))
altura = int(input("Ingrese la altura del rectangulo: "))
print(f"Su perimetro es: {2 * (base + altura)}")
print(f"Su area es: {base * altura}")

#Problema 6
a = 10
b = 5
aux = b
b = a
a = aux

#Problema 7
a = 10
b = 5
a, b = b, a

#Problema 8
nota1 = int(input("Ingrese la nota del primer parcial: "))
nota2 = int(input("Ingrese la nota del segundo parcial: "))
promedio = (nota1 + nota2) / 2
print(f"El promedio de las notas es: {promedio}")

#Problema 9
dolarpesos = 80.5
realpesos = 14.1
europesos = 69.5
pesos = int(input("Cuantos pesos tiene? "))
print(f"Usted tiene ${pesos} pesos argentinos, los cuales se convierten en:")
print(f"- U${round(pesos / dolarpesos, 2)}.")
print(f"- R${round(pesos / realpesos, 2)}.")
print(f"- €{round(pesos / europesos, 2)}.")

