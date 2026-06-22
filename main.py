import cv2
from PIL import Image

from util import get_limits

CAP = cv2.VideoCapture(0) # only 1 webcam, so it is 0
YELLOW = [0, 255, 255]
def main():
    while True:
        ret, frame = CAP.read()

        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_limit, upper_limit = get_limits(YELLOW)
        
        mask = cv2.inRange(hsvImage, lower_limit, upper_limit)

        mask_ = Image.fromarray(mask)

        boundingBox = mask_.getbbox()

        if boundingBox:
            x1, y1, x2, y2 = boundingBox
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    CAP.release()

    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()

