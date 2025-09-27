import pandas as pd
import plotly.express as px

# Carregar os dados do CSV
df = pd.DataFrame(pd.read_csv('bd\df_api_mock.csv', encoding='latin1', sep=';'))

# Filtrar as colunas relevantes
totalRegioes_df = df[['Regiao', 'CENSO 2010', 'CENSO 2022']]


# Criar o gráfico de barras
fig = px.bar(totalRegioes_df, x='Regiao', y=['CENSO 2010', 'CENSO 2022'], title='População por Região (2010 vs 2022)', 
labels={'Diferença': 'Diferença de População', 'Regiao': 'Região'})

fig.write_html('templates\iframes\TotalRegioesSMALL.html')
