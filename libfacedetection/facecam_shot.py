import cv2
import time
from ctypes import *

###调用电脑摄像头检测人脸并截图
def CatchPICFromVideo(window_name, camera_idx):
    cv2.namedWindow(window_name)

    #视频来源，可以来自一段已存好的视频，也可以直接来自USB摄像头
    cap = cv2.VideoCapture(camera_idx)

    while cap.isOpened():
        ok, img = cap.read() #读取一帧数据

        if not ok:
            break

        cv2.imwrite("cap_640x480.jpg", img)

        ratio = 1/2
        img_s = cv2.resize(img, (0, 0), fx = ratio, fy = ratio)
        cv2.imwrite("cap_320x240.jpg", img_s)

        ratio = 1/4
        img_s = cv2.resize(img, (0, 0), fx = ratio, fy = ratio)
        cv2.imwrite("cap_160x120.jpg", img_s)

        ratio = 1/8
        img_s = cv2.resize(img, (0, 0), fx = ratio, fy = ratio)
        cv2.imwrite("cap_128x96.jpg", img_s)

        break

    #释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    CatchPICFromVideo("face detection", 0)

