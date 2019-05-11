# 树莓派libfacedetection性能测试

## 制作3种规格照片文件
facecam_shot.py  
```
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
```

## 性能测试
benchmark_libface.py  
```
import cv2
import sys
import time
from ctypes import *


sum = 0
N = 100

libface = CDLL('./libfacedetection.so')

result_buffer = create_string_buffer(0x20000)
results = 0

img = cv2.imread(sys.argv[1])
if img is None:
    print('Can not load the image file {}.'.format(sys.argv[1]))
    sys.exit()

pResults = cast(results, POINTER(c_int))
libface._Z14facedetect_cnnPhS_iii.restype = POINTER(c_int)

start = time.time()

for i in range(N):
    pResults = libface._Z14facedetect_cnnPhS_iii(byref(result_buffer),
                                                 byref(img.ctypes.data_as(POINTER(c_char)).contents), img.shape[1],
                                                 img.shape[0], img.shape[1] * 3)
    end = time.time()
sum = end - start

print('每次耗时：{}， {} fps. '.format(sum/N, 1/(sum/N)))

```

## 性能测试结果
```
(venv) pi@raspberrypi:~/Develop/testso $ python3 benchmark_libface.py cap_160x120.jpg
每次耗时：0.02817378044128418， 35.49399421508445 fps. 
(venv) pi@raspberrypi:~/Develop/testso $ python3 benchmark_libface.py cap_320x240.jpg
每次耗时：0.12004116296768189， 8.330475774124459 fps. 
(venv) pi@raspberrypi:~/Develop/testso $ python3 benchmark_libface.py cap_640x480.jpg
每次耗时：0.4915662336349487， 2.03431385554165 fps. 
```
