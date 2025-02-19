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

def gaussianPyramid(imageFileName, numberOfLayers):

    imageGausPyrmaid = cv2.imread(imageFileName)
    heightImageOG,widthImageOG, _ = imageGausPyrmaid.shape

    for layer in range(numberOfLayers):
        #(3,3) is the intensity of the blur 
        imageGausPyrmaid = cv2.GaussianBlur(imageGausPyrmaid,(3,3),0)
        imageGausPyrmaid = cv2.pyrDown(imageGausPyrmaid)

    # bring image back to normal size
    imageGausPyrmaid = cv2.resize(imageGausPyrmaid,(widthImageOG, heightImageOG))
    # output image after being blured, downsized and brought back up to original size
    #cv2.imwrite("GaussianBlur(" + (str(layer+1)) + ")-" + imageFileName, imageGausPyrmaid)
    cv2.imwrite("Gaus-"+imageFileName, imageGausPyrmaid)

import cv2

def laplacianPyramid(imageFileName, numberOfLayers):

    imageGausPyramid = cv2.imread(imageFileName)
    heightOG, widthOG, _ = imageGausPyramid.shape
    # Have to keep track of images this time from  gausian pyramid
    theGaussianPyramid = [imageGausPyramid]
    
    # Gaussian pyramid
    for i in range(numberOfLayers):
        # Apply Gaussian blur
        imageGausPyramid = cv2.GaussianBlur(imageGausPyramid, (3, 3), 0)
        imageGausPyramid = cv2.pyrDown(imageGausPyramid)
        theGaussianPyramid.append(imageGausPyramid)
    
    

   # we don't need the whole pyramid as we only care about one image for the face merge
    
    # star at 
    for i in range(numberOfLayers-1, 0, -1):
        # get layer from above
        gaussianLayerUp = cv2.pyrUp(theGaussianPyramid[i])
        # get dimensions for resizing, will need it when subtract the 2 layers
        heightcurrentGaus, widthcurrentGaus, _ = theGaussianPyramid[i-1].shape
        # resize image to the layer bellow
        # I have to resize image because I didnt resize it when checking if the keylist were empty
        # maybe I can do that so i don't have to worry abour reziing each time
        gaussianLayerUpAdjustedSize = cv2.resize(gaussianLayerUp, (widthcurrentGaus, heightcurrentGaus))
        # subtract the layer bellow with the current layer, we cna subtract it properly since the size is adjusted
        imagelapPyramid = cv2.subtract(theGaussianPyramid[i-1], gaussianLayerUpAdjustedSize)
        if(i == 2):
            imagelapPyramid = cv2.resize(imagelapPyramid,(widthOG, heightOG))
            cv2.imwrite("lap"+imageFileName, imagelapPyramid)

    





    
