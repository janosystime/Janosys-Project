import pandas as pd
import plotly.express as px


# Carregar o DataFrame a partir do arquivo CSV
# O nome do arquivo é 'tabela_rendimento_medio_bairro.csv''
df = pd.read_csv('public/bd/tabela_rendimento_medio_bairro.csv')

# 1. Garantir que a coluna de rendimento é numérica (caso haja algum problema na importação)
# df['Rendimento Médio (R$)'] = pd.to_numeric(df['Rendimento Médio (R$)'], errors='coerce')

# 2. Calcular o Rendimento Médio por Região
df_rendimento_medio_regiao = df.groupby('Região')['Rendimento Médio (R$)'].mean().reset_index()
df_rendimento_medio_regiao.round(2)


df_rendimento_medio_regiao

# Assumindo que o DF 'df_rendimento_medio_regiao' já foi criado com o código Pandas acima

fig = px.bar(
    df_rendimento_medio_regiao,
    x='Região',
    y='Rendimento Médio (R$)',
    title='Rendimento Médio(R$) em São José dos Campos',
    color='Rendimento Médio(R$)',
    color_continuous_scale=px.colors.sequential.Viridis,
    text=df_rendimento_medio_regiao['Rendimento Médio (R$)'].round(2).apply(lambda x: f'R$ {x:,.2f}')
)

fig.update_layout(
    xaxis_title='Região',
    yaxis_title='Rendimento Médio (R$)',
    xaxis={'categoryorder':'total descending'}
)

fig.update_layout(
    title={'font': {'family': 'Segoe UI', 'size': 21, 'color': '#154389', "weight": "bold"}, 'x': 0, 'xanchor': 'left'})
fig.add_annotation(x=1, y=-0.08, xref='paper', yref='paper', text='Fonte: IBGE Censo (2022) / PMSJC.', showarrow=False, font={'size': 10, 'color': '#666'})

fig.show()

#fig.write_html('static/iframes/grafico_renda.html', full_html=True, include_plotlyjs="cdn", config={'displayModeBar': False})
