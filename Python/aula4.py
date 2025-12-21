numeros = [10, 20, 30, 40, 50]

# Mostrar número específico
print(numeros[2])

# For de 1 a 10
for numero in range(1, 11):
    print(numero)

# While de 1 a 20
contador = 1
while contador <= 20:
    print(contador)
    contador += 1

# Mostrar números pares da lista
for numero in numeros:
    if numero % 2 == 0:
        print("Par:", numero)

# Mostrar todos
for numero in numeros:
    print(numero)

# Maiores que 25
for numero in numeros:
    if numero > 25:
        print("Maior que 25:", numero)

# Soma
total = 0
for numero in numeros:
    total += numero

print("Soma total:", total)
