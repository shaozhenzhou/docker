# OPENBLAS
```
pi@NanoPi-M4:~$ sudo find / -name libblas.so*
/etc/alternatives/libblas.so.3-aarch64-linux-gnu
/etc/alternatives/libblas.so-aarch64-linux-gnu
find: ‘/run/user/1000/gvfs’: 权限不够
/usr/lib/aarch64-linux-gnu/blas/libblas.so.3
/usr/lib/aarch64-linux-gnu/blas/libblas.so.3.7.1
/usr/lib/aarch64-linux-gnu/atlas/libblas.so.3
/usr/lib/aarch64-linux-gnu/atlas/libblas.so
/usr/lib/aarch64-linux-gnu/atlas/libblas.so.3.10.3
/usr/lib/aarch64-linux-gnu/libblas.so.3
/usr/lib/aarch64-linux-gnu/libblas.so
/var/lib/dpkg/alternatives/libblas.so.3-aarch64-linux-gnu
/var/lib/dpkg/alternatives/libblas.so-aarch64-linux-gnu

pi@NanoPi-M4:~$ sudo find / -name liblapack.so*
/etc/alternatives/liblapack.so.3-aarch64-linux-gnu
/etc/alternatives/liblapack.so-aarch64-linux-gnu
find: ‘/run/user/1000/gvfs’: 权限不够
/usr/lib/aarch64-linux-gnu/lapack/liblapack.so.3
/usr/lib/aarch64-linux-gnu/lapack/liblapack.so.3.7.1
/usr/lib/aarch64-linux-gnu/atlas/liblapack.so.3.10.3
/usr/lib/aarch64-linux-gnu/atlas/liblapack.so.3
/usr/lib/aarch64-linux-gnu/atlas/liblapack.so
/usr/lib/aarch64-linux-gnu/liblapack.so.3
/usr/lib/aarch64-linux-gnu/liblapack.so
/var/lib/dpkg/alternatives/liblapack.so.3-aarch64-linux-gnu
/var/lib/dpkg/alternatives/liblapack.so-aarch64-linux-gnu


pi@NanoPi-M4:~$ sudo find / -name libatlas.so*
find: ‘/run/user/1000/gvfs’: 权限不够
/usr/lib/aarch64-linux-gnu/libatlas.so.3
/usr/lib/aarch64-linux-gnu/libatlas.so
/usr/lib/aarch64-linux-gnu/libatlas.so.3.10.3






pi@NanoPi-M4:~$ ls /usr/lib/aarch64-linux-gnu/blas -la
总用量 392
drwxr-xr-x   2 root root   4096 5月   4 18:55 .
drwxr-xr-x 105 root root  69632 5月  20 16:10 ..
lrwxrwxrwx   1 root root     16 11月 29  2017 libblas.so.3 -> libblas.so.3.7.1
-rw-r--r--   1 root root 326840 11月 29  2017 libblas.so.3.7.1
pi@NanoPi-M4:~$ ls /usr/lib/aarch64-linux-gnu/lapack -la
总用量 5056
drwxr-xr-x   2 root root    4096 5月  20 16:24 .
drwxr-xr-x 105 root root   69632 5月  20 16:10 ..
lrwxrwxrwx   1 root root      18 11月 29  2017 liblapack.so.3 -> liblapack.so.3.7.1
-rw-r--r--   1 root root 5101128 11月 29  2017 liblapack.so.3.7.1
pi@NanoPi-M4:~$ ls /usr/lib/aarch64-linux-gnu/atlas -la
总用量 22724
drwxr-xr-x   2 root root    4096 5月  19 17:47 .
drwxr-xr-x 105 root root   69632 5月  20 16:10 ..
-rw-r--r--   1 root root 6069784 9月  14  2017 libblas.a
lrwxrwxrwx   1 root root      17 9月  14  2017 libblas.so -> libblas.so.3.10.3
lrwxrwxrwx   1 root root      17 9月  14  2017 libblas.so.3 -> libblas.so.3.10.3
-rw-r--r--   1 root root 2484232 9月  14  2017 libblas.so.3.10.3
-rw-r--r--   1 root root 9448606 9月  14  2017 liblapack.a
lrwxrwxrwx   1 root root      19 9月  14  2017 liblapack.so -> liblapack.so.3.10.3
lrwxrwxrwx   1 root root      19 9月  14  2017 liblapack.so.3 -> liblapack.so.3.10.3
-rw-r--r--   1 root root 5189512 9月  14  2017 liblapack.so.3.10.3




-- Searching for BLAS and LAPACK
-- Searching for BLAS and LAPACK
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.29.1") 
-- Checking for module 'cblas'
--   No package 'cblas' found
-- Checking for module 'lapack'
--   Found lapack, version 3.10.3
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of void*
-- Check size of void* - done
-- Found LAPACK library
-- Found ATLAS BLAS library
-- Looking for cblas_ddot
-- Looking for cblas_ddot - not found
-- BLAS library does not have cblas symbols, so dlib will not use BLAS or LAPACK
 *****************************************************************************
 *** No BLAS library found so using dlib's built in BLAS.  However, if you ***
 *** install an optimized BLAS such as OpenBLAS or the Intel MKL your code ***
 *** will run faster.  On Ubuntu you can install OpenBLAS by executing:    ***
 ***    sudo apt-get install libopenblas-dev liblapack-dev                 ***
 *** Or you can easily install OpenBLAS from source by downloading the     ***
 *** source tar file from http://www.openblas.net, extracting it, and      ***
 *** running:                                                              ***
 ***    make; sudo make install                                            ***
 *****************************************************************************
```




