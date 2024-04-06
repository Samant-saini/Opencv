import cv2 as cv

# #to read the images 
# img=cv.imread("cat.jpg")


# #to display the image
# cv.imshow("cat",img)


def rescale(frame,scale=0.25):
    #this method will work for images , videos , livevideos
    width=int(frame.shape[1]* scale)
    height=int(frame.shape[0]*scale)
    dimension=(width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
    

def res(width,height):

    #only for live web cam video
    capture.set(3,width)
    capture.set(4,height)

capture=cv.VideoCapture("video.mp4") 
while True:
    isTrue, frame=capture.read()


    frame_resize=rescale(frame)
    cv.imshow("video",frame)

    cv.imshow("rescale video",frame_resize)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows