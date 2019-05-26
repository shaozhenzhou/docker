# 树莓派UbuntuMate安装vnc

## 解决无法加载字体(针对tightvncserver)
You should add the correct font path to the ~/.vnc/tightvncserver.conf or /etc/tightvncserver.conf files:
```
$ nano ~/.vnc/tightvncserver.conf
# 添加以下内容
$fontPath = "/usr/share/fonts/X11/misc/:/usr/share/fonts/truetype/:/usr/share/fonts/opentype/:/usr/share/fonts/X11/type1/:/usr/share/fonts/:/usr/share/fonts/Type1";
```


## 解决无法加载字体(针对vnc4server)
```
$ sudo nano /usr/bin/vncserver
# 修改字体段落，修改为：
if (!$fontPath) {
  $fontPath = "/usr/share/fonts/X11/misc/,".
              "/usr/share/fonts/X11/Type1/"
}

```

## 解决dbus问题
```
# 避免 Could not acquire name on session bus 错误
unset DBUS_SESSION_BUS_ADDRESS
```
 ## 解决键盘映射问题
```
# The export XKL_XMODMAP_DISABLE=1 line is needed to avoid keyboard mis-mapping
export XKL_XMODMAP_DISABLE=1
```


## 解决无法找到Xresources问题
With certain installs of TightVNC, window managers such as Xmonad will fail to initialize. TightVNC requires each user to have an .Xresources file in their home directory. Your .Xresources file is missing if TightVNC reports an error message like:
You should create the correct file, and TightVNC will populate it automatically. This can be done with the command:
```
touch ~/.Xresources
```

## (未解决)解决“Unable to start xrandr manager: 没有 RANDR 扩展” 问题
```
#参看xrandr版本
$ xrandr --version
xrandr program version       1.5.0
RandR extension missing
```

## xstartup配置文件 
```
GNU nano 2.9.3                                                                                                               /home/pi/.vnc/xstartup                                                                                                                          

#!/bin/sh

# The export XKL_XMODMAP_DISABLE=1 line is needed to avoid keyboard mis-mapping
export XKL_XMODMAP_DISABLE=1

# Uncomment the following two lines for normal desktop:
#unset SESSION_MANAGER

# 避免 Could not acquire name on session bus 错误
unset DBUS_SESSION_BUS_ADDRESS

[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources

# -solid Color  将根窗口的背景设置为指定颜色。此标志只用于颜色服务程序。
xsetroot -solid grey

# 启动粘贴板复制功能
vncconfig -iconic &

# 自动打开终端窗口
#x-terminal-emulator -geometry 80x24+10+10 -ls -title "$VNCDESKTOP Desktop" &

# 不需要打开x-window-manager
#x-window-manager &

# mate窗口管理器
mate-session &
# mate小程序面板
# mate-panel &

```

## 自启动配置（ubuntu-16.10 开始不再使用initd管理系统，改用systemd）


## （作废）自启动脚本 /etc/init.d/vnc
```
#! /bin/sh
export USER="pi"
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/bin/X11"
NAME=vnc

DISPLAY="1"
DEPTH="24"
GEOMETRY="1920x1080"
OPTIONS="-depth ${DEPTH} -geometry ${GEOMETRY} :${DISPLAY}"

start()
{
    su - $USER -c "vncserver ${OPTIONS}"
}
stop()
{
    su - $USER -c "vncserver -clean -kill :${DISPLAY}"
}
case "$1" in
    start)
        echo -n "Starting vncserver for user '${USER}' on :${DISPLAY} "
        start
        ;;
    stop)
        echo -n "Stopping vncserver for user '${USER}' on :${DISPLAY}"
        stop
        ;;
    restart)
        echo -n "Restarting vncserver for user '${USER}' on :${DISPLAY} "
        stop
        start
        ;;
****)
        echo "Usage: /etc/init.d/$NAME {start|stop|restart}"
        exit 1
        ;;
esac
exit 0

```


