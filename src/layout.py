import dash_bootstrap_components as dbc
from dash import html, dcc
from src.charts import criar_grafico_status, criar_grafico_pagamentos, criar_grafico_faturamento

def criar_layout(df):
    fig_status = criar_grafico_status(df)
    fig_pagamentos = criar_grafico_pagamentos(df)
    fig_faturamento = criar_grafico_faturamento(df)

    faturamento_total = df["payment_value"].sum()
    faturamento_medio = df["payment_value"].mean()
    faturamento_maximo = df["payment_value"].max()
    faturamento_minimo = df["payment_value"].min()
    return dbc.Container([
    html.H1("Dashboard de E-commerce Olist", className="text-center my-4"),
    
    dbc.Row([
    dbc.Col(dbc.Card(dbc.CardBody([
        html.P("Faturamento Total", style={"margin": "0"}),
        html.H6(f"R$ {faturamento_total:,.2f}")
    ]), style={"textAlign": "center", "padding": "5px", "height": "100px"}), width=3),
    dbc.Col(dbc.Card(dbc.CardBody([
        html.P("Ticket Médio", style={"margin": "0"}),
        html.H6(f"R$ {faturamento_medio:,.2f}")
    ]), style={"textAlign": "center", "padding": "5px", "height": "100px"}), width=3),
    dbc.Col(dbc.Card(dbc.CardBody([
        html.P("Ticket Máximo", style={"margin": "0"}),
        html.H6(f"R$ {faturamento_maximo:,.2f}")
    ]), style={"textAlign": "center", "padding": "5px", "height": "100px"}), width=3),
    dbc.Col(dbc.Card(dbc.CardBody([
        html.P("Ticket Mínimo", style={"margin": "0"}),
        html.H6(f"R$ {faturamento_minimo:,.2f}")
    ]), style={"textAlign": "center", "padding": "5px", "height": "100px"}), width=3),
], className="mb-4"),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_pagamentos), width=6),
        dbc.Col(dcc.Graph(figure=fig_faturamento), width=6),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_status), width=12),
    ]),
], fluid=True)
