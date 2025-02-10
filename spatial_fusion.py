# Contains the function(s) for creating the hybrid
    # image in the spatial domain
    # using Gaussian/Lapacian pyramids
# Must produce and save spatial_hybrid.jpg
#JPG

# i gotta find away to makea gausian pryramid
# Gausia pyramid is smoothing the image
# but also down sampling it
# I know pyrDown helps with down sampling
# But I also need to smooth it out
# Found a function that smooths
    # GaussianBlur, perfect

import cv2

def gaussianPyramid(imageFileName, numberofLayers):

    imageGausPyrmaid = cv2.imread(imageFileName)
    

    for numberofLayer in range(numberofLayers):
        imageGausPyrmaid = cv2.GaussianBlur(imageGausPyrmaid,(7,7),0)
        imageGausPyrmaid = cv2.pyrDown(imageGausPyrmaid)
