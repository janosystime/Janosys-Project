import pandas as pd
import plotly.express as px

df_populacao = pd.read_csv("dados_sjc_regiao.csv", sep=";")
df_populacao_60mais = df_populacao.groupby("Região", as_index=False)[["60 a 69 anos", "70 anos ou mais"]].sum(numeric_only=True)
df_populacao_60mais["60 Mais"] = pd.to_numeric(df_populacao_60mais["60 a 69 anos"], errors="coerce").fillna(0) + pd.to_numeric(df_populacao_60mais["70 anos ou mais"], errors="coerce").fillna(0)
df_populacao_60mais["60 Mais"] = df_populacao_60mais["60 Mais"].astype(int)

df_casa_idoso = pd.read_csv("tabela_casaidoso_regiao.csv", sep=",")
df_casa_idoso_regiao = df_casa_idoso.groupby("Região", as_index=False).size().rename(columns={"size": "qtde_casas"})

df_idoso = pd.merge(df_populacao_60mais[["Região", "60 Mais"]], df_casa_idoso_regiao, on="Região", how="left").fillna({"qtde_casas": 0})
df_idoso["qtde_casas"] = pd.to_numeric(df_idoso["qtde_casas"], errors="coerce").fillna(0).astype(int)

fig = px.bar(df_idoso, x="Região", y=["60 Mais"], barmode="group", labels={"value": "Quantidade", "variable": "Indicador"}, title="Idosos por Região", text_auto=True)
fig.update_layout(xaxis_title="Região <br><br> * Existem apenas quatro unidades da Casa do Idoso na cidade(Norte, Sul, Leste e Oeste)", yaxis_title="Quantidade de Idosos")