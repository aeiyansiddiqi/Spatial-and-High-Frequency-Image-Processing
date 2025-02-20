# A main Python file (driver script)
    # that can be run to generate all
    # required output files
# It should call the appropriate functions
    # (describe bellow)

# Thoughts:
    # Okay, so I gotta figure out how to
    # 1. Allign the images first
        # If keyfile is given, easy, just change size
        # If keyfile is given, gotta learn how to make
            # it so that the poitns overlap
            # however the image should have the same
            # dimensions as the image1
        # I might as well grayscale all the images after that

    # 2. After alignment is done
        # Figure out spatial domain
            # Gausian Pyramid will give the
            # low detail images
            # Laplacian will give the high
            # detail images
        # Then figure out away to overlap them


    # 3. Figure out Frequncy domain
        # Turn image into FFT
        # Extract heigh freqency from one image
        # Extract low frequency from other image
        # Overlap images to turn hybrid



import alignment1
import sys
import cv2
import numpy as np
import spatial_fusion
import frequency_fusion

################################# collect file names from command prompt #########################

args = sys.argv

image1FileName = args[1]
image2FileName = args[2]
keypoints1FileName = args[3]
keypoints2FileName = args[4]

#################################################################################

###################### Create folder for all the image files that we will be needing for the hybrid images ###################3
import os

folder_name = "roughImageFolder"

os.makedirs(folder_name, exist_ok=True)

####################### Align image ############################################

alignment1.alignImage2(image1FileName,image2FileName,keypoints1FileName,keypoints2FileName)

##################################################################################

################### turn images into grayscale #####################################
alignment1.grayScale(image1FileName)
alignment1.grayScale("aligned.jpg")
alignment1.grayScale(image2FileName)
#####################################################################################

########Get gausisan Image #############################
spatial_fusion.gaussianPyramid("roughImageFolder/" +image1FileName,4)

######## Get Laplacian Image #########################################################
spatial_fusion.laplacianPyramid("roughImageFolder/" +"aligned.jpg",4)

######################## Merge the gausian Image with the laplcian image ########################################
alignment1.hybrid("roughImageFolder/Gaus-image1.jpg","roughImageFolder/lapaligned.jpg","spatial_hybrid.jpg")

##################################################################################################################

############################ Frequency Image ###################################3



## High Freqyency ###########################################################
# turn image into fourier domain
imagetoFFT = frequency_fusion.imageToFourierDomain("roughImageFolder/" +"image1.jpg")
# get the dimensions of the image
rowsOfImage, colOfImage = frequency_fusion.imagePixels("roughImageFolder/" +"image1.jpg")
# create a high frequency filter by erasing all the low frequencies (we do this by erasing all the values in the middle in the form of a circle)
# the radius of the circle is 10 in the current case, the bigger the radius, the more low frequencyeis we are removing
filterWindow = frequency_fusion.filterWindowHighFreq(10, rowsOfImage, colOfImage)
### Apply the filter onto teh image
imageFFTAppliedFilter = frequency_fusion.applyFilter(imagetoFFT,filterWindow)
# Output the high frequency image
frequency_fusion.fftToSpatial(imageFFTAppliedFilter, True)

#imagetoFFT = frequency_fusion.imageToFourierDomain("image2.jpg")
#rowsOfImage, colOfImage = frequency_fusion.imagePixels("image2.jpg")

### Low Frequency ##################################################################

# turn image into fourier domain
imagetoFFT = frequency_fusion.imageToFourierDomain("roughImageFolder/" +"aligned.jpg")
# get the dimensions of the image
rowsOfImage, colOfImage = frequency_fusion.imagePixels("roughImageFolder/" +"aligned.jpg")
# create a high frequency filter by erasing all the low frequencies (we do this by erasing all the values in the middle in the form of a circle)
# the radius of the circle is 10 in the current case, the bigger the radius, the more low frequencyeis we are removing
filterWindow = frequency_fusion.filterWindowLowFreq(10, rowsOfImage, colOfImage)
### Apply the filter onto teh image
imageFFTAppliedFilter = frequency_fusion.applyFilter(imagetoFFT,filterWindow)
# Output the low frequency image
frequency_fusion.fftToSpatial(imageFFTAppliedFilter, False)

alignment1.hybrid("roughImageFolder/lowFreq.jpg","roughImageFolder/highFreq.jpg","frequency_hybrid.jpg")


################################################################################


