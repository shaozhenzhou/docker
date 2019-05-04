# 树莓派安装face_recognition

## 为编译dlib配置缓存文件  
`sudo nano /etc/dphys-swapfile`  
将 CONF_SWAPSIZE=100 改为 CONF_SWAPSIZE=1024  
重新启动缓存，使其生效
```
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start
```

## 手动下载 [face_recognition_models-0.3.0-py2.py3-none-any.whl](https://pypi.org/project/face_recognition_models/)  
`https://files.pythonhosted.org/packages/cf/3b/4fd8c534f6c0d1b80ce0973d01331525538045084c73c153ee6df20224cf/face_recognition_models-0.3.0.tar.gz`

## 手动安装 face_recognition_models  
> 为防止face_recognition自带的setup.py去国外网站下载模型数据，从而导致安装失败，需要手动下载，在安装face_recognition之前，先完成模型数据的安装  
解压缩 face_recognition_models-0.3.0.tar.gz  
pip3 install wheel  
pip3 isntall ~/Downloads/face_recognition_models-0.3.0-py2.py3-none-any.whl  

## 安装face_recognition  
`pip3 install face_recognition`  

## 将缓存文件改回来
`sudo nano /etc/dphys-swapfile`  
将 CONF_SWAPSIZE=1024 改为 CONF_SWAPSIZE=100  
重新启动缓存，使其生效
```
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start
```
