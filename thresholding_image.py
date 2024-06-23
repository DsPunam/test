#there are three type of thresholding : they are 
# 1.simple thresholding 
# 2.adaptive thresholding 
# 3.Otsu's thresholding.

import cv2 as cv 

image=cv.imread("E:\python program\Open CV\Pictures\cat.jpg")
cv.imshow("original",image)

#simple thresholding
'''
Here, the matter is straight-forward. For every pixel, the same threshold value is applied. 
If the pixel value is smaller than the threshold, it is set to 0, otherwise it is set to a maximum value. 
The function cv.threshold is used to apply the thresholding. The first argument is the source image, which 
should be a grayscale image. The second argument is the threshold value which is used to classify the pixel values. 
The third argument is the maximum value which is assigned to pixel values exceeding the threshold. OpenCV provides 
different types of thresholding which is given by the fourth parameter of the function. Basic thresholding as 
described above is done by using the type cv.THRESH_BINARY. All simple thresholding types are:

cv.THRESH_BINARY
cv.THRESH_BINARY_INV
cv.THRESH_TRUNC
cv.THRESH_TOZERO
cv.THRESH_TOZERO_INV
'''
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
thresholded_value,thres_img=cv.threshold(gray,150,255,cv.THRESH_BINARY)
thresholded_value,thres_img_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow("thresholded image",thres_img)
cv.imshow("thresholded image inverse",thres_img_inv)
# cv.waitKey(0)

#adaptive thresholding
'''
In the previous section, we used one global value as a threshold. But this might not be good in all cases, 
e.g. if an image has different lighting conditions in different areas. In that case, adaptive thresholding can help.
Here, the algorithm determines the threshold for a pixel based on a small region around it. So we get different 
thresholds for different regions of the same image which gives better results for images with varying illumination.

In addition to the parameters described above, the method cv.adaptiveThreshold takes three input parameters:

The adaptiveMethod decides how the threshold value is calculated:

cv.ADAPTIVE_THRESH_MEAN_C: The threshold value is the mean of the neighbourhood area minus the constant C.
cv.ADAPTIVE_THRESH_GAUSSIAN_C: The threshold value is a gaussian-weighted sum of the neighbourhood values minus the 
                               constant C.
The blockSize determines the size of the neighbourhood area and C is a constant that is subtracted from the mean or 
weighted sum of the neighbourhood pixels.
'''
adaptive_thres=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,5)
cv.imshow("adaptive threshold",adaptive_thres)
# cv.waitKey(0)

#otsu's thresholding
'''
In global thresholding, we used an arbitrary chosen value as a threshold. In contrast, Otsu's method avoids 
having to choose a value and determines it automatically.

Consider an image with only two distinct image values (bimodal image), where the histogram would only consist 
of two peaks. A good threshold would be in the middle of those two values. Similarly, Otsu's method determines 
an optimal global threshold value from the image histogram.

In order to do so, the cv.threshold() function is used, where cv.THRESH_OTSU is passed as an extra flag. 
The threshold value can be chosen arbitrary. The algorithm then finds the optimal threshold value which is 
returned as the first output.
'''
thresholded_value1,otsu_thres_img=cv.threshold(gray,150,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imshow("otsu thresholded image",otsu_thres_img)

cv.waitKey(0)