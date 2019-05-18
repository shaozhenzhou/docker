# 配置Docker镜像加速
- 登录aliyun获得镜像地址
- 地址：https://cr.console.aliyun.com/cn-hangzhou/mirrors
- 菜单：镜像加速器
- 复制镜像加速地址：https://934j9la1.mirror.aliyuncs.com
- 连接docker虚拟机
```
docker-machine ssh default 
```
- 运行以下命令
```
sudo sed -i "s|EXTRA_ARGS='|EXTRA_ARGS='--registry-mirror=https://934j9la1.mirror.aliyuncs.com |g" /var/lib/boot2docker/profile 
```
- 退出docker虚拟机ssh连接
```
exit 
```
- 重新启动docker虚拟机
```
docker-machine restart default
```
- 虚拟机可能地址变动，重新刷新环境变量
```
docker-machine env
```
- 重新连接docker环境到PowerShell
```
docker-machine env | Invoke-Expression
```
- 查看mirror参数
```
docker info

# 得到以下mirror配置信息
Registry Mirrors:
 https://934j9la1.mirror.aliyuncs.com/
```

