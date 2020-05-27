# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import os

input_folder = dataiku.Folder('aktVDyjf')
s3_folder = dataiku.Folder('xvuUSlqo')

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
input_path = input_folder.get_path()

for file_path in input_folder.list_paths_in_partition():
    full_path = os.path.join(input_path, file_path.replace('/',''))
    s3_folder.upload_file(file_path, full_path)