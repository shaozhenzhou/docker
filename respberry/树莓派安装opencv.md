# 树莓派安装opencv

## 1、安装numpy
打开命令行界面，输入以下命令，安装Python科学计算库numpy

sudo pip3 install numpy

## 2、在树莓派设置中把根目录扩大到整个SD卡
命令行界面输入命令，进入树莓派配置界面。用上下键和左右键切换光标位置。

sudo raspi-config

选择Expand Filesystem，将根目录扩展到这个SD卡，充分利用SD卡的存储空间。如果不进行这一步，后续命令会出现卡死。退出设置界面，重启树莓派。

sudo reboot

## 3、安装OpenCV所需的库
挨个运行下面八条命令。共需要七分钟（注意倒数第三条命令中要安装四个-dev软件包）。

```
sudo apt-get install build-essential git cmake pkg-config -y
sudo apt-get install libjpeg8-dev -y
sudo apt-get install libtiff5-dev -y
sudo apt-get install libjasper-dev -y
sudo apt-get install libpng12-dev -y

sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y

sudo apt-get install libgtk2.0-dev -y
sudo apt-get install libatlas-base-dev gfortran -y
```
## 4、下载OpenCV
在命令行输入以下三条命令，下载两个压缩包到树莓派的/home/pi/Downloads目录下。第一个压缩包86.8MB，第二个压缩包54.5MB：
```
wget https://github.com/Itseez/opencv/archive/3.4.0.zip

wget https://github.com/Itseez/opencv_contrib/archive/3.4.0.zip
```

如果下载速度很慢（比如每秒几个KB）：
方法1：可以在电脑浏览器中输入wget后面的链接下载压缩包，再用Fillzilla或者U盘等方法把文件传输到树莓派的/home/pi/Downloads目录下（一定不能错）。
方法2：:可以用电脑在百度网盘链接下载这两个压缩包之后再用Fillzilla或者U盘等方法把文件传输到树莓派的/home/pi/Downloads目录下（一定不能错）。

解压这两个压缩包
```
cd /home/pi/Downloads
unzip opencv-3.4.0.zip
unzip opencv_contrib-3.4.0.zip
```
## 5、设置编译参数
设置编译参数
```
cd /home/pi/Downloads/opencv-3.4.0
mkdir build
cd build
```

设置CMAKE参数，注意，下面这是一行命令（包括最后那俩点儿），需要耐心等待十五分钟左右：
### 如果是树莓派默认的python3.5环境
```
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D OPENCV_EXTRA_MODULES_PATH=/home/pi/Downloads/opencv_contrib-3.4.0/modules -D BUILD_EXAMPLES=ON -D WITH_LIBV4L=ON PYTHON3_EXECUTABLE=/usr/bin/python3.5 PYTHON_INCLUDE_DIR=/usr/include/python3.5 PYTHON_LIBRARY=/usr/lib/arm-linux-gnueabihf/libpython3.5m.so PYTHON3_NUMPY_INCLUDE_DIRS=/usr/lib/python3/dist-packages/numpy/core/include ..
```
### 如果是NanoPi默认的python3.6环境
```
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D OPENCV_EXTRA_MODULES_PATH=/home/pi/Downloads/opencv_contrib-3.4.0/modules -D BUILD_EXAMPLES=ON -D WITH_LIBV4L=ON PYTHON3_EXECUTABLE=/usr/bin/python3.6 PYTHON_INCLUDE_DIR=/usr/include/python3.6 PYTHON_LIBRARY=/usr/lib/aarch64-linux-gnu/libpython3.6m.so PYTHON3_NUMPY_INCLUDE_DIRS=/home/pi/Develop/vision/venv/lib/python3.6/site-packages/numpy/core/include ..
```

## 6、编译
最后一步，也是最重要的一步：编译

保证树莓派有至少5G的存储空间，建议本命令用树莓派桌面上的命令行工具运行，而不要使用远程ssh连接。因为执行命令时间太长，中途如果ssh断线的话无法得知是否已经安装完毕。
```
cd /home/pi/Downloads/opencv-3.4.0/build
sudo make -j4
```


```make```命令执行完成之后，执行下面的命令，执行命令需要一分钟：
```
sudo make insall
```
## 7、在Python3上测试OpenCV
安装好之后，在命令行中输入python3，回车

```import cv2```
回车

```cv2.__version__```
回车

## 7、在虚拟环境创建软链
如果需要在venv虚拟环境中使用cv2，则需要在虚拟环境中创建软链  
`ln -s /usr/local/lib/python3.5/dist-packages/cv2.cpython-35m-arm-linux-gnueabihf.so  ~/Develop/vision/venv/lib/python3.5/site-packages/.`




