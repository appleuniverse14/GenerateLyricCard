import cv2
import numpy as np


def generateImage(dict):
    pass


def imageToPDF():
    pass


# test
if __name__ == '__main__':
    print(cv2.__version__)
    img = cv2.imread("img/test.jpg", cv2.IMREAD_UNCHANGED)
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", img)
    cv2.waitKey()
    cv2.destroyAllWindows()
