import cv2
import time
from ctypes import *

###调用电脑摄像头检测人脸并截图
def CatchPICFromVideo(window_name, camera_idx):
    libface = CDLL('./libfacedetection.so')
    #初始化识别结果存储缓存区域
    result_buffer = create_string_buffer(0x20000)
    #初始化识别结果
    results = 0
    #识别结果开始位置
    start_pos = 4
    #识别结果每个结果集的偏移量
    offset = 142 * 2
    #识别出人脸后要画的边框的颜色，RGB格式, color是一个不可增删的数组
    color = (0, 255, 0)

    # 指定函数输出结果为指针类型
    pResults = cast(results, POINTER(c_int))
    libface._Z14facedetect_cnnPhS_iii.restype = POINTER(c_int)

    cv2.namedWindow(window_name)

    #视频来源，可以来自一段已存好的视频，也可以直接来自USB摄像头
    cap = cv2.VideoCapture(camera_idx)

    while cap.isOpened():
        ok, img = cap.read() #读取一帧数据

        if not ok:
            break

        start = time.time()

        # 为加快处理速度，将图像缩小，倍率为ratio
        ratio = 1/4
        img_s = cv2.resize(img, (0, 0), fx = ratio, fy = ratio)
        pResults = libface._Z14facedetect_cnnPhS_iii(byref(result_buffer),
                                                     byref(img_s.ctypes.data_as(POINTER(c_char)).contents), img_s.shape[1],
                                                     img_s.shape[0], img_s.shape[1] * 3)

        for x in range(pResults.contents.value):
            # 每一个组结果的起始位置为：初始位置+偏移量*第几个结果
            pos = start_pos + offset * x
            x, y, w, h = [int(i / ratio) for i in memoryview(result_buffer[pos:pos + 8]).cast('H')]

            #画出矩形框
            img = cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

        #显示图像
        cv2.imshow(window_name, img)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 按q键退出
            break
        end = time.time()
    	# Time elapsed
        seconds = end - start
        fps  = 1 / seconds
        print( "Estimated frames per second : {0}".format(fps))


    #释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    CatchPICFromVideo("face detection", 0)

