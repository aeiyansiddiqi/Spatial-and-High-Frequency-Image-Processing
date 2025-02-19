# Contains the function(s) to read
    # keypoints and perform either
    # rigid (affine) or non-rigid
    # registration

# 1. Alingment
    # It would be easier to start off this with checking
    # if the key files are empty
    # and just resizing the 2nd image
    
    # name of images and key point files
    # will be coming from command line
    # should not be hardcoded
import cv2
import numpy as np


# function that will output aligned image based off image2 and image1's dimensions
def alignImage2(image1FileName, image2FileName, keypoints1FileName,keypoints2FileName):

    # now i should check if the 2 files are empty
    KeypointsFileEmptyBoolean = False
    # open the files
    with open(keypoints1FileName, "r") as keypointFileObj1:
        # check first character
        firstChar = keypointFileObj1.read(1)

        if not firstChar:
            KeypointsFileEmptyBoolean = True

    with open(keypoints2FileName, "r") as keypointFileObj2:
        # check first character
        firstChar = keypointFileObj2.read(1)

        if not firstChar:
            KeypointsFileEmptyBoolean = True

    # Now I'm done checking if the files were empty
    # Lets make the code execution for if the files would
    # have been empty
    if (KeypointsFileEmptyBoolean == True):
        # get dimensions of image one as reference
        image1Obj =cv2.imread(image1FileName)
        heightImage1,widthImage1, _ = image1Obj.shape

        # resize image
        image2Obj = cv2.imread(image2FileName)

        image2Resized_Aligned = cv2.resize(image2Obj,(widthImage1, heightImage1))

        cv2.imwrite("aligned.jpg", image2Resized_Aligned)


    # now we should figure out how to created the aligned
    # image if the keypoint files were not empty
    else:

        #get the images to apply Affine Transformation
        image1Obj = cv2.imread(image1FileName)
        heightImage1,widthImage1, _ = image1Obj.shape
        image2Obj = cv2.imread(image2FileName)

        keypoints1 = np.loadtxt(keypoints1FileName)
        keypoints2 = np.loadtxt(keypoints2FileName)


        # get affine matriz
        affineMatrix, _ = cv2.estimateAffine2D(keypoints2,keypoints1)

        # apply the matrix onto image2 with the dimensions of image1
        allignedImage2 = cv2.warpAffine(image2Obj,affineMatrix,(widthImage1,heightImage1)) 
        image2Resized_Aligned = cv2.resize(image2Obj,(widthImage1, heightImage1))
        cv2.imwrite("aligned.jpg",allignedImage2)




# function to turn images into grayscale
def grayScale(imageFileName):
    imageObj = cv2.imread(imageFileName)
    imageGray = cv2.cvtColor(imageObj,cv2.COLOR_BGR2GRAY)
    cv2.imwrite(imageFileName,imageGray)

# I initally used this for the spatial domain but I am now using it for frequency domain as well
def hybrid(imageFileName1, imageFileName2, name):
    # get weight of images as in alpha and beta
    alpha = 0.4
    beta = 0.6

    
    image1Gaus = cv2.imread(imageFileName1)
    image2Lap = cv2.imread(imageFileName2)

    # get dimensions of image1
    image2Lap = cv2.resize(image2Lap, (image1Gaus.shape[1], image1Gaus.shape[0]))
    # apply with weights of the images, the last arguemtn is 0 as it is meant for Gama, which is brightness
    hybridImage = cv2.addWeighted(image1Gaus,alpha,image2Lap,beta,0)

    #cv2.imwrite("spatial_hybrid.jpg",hybridImage)
    cv2.imwrite(name,hybridImage)
    



        




