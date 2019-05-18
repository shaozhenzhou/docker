# 安装DockerToolbox
`Windows10家庭版需要通过docker toolbox来安装`
- 下载Docker
下载地址：http://mirrors.aliyun.com/docker-toolbox/windows/docker-toolbox/
- 安装Docker Toolbox
## 简易启动模式
- 运行Docker Quickstart Terminal
- 过程中确认windows对网络安全提示
- 输入命令查看docker是否安装成功
```
# 查看docker配置信息
docker info

# 查看docker镜像
docker images

# 查看docker容器（-a 显示所有）
docker ps -a
```
## 手动启动模式
```
# 查看docker-machine版本
docker-machine -v

# 创建Docker虚拟机
docker-machine create --driver=virtualbox defalut

# 查看docker虚拟机进程
docker-machine ls

# 获得虚拟机环节变量
docker-machine env default

# 连接Docker Linux，在PowerShell中使用docker命令
docker-machine env default | Invoke-Expression

# 查看docker镜像
docker images
```
