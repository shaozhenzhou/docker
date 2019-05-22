# NanoPi OpenCV3.4.0编译安装

## 1、下载OpenCV
在命令行输入以下三条命令，下载两个压缩包到/home/pi/Downloads目录下。第一个压缩包86.8MB，第二个压缩包54.5MB：
```
wget https://github.com/Itseez/opencv/archive/3.4.0.zip

wget https://github.com/Itseez/opencv_contrib/archive/3.4.0.zip
```

解压这两个压缩包
```
cd /home/pi/Downloads
unzip opencv-3.4.0.zip
unzip opencv_contrib-3.4.0.zip
```

## 2、安装OpenCV所需的库
```
sudo apt-get install build-essential git cmake pkg-config -y
sudo apt-get install libjpeg8-dev -y
sudo apt-get install libtiff5-dev -y
sudo apt-get install libjasper-dev -y
sudo apt-get install libpng12-dev -y

sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y

sudo apt-get install libgtk2.0-dev -y
sudo apt-get install gfortran -y
```

## 3、 安装openblas及liblapacke
```
sudo apt-get install libopenblas-dev
sudo apt-get install liblapacke-dev

```
## 4、修改 OpenCVFindOpenBLAS.cmake ，添加openblas搜索路径
添加路径：/usr/include/aarch64-linux-gnu , /usr/lib/aarch64-linux-gnu
可通过以下命令查找libopenblas.so文件所在目录
```
sudo find / -name libopenblas.so
```
修改opencv目录cmake下的OpenCVFindOpenBLAS.cmake
```
SET(Open_BLAS_INCLUDE_SEARCH_PATHS
  /usr/include/aarch64-linux-gnu
  $ENV{OpenBLAS_HOME}
  $ENV{OpenBLAS_HOME}/include
  /opt/OpenBLAS/include
  /usr/local/include/openblas
  /usr/include/openblas
  /usr/local/include/openblas-base
  /usr/include/openblas-base
  /usr/local/include
  /usr/include
)

SET(Open_BLAS_LIB_SEARCH_PATHS
        /usr/lib/aarch64-linux-gnu
        $ENV{OpenBLAS}cd
        $ENV{OpenBLAS}/lib
        $ENV{OpenBLAS_HOME}
        $ENV{OpenBLAS_HOME}/lib
        /opt/OpenBLAS/lib
        /usr/local/lib64
        /usr/local/lib
        /lib/openblas-base
        /lib64/
        /lib/
        /usr/lib/openblas-base
        /usr/lib64
        /usr/lib
```

## 5、创建 apacke.h 软链到 /usr/include/aarch64-linux-gnu目录
```
sudo ln -s /usr/include/lapacke.h /usr/include/aarch64-linux-gnu
```

## 6、检查相关文件是否就位
```
sudo find / -name libopenblas.so
sudo find / -name cblas.h
sudo find / -name /lapacke.h
```
确保这三个文件都在 /usr/include/aarch64-linux-gnu 下

## 7、手动添加难以自动下载的2个文件
下载tiny-dnn：  
`https://github.com/tiny-dnn/tiny-dnn/archive/v1.0.0a3.tar.gz`  
复制到  /home/pi/Downloads/opencv-3.4.0/.cache/tiny_dnn/adb1c512e09ca2c7a6faef36f9c53e59-v1.0.0a3.tar.gz  
`cp ~/Downloads/tiny-dnn-1.0.0a3.tar.gz ~/Downloads/opencv-3.4.0/.cache/tiny_dnn/adb1c512e09ca2c7a6faef36f9c53e59-v1.0.0a3.tar.gz`  
  
下载face_landmark_model.dat：
`https://raw.githubusercontent.com/opencv/opencv_3rdparty/8afa57abc8229d611c4937165d20e2a2d9fc5a12/face_landmark_model.dat`  
复制到：/home/pi/Downloads/opencv-3.4.0/.cache/data/7505c44ca4eb54b4ab1e4777cb96ac05-face_landmark_model.dat  
`cp ~/Downloads/face_landmark_model.dat ~/Downloads/opencv-3.4.0/.cache/data/7505c44ca4eb54b4ab1e4777cb96ac05-face_landmark_model.dat`  
注：.cache、tiny_dnn、data 目录尚未创建的话，可以手动创建，并拷贝文件。

## 8、cmake
注意最后的选项需要指定numpy的include目录
```
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D OPENCV_EXTRA_MODULES_PATH=/home/pi/Downloads/opencv_contrib-3.4.0/modules -D BUILD_EXAMPLES=ON -D WITH_LIBV4L=ON PYTHON3_EXECUTABLE=/usr/bin/python3.6 PYTHON_INCLUDE_DIR=/usr/include/python3.6 PYTHON_LIBRARY=/usr/lib/aarch64-linux-gnu/libpython3.6m.so PYTHON3_NUMPY_INCLUDE_DIRS=/home/pi/Develop/venv/lib/python3.6/site-packages/numpy/core/include ..
```
检查cmake信息，在cmake输出中查找以下信息，为成功配置
```
-- Found OpenBLAS libraries: /usr/lib/aarch64-linux-gnu/libopenblas.so
-- Found OpenBLAS include: /usr/include/aarch64-linux-gnu
-- LAPACK(OpenBLAS): LAPACK_LIBRARIES: /usr/lib/aarch64-linux-gnu/libopenblas.so
-- LAPACK(OpenBLAS): Support is enabled.
```

## 9、编译
最后一步，也是最重要的一步：编译

保证至少8G的存储空间。
```
cd /home/pi/Downloads/opencv-3.4.0/build
sudo make -j4
```

