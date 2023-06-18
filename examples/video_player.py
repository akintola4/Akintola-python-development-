# We will use this file to play the video

#import the required module
import cv2

#define a function to play the video
def playVideo():
    #create a video capture object
    cv2.namedWindow("Empty Window", cv2.WINDOW_NORMAL)
    #here we create a window to display the video
    cv2.resizeWindow("Empty Window", 600, 600)
    #here we resize the window
    cv2.waitKey(0)
    #here we wait for a key to be pressed
    cv2.destroyAllWindows()
    #here we destroy all the windows
    playVideo()
    #here we call the function again to play the video again