## 注：如果自动下载tiny-dnn和face_landmark_model.dat失败，则需要手动下载并复制到缓存目录
下载tiny-dnn：  
`https://github.com/tiny-dnn/tiny-dnn/archive/v1.0.0a3.tar.gz`  
复制到  /home/pi/Downloads/opencv-3.4.0/.cache/tiny_dnn/adb1c512e09ca2c7a6faef36f9c53e59-v1.0.0a3.tar.gz  
`cp ~/Downloads/tiny-dnn-1.0.0a3.tar.gz ~/Downloads/opencv-3.4.0/.cache/tiny_dnn/adb1c512e09ca2c7a6faef36f9c53e59-v1.0.0a3.tar.gz`  
  
下载face_landmark_model.dat：
`https://raw.githubusercontent.com/opencv/opencv_3rdparty/8afa57abc8229d611c4937165d20e2a2d9fc5a12/face_landmark_model.dat`  
复制到：/home/pi/Downloads/opencv-3.4.0/.cache/data/7505c44ca4eb54b4ab1e4777cb96ac05-face_landmark_model.dat  
`cp ~/Downloads/face_landmark_model.dat ~/Downloads/opencv-3.4.0/.cache/data/7505c44ca4eb54b4ab1e4777cb96ac05-face_landmark_model.dat`  
`cp ~/Downloads/face_landmark_model.dat ~/Downloads/opencv-3.4.0/build/share/OpenCV/testdata/cv/face//face_landmark_model.dat
`
注：如果首次安装tiny-dnn目录，以及data目录尚未创建的话，可以手动创建，并拷贝文件。


```
cmake -D CMAKE_C_FLAGS=-O3 -mfpu=neon -DNEON=ON -D CMAKE_BUILD_TYPE=RELEASE -D ENABLE_NEON=ON -D CMAKE_INSTALL_PREFIX=/usr/local -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D OPENCV_EXTRA_MODULES_PATH=/home/pi/Downloads/opencv_contrib-3.4.0/modules -D BUILD_EXAMPLES=ON -D WITH_LIBV4L=ON PYTHON3_EXECUTABLE=/usr/bin/python3.6 PYTHON_INCLUDE_DIR=/usr/include/python3.6 PYTHON_LIBRARY=/usr/lib/aarch64-linux-gnu/libpython3.6m.so PYTHON3_NUMPY_INCLUDE_DIRS=/home/pi/Develop/vision/venv/lib/python3.6/site-packages/numpy/core/include ..
sudo make -j4
sudo make insall


```

