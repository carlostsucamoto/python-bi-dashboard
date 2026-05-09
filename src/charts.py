import plotly.express as px
import pandas as pd

def criar_grafico_status(df):
    status = df["order_status"].value_counts()
    fig_status = px.bar(x=status.index, y=status.values, title="Status da compra", template="plotly_dark")

    return fig_status

def criar_grafico_pagamentos(df):
    contador_valores = df["payment_type"].value_counts()
    fig_pagamentos = px.pie(values=contador_valores.values, names=contador_valores.index, title="Formas de Pagamento",template="plotly_dark")



    return fig_pagamentos

def criar_grafico_faturamento(df):
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
    df["mes"] = df["order_purchase_timestamp"].dt.month
    contador_valores = df["payment_type"].value_counts()
    faturamento_por_mes = df.groupby("mes")["payment_value"].sum()
    fig_faturamento = px.bar(x = faturamento_por_mes.index, y = faturamento_por_mes.values, title = "Faturamento do mes",template="plotly_dark")
    return fig_faturamento