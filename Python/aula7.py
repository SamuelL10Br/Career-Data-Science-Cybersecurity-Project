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