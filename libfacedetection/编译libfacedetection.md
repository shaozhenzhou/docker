# 编译libfacedetection

## 现在libfacedetection源码
```
cd Develop
git clone https://github.com/ShiqiYu/libfacedetection.git
```
## 修改aarch64-toolchain.cmake
源码中的cmake文件，使用的不是树莓派自带的编译器，需要修改  
```
nano aarch64-toolchain.cmake
set(CMAKE_CXX_COMPILER "/usr/bin/arm-linux-gnueabihf-g++")
set(CMAKE_C_COMPILER "/usr/bin/arm-linux-gnueabihf-gcc")
```
## 修改CMakeLists.txt，打开编译demo，便于测试是否编译成功
```
nano CMakeLists.txt
option(DEMO "build the demo" ON)
```
## 编译源码
### build目录
```
pi@raspberrypi:~/Develop/libfacedetection $ mkdir build; cd build; rm -rf *
```
### cmake
```
pi@raspberrypi:~/Develop/libfacedetection/build $ cmake ..
-- The C compiler identification is GNU 6.3.0
-- The CXX compiler identification is GNU 6.3.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found OpenCV: /usr/local (found version "3.4.0") 
-- Configuring done
-- Generating done
-- Build files have been written to: /home/pi/Develop/libfacedetection/build
```
### 查看Makefile文件
```
pi@raspberrypi:~/Develop/libfacedetection/build $ ls
CMakeCache.txt  CMakeFiles  cmake_install.cmake  Makefile
```
### make
```
pi@raspberrypi:~/Develop/libfacedetection/build $ make
Scanning dependencies of target facedetection
[ 14%] Building CXX object CMakeFiles/facedetection.dir/src/facedetectcnn.cpp.o
[ 28%] Building CXX object CMakeFiles/facedetection.dir/src/facedetectcnn-floatdata.cpp.o
[ 42%] Building CXX object CMakeFiles/facedetection.dir/src/facedetectcnn-int8data.cpp.o
[ 57%] Building CXX object CMakeFiles/facedetection.dir/src/facedetectcnn-model.cpp.o
[ 71%] Linking CXX shared library libfacedetection.so
[ 71%] Built target facedetection
Scanning dependencies of target face_detect
[ 85%] Building CXX object CMakeFiles/face_detect.dir/example/libfacedetectcnn-example.cpp.o
[100%] Linking CXX executable face_detect
[100%] Built target face_detect
```
### 查看编译结果
```
pi@raspberrypi:~/Develop/libfacedetection/build $ ls
CMakeCache.txt  CMakeFiles  cmake_install.cmake  face_detect  libfacedetection.so  Makefile
```
### 测试
```
pi@raspberrypi:~/Develop/libfacedetection/build $ ./fdt_demo ../images/chloecalmon.png
6 faces detected.
face_rect=[306, 51, 127, 127], confidence=99, angle=0
face_rect=[441, 110, 172, 172], confidence=99, angle=0
face_rect=[1086, 99, 191, 191], confidence=99, angle=0
face_rect=[971, 59, 112, 112], confidence=99, angle=0
face_rect=[153, 138, 93, 93], confidence=94, angle=0
face_rect=[194, 17, 28, 28], confidence=72, angle=0
```



### 重新编译命令
```
sudo rm -r build
mkdir build; cd build; rm -rf *
sudo cmake ..
sudo make
  
```


