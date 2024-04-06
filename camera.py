import cv2 as cv 
cap=cv.VideoCapture(0)


while (True):
    isTrue,Frame=cap.read()
    cv.imshow("frame",Frame)
    
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
cap.release()
cv.destroyAllWindows()
 