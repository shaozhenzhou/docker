# 树莓派UbuntuMate更换APT源
装了Ubuntu后你会发现apt-get update 更新源会非常慢，因为默认Ubuntu的更新源在国外，有时候甚至无法连接，所以换成国内的源是必要的。国内的更新源比较多，比如阿里云、163、清华大学等等吧，但是树莓派是arm64平台，我试用了大部分源都对arm64都支持的不是很好，不过科技大学USTC的的源支持的很好，这里就拿更换中国科技大学的apt源来记录过程。
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
deb http://mirrors.ustc.edu.cn/ubuntu-ports/ bionic main multiverse restricted universe
deb http://mirrors.ustc.edu.cn/ubuntu-ports/ bionic-backports main multiverse restricted universe
deb http://mirrors.ustc.edu.cn/ubuntu-ports/ bionic-proposed main multiverse restricted universe
deb http://mirrors.ustc.edu.cn/ubuntu-ports/ bionic-security main multiverse restricted universe
deb http://mirrors.ustc.edu.cn/ubuntu-ports/ bionic-updates main multiverse restricted universe
deb-src http://mirrors.ustc.edu.cn/ubuntu-ports/ bionic main multiverse restricted universe
deb-src http://mirrors.ustc.edu.cn/ubuntu-ports/ bionic-backports main multiverse restricted universe
deb-src http://mirrors.ustc.edu.cn/ubuntu-ports/ bionic-proposed main multiverse restricted universe
deb-src http://mirrors.ustc.edu.cn/ubuntu-ports/ bionic-security main multiverse restricted universe
deb-src http://mirrors.ustc.edu.cn/ubuntu-ports/ bionic-updates main multiverse restricted universe
```
然后再执行apt update 就可以了，不过还是先要备份文件。


