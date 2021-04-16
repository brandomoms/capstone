import os
import sys
import tensorflow as tf
from tensorflow import keras
import numpy as np
from shapely.geometry.polygon import Polygon
from shapely.geometry import Point


# need these because polygon vertices are relative to the original images, not the cut rectangles
ORIG_HEIGHT = 960
ORIG_WIDTH = 1280


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


if __name__ == '__main__':

    # check file path to image is valid
    image_path = sys.argv[1]
    if not os.path.isfile(image_path):
        sys.exit()

    # load model from file
    model = tf.keras.models.load_model('saved_model')
    model.summary()

    # load masks from pickle
    pickle_path = './mask_polygons.p'
    pkl = open(pickle_path, 'rb')
    mask_polygons = pickle.load(pkl)
    pkl.close()

    # split image into squares
    cam = sys.argv[2]
    mask_poly = mask_polygons[cam]
    squares = cut_squares(data[img]['img_data'], mask_poly)

    # classify each square
    classifications = [model.predict(s) for s in squares]

    # log class (0-1, ratio of most common class to total squares)
    print(classifications) #TODO change, see comment above
