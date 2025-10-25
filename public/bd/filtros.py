import pandas as pd
import plotly.express as px

# Carregar os dados do CSV e retirar linhas sem valores
df = pd.DataFrame(pd.read_csv('mockado_df.csv', encoding='latin1', sep=';'))
df = df.dropna()

# Exibir as primeiras linhas e informações do DataFrame
df.head()
df.info()

# Filtrar as colunas relevantes e mostrar o DataFrame resultante
totalRegioes_df = df[['Regiao', 'CENSO 2010', 'CENSO 2022']]
totalRegioes_df.head()


# Criar o gráfico de barras
fig = px.bar(
    totalRegioes_df, 
    x='Regiao', 
    y=['CENSO 2010', 'CENSO 2022'], 
    title='População por Região (2010 vs 2022)',
    labels={'Diferença': 'Diferença de População', 'Regiao': 'Região'},
    barmode='group', 
    text_auto='.2s', 
    color_discrete_sequence=['#A8C8FF','#FFF5B1'])

fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

fig.update_layout(showlegend=False)

fig.write_html('TotalRegioes.html')
