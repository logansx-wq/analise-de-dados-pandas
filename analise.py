import pandas as pd

# 1. Carregamento dos dados
df_metas = pd.read_csv("Metas.csv", sep=";", decimal=",", encoding="utf-8-sig")
df_produtos = pd.read_excel("Cadastros.xlsx", sheet_name="dProdutos")
df_clientes = pd.read_excel("Cadastros.xlsx", sheet_name="dClientes")
df_vendedores = pd.read_excel("Cadastros.xlsx", sheet_name="dVendedores")
df_vendas = pd.read_excel("Vendas.xlsx", sheet_name="fVendas")

# 2. Tratamentos de tipagem e limpeza
df_metas["Mes_Ref"] = pd.to_datetime(df_metas["Mes_Ref"], format="%d/%m/%Y")
df_clientes.dropna(subset=["ID_Cliente"], inplace=True)
df_clientes["ID_Cliente"] = df_clientes["ID_Cliente"].astype(int)

# 3. Métricas de Vendas
df_vendas["Faturamento_Bruto"] = df_vendas["Quantidade"] * df_vendas["Preco_Unitario"]
df_vendas["Valor_Desconto"] = df_vendas["Faturamento_Bruto"] * df_vendas["Desconto_Perc"]
df_vendas["Faturamento_Liquido"] = df_vendas["Faturamento_Bruto"] - df_vendas["Valor_Desconto"]

# 4. Cruzamentos (Joins)
df_consolidado = df_vendas.merge(
    df_produtos.drop(columns=["Preco_Unitario"]),
    on="ID_Produto",
    how="left"
)
df_consolidado = df_consolidado.merge(df_clientes, on="ID_Cliente", how="left")
df_consolidado = df_consolidado.merge(df_vendedores, on="ID_Vendedor", how="left")

# Custos e Lucro
df_consolidado["Custo_Total"] = df_consolidado["Quantidade"] * df_consolidado["Custo_Unitario"]
df_consolidado["Lucro"] = df_consolidado["Faturamento_Liquido"] - df_consolidado["Custo_Total"]

# 5. Comparativo com Metas
# Cria o primeiro dia do mês para cruzar com a tabela de metas
df_consolidado["Mes_Ref"] = df_consolidado["Data"].dt.to_period("M").dt.to_timestamp()

# Agrupa vendas por mês e vendedor
vendas_mensais = (
    df_consolidado.groupby(["Mes_Ref", "ID_Vendedor", "Vendedor"], as_index=False)
    .agg(Faturamento_Realizado=("Faturamento_Liquido", "sum"))
)

# Cruza com a tabela de metas
df_performance = vendas_mensais.merge(df_metas, on=["Mes_Ref", "ID_Vendedor"], how="left")
df_performance["Atingimento_Perc"] = (
    (df_performance["Faturamento_Realizado"] / df_performance["Meta_Valor"]) * 100
).round(2)

# 6. Exportação dos Dados Tratados
df_consolidado.to_csv("vendas_consolidadas.csv", index=False, sep=";", decimal=",", encoding="utf-8-sig")

# 7. Exibição de Resultados
print("=== Amostra de Desempenho vs Metas ===")
print(df_performance.head(6))

print("\n=== Exportação Concluída ===")
print("Arquivo 'vendas_consolidadas.csv' gerado com sucesso!")