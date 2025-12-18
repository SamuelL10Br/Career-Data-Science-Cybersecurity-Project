#Brincando com o else-if

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Acesso permitido")
else:
    print("Acesso negado")

#Nota do aluno

nota = float(input("Digite a nota do aluno:"))

if nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")

#Usando o 'elif' para notas

nota1 = float(input("Digite a nota: "))

if nota1 >= 7:
    print("Aprovado")
elif nota1 >= 5:
    print("Recuperação")
else:
    print("Reprovado")