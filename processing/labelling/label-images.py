#NOTE#
'''
To run:
    python3 label-images.py images/ images.csv
'''


#TODO#
'''
    - change dtype of `class` col
    - display image
'''


import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image


classes = {
    1 : 'ICE',
    2 : 'SNOW_SLUSH', # was SNOW
    3 : 'TRACK',
    4 : 'CLEAR', # was WET
    5 : 'UNK'
}

num_classes = len(classes)
img_dir = sys.argv[1]
image_csv = sys.argv[2]
images_df = pd.read_csv(image_csv, dtype=str)
for i in range(len(images_df)):
    print(images_df.at[i, 'class'])
    if np.isnan(images_df.at[i, 'class']):
        images_df.at[i, 'class'] = ''
        try:
            if i % 20 == 0:
                print('saving to csv...')
                images_df.to_csv(f'classified_{image_csv}')

            fname = 'images/' + images_df.at[i, 'filename']
            with Image.open(fname, 'r') as pil_im:
                print(fname, f'{i}/{len(images_df)}')

                classified = False
                while not classified:
                    plt.imshow(np.asarray(pil_im))
                    plt.show()
                    inp = input(f'Enter class: '\
                                 '0 - {classes[0]};\n '\
                                 '1 - {classes[1]};\n '\
                                 '2 - {classes[2]};\n  '\
                                 '3 - {classes[3]};\n '\
                                 '4 - {classes[4]};\n '\
                                 '5 - {classes[5]}\n>> '
                    )
                    classes_sel = list(inp)
                    for c in classes_sel:
                        if int(c) in range(len(classes)):
                            images_df.at[i, 'class'] += f'/{classes[int(c)]}'
                            classified = True
                        else:
                            print('!!! unrecognized class selection !!!')
                            break

                print(images_df.at[i, 'class'])

        except Exception as e:
            print()
            print('Exception:')
            print(e)
            print()


print('saving to csv...')
images_df.to_csv(f'classified_{image_csv}')
