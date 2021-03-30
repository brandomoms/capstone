# prepare images for classification
# display image in debugger: import matplotlib.pyplot as plt; plt.matshow( <your nparray> ); plt.show()


import os
import pickle
import numpy as np


mask_polygons_pickle = '../pickles/mask_polygons.p' # XY coordinates of mask
masks_pickle = '../pickles/masks.p' # mask arrays with same dim as images
images_dir ='../images/orig'
save_dir = '../images/rect'


'''
find min area rectangle of black pixels that can fit a given quadrilateral

INPUTS
    poly: a list of 4 tuples, each specifiying the array coordinates of the
          corners of the quadrilateral

(a1, b1)---------(a4, b4)
       |         |
       |         |
       |         |
       |         |
       |         |
       |         |
(a2, b2)---------(a3, b3)
'''
def get_outline_rect(poly):

    a1 = a2 = min([c[0] for c in mask_poly])
    a3 = a4 = max([c[0] for c in mask_poly])
    b1 = b4 = min([c[1] for c in mask_poly])
    b2 = b3 = max([c[1] for c in mask_poly])

    r_h = b2 - b1
    r_w = a4 - a1
    # black rectangle with dim: max(poly_h1, poly_h2) X max(poly_w1, poly_w2)
    blk_rect = np.zeros((r_h, r_w))
    import pdb; pdb.set_trace()
    return blk_rect


# read mask polygons
with open(mask_polygons_pickle, 'rb') as p:
    mask_polygons = pickle.load(p)

# read mask images
with open(masks_pickle, 'rb') as p:
    masks = pickle.load(p)

# read each image
for img in os.listdir(images_dir):
    print(img) #db

    with open(f'{images_dir}/{img}') as src_img:
        cam = img.split('_')[0]
        mask_poly = mask_polygons[cam]

        # create rectangular layer
        rect = get_outline_rect(mask_poly)

        # set values of pixels in rect to pixels in source image if it falls inside the mask




    # generate new image with same dim as rectangle and pixel values set to max of stack layers

    break #db

# write images
# 'rect_' + filename
