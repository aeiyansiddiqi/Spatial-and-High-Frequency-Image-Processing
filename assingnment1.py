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


# collect file names from command prompt
import alignment1
import sys
import cv2
import numpy as np
import spatial_fusion

args = sys.argv

image1FileName = args[1]
image2FileName = args[2]
keypoints1FileName = args[3]
keypoints2FileName = args[4]

alignment1.alignImage2(image1FileName,image1FileName,keypoints1FileName,keypoints2FileName)
# turn images into grayscale
alignment1.grayScale(image1FileName)
alignment1.grayScale("aligned.jpg")
alignment1.grayScale(image2FileName)
spatial_fusion.gaussianPyramid(image1FileName,4)
spatial_fusion.laplacianPyramid("aligned.jpg",4)
alignment1.hybrid("Gaus-image1.jpg","lapaligned.jpg")
