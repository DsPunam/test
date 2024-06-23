import cv2 as cv
import numpy as np 

blank=np.zeros((255,255,3),dtype="uint8")
#blank[:]=(100,50,200)
#cv.imshow("blank_image",blank)

#drawing a rectangle
rectangle=cv.rectangle(blank,(100,100),(200,200),(100,50,200),cv.FILLED)    #cv2.rectangle(image, start_point, end_point, color, thickness)
#cv.imshow("rectangle",rectangle)

circle=cv.circle(blank,(200,200),50,(255,0,0),cv.FILLED)     #cv2.circle(image, center_coordinates, radius, color, thickness)
#cv.imshow("circle",circle)

line=cv.line(blank,(100,100),(200,200),(255,255,255),2)     #cv2.line(image, start_point, end_point, color, thickness)
#cv.imshow("line",line)

#cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
text=cv.putText(blank,"Hello, my name is Punam Chatterjee.",(0,10),cv.FONT_HERSHEY_TRIPLEX,0.5,(255,0,0),1)
cv.imshow("text",text)
cv.waitKey(0)