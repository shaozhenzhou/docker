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

