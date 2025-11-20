import pandas as pd
import plotly.express as px

## Renda Media 2010
## Renda media em 2010 = 3669.52
df_renda_pc_2010 = pd.read_csv('public/bd/df_renda_media_regiao.csv', sep=',')
df_renda_pc_2010["Desvio %"] = (df_renda_pc_2010['renda_media_2010'] / 3669.52)
df_renda_pc_2010["Diferença %"] = ((df_renda_pc_2010['Desvio %'] -1)*100).apply(lambda x: f"{x:.2f}%")
df_renda = df_renda_pc_2010

## Renda Media 2025
## Renda media em 2025 = 4072.97
df_renda["Projeção 2025"] =  (df_renda['Desvio %'] * 4072.97).round(2)
df_renda

## Desvio Padrão


## Calculo Bruto ZO



## Printar Grafico
fig = px.line(df_renda, x='regiao', y=['Diferença %', 'renda_media_2010'], text='Diferença %')
fig.add_shape(
type="line",
x0=df_renda['regiao'].iloc[0],   # início da linha em x
x1=df_renda['regiao'].iloc[-1],  # fim da linha em x
y0=3669.52, y1=3669.52,                      # valor constante no eixo y
line=dict(color="red", width=2, dash="dash"),  # cor e estilo
xref="x", yref="y")
fig.add_annotation(
x=df_renda['regiao'].iloc[0],   # pode ser o fim ou o início, ajuste como preferir
y=3669.52,
text="R$ 3.669,52",
showarrow=False,
font=dict(color="red", size=12),
xanchor="left",
yanchor="bottom"
)
fig.update_layout(xaxis_title=" ",yaxis_title="Rendimento Médio (2010)", title_x=0.5, plot_bgcolor="white", bargap=0.2, showlegend=False)
fig.update_traces(textposition='top right')
fig.show()
fig.write_html('public/bd/grafico_renda.html', full_html=True, include_plotlyjs="cdn")

