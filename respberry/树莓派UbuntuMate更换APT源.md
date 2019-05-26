# 树莓派UbuntuMate更换APT源
树莓派为arm64架构，在更换为国内源（如aliyun，163等）后，会出现以下错误，并导致安装软件还是从国外官方站点下载，速度很慢：
```
E: http://mirrors.aliyun.com/ubuntu/dists/bionic/main/binary-arm64/Packages  404  Not Found [IP: 115.223.15.217 80]
E: http://mirrors.aliyun.com/ubuntu/dists/bionic-security/main/binary-arm64/Packages  404  Not Found [IP: 115.223.15.217 80]
E: http://mirrors.aliyun.com/ubuntu/dists/bionic-updates/main/binary-arm64/Packages  404  Not Found [IP: 115.223.15.217 80]
E: http://mirrors.aliyun.com/ubuntu/dists/bionic-proposed/main/binary-arm64/Packages  404  Not Found [IP: 115.223.15.217 80]
E: http://mirrors.aliyun.com/ubuntu/dists/bionic-backports/main/binary-arm64/Packages  404  Not Found [IP: 115.223.15.217 80]
```

## 更换为 科技大学USTC的的源
参考文章：[https://raspberrypi.club/87.html]
官方地址：[http://mirrors.ustc.edu.cn]

将/etc/apt/sources.list文件中软件源的地址改为 http://mirrors.ustc.edu.cn/ubuntu-ports

然后执行apt update 或者apt-get update 就可以生效了。

下面是官方给出的Ubuntu 16.04的实例配置：
```
# 默认注释了源码仓库，如有需要可自行取消注释
deb https://mirrors.ustc.edu.cn/ubuntu-ports/ xenial main restricted universe multiverse
# deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ xenial main main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu-ports/ xenial-updates main restricted universe multiverse
# deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ xenial-updates main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu-ports/ xenial-backports main restricted universe multiverse
# deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ xenial-backports main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu-ports/ xenial-security main restricted universe multiverse
# deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ xenial-security main restricted universe multiverse
 
# 预发布软件源，不建议启用
# deb https://mirrors.ustc.edu.cn/ubuntu-ports/ xenial-proposed main restricted universe multiverse
# deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ xenial-proposed main restricted universe multiverse
```
其实我们不需要这么麻烦，一条命令即可解决源的更换，在备份好文件后执行以下命令：
```
sed -i 's/ports.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
```
然后在执行apt update 就可以了，不过还是先要备份文件。


