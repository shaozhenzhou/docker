# 树莓派编译安装dlib

## 下载dlib，解压


## 为编译dlib配置缓存文件  
```
sudo nano /etc/dphys-swapfile
```  
将 CONF_SWAPSIZE=100 改为 CONF_SWAPSIZE=1024  
重新启动缓存，使其生效
```
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start
```
## 编译，制作whell文件
进入dlib解压目录
```
python3 setup.py bdist_wheel --compiler-flags "-mfpu=neon -O3" --set CMAKE_BUILD_TYPE=RELEASE --clean
```
## 安装dlib wheel
```
pip install dlib.wheel
```

## 将缓存文件改回来
`sudo nano /etc/dphys-swapfile`  
将 CONF_SWAPSIZE=1024 改为 CONF_SWAPSIZE=100  
重新启动缓存，使其生效
```
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start
```

