import os
import plotly.express as px
import pandas as pd
import numpy as np

pasta_dados = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
df_pedidos = pd.read_csv(os.path.join(pasta_dados, "olist_orders_dataset.csv"), nrows=10000)
df_itens = pd.read_csv(os.path.join(pasta_dados, "olist_order_items_dataset.csv"), nrows=10000)
df_pagamentos = pd.read_csv(os.path.join(pasta_dados, "olist_order_payments_dataset.csv"), nrows=10000)
df_produtos = pd.read_csv(os.path.join(pasta_dados, "olist_products_dataset.csv"), nrows=10000)
df_clientes = pd.read_csv(os.path.join(pasta_dados, "olist_customers_dataset.csv"), nrows=10000)
df_merge = df_pedidos.merge(df_pagamentos, on="order_id")
faturamento_total = np.sum(df_merge["payment_value"])
print(f"Faturamento total: R$ {faturamento_total:,.2f}")
faturamento_medio = np.mean(df_merge["payment_value"])
print(f"Ticket médio: R$ {faturamento_medio:,.2f}")
faturamento_maximo = np.max(df_merge["payment_value"])
print(f"Ticket máximo: R$ {faturamento_maximo:,.2f}")
faturamento_minimo = np.min(df_merge["payment_value"])
print(f"Ticket mínimo: R$ {faturamento_minimo:,.2f}")
contador_valores = df_merge["payment_type"].value_counts()
print(contador_valores)
fig_pagamentos = px.pie(values=contador_valores.values, names=contador_valores.index, title="Formas de Pagamento")
df_merge["order_purchase_timestamp"] = pd.to_datetime(df_merge["order_purchase_timestamp"])
df_merge["mes"] = df_merge["order_purchase_timestamp"].dt.month
faturamento_por_mes = df_merge.groupby("mes")["payment_value"].sum()
print(faturamento_por_mes)
fig_faturamento = px.bar(x = faturamento_por_mes.index, y = faturamento_por_mes.values, title = "Faturamento do mes")
fig_faturamento.show()
fig_pagamentos.show()