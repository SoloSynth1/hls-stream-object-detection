import argparse
import sys

import cv2


def main(stream_url):
    cap = cv2.VideoCapture(stream_url)
    if (cap.isOpened() == False):
        print('!!! Unable to open URL')
        sys.exit(-1)

    # retrieve FPS and calculate how long to wait between each frame to be display
    fps = cap.get(cv2.CAP_PROP_FPS)
    wait_ms = int(1000 / fps)
    print('FPS:', fps)

    while True:
        # read one frame
        ret, frame = cap.read()

        # TODO: perform frame processing here
        cv2.putText(frame, "It works!", (100, 100), 0, 2, 255)

        # display frame
        cv2.imshow('Press q to exit', frame)
        if cv2.waitKey(wait_ms) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='YOLOv4 object detection trial')
    parser.add_argument('stream_url', type=str, help='Stream URL')

    args = parser.parse_args()
    stream_url = args.stream_url
    main(stream_url)
