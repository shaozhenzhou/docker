# OPENBLAS

## after install openblas atlas lapack cblas...
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
 
```
(venv) pi@NanoPi-M4:~/Develop/vision/examples/face_recognition$ export OPANBLAS_NUM_THREADS=2
(venv) pi@NanoPi-M4:~/Develop/vision/examples/face_recognition$ python3 facecam_one2one.py -c 8 -m libface -t 0.45 -w 1 -v True
[INFO] 载入 邵震洲 的 3 个人脸数据...
Xlib:  extension "RANDR" missing on display ":1.0".
[1] faceDetect 耗时 0.04177403450012207: . 
[2] shapePredict 耗时 0.017442703247070312: . 
[3] get_face_chip 耗时 0.001931905746459961: . 
[4] compute_face_descriptor 耗时 0.2901155948638916: . 
[5] numpy.array 耗时 9.608268737792969e-05: . 
[0.39446988 0.37935403 0.40256199]
[6] compare 耗时 0.0022046566009521484: . is find: True
[1] faceDetect 耗时 0.029941558837890625: . 
[2] shapePredict 耗时 0.017508506774902344: . 
[3] get_face_chip 耗时 0.0019273757934570312: . 
[4] compute_face_descriptor 耗时 0.19588518142700195: . 
[5] numpy.array 耗时 6.318092346191406e-05: . 
[0.42288705 0.38896902 0.44038137]
[6] compare 耗时 0.0017435550689697266: . is find: True
[1] faceDetect 耗时 0.025814294815063477: . 
[2] shapePredict 耗时 0.015752553939819336: . 
[3] get_face_chip 耗时 0.0019421577453613281: . 
[4] compute_face_descriptor 耗时 0.1848924160003662: . 
[5] numpy.array 耗时 5.435943603515625e-05: . 
[0.42573228 0.38673605 0.4417031 ]
[6] compare 耗时 0.0017976760864257812: . is find: True
[1] faceDetect 耗时 0.026836395263671875: . 
[2] shapePredict 耗时 0.025004863739013672: . 
[3] get_face_chip 耗时 0.001895904541015625: . 
[4] compute_face_descriptor 耗时 0.1847374439239502: . 
[5] numpy.array 耗时 5.364418029785156e-05: . 
[0.42629598 0.39226357 0.44699121]
[6] compare 耗时 0.0017497539520263672: . is find: True
[1] faceDetect 耗时 0.06320881843566895: . 
[2] shapePredict 耗时 0.015877246856689453: . 
[3] get_face_chip 耗时 0.0017426013946533203: . 
[4] compute_face_descriptor 耗时 0.180588960647583: . 
[5] numpy.array 耗时 6.29425048828125e-05: . 
[0.42569668 0.39137836 0.44359426]
[6] compare 耗时 0.0020062923431396484: . is find: True
[INFO] In 1.08 sec , True: 3 , False: 0 , Recognition rate 100.00%
[1] faceDetect 耗时 0.019308805465698242: . 
[2] shapePredict 耗时 0.015018224716186523: . 
[3] get_face_chip 耗时 0.0010445117950439453: . 
[4] compute_face_descriptor 耗时 0.13967394828796387: . 
[5] numpy.array 耗时 3.814697265625e-05: . 
[0.38863022 0.36446401 0.41208408]
[6] compare 耗时 0.001219034194946289: . is find: True
[1] faceDetect 耗时 0.013272762298583984: . 
[2] shapePredict 耗时 0.01516103744506836: . 
[3] get_face_chip 耗时 0.0010616779327392578: . 
[4] compute_face_descriptor 耗时 0.1369764804840088: . 
[5] numpy.array 耗时 3.838539123535156e-05: . 
[0.41355796 0.37288625 0.42813597]
[6] compare 耗时 0.0011754035949707031: . is find: True
[1] faceDetect 耗时 0.013328313827514648: . 
[2] shapePredict 耗时 0.010209321975708008: . 
[3] get_face_chip 耗时 0.0011355876922607422: . 
[4] compute_face_descriptor 耗时 0.12943577766418457: . 
[5] numpy.array 耗时 0.0001995563507080078: . 
[0.36552079 0.3278516  0.40060149]
[6] compare 耗时 0.0011386871337890625: . is find: True
[1] faceDetect 耗时 0.013411283493041992: . 
[2] shapePredict 耗时 0.008115053176879883: . 
[3] get_face_chip 耗时 0.001177072525024414: . 
[4] compute_face_descriptor 耗时 0.13486409187316895: . 
[5] numpy.array 耗时 0.0002028942108154297: . 
[0.37473824 0.3304121  0.41557291]
[6] compare 耗时 0.0011813640594482422: . is find: True
[1] faceDetect 耗时 0.013804197311401367: . 
[2] shapePredict 耗时 0.006161928176879883: . 
[3] get_face_chip 耗时 0.0011322498321533203: . 
[4] compute_face_descriptor 耗时 0.16379547119140625: . 
[5] numpy.array 耗时 3.695487976074219e-05: . 
[0.37463595 0.34126348 0.40594757]
[6] compare 耗时 0.0011675357818603516: . is find: True
[INFO] In 1.06 sec , True: 4 , False: 0 , Recognition rate 100.00%
[1] faceDetect 耗时 0.029458999633789062: . 
[2] shapePredict 耗时 0.006291627883911133: . 
[3] get_face_chip 耗时 0.0011508464813232422: . 
[4] compute_face_descriptor 耗时 0.17031526565551758: . 
[5] numpy.array 耗时 5.793571472167969e-05: . 
[0.38423525 0.35680517 0.41556176]
[6] compare 耗时 0.0028870105743408203: . is find: True
[1] faceDetect 耗时 0.02535724639892578: . 
[2] shapePredict 耗时 0.015540361404418945: . 
[3] get_face_chip 耗时 0.0018787384033203125: . 
[4] compute_face_descriptor 耗时 0.19990754127502441: . 
[5] numpy.array 耗时 5.1975250244140625e-05: . 
[0.37859237 0.32446484 0.39002595]
[6] compare 耗时 0.00174713134765625: . is find: True
[1] faceDetect 耗时 0.025155305862426758: . 
[2] shapePredict 耗时 0.015303611755371094: . 
[3] get_face_chip 耗时 0.0018315315246582031: . 
[4] compute_face_descriptor 耗时 0.16968965530395508: . 
[5] numpy.array 耗时 6.318092346191406e-05: . 
[0.37782728 0.31767632 0.38637286]
[6] compare 耗时 0.0017576217651367188: . is find: True
[1] faceDetect 耗时 0.025295257568359375: . 
[2] shapePredict 耗时 0.015528440475463867: . 
[3] get_face_chip 耗时 0.0018494129180908203: . 
[4] compute_face_descriptor 耗时 0.17029190063476562: . 
[5] numpy.array 耗时 5.4836273193359375e-05: . 
[0.36962071 0.32206373 0.40163452]
[6] compare 耗时 0.0017278194427490234: . is find: True
[INFO] In 1.10 sec , True: 3 , False: 0 , Recognition rate 100.00%
[1] faceDetect 耗时 0.025183439254760742: . 
[2] shapePredict 耗时 0.01811528205871582: . 
[3] get_face_chip 耗时 0.0018432140350341797: . 
[4] compute_face_descriptor 耗时 0.17160677909851074: . 
[5] numpy.array 耗时 5.364418029785156e-05: . 
[0.36457075 0.31017368 0.40173088]
[6] compare 耗时 0.00174713134765625: . is find: True
[1] faceDetect 耗时 0.025185108184814453: . 
[2] shapePredict 耗时 0.015915632247924805: . 
[3] get_face_chip 耗时 0.0018239021301269531: . 
[4] compute_face_descriptor 耗时 0.17549490928649902: . 
[5] numpy.array 耗时 5.626678466796875e-05: . 
[0.36777485 0.31538244 0.39758494]
[6] compare 耗时 0.0017998218536376953: . is find: True
[INFO] elapsed time: 6.23
[INFO] approx. FPS: 2.57

```
