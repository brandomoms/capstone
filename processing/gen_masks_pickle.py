import pickle

mask_polygons = {
    'alaskacam' : [(0, 960), (980, 460), (1127, 460), (600, 955)],
    'fourthavenue' : [(0, 850), (870, 380), (1060, 380), (600, 960)],
    'glennweb' : [(700, 960), (315, 315), (520, 315), (1280, 775)],
    'hilton' : [(936, 877), (294, 536), (430, 521), (1030, 820)],
    'potterws' : [(1280, 960), (1280, 660), (455, 443), (245, 443)],
    'searsmall' : [(1280, 773), (445, 532), (565, 525), (1280, 657)],
    'shipcreek' : [(870, 960), (427, 395), (615, 395), (1280, 850)]
}

pickle.dump(mask_polygons, open('mask_polygons.p','wb'))
