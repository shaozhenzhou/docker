# 编译libfacedetection

## 下载libfacedetection源码
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

## 编译加速版本
加速相关有4个参数需要设置，分别为：  
```
add_definitions(-mfpu=neon)  #如果要启用NEON，这个参数必须加，否则编译出错
add_definitions(-D_ENABLE_INT8)
add_definitions(-D_ENABLE_NEON)
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3")
```

## 修改后的 CMakeLists.txt 文件
```
# CMakeLists for libfacedetectcnn

project(facedetection)

cmake_minimum_required(VERSION 2.8)

option(ENABLE_MFPU "use mfpu=neon" ON)
option(ENABLE_INT8 "use int8" ON)
option(ENABLE_AVX2 "use avx2" OFF)
option(ENABLE_NEON "whether use neon, if use arm please set it on" ON)
option(DEMO "build the demo" ON)

SET(fdt_base_dir   ${PROJECT_SOURCE_DIR})
SET(fdt_src_dir    ${fdt_base_dir}/src)
SET(fdt_inc_dir    ${fdt_base_dir}/src)

SET(fdt_lib_name   facedetection)
SET(fdt_lib_static ${fdt_lib_name})
SET(fdt_lib_shared ${fdt_lib_name}_shared)

FILE(GLOB_RECURSE fdt_source_files ${fdt_src_dir}/*.cpp)
LIST(SORT         fdt_source_files)

if(ENABLE_MFPU)
	message("using mfpu=neon")
	add_definitions(-mfpu=neon)
endif()

if(ENABLE_INT8)
	message("using int8")
	add_definitions(-D_ENABLE_INT8)
endif()

if(ENABLE_AVX2)
	message("using avx2")
	add_definitions(-D_ENABLE_AVX2)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -mavx2 -mfma")
endif()

if(ENABLE_NEON)
	message("using arm")
	add_definitions(-D_ENABLE_NEON)
endif()

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3")

INCLUDE_DIRECTORIES(${fdt_inc_dir})

# Create a static library (.a)
ADD_LIBRARY(${fdt_lib_static} STATIC ${fdt_source_files})

# Create a shared library (.so)
ADD_LIBRARY(${fdt_lib_shared} SHARED ${fdt_source_files})
SET_TARGET_PROPERTIES(${fdt_lib_shared} PROPERTIES OUTPUT_NAME "${fdt_lib_name}")
SET_TARGET_PROPERTIES(${fdt_lib_shared} PROPERTIES PREFIX "lib")

# Create demo. OpenCV is requred.
if (DEMO)
    #if(WIN32)
    #    set(OpenCV_DIR "D:/opencv343/build") # TODO
    #endif()
    find_package(OpenCV REQUIRED)
    include_directories(${OpenCV_INCLUDE_DIRS})

    set(fdt_demo_files ${fdt_base_dir}/example/libfacedetectcnn-example.cpp)
    add_executable(fdt_demo ${fdt_demo_files})
    target_link_libraries(fdt_demo ${fdt_lib_static} ${OpenCV_LIBS})
endif()

if (GSTREAMER)
    find_package(OpenCV REQUIRED)

    include(FindPkgConfig)
    pkg_search_module(GSTREAMER REQUIRED gstreamer-1.0)
    pkg_search_module(GSTREAMER_BASE REQUIRED gstreamer-base-1.0)
    pkg_search_module(GSTREAMER_VIDEO REQUIRED gstreamer-video-1.0)

    add_library(gstfacedetect SHARED
        example/libfacedetect.cpp
    )

    include_directories(gstfacedetect PRIVATE
        ${GSTREAMER_INCLUDE_DIRS}
        ${GSTREAMER_BASE_INCLUDE_DIRS}
        ${GSTREAMER_VIDEO_INCLUDE_DIRS}
        ${OpenCV_INCLUDE_DIRS}
    )

    target_link_libraries(gstfacedetect
        ${GSTREAMER_LIBRARIES}
        ${GSTREAMER_BASE_LIBRARIES}
        ${GSTREAMER_VIDEO_LIBRARIES}
        ${OpenCV_LIBS}
        ${fdt_lib_shared}
    )

endif()

```


### 重新编译命令
```
sudo rm -r build
mkdir build; cd build; rm -rf *
sudo cmake ..
sudo make
  
```


