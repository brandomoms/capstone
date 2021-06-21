'''
returns the class (0 for non-hazardous road, 1 for hazardous road) for a given image
'''


import os
import sys
import tensorflow as tf
#from tensorflow import keras
import numpy as np
from shapely.geometry.polygon import Polygon
from shapely.geometry import Point
import pickle
from PIL import Image


# Take a rectangular image and return a list of width X width square sub images
# The squares are taken using a sliding window that filters squares not falling mostly within the given polygon
# Slide by <width> to minimize overlap
def cut_squares(img, poly, width=32, slide=32):
    squares = []
    for y in range(0, img.shape[0] - width, slide):
        for x in range(0, img.shape[1] - width, slide):
            if square_in_poly(x, y, width, poly):
                square = img[y:y+width, x:x+width]
                squares.append(square)
    return squares


# given the upperleft coordinate and size of a square, determine if it falls in polygon
def square_in_poly(s_ul_x, s_ul_y, s_width, poly):
    # check that at lest 6 of check if upper, lower, leftmost, rightmost, and corner points in poly
    c = 0
    poly = Polygon(poly)
    for y in (s_ul_y, s_ul_y + (s_width // 2), s_ul_y + s_width):
        for x in (s_ul_x, s_ul_x + (s_width // 2), s_ul_x + s_width):
            if not poly.contains(Point((x,y))):
                c += 1
    return c < 3


def classify_hzd(image_path, mask):

    # check file path to image is valid
    if not os.path.isfile(image_path):
        sys.exit()

    # load model from file
    model = tf.keras.models.load_model(model_path)
    model.summary()

    # load masks from pickle
    pickle_path = './mask_polygons.p'
    pkl = open(pickle_path, 'rb')
    mask_polygons = pickle.load(pkl)
    pkl.close()

    # split image into squares
    k = image_path.split('/')[-1]
    mask_poly = mask_polygons[mask]
    data = np.asarray(Image.open(image_path))
    squares = cut_squares(data, mask_poly)
    squares = np.array(squares).astype(np.float32) / 255.0

    # classify each square
    classifications = model.predict(squares)

    # log predicted class (0-1, ratio of most common class to total squares)
    hzd_ratio = sum([1 if a[1] > a[0] else 0 for a in classifications]) / len(classifications)
    if hzd_ratio >= 0.5:
        return '1'
    else:
        return '0'
