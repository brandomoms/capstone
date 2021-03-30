import sys
import matplotlib.pyplot as plt
import numpy as np
import pdb
from PIL import Image, ImageDraw

image_path = sys.argv[1]
with Image.open(image_path, 'r') as im:
    print(np.asarray(im).shape)
    # draw = ImageDraw.Draw(im)
    # road_poly = [(870, 960), (427, 395), (615, 395), (1280, 850)]
    # draw.polygon(road_poly, fill='red')
    #
    # #mask[rr, cc] = False
    # #mask = np.ones(shape=image.shape[0:2], dtype="bool")
    #
    # plt.imshow(np.asarray(im))
    # plt.show()
    #import pdb; pdb.set_trace()
