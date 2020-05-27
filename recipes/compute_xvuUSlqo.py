# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu


input_folder = dataiku.Folder('aktVDyjf')
s3_folder = dataiku.Folder('xvuUSlqo')



with open("local_file_to_upload") as f:
    folder.upload_stream("name_of_file_in_folder", f)


# Write recipe outputs
images_s3 = dataiku.Folder("xvuUSlqo")
images_s3_info = images_s3.get_info()
