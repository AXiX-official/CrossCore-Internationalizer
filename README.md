# CrossCore-Internationalizer

一个使用官方资源帮助你访问交错战线(CrossCore)的国际服资源的非官方工具。

## 原理

截止本仓库发布时，官方开关只剩一个和谐文件索引没有放出,正式服中的索引文件内容为`close`。本仓库通过重定向请求到本仓库的索引文件，从而能从正式服下载反和谐资源。

## 依赖

1. [Virtual-Hosts](https://github.com/x-falcon/Virtual-Hosts)
2. python3
   1. mitmproxy

## 使用方法

1. 修改`Android/data/com.megagame.crosscore*/files`下的`internation.txt`中的`0`为任意非零值，或者直接删除`internation_close.txt`文件。
2. 从[Virtual-Hosts](https://github.com/x-falcon/Virtual-Hosts)仓库的[Release](https://github.com/x-falcon/Virtual-Hosts/releases)界面获取Virtual-Hosts的安装包，在模拟器/安卓设备上安装Virtual-Hosts。
3. Clone本仓库到本地。保证电脑和模拟器/安卓设备在同一局域网下,使用ipconfig/ifconfig等命令获取电脑的局域网IP地址。在模拟器/安卓设备上创建或上传一个hosts.txt文件，内容为如下格式：
   ```
   192.168.*.* cdn.megagamelog.com
   ```
   其中192.168.*.*为电脑的局域网IP地址。
4. 在Virtual-Hosts中添加hosts.txt文件，然后启用Virtual-Hosts。
5. 如果没安装过mitmproxy，运行`pip install mitmproxy`安装mitmproxy。然后将`/.mitmproxy / mitmproxy-ca-cert.cer`证书文件安装到模拟器/安卓设备上。
6. 在本仓库的根目录下运行`mitmproxy -p 443 -s server.py`，然后在模拟器/安卓设备上启动交错战线，即可更新国际服资源(请勿在更新过程中关闭mitmproxy)。

## 最后

如果有任何问题，欢迎提issue。
如果你有更好的方法，欢迎提PR。