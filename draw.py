import numpy as np
import cv2 as cv

#creating a window of black colour
blank=np.zeros((500,500,3),dtype="uint8")



#paint the image by certain colour
# blank[:]=0,0,255

# #amking a small section color of the window
# blank[200:300,300:400]=0,255,0

# #draw a rectangle
# cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)#thickness=cv.FILLED or -1(to fill the inside of the reactangle)
# cv.imshow("rectangle",blank)


# cv.circle(blank,(250,250),40,(255,0,255),thickness=-1)
# cv.imshow("circle",blank)

# cv.line(blank,(0,0),(250,350),(0,255,255),thickness=3)


# cv.shape(windowscreeen,from , to ,color, thicknesss)
# cv.imshow("line",blank)



cv.putText(blank,"hello",(255,255),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,134),2)
cv.imshow("text",blank)


cv.imshow("red",blank)
# img=cv.imread("cat.jpg")
# cv.imshow("cat",img)

cv.waitKey(0)