import pandas as pd
import plotly.express as px
 

df = pd.read_csv("dados_sjc.csv", sep=";")

df = df.drop(columns=["Menos de 1 ano", "1 a 4 anos"], errors="ignore")

df = df.replace("X",0)

for col in df.columns[6:]:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)  

mapeamento_regioes = {
    "Setor Socioeconômico 03": "Centro",
    "Setor Socioeconômico 03A": "Centro",
    "Setor Socioeconômico 04": "Centro",
    "Setor Socioeconômico 20": "Centro",
    "Setor Socioeconômico 26": "Centro",
    "Setor Socioeconômico 09": "Sudeste",
    "Setor Socioeconômico 10": "Sudeste",
    "Setor Socioeconômico 29": "Sudeste",
    "Setor Socioeconômico 01": "Norte",
    "Setor Socioeconômico 01A": "Norte",
    "Setor Socioeconômico 02": "Norte",
    "Setor Socioeconômico 02A": "Norte",
    "Setor Socioeconômico 25": "Norte",
    "Setor Socioeconômico 25A": "Norte",
    "Setor Socioeconômico 11": "Sul",
    "Setor Socioeconômico 12": "Sul",
    "Setor Socioeconômico 13": "Sul",
    "Setor Socioeconômico 14": "Sul",
    "Setor Socioeconômico 15": "Sul",
    "Setor Socioeconômico 16": "Sul",
    "Setor Socioeconômico 28": "Sul",
    "Setor Socioeconômico 05": "Leste",
    "Setor Socioeconômico 05A": "Leste",
    "Setor Socioeconômico 06": "Leste",
    "Setor Socioeconômico 06A": "Leste",
    "Setor Socioeconômico 07": "Leste",
    "Setor Socioeconômico 08": "Leste",
    "Setor Socioeconômico 27": "Leste",
    "Setor Socioeconômico 30": "Leste",
    "Setor Socioeconômico 31": "Leste",
    "Setor Socioeconômico 17": "Oeste",
    "Setor Socioeconômico 17A": "Oeste",
    "Setor Socioeconômico 18": "Oeste",
    "Setor Socioeconômico 19": "Oeste",
    "Setor Socioeconômico 21": "Oeste"
    }

df["Região"] = df["Nome do Bairro"].map(mapeamento_regioes)    

faixas_etarias = [
    "0 a 4 anos", "5 a 9 anos", "10 a 14 anos", "15 a 17 anos",
    "18 e 19 anos", "20 a 24 anos", "25 a 29 anos", "30 a 39 anos",
    "40 a 49 anos", "50 a 59 anos", "60 a 69 anos", "70 anos ou mais"
]

df_regioes = df.groupby("Região")[faixas_etarias].sum().reset_index()

df_regioes["Crianças"] = df_regioes[["0 a 4 anos", "5 a 9 anos"]].sum(axis=1)
df_regioes["Jovens"] = df_regioes[["10 a 14 anos", "15 a 17 anos", "18 e 19 anos", "20 a 24 anos"]].sum(axis=1)
df_regioes["Adultos"] = df_regioes[["25 a 29 anos", "30 a 39 anos", "40 a 49 anos", "50 a 59 anos"]].sum(axis=1)
df_regioes["Idosos"] = df_regioes[["60 a 69 anos", "70 anos ou mais"]].sum(axis=1)

df_faixas = df_regioes[["Região", "Crianças", "Jovens", "Adultos", "Idosos"]]

df_melt = df_faixas.melt(
    id_vars="Região",
    var_name="Faixa Etária",
    value_name="População"
)

fig = px.bar(
    df_melt,
    x="Região",
    y="População",
    color="Faixa Etária",
    title="Distribuição da População por Faixa Etária e Região - São José dos Campos",
    text_auto=True
)

fig.update_layout(
    xaxis_title="Região",
    yaxis_title="População Total",
    title_x=0.5,
    plot_bgcolor="white",
    bargap=0.2
)

fig.show()

