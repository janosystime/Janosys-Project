import pandas as pd 
import plotly.express as px

## População 60+ por região

df_populacao = pd.read_csv("public/bd/dados_sjc_regiao.csv", sep=";")
df_populacao_idosa = df_populacao.groupby("Região", as_index=False)[["60 a 69 anos", "70 anos ou mais"]].sum()
df_populacao_idosa["60+"] = df_populacao_idosa["60 a 69 anos"] + df_populacao_idosa["70 anos ou mais"]
df_populacao_60mais = df_populacao_idosa[["Região", "60+"]]
df_populacao_60mais

## Ubs por Região

df_ubs = pd.read_csv("public/bd/UBS_por_regiao.csv", sep=",")
df_ubs_regiao = df_ubs.groupby("Região", as_index=False)["Nome da UBS"].size()
df_ubs_regiao

## DF idoso e UBS
df_idoso_ubs = pd.merge(df_populacao_60mais, df_ubs_regiao, on="Região", how="outer")       # mantém todas as regiões da população; creches ausentes ficam NaN
df_idoso_ubs

## Idoso e UBS % Total
df_idoso_ubs["Idosos"] = ((df_idoso_ubs["60+"] / (df_idoso_ubs["60+"].sum()))*100).round(2)
df_idoso_ubs["Unidades Básicas de Saúde"] = ((df_idoso_ubs["size"] / (df_idoso_ubs["size"].sum()))*100).round(2)

df_idoso_ubs

#Criando Grafico com relação ao total/tegião" 
fig = px.bar(df_idoso_ubs,x="Região",y=["Idosos", "Unidades Básicas de Saúde"],barmode="group",labels={"value": "Quantidade", "variable": "Tipo"},title="IDOSOS E UBS POR REGIÃO", text_auto=True)
fig.update_layout(xaxis_title="",yaxis_title="%", title_x=0.5, plot_bgcolor="white", bargap=0.2)

fig.update_layout(
    title={'font': {'family': 'Segoe UI', 'size': 21, 'color': '#154389', "weight": "bold"}, 'x': 0, 'xanchor': 'left'})
fig.add_annotation(x=1, y=-0.08, xref='paper', yref='paper', text='Fonte: IBGE Censo (2022) / PMSJC.', showarrow=False, font={'size': 10, 'color': '#666'})



fig.show()

#fig.write_html('static/iframes/grafico_idoso_ubs.html', full_html=True, include_plotlyjs="cdn", config={'displayModeBar': False})
