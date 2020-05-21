# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
prices_prepared = dataiku.Dataset("prices_prepared")
df = prices_prepared.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df['Close_shifted'] = df.groupby(['Symbol'])['Close'].shift(1)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df['Close_shifted'] = df['Close_shifted'].fillna(df['Close'])
df['perc_change'] = 100*(df['Close']-df['Close_shifted'])/df['Close_shifted']

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df['up'] = df['perc_change'].apply(lambda x: x if x >0 else 0)
df['down'] = df['perc_change'].apply(lambda x: x if x<0 else 0)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df['up_mean'] = df.groupby('Symbol')['up'].transform(lambda x: x.rolling(14, 1).mean())
df['down_mean'] = df.groupby('Symbol')['down'].abs().transform(lambda x: x.rolling(14, 1).mean())

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df['rs_sma'] = df['up_mean'] / df['down_mean']

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df['rsi_sma'] = 100 - 100 / (1+df['rs_sma'])
df['overbought'] = df['rsi_sma'].apply(lambda x: 1 if x>=70 else 0)
df['oversold'] = df['rsi_sma'].apply(lambda x: 1 if x <= 30 else 0)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
prices_rsi = dataiku.Dataset("prices_rsi")
prices_rsi.write_with_schema(df)