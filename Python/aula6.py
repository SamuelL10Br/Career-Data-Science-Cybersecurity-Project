# Criando dados e fazendo chamadas
aluno = {
    "nome": "Samuel",
    "idade": 22,
    "curso": "ADS"
}
print(aluno["nome"])
print(aluno["idade"])
print(aluno["curso"])

# Usando o for para filrar dados em colchete(chave-valor)
for chave, valor in aluno.items():
    print(chave, ":", valor)
    
# Criando dados mais complexos para filtragem e percorrer os dados
usuarios = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Carlos", "idade": 17},
    {"nome": "João", "idade": 30}
]

for usuario in usuarios:
    if usuario["idade"] >= 18:
        print(usuario["nome"], "é maior de idade")

