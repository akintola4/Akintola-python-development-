#we can play a video from a file using the following code
import cv2
#here we import the opencv module

# Open the video file
video_path = 'test_video.mp4'
video = cv2.VideoCapture(video_path)

# Check if the video file was successfully opened
if not video.isOpened():
    print("Error opening video file")
    exit()

# Read and display frames from the video
while video.isOpened():
    ret, frame = video.read()

    if ret:
        # Display the frame (you can perform additional processing here)
        cv2.imshow('Video', frame)

        # Wait for 'q' key to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture object and close the windows
video.release()
cv2.destroyAllWindows()
#here we create a function to play the video
