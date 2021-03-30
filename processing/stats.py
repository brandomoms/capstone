# select relevant part of image using mask, and associate the resulting array with the appropriate record from the csv

import os
import pickle
from PIL import Image, ImageDraw
import numpy as np
from matplotlib.pyplot import imshow
import time

masks = pickle.load(open('masks.p', 'rb'))

stats = {}

image_dir = 'sample_images'
for image_file in os.listdir(image_dir):
    if (image_file[-4:] == '.jpg'):

        # read image as array
        pil_im = Image.open(f'{image_dir}/{image_file}', 'r')
        arr = np.asarray(pil_im)
        #print(arr.shape)

        # mask image
        cam = image_file.split('_')[0]
        mask = masks[cam]

        stats[image_file] = {
            'red' : [],
            'green' : [],
            'blue' : []
        }

        for i in range(mask.shape[0]):
            for j in range(mask.shape[1]):
                if mask[i][j] != 0:
                    stats[image_file]['red'].append(arr[i][j][0])
                    stats[image_file]['green'].append(arr[i][j][1])
                    stats[image_file]['blue'].append(arr[i][j][2])

import pdb; pdb.set_trace()
