# NanoPi-M4 安装VNC

# NanoPi-M4 特性
本文实现了RK3399 NanoPi-M4的VNC的开机自启动，以及原版桌面的显示  
系统：FriendlyDesktop  
最新版本 － 基于Ubuntu 18.04 64位系统构建。  
易于开发 － 兼容FriendlyCore的特性，集成经过优化的Qt5.10, QtCreator和Arduino IDE。  
轻巧 － 只需要很少的CPU资源即可执行顺畅，而且当内存容量充足时表现特别出色。  
省能源 － 它比其他常见的系统需要较少的资源运行相同的工作。  
简朴美 － 借由GTK+ 2，它拥有美观、支持国际化的用户界面。  
使用简单 － 提供用户如微软Windows般的应用程序列表。  
可自定义性 － 用户可以轻易自定义LXDE的外观。  
兼容标准 － 兼容于freedesktop.org标准。  
用于友善电子RK3399平台的FriendlyDesktop已经最佳化了对Mali GPU和VPU的支持，系统中已集成X.org驱动，支持Hardware Cursor、OpenGL图形加速等,支持4K硬解视频播放。  

## 安装LXDE桌面环境（也可以换成xfce4桌面），开启启动脚本不影响使用：
```
sudo apt-get install xorg lxde-core
```

## 安装Tightvncserver
```
sudo apt-get install tightvncserver
```

## 安装好过后输入以下命令设置VNC密码：
```
vncpasswd
```
先输入两次密码，密码长度最好在6-8个字节，然后会询问是否设置一个查看密码，个人建议选 n）；  

## 设置完密码后，第一次运行vncserver生成配置文件
```
vncserver
```

## 编辑~/.vnc/xstartup文件，在文章末尾添加：
```
lxterminal &
/usr/bin/lxsession -s LXDE &
```

## 进入最高权限模式并编辑
```
sudo su
```

## 把以下内容写入 /etc/init.d/tightvncserver 
```
sudo nano /etc/init.d/tightvncserver

#!/bin/sh
### BEGIN INIT INFO
# Provides: tightvncserver
# Required-Start: $syslog $remote_fs $network
# Required-Stop: $syslog $remote_fs $network
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: Starts VNC Server on system start.
# Description: Starts tight VNC Server. Script written by James Swineson.
### END INIT INFO
# /etc/init.d/tightvncserver
VNCUSER='pi'
case "$1" in
        start)
                su $VNCUSER -c '/usr/bin/tightvncserver :1'
                echo "Starting TightVNC Server for $VNCUSER"
        ;;
        stop)
                pkill Xtightvnc
                echo "TightVNC Server stopped"
        ;;
        *)
                echo "Usage: /etc/init.d/tightvncserver {start|stop}"
                exit 1
        ;;
esac
exit 0
```
crtl+o保存；ctrl+x：退出；Enter：确定  
注：用户名要修改成自己的修改USER变量。  

## 修改文件权限，并更新开机启动列表
```
sudo chmod 755 /etc/init.d/tightvncserver
sudo update-rc.d tightvncserver defaults
sudo reboot
```
不需要到板子上面开启vncserver了，直接打开VNC Viewer登录。  

## 取消开机启动也很简单，就一行代码：
```
sudo update-rc.d -f tightvncserver remove
```

## 重点回顾：
1.修改~/vnc/xstartup 文件，增加终端配置：  
lxterminal &  
/usr/bin/lxsession -s LXDE &  
2.用root权限修改脚本  
sudo su  
3.写入/etc/init.d/tightvncserver脚本，及修改它的权限
sudo chmod 755 /etc/init.d/tightvncserver   
sudo update-rc.d tightvncserver defaults  





