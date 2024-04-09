import cv2
import numpy as np


# event=[i for i in dir(cv2) if "EVENT" in i]
# print(event)

def clickEvent(event,x,y, flag, param):
        if event==cv2.EVENT_LBUTTONDOWN:
            print(x,',',y)
            font=cv2.FONT_HERSHEY_SIMPLEX
            STRX=str(x)+','+str(y)
            cv2.putText(img,STRX,(x,y),font, 1,(255,255,0),2)
            cv2.imshow("image",img)

        if event==cv2.EVENT_RBUTTONDOWN:
                blue=img[y,x,0]
                green=img[y,x,1]
                red=img[y,x,2]
                print(blue,',',red,",",green)
                font=cv2.FONT_HERSHEY_SIMPLEX
                STRbgr=str(blue)+','+str(green)+','+str(red)
                cv2.putText(img,STRbgr,(x,y),font, 1,(255,0,255),2)
                cv2.imshow("image",img)
              
# img=np.zeros((512,512,3), np.uint8)
img=cv2.imread("cat.jpg")

cv2.imshow("image",img)
#cv2.setMouseCallback(image,event)
cv2.setMouseCallback("image",clickEvent)
cv2.waitKey(0)
cv2.destroyAllWindows()    
    