import pandas as pd
import plotly.express as px

#Definindo os DFs
df_populacao = pd.read_csv("dados_sjc_regiao.csv", sep=";")
df_populacao_0a4 = df_populacao.groupby("Região", as_index=False)["0 a 4 anos"].sum()
df_populacao_0a4.head()

df_creche = pd.read_csv("tabela_creche_regiao.csv", sep=",")
df_creche_regiao = df_creche.groupby("Região", as_index=False).size()
df_creche_regiao.rename(columns={'size': 'Creches'}, inplace=True)
df_creche_regiao.head()

#Regiao x População 0 a 4 anos x Creches

df_populacao_creche = pd.merge(df_populacao_0a4, df_creche_regiao, on="Região", how="outer")       # mantém todas as regiões da população; creches ausentes ficam NaN
df_populacao_creche.head()

#Dividir criança por creche
df_populacao_creche["Crianças por Creche"] = df_populacao_creche["0 a 4 anos"] // df_populacao_creche["Creches"]
df_populacao_creche["Crianças por Creche"] = df_populacao_creche["Crianças por Creche"].round(2)
df_populacao_creche = df_populacao_creche.fillna(0)
df_populacao_creche.head()

#Criando Grafico
fig = px.bar(df_populacao_creche,x="Região",y=["0 a 4 anos", "Creches", "Crianças por Creche"],barmode="group",labels={"value": "Quantidade", "variable": "Tipo"},title="Crianças(0 a 4 anos) por Creche", text_auto=True)
fig.update_layout(xaxis_title="Região",yaxis_title="Criança por Creche", title_x=0.5, plot_bgcolor="white", bargap=0.2)

fig.show()