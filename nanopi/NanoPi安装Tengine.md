# NanoPi安装Tengine
Tengine 是OPEN AI LAB为嵌入式设备开发的一个轻量级、高性能并且模块化的引擎。
Tengine在嵌入式设备上支持CPU，GPU，DLA/NPU，DSP异构计算的计算框架，实现异构计算的调度器，基于ARM平台的高效的计算库实现，针对特定硬件平台的性能优化，动态规划计算图的内存使用，提供对于网络远端AI计算能力的访问支持，支持多级别并行，整个系统模块可拆卸，基于事件驱动的计算模型，吸取已有AI计算框架的优点，设计全新的计算图表示。
参考：
GPU CPU异构调度跑MobilenetSSD [https://github.com/OAID/Tengine/wiki/GPU-CPU%E5%BC%82%E6%9E%84%E8%B0%83%E5%BA%A6%E8%B7%91MobilenetSSD]  
Tengine安装教程 [https://github.com/OAID/Tengine/wiki/Tengine%E5%AE%89%E8%A3%85%E6%95%99%E7%A8%8B]  


## 安装依赖库
```
sudo apt-get install libprotobuf-dev protobuf-compiler libboost-all-dev libgoogle-glog-dev libopencv-dev libopenblas-dev
```
protobuf 是一种轻便高效的数据存储格式，这是caffe各种配置文件所使用的数据格式  
boost 是一个c++的扩展程序库，稍后Tengine的编译依赖于该库  
google-glog 是一个google提供的日志系统的程序库  
opencv 是一个开源的计算机视觉库  
openblas 是一个开源的基础线性代数子程序库  

## 安装scons
scons是一个Python写的自动化构建工具，需要安装python和scons后才能运行，能够跨平台。其集成功能类似于autoconf/automake ，是一个简洁可靠的工具。现在很多系统都自带python 所以直接安装scons即可。  
下载：地址 [https://sourceforge.net/projects/scons/files/scons/3.0.5/scons-3.0.5.tar.gz]
```
cd ~/Downloads
wget https://sourceforge.net/projects/scons/files/scons/3.0.5/scons-3.0.5.tar.gz
tar -zxvf scons-3.0.5.tar.gz
cd scons-3.0.5
sudo python setup.py install
```

## 安装ACL
```
git clone https://github.com/ARM-software/ComputeLibrary.git
cd ~/Develop/ComputeLibrary
scons Werror=1 -j4 debug=0 asserts=1 neon=0 opencl=1 embed_kernels=1 os=linux arch=arm64-v8a
```

## set GPU frequency
```
sudo su
echo "performance" >/sys/devices/platform/ff9a0000.gpu/devfreq/ff9a0000.gpu/governor
cat /sys/devices/platform/ff9a0000.gpu/devfreq/ff9a0000.gpu/cur_freq
```

## 安装Tengine(build tengine with ACL)
### edit makefile.config
```
cp makefile.config.example makefile.config
nano makefile.config

CONFIG_ACL_GPU=y
ACL_ROOT=/home/pi/Develop/ComputeLibrary
```
### build
```
make -j4 
make install
```

### build mssd
download model from Tengine model zoo [ https://pan.baidu.com/s/1LXZ8vOdyOo50IXS0CUPp8g ] (psw: 57vb) to ~/tengine/models/:
build
```
cd example/mobilenet_ssd
# 修改mssd.cpp，将CV_FILLED，改为-1
cmake -DTENGINE_DIR=/home/pi/Develop/Tengine .
make 
```

## run mssd
```
export GPU_CONCAT=0           # disable gpu run concat,     avoid frequent data transfer between cpu and gpu
export ACL_FP16=1             # enable gpu fp16
export REPEAT_COUNT=50        # repeat count to run mssd,     get avg time
taskset 0x1 ./MSSD -d acl_opencl          # -d acl_opencl to use gpu, taskset 0x1 to bind cpu0(A53)

pi@NanoPi-M4:~/Develop/Tengine/examples/mobilenet_ssd$ taskset 0x1 ./MSSD -d acl_opencl 
/home/pi/Develop/Tengine/examples/mobilenet_ssd/MSSD
proto file not specified,using /home/pi/Develop/Tengine/models/MobileNetSSD_deploy.prototxt by default
model file not specified,using /home/pi/Develop/Tengine/models/MobileNetSSD_deploy.caffemodel by default
image file not specified,using /home/pi/Develop/Tengine/tests/images/ssd_dog.jpg by default
ACL Graph Initialized
Driver: ACLGraph probed 1 devices
--------------------------------------
repeat 50 times, avg time per run is 174.168 ms
detect result num: 3 
dog     :100%
BOX:( 138.419 , 209.091 ),( 324.504 , 541.568 )
car     :100%
BOX:( 467.356 , 72.9224 ),( 687.269 , 171.123 )
bicycle :100%
BOX:( 107.053 , 140.221 ),( 574.472 , 415.248 )
======================================
[DETECTED IMAGE SAVED]: save.jpg
======================================
```



