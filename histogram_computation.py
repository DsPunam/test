# It is a method that improves the contrast in an image, in order to stretch out the intensity range
# by using histogram distribution of pixel intensity in image
import cv2 as cv 
import matplotlib.pyplot as plt 

image=cv.imread("E:/python program/Open CV/Pictures/cat.jpg")
gray_image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)

#HISTOGRAM FOR GRAY SCALE
#cv.calcHist(	images, channels, mask, histSize, ranges[, hist[, accumulate]]	) ->	hist
# images: list of images as numpy arrays. All images must be of the same dtype and same size.
# channels: list of the channels used to calculate the histograms.
# mask: optional mask (8 bit array) of the same size as the input image.
# histSize: histogram sizes in each dimension
# ranges: Array of the dims arrays of the histogram bin boundaries in each dimension
# hist: Output histogram
# accumulate: accumulation flag, enables to compute a single histogram from several sets of arrays.
# Return: It returns an array of

# Yes, histSize is the number of bins in a histogram. It is a parameter that is used to specify the 
# number of bins that the histogram should have. The default value for histSize is 256

hist=cv.calcHist([gray_image],[0],None,[255],[0,255])

# plt.title("histogram for gray image")
# plt.xlabel("bins")
# plt.ylabel("no of pixels")
# plt.plot(hist,color='r')
# plt.show()
# cv.imshow("GRAY_image",gray_image)

#histogram for color image
color=("b","g","r")

plt.title("histogram for color image")
plt.xlabel("bins")
plt.ylabel("no of pixels")
hist_all_channels = []

for i,c in enumerate(color):
    hist=cv.calcHist([image],[i],None,[255],[0,255])
    hist_all_channels.append(hist)
    plt.plot(hist, color=c)

plt.show()
cv.waitKey(0)