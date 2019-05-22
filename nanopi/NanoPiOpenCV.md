# NanoPiOpenCV

## 1. Install
```
sudo apt-get install libopenblas-dev
sudo apt-get install liblapacke-dev

```
# 2.Modify OpenCVFindOpenBLAS.cmake
Add PATH /usr/include/aarch64-linux-gnu , /usr/lib/aarch64-linux-gnu
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
## 3.make softlink to lapacke.h
```
sudo ln -s /usr/include/lapacke.h /usr/include/aarch64-linux-gnu
```

## 4.cmake
```
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D OPENCV_EXTRA_MODULES_PATH=/home/pi/Downloads/opencv_contrib-3.4.0/modules -D BUILD_EXAMPLES=ON -D WITH_LIBV4L=ON PYTHON3_EXECUTABLE=/usr/bin/python3.6 PYTHON_INCLUDE_DIR=/usr/include/python3.6 PYTHON_LIBRARY=/usr/lib/aarch64-linux-gnu/libpython3.6m.so PYTHON3_NUMPY_INCLUDE_DIRS=/home/pi/Develop/venv/lib/python3.6/site-packages/numpy/core/include ..
```

# notes
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


