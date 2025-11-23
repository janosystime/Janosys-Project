import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go


#Definindo os DFs Populacao 0 a 4 anos
df_populacao = pd.read_csv("public/bd/dados_sjc_regiao.csv", sep=";")
df_populacao_0a4 = df_populacao.groupby("Região", as_index=False)["0 a 4 anos"].sum()
df_populacao_0a4['População Infantil%'] = ((df_populacao_0a4['0 a 4 anos'] / (df_populacao_0a4['0 a 4 anos'].sum()))*100).round(2)
df_populacao_0a4
#
#df_escolas_infantis = pd.read_csv('public/bd/tabela_escolas_infantis_sjc.csv', sep=';')
#df_escolas_infantis
#df_escolas_infantis_clean = df_escolas_infantis[['NO_ENTIDADE', 'TP_DEPENDENCIA', 'NO_BAIRRO', 'QT_MAT_INF']]
#df_escolas_infantis_clean
#df_escolas_infantis_clean.to_csv('public/bd/tabela_escolas_infantis_clean.csv', index=False)

#Adicionando a coluna região
#df_bairros = pd.read_csv('public/bd/tabela_bairro_regiao.csv', encoding='utf-8', sep=',')
#df_bairros
#df_escolas_regiao = df_escolas_infantis_clean.merge(
#    df_bairros,
#    left_on='NO_BAIRRO',
#    right_on='bairro',
#    how='left'
#)
## DF regiao e escolas

df_escola_infantil_bairro = pd.read_csv('public/bd/tabela_escolas_regiao.csv')
#df_escola_infantil_bairro

#Escolas Publicas e Privadas

df_filtrado = df_escola_infantil_bairro[df_escola_infantil_bairro['TP_DEPENDENCIA'].isin([3,4])]
df_escolas_municipais_privadas = df_filtrado.pivot_table(
   index='região',
   columns='TP_DEPENDENCIA',
   aggfunc='size',
    fill_value=0
).reset_index()

df_escolas_municipais_privadas.columns.name = None
df_escolas_municipais_privadas = df_escolas_municipais_privadas.rename(columns={3: 'Municipal', 4: 'Particular'})
df_escolas_municipais_privadas

df_escolas_municipais_privadas['Proporção Municipal'] = ((df_escolas_municipais_privadas['Municipal'] / (df_escolas_municipais_privadas['Municipal'].sum() + df_escolas_municipais_privadas['Particular'].sum()))*100).round(2)
df_escolas_municipais_privadas['Proporção Particular'] = ((df_escolas_municipais_privadas['Particular'] / (df_escolas_municipais_privadas['Municipal'].sum() + df_escolas_municipais_privadas['Particular'].sum()))*100).round(2)
df_escolas_municipais_privadas['Proporção Geral]'] = (((df_escolas_municipais_privadas['Municipal'] + df_escolas_municipais_privadas['Particular']) / (df_escolas_municipais_privadas['Municipal'].sum() + df_escolas_municipais_privadas['Particular'].sum()))*100).round(2)
df_escolas_municipais_privadas['Proporção de Crianças de 0 a 4 anos'] = df_populacao_0a4['População Infantil%']
df_escolas_municipais_privadas


categorias = df_escolas_municipais_privadas['região'].tolist()
y1 = df_escolas_municipais_privadas['Proporção de Crianças de 0 a 4 anos'].tolist()
y2 = df_escolas_municipais_privadas['Proporção Municipal'].tolist()
y3 = df_escolas_municipais_privadas['Proporção Particular'].tolist()

fig = go.Figure()

# Barra isolada (não empilhada)
fig.add_trace(go.Bar( x=categorias,y=y1,name='Crianças de 0 a 4 anos',offsetgroup=1,text=[f"{v:.2f}%" for v in y1],textposition='outside'))

# Barras empilhadas
fig.add_trace(go.Bar(x=categorias,y=y2,name='Escolas Infantis Municipais',offsetgroup=2,text=[f"{v:.2f}%" for v in y2],textposition='inside'))
fig.add_trace(go.Bar(x=categorias,y=y3,name='Escolas Infantis Particulares',offsetgroup=2,base=y2,text=[f"{v:.2f}%" for v in y3],textposition='inside'))

fig.update_layout(barmode='group',title='CRIANÇAS E ESCOLAS INFANTIS POR REGIÃO',yaxis_title='Proporção (%)',xaxis_title='',plot_bgcolor='white')

#Estilizando titulo e comentarios 

fig.update_layout(
    title={'font': {'family': 'Segoe UI', 'size': 21, 'color': '#154389', "weight": "bold"}, 'x': 0, 'xanchor': 'left'}
)
fig.add_annotation(x=1, y=-0.08, xref='paper', yref='paper', text='Fonte: IBGE Censo (2022) / Censo Escolar (2024).',
    showarrow=False,
    font={'size': 10, 'color': '#666'}
)

fig.show()





#fig.write_html('static/iframes/grafico_criancas_creches.html', full_html=True, include_plotlyjs="cdn", config={'displayModeBar': False})

#fig=px.bar(df_escolas_municipais_privadas,x='região',y=['Proporção de Crianças de 0 a 4 anos', 'Proporção Municipal','Proporção Particular'], barmode='group', text_auto=True)
#fig.show()