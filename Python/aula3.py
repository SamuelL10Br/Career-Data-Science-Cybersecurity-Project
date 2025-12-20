# Uso de loops(while)

# Enquanto uma condição for verdadeira, execute o código.
# contador = 1 -> começa em 1
# contador <= 5 -> condição
# contador += 1 -> evita loop infinito
# *Se esquecer de incrementar, trava o programa!

contador = 1

while contador <= 5:
    print(contador)
    contador +=1

# -------------------------------------------------------#

# loop(for) - Percorre uma sequência de valores automaticamente.
for i in range(1, 6):
    print(i)
# range(1, 6) -> começa em 1 e vai até 5 (o último número não entra)

for numero in range(1, 11):
    if numero % 2 == 0:
        print(numero)

# Filtragem de dado, base de ETL
dados = [10, 15, 20, 25, 30]

for valor in dados:
    if valor >= 20:
        print(valor)


