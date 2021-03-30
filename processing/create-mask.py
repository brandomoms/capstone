import sys
import matplotlib.pyplot as plt
import numpy as np
import pdb
from PIL import Image, ImageDraw
import pickle
from matplotlib.pyplot import imshow




# make mask pickles from polygons
mask_polygons = pickle.load(open('mask_polygons.p', 'rb'))
DIM = (1280,960)
masks = {}
for mp in mask_polygons:
    #print(mp)
    poly = mask_polygons[mp]
    mask = Image.new('L', DIM, 0)
    ImageDraw.Draw(mask).polygon(poly, outline=255, fill=255)
    # imshow(mask)
    # plt.show()
    arr = np.array(mask)
    masks[mp] = arr

pickle.dump(masks, open(f'masks.p', 'wb'))
