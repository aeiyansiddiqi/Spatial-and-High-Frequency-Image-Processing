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
def imageToFourierDomain(imageName):
    imagetoFFT= cv2.imread(imageName)
    imagetoFFT = cv2.cvtColor(imagetoFFT,cv2.COLOR_BGR2GRAY)
    imagetoFFT = np.float32(imagetoFFT)
    imagetoFFT = np.fft.fft2(imagetoFFT)
    imagetoFFT = np.fft.fftshift(imagetoFFT)

    return imagetoFFT

def imagePixels(imageName):
    imageForDimnesionExtraction = cv2.imread(imageName)
    rowsOfImage, columnsOfImage, _ = imageForDimnesionExtraction.shape

    return rowsOfImage, columnsOfImage

def filterWindowHighFreq( desiredLevelofFilter, imageRows, imageCols):
    #fftImage = imageToFourierDomain(imageName)
    #imageRows, imageCols = imagePixels(imageName)
    imageCenterRow = imageRows //2
    imageCenterCol = imageCols //2
    ## create window the size of the whoel image, we're not going to slide the window, just apply it on the whole thing
    filterWindow = np.ones((imageRows, imageCols), dtype=np.uint8)

    for rowPixel in range(imageRows):
        for columnPixel in range(imageCols):
            #d = √[(x2 - x1)2 + (y2 - y1)2
            distance = np.sqrt((rowPixel-imageCenterRow)**2 + (columnPixel-imageCenterCol)**2)
            if (distance <= desiredLevelofFilter ):
                filterWindow[rowPixel,columnPixel] = 0
    
    #imageFFTAppliedFilter = fftImage * filterWindow

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
            distance = np.sqrt((rowPixel-imageCenterRow)**2 + (columnPixel-imageCenterCol)**2)
            if (distance > desiredLevelofFilter ):
                filterWindow[rowPixel,columnPixel] = 0
    
    #imageFFTAppliedFilter = fftImage * filterWindow

    return filterWindow


def applyFilter(fftImage, filterWindow):
    imageFFTAppliedFilter = fftImage * filterWindow
    return imageFFTAppliedFilter

def fftToSpatial(imageFFTAppliedFilter, booleanForHighorLow):
    # opposite of imagetoForurierDomain
    # inverse it

    imagetoFFT = np.fft.ifftshift(imageFFTAppliedFilter)
    spatialImage = np.fft.ifft2(imagetoFFT)
    spatialImage =np.abs(spatialImage)
    # getting errors [ WARN:0@1.282] global loadsave.cpp:848 imwrite_ Unsupported depth image for selected encoder is fallbacked to CV_8U.
    #spatialImage = np.uint8(np.clip(spatialImage, 0, 255))
    spatialImage = np.uint8(spatialImage)
    if booleanForHighorLow == True:
        cv2.imwrite("highFreq.jpg", spatialImage)
    else:
        cv2.imwrite("lowFreq.jpg", spatialImage)













