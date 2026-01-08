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


