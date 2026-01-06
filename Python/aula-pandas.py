#Primeiro contato (DataFrame)
import pandas as pd

dados = {
    "nome": ["Samuel", "Ana", "José"],
    "idade": [22, 39, 24],
    "profissão": ["Cientista de Dados", "Analista de Dados", "Desenvolvedor Mobile"]
}

df = pd.DataFrame(dados)
print(df)

#Acessando colunas
print(df["nome"])

#Ou
print(df["idade"])

#Filtrando dados (O poder do pandas)
#Pessoas maiores de idade:
maiores = df[df["idade"] >= 18]
print(maiores)

#Pessoas com idade >= 30:
print(df[df["idade"] >= 30])

#Selecionando colunas + filtro
print(df[df["idade"] >= 30][["nome", "profissao"]])

#Lendo CSV com pandas
df = pd.read_csv("dados.csv")
print(df)

#Exemplo completo
import pandas as pd

# Lendo CSV
df = pd.read_csv("dados.csv")

print("Dados completos:")
print(df)

print("\nPessoas com idade >= 30:")
print(df[df["idade"] >= 30])

print("\nApenas nome e profissão:")
print(df[["nome", "profissao"]])

#Usando pandas para transformar um dado CSV
#Filtrar idades entre 20 e 40
#Filtrar por uma única profissão

import pandas as pd
df = pd.read_csv("dados.csv")
df.columns = ["nome","idade","profissao"] #Alterando nomes da coluna

print("Dados completos:")
print(df)

print("\nPessoas com idade >= 20 e <=40:")
print(df[(df["idade"] >= 20) & (df["idade"] <= 40)])

print("\n Buscar por uma profissão única:")
print(df[df["profissao"] == "Cientista de Dados"])

#Para 5 colunas
import pandas as pd  # Importa a biblioteca pandas e cria o apelido "pd"

# Lê o arquivo CSV e transforma em um DataFrame (tabela)
df = pd.read_csv(
    "dados.csv",            # Nome do arquivo CSV que será lido
    sep=",",                # Define que o separador de colunas é a vírgula (,)
    header=0,               # Indica que a primeira linha do arquivo é o cabeçalho
    skipinitialspace=True,  # Remove espaços extras após a vírgula (", ")
    engine="python"         # Usa o engine Python (mais tolerante a CSV mal formatado)
)

print(df)  # Exibe o DataFrame completo no terminal
