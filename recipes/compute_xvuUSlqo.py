# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu





# Write recipe outputs
images_s3 = dataiku.Folder("xvuUSlqo")
images_s3_info = images_s3.get_info()
