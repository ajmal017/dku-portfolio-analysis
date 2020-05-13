# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE_MAGIC_CELL
# Automatically replaced inline charts by "no-op" charts
# %pylab inline
import matplotlib
matplotlib.use("Agg")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
from dataiku import pandasutils as pdu
import pandas as pd
import requests
import json

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
api_key = dataiku.get_custom_variables(project_key='PORTFOLIOANALYSIS').get('api_alpha')

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
url = 'https://www.alphavantage.co/query'

def get_daily_ts(symbol):

    data = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": symbol,
        "apikey": api_key,
        "outputsize": "compact"
        }

    r = requests.get(url, params=data)
    df = pd.DataFrame(json.loads(r.text).get('Time Series (Daily)')).transpose().reset_index()
    df.columns = ['Date','Open','High','Low','Close','Adj_Close','Volume','Dividend_amount','Split_coeff']
    df.insert(loc=1, column='Symbol', value=symbol)
    return df

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import os
import json

folder_path = dataiku.Folder('conf').get_path()
file_path = os.path.join(folder_path,'portfolio.json')

with open(file_path,'rb') as f:
    holdings = json.load(f)

symbols = [position.get('name') for position in holdings['holdings']]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
end_df = pd.DataFrame()

for symbol in symbols:
    df = get_daily_ts(symbol)
    end_df = end_df.append(df, ignore_index=True)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Recipe outputs
v21fn3jz = dataiku.Folder("V21Fn3jz")
v21fn3jz_info = v21fn3jz.get_info()