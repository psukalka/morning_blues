"""
Date: 02/07/19
Understanding video related utilities in OpenCV

*) To capture a video VideoCapture object is needed.
    Properties of video can also be accessed by cap.get(propId) : propId can be 0-18 (https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-get)
*) Video display comes very slow. CV2 might not be right library for displaying videos.

"""
import cv2


def display_gray_video(
        path="/Users/pavansukalkar/Downloads/Videos/comic1.mp4"):
    cap = cv2.VideoCapture(path)
    fps = int(cap.get(5))
    while cap.isOpened():
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(fps) & 0xFF == ord('q'):
            # Press 'q' to exit
            break
    cap.release()
    cv2.destroyAllWindows()


display_gray_video()
