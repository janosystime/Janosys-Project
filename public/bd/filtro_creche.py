import pandas as pd
import plotly.express as px

#Definindo os DFs
df_populacao = pd.read_csv("public/bd/dados_sjc_regiao.csv", sep=";")
df_populacao_0a4 = df_populacao.groupby("Região", as_index=False)["0 a 4 anos"].sum()
df_populacao

df_creche = pd.read_csv("public/bd/tabela_creche_regiao.csv", sep=",")
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

#Crianças e Creches em Relação Total/Região
df_populacao_creche["Crianças %Total"] = (df_populacao_creche["0 a 4 anos"] / (df_populacao_creche["0 a 4 anos"].sum())*100).round(2)
df_populacao_creche["Creches %Total"] = (df_populacao_creche["Creches"] / (df_populacao_creche["Creches"].sum())*100).round(2)
df_populacao_creche.head()

#Criando Grafico com todos os dados
fig = px.bar(df_populacao_creche,x="Região",y=["0 a 4 anos", "Creches", "Crianças por Creche", "Crianças %Total", "Creches %Total"],barmode="group",labels={"value": "Quantidade", "variable": "Tipo"},title="Crianças(0 a 4 anos) por Creche", text_auto=True)
fig.update_layout(xaxis_title="Região",yaxis_title="Criança por Creche", title_x=0.5, plot_bgcolor="white", bargap=0.2)


#Criando Grafico com relação ao total/tegião" 
fig = px.bar(df_populacao_creche,x="Região",y=["Crianças %Total", "Creches %Total"],barmode="group",labels={"value": "Quantidade", "variable": "Tipo"},title="Crianças e Creches por Região em Relação ao Total da Cidade", text_auto=True)
fig.update_layout(xaxis_title="Região",yaxis_title="%", title_x=0.5, plot_bgcolor="white", bargap=0.2)

fig.show()