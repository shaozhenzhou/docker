# 树莓派UbuntuMate安装vnc

## 安装
```
sudo apt-get vnc4server
```

## 设置密码
```
vncpasswd
```

## 首次启动vnc
```
vncserver
```

## 修改 ~/.vnc/xstartup 配置信息
```
$ sudo nano ~/.vnc/xstartup
# 
```
### xstartup配置文件 
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

### 解决无法加载字体(针对tightvncserver)
You should add the correct font path to the ~/.vnc/tightvncserver.conf or /etc/tightvncserver.conf files:
```
$ nano ~/.vnc/tightvncserver.conf
# 添加以下内容
$fontPath = "/usr/share/fonts/X11/misc/:/usr/share/fonts/truetype/:/usr/share/fonts/opentype/:/usr/share/fonts/X11/type1/:/usr/share/fonts/:/usr/share/fonts/Type1";
```


### 解决无法加载字体(针对vnc4server)
```
$ sudo nano /usr/bin/vncserver
# 修改字体段落，修改为：
if (!$fontPath) {
  $fontPath = "/usr/share/fonts/X11/misc/,".
              "/usr/share/fonts/X11/Type1/"
}

```

### 解决dbus问题
```
# 避免 Could not acquire name on session bus 错误
unset DBUS_SESSION_BUS_ADDRESS
```
### 解决键盘映射问题
```
# The export XKL_XMODMAP_DISABLE=1 line is needed to avoid keyboard mis-mapping
export XKL_XMODMAP_DISABLE=1
```


### 解决无法找到Xresources问题
With certain installs of TightVNC, window managers such as Xmonad will fail to initialize. TightVNC requires each user to have an .Xresources file in their home directory. Your .Xresources file is missing if TightVNC reports an error message like:
You should create the correct file, and TightVNC will populate it automatically. This can be done with the command:
```
touch ~/.Xresources
```

### (未解决)解决“Unable to start xrandr manager: 没有 RANDR 扩展” 问题
```
#参看xrandr版本
$ xrandr --version
xrandr program version       1.5.0
RandR extension missing
```

## 自启动配置（ubuntu-16.10 开始不再使用initd管理系统，改用systemd）

### (推荐)采用systemd配置自启动
#### 创建service文件
```
$ sudo nano /etc/systemd/system/vncserver@.service
```
文件内容：
```
[Unit]
Description=Start VNCSERVER at startup
After=syslog.target network.target

[Service]
Type=forking
User=pi
Group=pi
WorkingDirectory=/home/pi

PIDFile=/home/pi/.vnc/%H:%i.pid
ExecStartPre=-/usr/bin/vncserver -kill :%i > /dev/null 2>&1
ExecStart=/usr/bin/vncserver -depth 24 -geometry 1920x1080 :%i
ExecStop=/usr/bin/vncserver -kill :%i

[Install]
WantedBy=multi-user.target

```

#### 装载service
```
$ sudo systemctl daemon-reload
```

#### 使能service
```
$ sudo systemctl enable vncserver@1.service

pi@RespBerryPi:~$ sudo systemctl enable vncserver@1.service
Created symlink /etc/systemd/system/multi-user.target.wants/vncserver@1.service → /etc/systemd/system/vncserver@.service.
```

