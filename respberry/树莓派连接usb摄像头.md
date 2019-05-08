# 树莓派连接usb摄像头

## 连接摄像头
在设备usb口插入摄像头

## 查看USB设备
`lsusb`
如果正常，可以看到类似信息：  
```
pi@raspberrypi:~ $ lsusb
Bus 001 Device 010: ID 046d:0825 Logitech, Inc. Webcam C270
Bus 001 Device 004: ID 0424:7800 Standard Microsystems Corp. 
Bus 001 Device 003: ID 0424:2514 Standard Microsystems Corp. USB 2.0 Hub
Bus 001 Device 002: ID 0424:2514 Standard Microsystems Corp. USB 2.0 Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```
## 查看视频设备
```
pi@raspberrypi:~ $ ls /dev/video*
/dev/video0
```
## 查看演示视频
```
sudo apt-get install luvcview
luvcview
```

