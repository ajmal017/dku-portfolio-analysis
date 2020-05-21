# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
prices_prepared = dataiku.Dataset("prices_prepared")
prices_prepared_df = prices_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

prices_rsi_df = prices_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
prices_rsi = dataiku.Dataset("prices_rsi")
prices_rsi.write_with_schema(prices_rsi_df)
