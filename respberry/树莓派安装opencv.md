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
