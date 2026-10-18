import pandas as pd

# 1. Carregamento dos dados
# Definindo sep=";" e decimal="," para ler o CSV sem quebras indevidas
df_metas = pd.read_csv("Metas.csv", sep=";", decimal=",", encoding="utf-8-sig")
df_produtos = pd.read_excel("Cadastros.xlsx", sheet_name="dProdutos")
df_clientes = pd.read_excel("Cadastros.xlsx", sheet_name="dClientes")
df_vendedores = pd.read_excel("Cadastros.xlsx", sheet_name="dVendedores")
df_vendas = pd.read_excel("Vendas.xlsx", sheet_name="fVendas")

# 2. Tratamento da tabela df_metas
# Converte a coluna de data para datetime
df_metas["Mes_Ref"] = pd.to_datetime(df_metas["Mes_Ref"], format="%d/%m/%Y")

# 3. Tratamento da tabela df_clientes
# Remove eventuais linhas em branco e ajusta o ID para inteiro
df_clientes.dropna(subset=["ID_Cliente"], inplace=True)
df_clientes["ID_Cliente"] = df_clientes["ID_Cliente"].astype(int)

# 4. Diagnóstico das tabelas tratadas
print("=== Metas Tratadas ===")
print(df_metas.info())
print(df_metas.head(3))

print("\n=== Clientes Tratados ===")
print(df_clientes.info())