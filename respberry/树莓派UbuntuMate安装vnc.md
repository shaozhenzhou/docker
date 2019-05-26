# 树莓派UbuntuMate安装vnc

## 解决无法加载字体
You should add the correct font path to the ~/.vnc/tightvncserver.conf or /etc/tightvncserver.conf files:
```
$ nano ~/.vnc/tightvncserver.conf
# 添加以下内容
$fontPath = "/usr/share/fonts/X11/misc/:/usr/share/fonts/truetype/:/usr/share/fonts/opentype/:/usr/share/fonts/X11/type1/:/usr/share/fonts/:/usr/share/fonts/Type1";
```
## 解决无法找到Xresources问题
With certain installs of TightVNC, window managers such as Xmonad will fail to initialize. TightVNC requires each user to have an .Xresources file in their home directory. Your .Xresources file is missing if TightVNC reports an error message like:
You should create the correct file, and TightVNC will populate it automatically. This can be done with the command:
```
touch ~/.Xresources
```
## 解决“Unable to start xrandr manager: 没有 RANDR 扩展” 问题
```
#参看xrandr版本
```
$ xrandr --version
xrandr program version       1.5.0
RandR extension missing
```



