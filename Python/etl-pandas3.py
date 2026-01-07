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