```
-- General configuration for OpenCV 3.4.0 =====================================
--   Version control:               unknown
-- 
--   Extra modules:
--     Location (extra):            /home/pi/Downloads/opencv_contrib-3.4.0/modules
--     Version control (extra):     unknown
-- 
--   Platform:
--     Timestamp:                   2019-05-18T15:26:44Z
--     Host:                        Linux 4.4.167 aarch64
--     CMake:                       3.10.2
--     CMake generator:             Unix Makefiles
--     CMake build tool:            /usr/bin/make
--     Configuration:               RELEASE
-- 
--   CPU/HW features:
--     Baseline:                    NEON FP16
--       required:                  NEON
--       disabled:                  VFPV3
-- 
--   C/C++:
--     Built as dynamic libs?:      YES
--     C++11:                       YES
--     C++ Compiler:                /usr/bin/c++  (ver 7.4.0)
--     C++ flags (Release):         -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-comment -Wno-implicit-fallthrough -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections    -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG
--     C++ flags (Debug):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Winit-self -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-comment -Wno-implicit-fallthrough -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections    -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG
--     C Compiler:                  /usr/bin/cc
--     C flags (Release):           -O3   -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Winit-self -Wno-narrowing -Wno-comment -Wno-implicit-fallthrough -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections    -fvisibility=hidden -O3 -DNDEBUG  -DNDEBUG
--     C flags (Debug):             -O3   -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Winit-self -Wno-narrowing -Wno-comment -Wno-implicit-fallthrough -fdiagnostics-show-option -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections    -fvisibility=hidden -g  -O0 -DDEBUG -D_DEBUG
--     Linker flags (Release):
--     Linker flags (Debug):
--     ccache:                      NO
--     Precompiled headers:         YES
--     Extra dependencies:          dl m pthread rt
--     3rdparty dependencies:
-- 
--   OpenCV modules:
--     To be built:                 aruco bgsegm bioinspired calib3d ccalib core datasets dnn dpm face features2d flann freetype fuzzy highgui img_hash imgcodecs imgproc line_descriptor ml objdetect optflow phase_unwrapping photo plot python2 python3 python_bindings_generator reg rgbd saliency shape stereo stitching structured_light superres surface_matching text tracking ts video videoio videostab xfeatures2d ximgproc xobjdetect xphoto
--     Disabled:                    js world
--     Disabled by dependency:      -
--     Unavailable:                 cnn_3dobj cudaarithm cudabgsegm cudacodec cudafeatures2d cudafilters cudaimgproc cudalegacy cudaobjdetect cudaoptflow cudastereo cudawarping cudev cvv dnn_modern hdf java matlab ovis sfm viz
--     Applications:                tests perf_tests examples apps
--     Documentation:               NO
--     Non-free algorithms:         NO
-- 
--   GUI: 
--     GTK+:                        YES (ver 2.24.32)
--       GThread :                  YES (ver 2.56.4)
--       GtkGlExt:                  NO
--     VTK support:                 NO
-- 
--   Media I/O: 
--     ZLib:                        /usr/lib/aarch64-linux-gnu/libz.so (ver 1.2.11)
--     JPEG:                        /usr/lib/aarch64-linux-gnu/libjpeg.so (ver )
--     WEBP:                        /usr/lib/aarch64-linux-gnu/libwebp.so (ver encoder: 0x020e)
--     PNG:                         /usr/lib/aarch64-linux-gnu/libpng.so (ver 1.6.34)
--     TIFF:                        /usr/lib/aarch64-linux-gnu/libtiff.so (ver 42 / 4.0.9)
--     JPEG 2000:                   build (ver 1.900.1)
--     OpenEXR:                     build (ver 1.7.1)
-- 
--   Video I/O:
--     DC1394:                      YES (ver 2.2.5)
--     FFMPEG:                      YES
--       avcodec:                   YES (ver 57.107.100)
--       avformat:                  YES (ver 57.83.100)
--       avutil:                    YES (ver 55.78.100)
--       swscale:                   YES (ver 4.8.100)
--       avresample:                NO
--     GStreamer:                   
--       base:                      YES (ver 1.14.1)
--       video:                     YES (ver 1.14.1)
--       app:                       YES (ver 1.14.1)
--       riff:                      YES (ver 1.14.1)
--       pbutils:                   YES (ver 1.14.1)
--     libv4l/libv4l2:              1.14.2 / 1.14.2
--     v4l/v4l2:                    linux/videodev.h linux/videodev2.h
--     gPhoto2:                     NO
-- 
--   Parallel framework:            pthreads
-- 
--   Trace:                         YES (built-in)
-- 
--   Other third-party libraries:
--     Lapack:                      NO
--     Eigen:                       NO
--     Custom HAL:                  YES (carotene (ver 0.0.1))
-- 
--   NVIDIA CUDA:                   NO
-- 
--   OpenCL:                        YES (no extra features)
--     Include path:                /home/pi/Downloads/opencv-3.4.0/3rdparty/include/opencl/1.2
--     Link libraries:              Dynamic load
-- 
--   Python 2:
--     Interpreter:                 /usr/bin/python2.7 (ver 2.7.15)
--     Libraries:                   /usr/lib/aarch64-linux-gnu/libpython2.7.so (ver 2.7.15+)
--     numpy:                       /usr/lib/python2.7/dist-packages/numpy/core/include (ver 1.13.3)
--     packages path:               lib/python2.7/dist-packages
-- 
--   Python 3:
--     Interpreter:                 /home/pi/Develop/vision/venv/bin/python3 (ver 3.6.8)
--     Libraries:                   /usr/lib/aarch64-linux-gnu/libpython3.6m.so (ver 3.6.8)
--     numpy:                       /home/pi/Develop/vision/venv/lib/python3.6/site-packages/numpy/core/include (ver 1.16.3)
--     packages path:               lib/python3.6/site-packages
-- 
--   Python (for build):            /usr/bin/python2.7
-- 
--   Java:
--     ant:                         NO
--     JNI:                         NO
--     Java wrappers:               NO
--     Java tests:                  NO
-- 
--   Matlab:                        NO
-- 
--   Install to:                    /usr/local
-- -----------------------------------------------------------------
-- 
-- Configuring done
-- Generating done
-- Build files have been written to: /home/pi/Downloads/opencv-3.4.0/build

```

