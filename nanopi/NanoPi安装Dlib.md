# NanoPi安装Dlib

## 下载Dlib
从Dlib网站下载：[http://dlib.net/]
```
wget http://dlib.net/files/dlib-19.17.tar.bz2
```

## 安装基础库
```
sudo apt-get install build-essential cmake
sudo apt-get install libgtk-3-dev
sudo apt-get install libboost-all-dev
```

## 安装OpenBLAS
```
git clone git://github.com/xianyi/OpenBLAS
cd OpenBLAS
sudo apt-get install gfortran
sudo make FC=gfortran
sudo make install
```
注：也可以通过apt安装编译版本
```
sudo apt-get install libopenblas-dev
sudo apt-get install libatlas-base-dev
```

## 安装wheel和twine
```
pip3 install wheel
pip3 install twine
```

## 编译安装 Dlib，生成whl文件
```
python3 setup.py bdist_wheel --compiler-flags "-O3" --set CMAKE_BUILD_TYPE=RELEASE --clean
```
注：以下参数不需要指定，安装程序会自动检测NEON，BLAS和LAPACK
--set ENABLE_NEON=ON --set DLIB_USE_BLAS=1 --set DLIB_USE_LAPACK=1 

## output
```
Invoking CMake setup: 'cmake /home/pi/Downloads/dlib-19.17/tools/python -DCMAKE_LIBRARY_OUTPUT_DIRECTORY=/home/pi/Downloads/dlib-19.17/build/lib.linux-aarch64-3.6 -DPYTHON_EXECUTABLE=/home/pi/Develop/vision/venv/bin/python3 -DCMAKE_CXX_FLAGS=-O3 -DCMAKE_BUILD_TYPE=RELEASE -DENABLE_NEON=ON -DDLIB_USE_BLAS=1 -DDLIB_USE_LAPACK=1 -DCMAKE_BUILD_TYPE=Release'
-- The C compiler identification is GNU 7.4.0
-- The CXX compiler identification is GNU 7.4.0
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
-- Found PythonInterp: /home/pi/Develop/vision/venv/bin/python3 (found version "3.6.8") 
-- Found PythonLibs: /usr/lib/aarch64-linux-gnu/libpython3.6m.so
-- Performing Test HAS_CPP14_FLAG
-- Performing Test HAS_CPP14_FLAG - Success
-- pybind11 v2.2.2
-- Using CMake version: 3.10.2
-- Compiling dlib version: 19.17.0
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE  
-- Looking for XOpenDisplay in /usr/lib/aarch64-linux-gnu/libX11.so;/usr/lib/aarch64-linux-gnu/libXext.so
-- Looking for XOpenDisplay in /usr/lib/aarch64-linux-gnu/libX11.so;/usr/lib/aarch64-linux-gnu/libXext.so - found
-- Looking for gethostbyname
-- Looking for gethostbyname - found
-- Looking for connect
-- Looking for connect - found
-- Looking for remove
-- Looking for remove - found
-- Looking for shmat
-- Looking for shmat - found
-- Looking for IceConnectionNumber in ICE
-- Looking for IceConnectionNumber in ICE - found
-- Found X11: /usr/lib/aarch64-linux-gnu/libX11.so
-- Looking for png_create_read_struct
-- Looking for png_create_read_struct - found
-- Looking for jpeg_read_header
-- Looking for jpeg_read_header - found
-- Searching for BLAS and LAPACK
-- Searching for BLAS and LAPACK
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.29.1") 
-- Checking for module 'cblas'
--   No package 'cblas' found
-- Checking for module 'lapack'
--   Found lapack, version 0.2.20+ds
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of void*
-- Check size of void* - done
-- Found OpenBLAS library
-- Looking for sgetrf_single
-- Looking for sgetrf_single - found
-- Using OpenBLAS's built in LAPACK
-- Looking for cblas_ddot
-- Looking for cblas_ddot - found
-- Looking for sgesv
-- Looking for sgesv - not found
-- Looking for sgesv_
-- Looking for sgesv_ - not found
CUDA_TOOLKIT_ROOT_DIR not found or specified
-- Could NOT find CUDA (missing: CUDA_TOOLKIT_ROOT_DIR CUDA_NVCC_EXECUTABLE CUDA_INCLUDE_DIRS CUDA_CUDART_LIBRARY) (Required is at least version "7.5")
-- DID NOT FIND CUDA
-- Disabling CUDA support for dlib.  DLIB WILL NOT USE CUDA
-- C++11 activated.
-- Configuring done
-- Generating done
CMake Warning:
  Manually-specified variables were not used by the project:

    ENABLE_NEON


-- Build files have been written to: /home/pi/Downloads/dlib-19.17/build/temp.linux-aarch64-3.6

```
