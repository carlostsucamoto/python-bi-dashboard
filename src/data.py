import os
import pandas as pd
import numpy as np


def carregar_dados():
    pasta_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pasta_dados = os.path.join(pasta_raiz, "data")

    df_pedidos = pd.read_csv(os.path.join(pasta_dados, "olist_orders_dataset.csv"), nrows=10000)
    df_itens = pd.read_csv(os.path.join(pasta_dados, "olist_order_items_dataset.csv"), nrows=10000)
    df_pagamentos = pd.read_csv(os.path.join(pasta_dados, "olist_order_payments_dataset.csv"), nrows=10000)
    df_produtos = pd.read_csv(os.path.join(pasta_dados, "olist_products_dataset.csv"), nrows=10000)
    df_clientes = pd.read_csv(os.path.join(pasta_dados, "olist_customers_dataset.csv"), nrows=10000)
    df_merge = df_pedidos.merge(df_pagamentos, on="order_id")

    print(pasta_raiz)
    return df_pedidos, df_itens, df_pagamentos, df_produtos, df_clientes, df_merge


carregar_dados()