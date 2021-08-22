import cv2
import sys

VIDEO_URL = "http://192.168.0.106/tv/stream.m3u8"


def main():
    cap = cv2.VideoCapture(VIDEO_URL)
    if (cap.isOpened() == False):
        print('!!! Unable to open URL')
        sys.exit(-1)

    # retrieve FPS and calculate how long to wait between each frame to be display
    fps = cap.get(cv2.CAP_PROP_FPS)
    wait_ms = int(1000 / fps)
    print('FPS:', fps)

    while (True):
        # read one frame
        ret, frame = cap.read()

        # TODO: perform frame processing here
        cv2.putText(frame, "It works!", (100, 100), 0, 2, 255)

        # display frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(wait_ms) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
