# Análise e Tratamento de Dados de Vendas com Pandas

Projeto de análise de dados desenvolvido com Python e Pandas, integrando tabelas fato e dimensões para apuração de faturamento, rentabilidade e desempenho comercial.

## Estrutura do Projeto
- `Cadastros.xlsx`: Tabelas dimensionais (`dProdutos`, `dClientes`, `dVendedores`).
- `Vendas.xlsx`: Registos de transações de vendas (`fVendas`).
- `Metas.csv`: Metas comerciais mensais por vendedor.
- `analise.py`: Script principal de ingestão, limpeza, enriquecimento e exportação.
- `vendas_consolidadas.csv`: Base tratada pronta para consumo analítico.

## Tratamentos Realizados
1. **Limpeza e Padronização:**
   - Remoção de registos nulos cadastrais.
   - Conversão de identificadores (`ID_Cliente`) para inteiros.
   - Tratamento de caracteres especiais e formatação de datas (`Mes_Ref`).
   - Normalização de tipos numéricos e separadores decimais em CSV.
2. **Métricas:**
   - Faturamento Bruto, Valor de Desconto e Faturamento Líquido.
   - Custo Operacional Total, Lucro Bruto e Margem de Lucro percentual.
3. **Modelagem Relacional (Merges):**
   - Cruzamento entre a tabela fato de vendas e as três dimensões de suporte.

## Como Executar
1. Instale as dependências:
   ```bash
   pip install pandas openpyxl