#Gerar Arquivo simples .txt
arquivo = open("dados.txt", "w")
arquivo.write("Samuel,22,Cientista de Dados\n")
arquivo.close

arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

#Gerando dados de forma profissional e completa .txt
with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Samuel,22,Cientista de Dados\n")
    arquivo.write("Livia,17,Engenheira de Dados\n")
    arquivo.write("José,37,Cybersecurity\n")

with open("dados.txt","r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo")
    print(conteudo)

#Leitura linha por linha
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())

# Criando arquivo CSV
with open("dados.csv","w", encoding="utf-8") as arquivo:
    arquivo.write("nome,idade,profissão\n")
    arquivo.write("Samuel,22,Cientista de Dados\n")
    arquivo.write("Ana,39,Analista de Dados\n")
    arquivo.write("José,24,Desenvolvedor Mobile\n")

# Lendo arquivo CSV
with open("dados.csv","r",encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())
# Uma forma mais profissional para escrever dados 'csv'
import csv

with open("dados.csv", "w",newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow(["nome, idade, salário, profissão"])
    escritor.writerow(["Samuel",22,25000,"Especialista de Dados"])
    escritor.writerow(["Ana",28,12000,"Analista de Dados"])
    escritor.writerow(["Júlia",35,30000,"CEO"])
    escritor.writerow(["Júnior",43,15000,"Desenvolvedor Mobile"])

# Lendo em forma de lista

import csv

with open("dados.csv", "r", encoding="utf-8") as arquivo:
    conteudo = list(csv.DictReader(arquivo))

print(conteudo)
