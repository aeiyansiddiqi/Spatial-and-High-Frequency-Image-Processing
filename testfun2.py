import frequency_fusion

imagetoFFT = frequency_fusion.imageToFourierDomain("image1.jpg")
rowsOfImage, colOfImage = frequency_fusion.imagePixels("image1.jpg")
filterWindow = frequency_fusion.filterWindowHighFreq(10, rowsOfImage, colOfImage)
imageFFTAppliedFilter = frequency_fusion.applyFilter(imagetoFFT,filterWindow)
frequency_fusion.fftToSpatial(imageFFTAppliedFilter, True)

imagetoFFT = frequency_fusion.imageToFourierDomain("image2.jpg")
rowsOfImage, colOfImage = frequency_fusion.imagePixels("image2.jpg")
filterWindow = frequency_fusion.filterWindowLowFreq(10, rowsOfImage, colOfImage)
imageFFTAppliedFilter = frequency_fusion.applyFilter(imagetoFFT,filterWindow)
frequency_fusion.fftToSpatial(imageFFTAppliedFilter, False)