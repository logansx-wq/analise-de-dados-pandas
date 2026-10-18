import pandas as pd

# 1. Carregamento dos dados
df_metas = pd.read_csv("Metas.csv", sep=";", decimal=",", encoding="utf-8-sig")
df_produtos = pd.read_excel("Cadastros.xlsx", sheet_name="dProdutos")
df_clientes = pd.read_excel("Cadastros.xlsx", sheet_name="dClientes")
df_vendedores = pd.read_excel("Cadastros.xlsx", sheet_name="dVendedores")
df_vendas = pd.read_excel("Vendas.xlsx", sheet_name="fVendas")

# 2. Tratamentos de dados
df_metas["Mes_Ref"] = pd.to_datetime(df_metas["Mes_Ref"], format="%d/%m/%Y")
df_clientes.dropna(subset=["ID_Cliente"], inplace=True)
df_clientes["ID_Cliente"] = df_clientes["ID_Cliente"].astype(int)

# 3. Métricas Financeiras
df_vendas["Faturamento_Bruto"] = df_vendas["Quantidade"] * df_vendas["Preco_Unitario"]
df_vendas["Valor_Desconto"] = df_vendas["Faturamento_Bruto"] * df_vendas["Desconto_Perc"]
df_vendas["Faturamento_Liquido"] = df_vendas["Faturamento_Bruto"] - df_vendas["Valor_Desconto"]

# 4. Joins (Tabela Fato com Dimensões)
df_consolidado = df_vendas.merge(df_produtos.drop(columns=["Preco_Unitario"]), on="ID_Produto", how="left")
df_consolidado = df_consolidado.merge(df_clientes, on="ID_Cliente", how="left")
df_consolidado = df_consolidado.merge(df_vendedores, on="ID_Vendedor", how="left")

# Custos, Lucro e Margem
df_consolidado["Custo_Total"] = df_consolidado["Quantidade"] * df_consolidado["Custo_Unitario"]
df_consolidado["Lucro"] = df_consolidado["Faturamento_Liquido"] - df_consolidado["Custo_Total"]
df_consolidado["Margem_Lucro_Perc"] = ((df_consolidado["Lucro"] / df_consolidado["Faturamento_Liquido"]) * 100).round(2)

# 5. Exportação da base analítica limpa
df_consolidado.to_csv("vendas_consolidadas.csv", index=False, sep=";", decimal=",", encoding="utf-8-sig")

# 6. Sumários Executivos
print("=" * 50)
print(f"FATURAMENTO TOTAL LÍQUIDO: R$ {df_consolidado['Faturamento_Liquido'].sum():,.2f}")
print(f"LUCRO TOTAL: R$ {df_consolidado['Lucro'].sum():,.2f}")
print("=" * 50)

print("\n--- TOP 5 PRODUTOS POR FATURAMENTO ---")
top_produtos = (
    df_consolidado.groupby("Produto")["Faturamento_Liquido"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
print(top_produtos.map("R$ {:,.2f}".format))

print("\n--- FATURAMENTO POR REGIÃO ---")
fat_regiao = (
    df_consolidado.groupby("Regiao")["Faturamento_Liquido"]
    .sum()
    .sort_values(ascending=False)
)
print(fat_regiao.map("R$ {:,.2f}".format))