#### 启动vnc服务
```
$ sudo systemctl start vncserver@1
```
#### 查看服务状态信息
```
$ sudo systemctl status vncserver@1

pi@RespBerryPi:~$ sudo systemctl status vncserver@1
● vncserver@1.service - Start VNCSERVER at startup
   Loaded: loaded (/etc/systemd/system/vncserver@.service; indirect; vendor preset: enabled)
   Active: active (running) since Sun 2019-05-26 19:33:05 CST; 7s ago
  Process: 3441 ExecStart=/usr/bin/vncserver -depth 24 -geometry 1920x1080 :1 (code=exited, status=0/SUCCESS)
  Process: 3437 ExecStartPre=/usr/bin/vncserver -kill :1 > /dev/null 2>&1 (code=exited, status=2)
 Main PID: 3448 (Xvnc4)
    Tasks: 179 (limit: 1056)
   CGroup: /system.slice/system-vncserver.slice/vncserver@1.service
           ├─3448 Xvnc4 :1 -desktop RespBerryPi:1 (pi) -auth /home/pi/.Xauthority -geometry 1920x1080 -depth 24 -rfbwait 30000 -rfbauth /home/pi/.vnc/passwd -rfbport 5901 -pn -fp /usr/share/fonts/X11/misc/,/usr/share/fonts/X11/Type1/ -co /etc/X11/rgb
           ├─3461 vncconfig -iconic
           ├─3462 mate-session
           ├─3465 dbus-launch --exit-with-session mate-session
           ├─3466 /usr/bin/dbus-daemon --syslog --fork --print-pid 5 --print-address 7 --session
           ├─3468 /usr/lib/at-spi2-core/at-spi-bus-launcher
           ├─3473 /usr/bin/dbus-daemon --config-file=/usr/share/defaults/at-spi2/accessibility.conf --nofork --print-address 3
           ├─3476 /usr/lib/at-spi2-core/at-spi2-registryd --use-gnome-session
           ├─3490 /usr/lib/dconf/dconf-service
           ├─3496 gnome-keyring-daemon --start
           ├─3502 /usr/bin/mate-settings-daemon
           ├─3514 marco --no-composite
           ├─3516 /usr/lib/gvfs/gvfsd
           ├─3521 /usr/lib/gvfs/gvfsd-fuse /home/pi/.gvfs -f -o big_writes
           ├─3535 mate-panel
           ├─3538 /usr/bin/pulseaudio --start --log-target=syslog
           ├─3555 caja
           ├─3560 /usr/lib/mate-panel/wnck-applet
           ├─3563 /usr/lib/mate-applets/trashapplet
           ├─3565 /usr/lib/aarch64-linux-gnu/brisk-menu//brisk-menu
           ├─3567 /usr/lib/mate-applets/mate-cpufreq-applet
           ├─3569 /usr/lib/mate-applets/mate-multiload-applet
           ├─3571 /usr/lib/mate-applets/command-applet
           ├─3573 /usr/lib/mate-panel/clock-applet
           ├─3576 /usr/lib/mate-panel/notification-area-applet
           ├─3577 /usr/lib/mate-indicator-applet/mate-indicator-applet-complete
           ├─3578 mate-screensaver
           ├─3588 update-notifier
           ├─3590 /usr/bin/python3 /usr/share/system-config-printer/applet.py
           ├─3592 nm-applet
           ├─3621 /usr/lib/gvfs/gvfs-udisks2-volume-monitor
           ├─3639 /usr/lib/deja-dup/deja-dup-monitor
           ├─3650 /usr/bin/python3 /usr/bin/blueman-applet
           ├─3653 mate-maximus
           ├─3661 /usr/lib/aarch64-linux-gnu/indicator-application/indicator-application-service
           ├─3665 /usr/lib/aarch64-linux-gnu/indicator-sound/indicator-sound-service
           ├─3668 /usr/lib/aarch64-linux-gnu/indicator-session/indicator-session-service
           ├─3671 /usr/lib/aarch64-linux-gnu/indicator-messages/indicator-messages-service
           ├─3675 /usr/lib/aarch64-linux-gnu/indicator-power/indicator-power-service
           ├─3721 /usr/lib/gvfs/gvfsd-trash --spawner :1.10 /org/gtk/gvfs/exec_spaw/0
           ├─3737 /usr/lib/gvfs/gvfsd-metadata
           ├─3746 /usr/lib/gvfs/gvfs-gphoto2-volume-monitor
           ├─3753 /usr/bin/python3 /usr/lib/update-notifier/apt-check
           ├─3754 /usr/lib/gvfs/gvfs-goa-volume-monitor
           ├─3760 /usr/lib/gvfs/gvfs-mtp-volume-monitor
           └─3765 /usr/lib/gvfs/gvfs-afc-volume-monitor

5月 26 19:33:12 RespBerryPi dbus-daemon[3466]: [session uid=1000 pid=3464] Activating service name='org.gtk.vfs.AfcVolumeMonitor' requested by ':1.38' (uid=1000 pid=3639 comm="/usr/lib/deja-dup/deja-dup-monitor " label="unconfined")
5月 26 19:33:12 RespBerryPi org.gtk.vfs.AfcVolumeMonitor[3466]: Volume monitor alive
5月 26 19:33:12 RespBerryPi dbus-daemon[3466]: [session uid=1000 pid=3464] Successfully activated service 'org.gtk.vfs.AfcVolumeMonitor'
5月 26 19:33:12 RespBerryPi wnck-applet[3560]: g_object_set: assertion 'G_IS_OBJECT (object)' failed
5月 26 19:33:12 RespBerryPi clock-applet[3573]: Negative content width -1 (allocation 1, extents 1x1) while allocating gadget (node button, owner GtkToggleButton)
5月 26 19:33:12 RespBerryPi brisk-menu[3565]: Failed to bind keyboard shortcut
5月 26 19:33:13 RespBerryPi brisk-menu[3565]: gdk_window_get_origin: assertion 'GDK_IS_WINDOW (window)' failed
5月 26 19:33:13 RespBerryPi brisk-menu[3565]: gdk_window_get_origin: assertion 'GDK_IS_WINDOW (window)' failed
5月 26 19:33:13 RespBerryPi brisk-menu[3565]: Negative content width -10 (allocation 1, extents 5x6) while allocating gadget (node button, owner GtkToggleButton)
5月 26 19:33:13 RespBerryPi brisk-menu[3565]: Negative content height -7 (allocation 1, extents 4x4) while allocating gadget (node button, owner GtkToggleButton)

```


### （作废）自启动脚本 /etc/init.d/vnc
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


