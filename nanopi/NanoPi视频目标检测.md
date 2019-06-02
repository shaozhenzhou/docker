# NanoPi视频目标检测

## 复制mssd样例
```
cp ~/Develop/Tengine/examples/mobilenet_ssd ~/Develop/Tengine/examples/mobilenet_ssd_video -r
```

## 修改CMakeLists.txt
修改项目名称为MSSD_video，修改源文件名称为mssd_video.cpp
```
cmake_minimum_required (VERSION 2.8)
project(MSSD_video)
add_definitions(-std=c++11)
set( TENGINE_DIR /home/pi/Develop/Tengine/)
set( INSTALL_DIR ${TENGINE_DIR}/install/)
set( TENGINE_LIBS tengine hclcpu)

if( ANDROID AND ("${CMAKE_SYSTEM_PROCESSOR}" STREQUAL "armv7-a"))
    set( PROTOBUF_LIB ${PROTOBUF_DIR}/arm32_lib/libprotobuf.so)
endif()
if( ANDROID AND ("${CMAKE_SYSTEM_PROCESSOR}" STREQUAL "aarch64"))
    set( PROTOBUF_LIB ${PROTOBUF_DIR}/arm64_lib/libprotobuf.so)
endif()

if( BLAS_DIR)
    if( ANDROID AND ("${CMAKE_SYSTEM_PROCESSOR}" STREQUAL "armv7-a"))
         set( BLAS_LIB ${BLAS_DIR}/arm32/lib/libopenblas.so)
    endif()
    if( ANDROID AND ("${CMAKE_SYSTEM_PROCESSOR}" STREQUAL "aarch64"))
         set( BLAS_LIB ${BLAS_DIR}/arm64/lib/libopenblas.so)
    endif()
endif()

if ( NOT (ARM OR ANDROID))
set (BLAS_LIB openblas)
endif()

set( CODE_SRCS mssd_video.cpp ../common/common.cpp)

#opencv
find_package(OpenCV REQUIRED)

#include
include_directories(${INSTALL_DIR}/include 
                    ${TENGINE_DIR}/examples/common )

#lib
link_directories( ${INSTALL_DIR}/lib)

#exe
add_executable(MSSD_video ${CODE_SRCS})
if( ANDROID)
   target_link_libraries(MSSD_video ${TENGINE_LIBS} ${PROTOBUF_LIB} ${OpenCV_LIBS} ${BLAS_LIB})
else()
   target_link_libraries(MSSD_video ${TENGINE_LIBS} ${OpenCV_LIBS} ${BLAS_LIB})
endif()
```

## 修改makefile文件
将MSSD替换为MSSD_video，将mobilenet_ssd替换为mobilenet_ssd_video  

## 删除CMakeCache.txt
```
rm CMakeCache.txt
```

## 编译项目
```
make
```
