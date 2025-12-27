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
    {"nome": "Ana", "idade": 22},
    {"nome": "Carlos", "idade": 17},
    {"nome": "João", "idade": 30}
]

for usuario in usuarios:
    if usuario["idade"] >= 18:
        print(usuario["nome"], "é maior de idade")

#Atividade prática para acessar dados
dicionarios = [
    {"nome":"Samuel","idade":22,"profissão":"Cientista De Dados e Segurança"},
    {"nome":"Victor","idade":16,"profissão":"Front-End Design"},
    {"nome":"Lívia","idade":48,"profissão":"UX-UI Design"}
]

for usuario in dicionarios:
    if usuario["idade"] >= 18:
        print(usuario["nome"],"é maior de idade")
    else:
        print(usuario["nome"],"Não é maior de idade")
