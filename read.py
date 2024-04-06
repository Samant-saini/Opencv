import cv2 as cv

# #to read the images 
# img=cv.imread("cat.jpg")


# #to display the image
# cv.imshow("cat",img)




#reading videos
capture=cv.VideoCapture("video.mp4") 
while True:
    isTrue, frame=capture.read()
    cv.imshow("video",frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows


