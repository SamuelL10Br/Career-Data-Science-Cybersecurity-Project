import pandas as pd
df = pd.read_csv("dados.csv")

# Selecionar mais de uma coluna
print(df[["nome","idade","profissao"]])

# Selecionando linhas
# Usando índice (posição)
print(df.iloc[0:5])

# Condição
print(df[df["idade"] > 30])

# Condição + coluna
print(df.loc[df["idade"] > 30, ["nome","idade"]])

# Filtrando dados (Where do SQL)
# Igualdade
print(df[df["profissao"] == "Especialista de Dados"])
# Maior / Menor
print(df[df["salario"] >= 5000])
# Múltiplas condições
print(df[(df["idade"] > 25) & (df["salario"] >= 5000)])

# Lidando com dados faltantes (NaN)
# Ver valores nulos
print(df.isna())
print(df.isna().sum())

# Remover linhas com Nan
print(df.dropna())

# Preencher valores
print(df["salario"].fillna(0))

# Preencher com média
print(df["profissao"].fillna(df["salario"].mean()))

# Ajustando texto (acento, maiúsculas, espaços)
# Remover espaços extras
df["profissao"] = df["profissao"].str.strip()

# Tudo minúsculo
df["profissao"] = df["profissao"].str.lower()

# Tudo maiúsculo
df["profissao"] = df["profissao"].str.upper()

# Substituir tetxo
df["profissao"] = df["profissao"].str.replace("engenheiro", "engineer")

# Criando novas colunas (feature engineering)
# Coluna baseada em outra
df["salario_anual"] = df["salario"] * 12

# Coluna com condição
df["senioridade"] = df["idade"].apply(
    lambda x: "Senior" if x >= 35 else "Junior"
)

# Ordenando dados
df.sort_values(by="idade")
df.sort_values(by="salario", ascending=False)

# Agrupando dados (GROUP BY)
# Média de salário por profissão
df.groupby("profissao")["salario"].mean()

# Contagem
df.groupby("profissao")["nome"].count()

# Múltiplas métricas
df.groupby("profissao").agg({
    "salario": ["mean", "max", "min"],
    "idade": "mean"
})

# Salvando arquivos
# Salvar em CSV
df.to_csv("dados_limpos.csv", index=False)

# Salvar em Excel
df.to_excel("dados_limpos.xlsx", index=False)