## After Clean:
### find blas and lapack
```
pi@NanoPi-M4:~/Downloads/dlib-19.17$ sudo find / -name liblapack.so*
find: ‘/run/user/1000/gvfs’: 权限不够
pi@NanoPi-M4:~/Downloads/dlib-19.17$ sudo find / -name libblas.so*
find: ‘/run/user/1000/gvfs’: 权限不够
pi@NanoPi-M4:~/Downloads/dlib-19.17$ sudo find / -name libatlas.so*
find: ‘/run/user/1000/gvfs’: 权限不够
```

### Install Dlib Setup
```
-- Searching for BLAS and LAPACK
-- Searching for BLAS and LAPACK
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.29.1") 
-- Checking for module 'cblas'
--   No package 'cblas' found
-- Checking for module 'lapack'
--   No package 'lapack' found
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of void*
-- Check size of void* - done
-- Found ATLAS BLAS library
-- Looking for cblas_ddot
-- Looking for cblas_ddot - not found
-- BLAS library does not have cblas symbols, so dlib will not use BLAS or LAPACK
 *****************************************************************************
 *** No BLAS library found so using dlib's built in BLAS.  However, if you ***
 *** install an optimized BLAS such as OpenBLAS or the Intel MKL your code ***
 *** will run faster.  On Ubuntu you can install OpenBLAS by executing:    ***
 ***    sudo apt-get install libopenblas-dev liblapack-dev                 ***
 *** Or you can easily install OpenBLAS from source by downloading the     ***
 *** source tar file from http://www.openblas.net, extracting it, and      ***
 *** running:                                                              ***
 ***    make; sudo make install                                            ***
 *****************************************************************************
 ```
 
 ## After reinstall openblas (sudo apt-get install libopenblas-dev)
 note: NO liblapack
 ### find blas and lapack
 ```
pi@NanoPi-M4:~/Downloads/dlib-19.17$ sudo find / -name libatlas.so*
find: ‘/run/user/1000/gvfs’: 权限不够

pi@NanoPi-M4:~/Downloads/dlib-19.17$ sudo find / -name libblas.so*
/etc/alternatives/libblas.so.3-aarch64-linux-gnu
/etc/alternatives/libblas.so-aarch64-linux-gnu
find: ‘/proc/15741’: 没有那个文件或目录
find: ‘/run/user/1000/gvfs’: 权限不够
/usr/lib/aarch64-linux-gnu/openblas/libblas.so
/usr/lib/aarch64-linux-gnu/openblas/libblas.so.3
/usr/lib/aarch64-linux-gnu/libblas.so.3
/usr/lib/aarch64-linux-gnu/libblas.so
/var/lib/dpkg/alternatives/libblas.so.3-aarch64-linux-gnu
/var/lib/dpkg/alternatives/libblas.so-aarch64-linux-gnu

pi@NanoPi-M4:~/Downloads/dlib-19.17$ sudo find / -name liblapack.so*
/etc/alternatives/liblapack.so.3-aarch64-linux-gnu
/etc/alternatives/liblapack.so-aarch64-linux-gnu
find: ‘/proc/15754’: 没有那个文件或目录
find: ‘/run/user/1000/gvfs’: 权限不够
/usr/lib/aarch64-linux-gnu/openblas/liblapack.so.3
/usr/lib/aarch64-linux-gnu/openblas/liblapack.so
/usr/lib/aarch64-linux-gnu/liblapack.so.3
/usr/lib/aarch64-linux-gnu/liblapack.so
/var/lib/dpkg/alternatives/liblapack.so.3-aarch64-linux-gnu
/var/lib/dpkg/alternatives/liblapack.so-aarch64-linux-gnu

```
### Install Dlib Setup
 
 ```
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

```
 

