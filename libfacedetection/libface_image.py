import cv2
import sys
from ctypes import *

libface = CDLL('./libfacedetection.so')

result_buffer = create_string_buffer(0x20000)
results = 0

image = cv2.imread(sys.argv[1])
if image is None:
    print('Can not load the image file {}.'.format(sys.argv[1]))
    sys.exit()

'''
# 为解决图像偏右问题，根据libfacedetection的要求，将图像按宽度裁剪为64的倍数
w, h = image.shape[1], image.shape[0]
ratio = int(w / 64) * 64 / w
img = image[0:int(h * ratio), 0:int(w * ratio)]
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
'''

img = image

# 指定函数输出结果为指针类型
pResults = cast(results, POINTER(c_int))

# libface._Z14facedetect_cnnPhS_iii.argtypes = [c_char, c_char, c_int, c_int, c_int]
libface._Z14facedetect_cnnPhS_iii.restype = POINTER(c_int)

#
# libfacedetection编译后，so中导出函数名称会有变化，通过 dm -D 命令找到facedetect_cnn的函数入口
# $ nm -D libfacedetection.so | grep facedetect_cnn
# 0000b11c T _Z14facedetect_cnnPhS_iii
#
# facedetectcnn.h 中的函数原型定义
# int * facedetect_cnn(unsigned char * result_buffer, //buffer memory for storing face detection results, !!its size must be 0x20000 Bytes!!
#                    unsigned char * rgb_image_data, int width, int height, int step); //input image, it must be BGR (three channels) insteed of RGB image!
#
# 结果缓存 result_buffer 、图像数据 rgb_image_data 必须用传址方式送入函数，采用ctypes的byref函数取得引用地址
# image为numpy.narray类型，byref会引发无法自动转换类型错误，需手动指定类型强制转换：byref(image.ctypes.data_as(ctypes.POINTER(ctypes.c_char)).contents)
#
pResults = libface._Z14facedetect_cnnPhS_iii(byref(result_buffer), byref(img.ctypes.data_as(POINTER(c_char)).contents), img.shape[1], img.shape[0], img.shape[1]*3)

# pResults为c_int指针，用pResults.contents.value取得其值
print('{} faces detected.'.format(pResults.contents.value if pResults else 0))

# result_buffer数据格式为：
# 第0-3字节，为识别到的人脸数量
# 第4字节以后，均为识别结果，每个结果占用空间为142*2字节
# 每个结果空间内，内容分别为:x, y, w, h, confidence, angle，每项信息占2字节
start_pos = 4
offset = 142*2
for x in range(pResults.contents.value):
    # 每一个组结果的起始位置为：初始位置+偏移量*第几个结果
    pos = start_pos + offset * x
    x,y,w,h,c,a = [i for i in memoryview(result_buffer[pos:pos+12]).cast('H')]

    print('face_rect=[{}, {}, {}, {}], confidence={}, angle={}'.format(x, y, w, h, c, a))
    image=cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

