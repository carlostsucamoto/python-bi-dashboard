import os
import pandas as pd
import numpy as np

pasta_dados = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
df_pedidos = pd.read_csv(os.path.join(pasta_dados, "olist_orders_dataset.csv"))
df_itens = pd.read_csv(os.path.join(pasta_dados, "olist_order_items_dataset.csv"))
df_pagamentos = pd.read_csv(os.path.join(pasta_dados, "olist_order_payments_dataset.csv"))
df_produtos = pd.read_csv(os.path.join(pasta_dados, "olist_products_dataset.csv"))
df_clientes = pd.read_csv(os.path.join(pasta_dados, "olist_customers_dataset.csv"))