# Análise e Tratamento de Dados de Vendas com Pandas

Projeto de análise de dados desenvolvido com Python e Pandas, integrando tabelas fato e dimensões para apuração de faturamento, rentabilidade e desempenho comercial.

## Estrutura do Projeto
- `Cadastros.xlsx`: Tabelas dimensionais (`dProdutos`, `dClientes`, `dVendedores`).
- `Vendas.xlsx`: Registos de transações de vendas (`fVendas`).
- `Metas.csv`: Metas comerciais mensais por vendedor.
- `analise.py`: Script principal de ingestão, limpeza, enriquecimento e exportação.
- `vendas_consolidadas.csv`: Base tratada pronta para consumo analítico.
- <img width="266" height="214" alt="image" src="https://github.com/user-attachments/assets/df292a90-d24c-4a91-b462-783c177ce89a" />

<img width="621" height="145" alt="image" src="https://github.com/user-attachments/assets/a0d2712c-4356-43cb-8502-0d3558d1f2cb" />


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
<img width="379" height="309" alt="image" src="https://github.com/user-attachments/assets/3d48fb62-a6ef-4825-baa7-a15cf03375b7" />


## Como Executar
1. Instale as dependências:
   ```bash
   pip install pandas openpyxl
2. Execute o arquivo "analise.py"
<img width="741" height="177" alt="image" src="https://github.com/user-attachments/assets/707dda4f-1be7-4fff-8185-7f17023b9164" />
