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
## 编译源码
```
mkdir build
cd build
camke ..
make
```


