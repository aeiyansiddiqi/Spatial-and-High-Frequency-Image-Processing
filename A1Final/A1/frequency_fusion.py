# Contains the function(s) for creating
    # the hybrid image in the frequency
    # domain using FFT-based filters
    # Must produce and save
    # frequency_hybrid.jpg

#Frequency-Domain Hybrid (30%)
    #Implementation (20%)
    # Correct usage of FFT-based filtering (high-pass and low-pass).
    # Handling of padding, frequency masks, and inverse transforms.


import numpy as np
import cv2

# we first have to figure out away to bring the imge to the Fourier Domain

# convert image to fourier domain
def imageToFourierDomain(imageName):
    imagetoFFT= cv2.imread(imageName)
    # image is already grayscsaled, just doing it again because I was having issues with using .shape
    imagetoFFT = cv2.cvtColor(imagetoFFT,cv2.COLOR_BGR2GRAY)
    imagetoFFT = np.float32(imagetoFFT)
    imagetoFFT = np.fft.fft2(imagetoFFT)
    # shift low frequencies to the center
    imagetoFFT = np.fft.fftshift(imagetoFFT)

    return imagetoFFT

# get dimensions of image we plan on doing the filter on
def imagePixels(imageName):
    imageForDimnesionExtraction = cv2.imread(imageName)
    rowsOfImage, columnsOfImage, _ = imageForDimnesionExtraction.shape

    return rowsOfImage, columnsOfImage

# 
def filterWindowHighFreq( desiredLevelofFilter, imageRows, imageCols):
    #fftImage = imageToFourierDomain(imageName)
    #imageRows, imageCols = imagePixels(imageName)
    # get center pixels of image
    imageCenterRow = imageRows //2
    imageCenterCol = imageCols //2
    # create window the size of the whoel image, we're not going to slide the window, just apply it on the whole thing
    filterWindow = np.ones((imageRows, imageCols), dtype=np.uint8)
    # go through every pixel
    for rowPixel in range(imageRows):
        for columnPixel in range(imageCols):
            #d = √[(x2 - x1)2 + (y2 - y1)2
            # use eucledian distance formula
            # check the pixels distance from the center is less than the deriedLevelofFilter (aka radius)
            # if it is, turn all the values into a 0, aka, a black circle in the middle
            distance = np.sqrt((rowPixel-imageCenterRow)**2 + (columnPixel-imageCenterCol)**2)
            if (distance <= desiredLevelofFilter ):
                filterWindow[rowPixel,columnPixel] = 0
    

    return filterWindow

def filterWindowLowFreq( desiredLevelofFilter, imageRows, imageCols):
    #fftImage = imageToFourierDomain(imageName)
    #imageRows, imageCols = imagePixels(imageName)
    imageCenterRow = imageRows //2
    imageCenterCol = imageCols //2
    ## create window the size of the whoel image, we're not going to slide the window, just apply it on the whole thing
    filterWindow = np.ones((imageRows, imageCols), dtype=np.uint8)


    for rowPixel in range(imageRows):
        for columnPixel in range(imageCols):
            #d = √[(x2 - x1)2 + (y2 - y1)2
            # check the pixels distance from the center is more than the deriedLevelofFilter (aka radius)
            # if it is, turn all the values into a 0, aka, all values except for the circle in the middle will be 0 or black
            distance = np.sqrt((rowPixel-imageCenterRow)**2 + (columnPixel-imageCenterCol)**2)
            if (distance > desiredLevelofFilter ):
                filterWindow[rowPixel,columnPixel] = 0
    

    return filterWindow


# apply the filter
def applyFilter(fftImage, filterWindow):
    imageFFTAppliedFilter = fftImage * filterWindow
    return imageFFTAppliedFilter

# bring image back to spatial, it is opposite of how we brought it into foruier
def fftToSpatial(imageFFTAppliedFilter, booleanForHighorLow):
    # opposite of imagetoForurierDomain
    # inverse it

    imagetoFFT = np.fft.ifftshift(imageFFTAppliedFilter)
    spatialImage = np.fft.ifft2(imagetoFFT)
    # was having trouble brining image back to saptial domain
    # as I was getting warnings that the system was 
    # automatically adjusting the encoding, this will help convert complex values to real values and avoid the warnings
    spatialImage =np.abs(spatialImage)
    # getting warnings [ WARN:0@1.282] global loadsave.cpp:848 imwrite_ Unsupported depth image for selected encoder is fallbacked to CV_8U.
    
    spatialImage = np.uint8(spatialImage)
    if booleanForHighorLow == True:
        cv2.imwrite("roughImageFolder/highFreq.jpg", spatialImage)
    else:
        cv2.imwrite("roughImageFolder/lowFreq.jpg", spatialImage)













