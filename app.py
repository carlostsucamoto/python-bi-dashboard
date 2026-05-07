import os
import plotly.express as px
import pandas as pd
import numpy as np
from dash import Dash, html, dcc

app = Dash(__name__)
pasta_dados = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
df_pedidos = pd.read_csv(os.path.join(pasta_dados, "olist_orders_dataset.csv"), nrows=10000)
df_itens = pd.read_csv(os.path.join(pasta_dados, "olist_order_items_dataset.csv"), nrows=10000)
df_pagamentos = pd.read_csv(os.path.join(pasta_dados, "olist_order_payments_dataset.csv"), nrows=10000)
df_produtos = pd.read_csv(os.path.join(pasta_dados, "olist_products_dataset.csv"), nrows=10000)
df_clientes = pd.read_csv(os.path.join(pasta_dados, "olist_customers_dataset.csv"), nrows=10000)
df_merge = df_pedidos.merge(df_pagamentos, on="order_id")
faturamento_total = np.sum(df_merge["payment_value"])
faturamento_medio = np.mean(df_merge["payment_value"])
faturamento_maximo = np.max(df_merge["payment_value"])
faturamento_minimo = np.min(df_merge["payment_value"])
contador_valores = df_merge["payment_type"].value_counts()

fig_pagamentos = px.pie(values=contador_valores.values, names=contador_valores.index, title="Formas de Pagamento")
df_merge["order_purchase_timestamp"] = pd.to_datetime(df_merge["order_purchase_timestamp"])
df_merge["mes"] = df_merge["order_purchase_timestamp"].dt.month
faturamento_por_mes = df_merge.groupby("mes")["payment_value"].sum()

fig_faturamento = px.bar(x = faturamento_por_mes.index, y = faturamento_por_mes.values, title = "Faturamento do mes")
app.layout = html.Div(children=[
    html.H1("Dashboard de E-commerce Olist"),
    dcc.Graph(figure=fig_pagamentos),
    dcc.Graph(figure=fig_faturamento),
])
if __name__ == "__main__":
    app.run(debug=True)