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
        image1Obj = cv2.imread("image1.jpg")
        heightImage1,widthImage1, _ = image1Obj.shape
        image2Obj = cv2.imread("image2.jpg")

        keypoints1 = np.loadtxt(keypoints1FileName)
        keypoints2 = np.loadtxt(keypoints2FileName)

        # estimateAffine2D expects floating points

        affineMatrix, _ = cv2.estimateAffine2D(keypoints2,keypoints1)

        allignedImage2 = cv2.warpAffine(image2Obj,affineMatrix,(widthImage1,heightImage1)) 
        image2Resized_Aligned = cv2.resize(image2Obj,(widthImage1, heightImage1))
        cv2.imwrite("aligned.jpg",allignedImage2)




def grayScale(imageFileName):
    imageObj = cv2.imread(imageFileName)
    imageGray = cv2.cvtColor(imageObj,cv2.COLOR_BGR2GRAY)
    cv2.imwrite(imageFileName,imageGray)

def hybrid(imageFileName1, imageFileName2, name):
    alpha = 0.5
    beta = 0.5

    image1Gaus = cv2.imread(imageFileName1)
    image2Lap = cv2.imread(imageFileName2)

    image2Lap = cv2.resize(image2Lap, (image1Gaus.shape[1], image1Gaus.shape[0]))
    hybridImage = cv2.addWeighted(image1Gaus,alpha,image2Lap,beta,0)

    #cv2.imwrite("spatial_hybrid.jpg",hybridImage)
    cv2.imwrite(name,hybridImage)
    



        




