from src.charts import criar_grafico_status, criar_grafico_pagamentos, criar_grafico_faturamento
from src.data import carregar_dados
from src.layout import criar_layout
from dash import Dash
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
_, _, _, _, _, df_merge = carregar_dados()
app.layout = criar_layout(df_merge)


if __name__ == "__main__":
    app.run(debug=True)