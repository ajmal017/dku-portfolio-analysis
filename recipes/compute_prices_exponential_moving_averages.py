# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
prices_prepared = dataiku.Dataset("prices_prepared")
df = prices_prepared.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
final_df = pd.DataFrame()

for symbol in df['Symbol'].unique():
    foo = df[df['Symbol']==symbol]
    for lag in [10,20,50,12,26]:
        foo['ema_%s' % str(lag)] = foo['Adj_Close'].ewm(span=lag,min_periods=0,adjust=False,ignore_na=False).mean()
    foo['macd'] = foo['ema_12']-foo['ema_26']
    foo['signal_line'] = foo['macd'].ewm(span=9, adjust=False).mean()
    final_df = final_df.append(foo, ignore_index=True)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
prices_exponential_moving_averages = dataiku.Dataset("prices_exponential_moving_averages")
prices_exponential_moving_averages.write_with_schema(final_df)