```make```命令执行完成之后，执行下面的命令，执行命令需要一分钟：
```
sudo make insall
```
## 10、在Python3上测试OpenCV
安装好之后，在命令行中输入python3，回车

```import cv2```
回车

```cv2.__version__```
回车

## 11、在虚拟环境创建软链
如果需要在venv虚拟环境中使用cv2，则需要在虚拟环境中创建软链  
`ln -s /usr/local/lib/python3.6/dist-packages/cv2.cpython-36m-arm-linux-gnueabihf.so  ~/Develop/vision/venv/lib/python3.6/site-packages/.`


# 附录，测试过程记录
## cmake opencv
```
-- Could not find OpenBLAS include. Turning OpenBLAS_FOUND off
-- Could not find OpenBLAS lib. Turning OpenBLAS_FOUND off
-- Could NOT find Atlas (missing: Atlas_CBLAS_INCLUDE_DIR Atlas_CLAPACK_INCLUDE_DIR Atlas_CBLAS_LIBRARY Atlas_BLAS_LIBRARY Atlas_LAPACK_LIBRARY) 

-- A library with BLAS API not found. Please specify library location.
-- LAPACK requires BLAS
-- A library with LAPACK API not found. Please specify library location.

```

## install openblas-base
```
sudo apt-get install libopenblas-base
```
```
-- Could not find OpenBLAS include. Turning OpenBLAS_FOUND off
-- Could not find OpenBLAS lib. Turning OpenBLAS_FOUND off
-- Could NOT find Atlas (missing: Atlas_CBLAS_INCLUDE_DIR Atlas_CLAPACK_INCLUDE_DIR Atlas_CBLAS_LIBRARY Atlas_BLAS_LIBRARY Atlas_LAPACK_LIBRARY) 
-- A library with BLAS API not found. Please specify library location.
-- LAPACK requires BLAS
-- A library with LAPACK API not found. Please specify library location.

```

## install openblas-dev
```
sudo apt-get install libopenblas-dev
```
```
-- Could not find OpenBLAS include. Turning OpenBLAS_FOUND off
-- Could not find OpenBLAS lib. Turning OpenBLAS_FOUND off
-- Could NOT find Atlas (missing: Atlas_CLAPACK_INCLUDE_DIR Atlas_CBLAS_LIBRARY Atlas_BLAS_LIBRARY) 
-- Looking for sgemm_
-- Looking for sgemm_ - found
-- A library with BLAS API found.
-- Looking for cheev_
-- Looking for cheev_ - found
-- A library with LAPACK API found.
```

## after sudo ldconfig
```
-- Could not find OpenBLAS include. Turning OpenBLAS_FOUND off
-- Could not find OpenBLAS lib. Turning OpenBLAS_FOUND off
-- Could NOT find Atlas (missing: Atlas_CLAPACK_INCLUDE_DIR Atlas_CBLAS_LIBRARY Atlas_BLAS_LIBRARY) 
-- A library with BLAS API found.
-- A library with LAPACK API found.
```
## install liblapacke-dev
```
sudo apt-get install liblapacke-dev
# 将会同时安装下列软件：
#  liblapacke libtmglib-dev libtmglib3

(venv) pi@NanoPi-M4:~/Downloads/opencv-3.4.0/build$ sudo find / -name lapacke.h
/usr/include/lapacke.h

(venv) pi@NanoPi-M4:~/Downloads/opencv-3.4.0/build$ sudo ln -s /usr/include/lapacke.h /usr/include/aarch64-linux-gnu

(venv) pi@NanoPi-M4:~/Downloads/opencv-3.4.0/build$ sudo find / -name lapacke.h
/usr/include/aarch64-linux-gnu/lapacke.h
/usr/include/lapacke.h
```

```
-- Found OpenBLAS libraries: /usr/lib/aarch64-linux-gnu/libopenblas.so
-- Found OpenBLAS include: /usr/include/aarch64-linux-gnu
-- LAPACK(OpenBLAS): LAPACK_LIBRARIES: /usr/lib/aarch64-linux-gnu/libopenblas.so
-- LAPACK(OpenBLAS): Support is enabled.

```
## dpk -l
```
(venv) pi@NanoPi-M4:~/Downloads/opencv-3.4.0/build$ 
(venv) pi@NanoPi-M4:~/Downloads/opencv-3.4.0/build$ dpkg -l | grep blas
ii  libblas3:arm64                       3.7.1-4ubuntu1                        arm64        Basic Linear Algebra Reference implementations, shared library
ii  libgslcblas0:arm64                   2.4+dfsg-6                            arm64        GNU Scientific Library (GSL) -- blas library package
ii  libopenblas-base:arm64               0.2.20+ds-4                           arm64        Optimized BLAS (linear algebra) library (shared library)
ii  libopenblas-dev:arm64                0.2.20+ds-4                           arm64        Optimized BLAS (linear algebra) library (development files)
(venv) pi@NanoPi-M4:~/Downloads/opencv-3.4.0/build$ dpkg -l | grep lapack
ii  liblapack-dev:arm64                  3.7.1-4ubuntu1                        arm64        Library of linear algebra routines 3 - static version
ii  liblapack3:arm64                     3.7.1-4ubuntu1                        arm64        Library of linear algebra routines 3 - shared version
ii  liblapacke:arm64                     3.7.1-4ubuntu1                        arm64        Library of linear algebra routines 3 - C lib shared version
ii  liblapacke-dev:arm64                 3.7.1-4ubuntu1                        arm64        Library of linear algebra routines 3 - Headers
(venv) pi@NanoPi-M4:~/Downloads/opencv-3.4.0/build$ dpkg -l | grep atlas

```


