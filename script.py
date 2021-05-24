import pandas as pd
import numpy as np
import os
import pathlib as pth
import openpyxl as xl

# Input values
text_file = r'C:\2105MULTUM\Multum Processing\Multum Processing 1 - formulary NDC-AMT reference file\amt-flat-file.txt'
excel_file = r'C:\2105MULTUM\Multum Processing\Multum Processing 1 - formulary NDC-AMT reference file\Multum Processing 1b - AMT flat file conversion.xlsx'
sheet_name_excel = 'prescriber type (from PBS text)'

df_obj = pd.read_csv(file_loc_name, sep = '\t', header=0, names = column_names)