import pandas as pd

# ===============================
# EXTRACT - Criando dados brutos
# ===============================
dados = {
    "nome": ["Samuel", "Ana", "José", "Maria"],
    "idade": [22, 39, None, 17],
    "salario": [25000, 12000, None, 4000]
}

df = pd.DataFrame(dados)
print("DADOS BRUTOS:")
print(df)

# ===============================
# TRANSFORM - Limpando dados
# ===============================
df["idade"] = df["idade"].fillna(0)
df["salario"] = df["salario"].fillna(0)

# Filtrar apenas maiores de idade
df = df[df["idade"] >= 18]

print("\nDADOS TRATADOS:")
print(df)

# ===============================
# LOAD - Salvando dados limpos
# ===============================
df.to_csv("dados_limpos.csv", index=False)

print("\nArquivo 'dados_limpos.csv' gerado com sucesso.")

# Atividade prática de ETL, filtrando dados e criando coluna.
import pandas as pd

dados = {
    "nome": ["Samuel","Ana","Tiago"],
    "idade": [22, 39, 45],
    "salario": [25000, 3400, 4567]
}

df = pd.DataFrame(dados)
df["salario_anual"] = df["salario"] * 12
print("\nAdicionando uma coluna para salário anual")
print(df)

df = df[df["idade"] >= 21]
df.to_csv("dados_finais.csv", index=False)
print("\nDados gerados com sucesso!")

# ETL with sort_values by salary wage high than 5000. hands-on activitys
import pandas as pd

#Extract
df = pd.read_csv("dados_finais.csv")

#Transform
df = df[df["salario"] > 5000]
df = df.sort_values(by="salario", ascending=False)

print("\nSalários filtrados e ordenados:")
print(df)

# Load 
df.to_csv("Dados_analise.csv", index=False)
print("\nArquivo 'dados_analise.csv' gerado com sucesso.")

# Média salarial por idade
import pandas as pd
df = pd.read_csv("dados_analise.csv")

# Transform - Agrupamento
media_salario = df.groupby("idade")["salario"].mean()

print("\nMédia de salário por idade:")
print(media_salario)

# Convertendo para DataFrame
resultado = media_salario.reset_index()

# Load
resultado.to_csv("media_salario_por_idade.csv", index=False)
print("\nArquivo 'media_salario_por_idade.csv' gerado com sucesso.")

# Join in pandas
import pandas as pd

# Tabela de pessoas
pessoas = {
    "id": [1, 2, 3],
    "nome": ["Samuel", "Ana", "Tiago"]
}

# Tabela de salários
salarios = {
    "id_pessoa": [1, 2, 3],
    "salario": [25000, 3400, 4567]
}

df_pessoas = pd.DataFrame(pessoas)
df_salarios = pd.DataFrame(salarios)

# JOIN (equivalente ao SQL JOIN)
df_join = pd.merge(
    df_pessoas,
    df_salarios,
    left_on="id",
    right_on="id_pessoa",
    how="inner"
)

print("\nResultado do JOIN:")
print(df_join)


