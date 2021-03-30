# read training image metadata csv

import pandas as pd
import numpy as np
import pickle
from PIL import Image, ImageDraw


df = pd.read_csv('classified_images_excel.csv')

df['class'] = df['class'].astype(str)

def dt_str_to_npdatetime64(row):
    #import pdb; pdb.set_trace()
    d_str, t_str = row.filename.split('_')[1:]
    t_str = t_str[:-4]
    return f'{d_str[:4]}-{d_str[4:6]}-{d_str[6:]}T{t_str[:2]}:{t_str[2:4]}:{t_str[4:]}'

#df['datetime'] = df.apply(lambda row : dt_str_to_npdatetime64(row))
df['datetime'] = df.apply(lambda row : dt_str_to_npdatetime64(row), axis=1)

import pdb; pdb.set_trace()
def split_class_str(row):
    classes = row['class'].split('/')
    return (
        'TRACK' in classes,
        'SNOW_SLUSH' in classes,
        'ICE' in classes,
        'CLEAR' in classes,
        'UNK' in classes
    )


print(df.apply(lambda row : split_class_str(row), axis=1))
df['TRACK'], df['SNOW_SLUSH'], df['ICE'], df['CLEAR'], df['UNK'] = zip(*df.apply(lambda row : split_class_str(row), axis=1))
df.to_csv('split_classes.csv')
print(df)
