import cv2
import numpy as np


# event=[i for i in dir(cv2) if "EVENT" in i]
# print(event)

def clickEvent(event,x,y, flag, param):
        if event==cv2.EVENT_LBUTTONDOWN:
            cv2.circle(img,(x,y),2,(0,255,255),-1)
            points.append((x,y))
            if len(points)>=2:
                   cv2.line(img,points[-1],points[-2],(25,250,0),6)
            cv2.imshow("image",img)

        if event==cv2.EVENT_RBUTTONDOWN:
                blue=img[y,x,0]
                green=img[y,x,1]
                red=img[y,x,2]
                cv2.circle(img,(x,y),2,(0,255,255),-1)
                mycolorimage=np.zeros((512,512,3),np.uint8)
                mycolorimage[:]=[blue,green, red]
                cv2.imshow("color",mycolorimage)
              
# img=np.zeros((512,512,3), np.uint8)
img=cv2.imread("cat.jpg")

points=[]

cv2.imshow("image",img)
#cv2.setMouseCallback(image,event)
cv2.setMouseCallback("image",clickEvent)
cv2.waitKey(0)
cv2.destroyAllWindows()    
    