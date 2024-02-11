# CrossCore-Internationalizer

一个使用官方资源帮助你访问交错战线(CrossCore)的国际服资源的非官方工具。
如果官方发布了非和谐资源，本仓库将停止更新。

## 省流

**推荐**

直接在[Release]()(暂缺)界面下载最新的反和谐包,或者自行使用`down.py`脚本下载对应版本的custom文件,如果是IOS请手动修改`platform`为`ios`。

**如果选择这个方法下面的旧方法就不需要尝试了**

`ios`平台的资源似乎不完整，推荐使用下面的`ios`方法，如果下面的方法对您来说太过复杂再尝试这个方法。


## 原理

截止本仓库发布时，官方开关只剩一个和谐文件索引没有放出,正式服中的索引文件内容为`close`。本仓库通过重定向请求到本仓库的索引文件，从而能从正式服下载反和谐资源。

## 优势

使用官方一手资源，不会出现各种奇怪的问题，能反和谐最新的资源(只要官方有做)。
没有任何封号风险，至少在下次大更新前。

## 缺点

如果你不擅长使用搜索引擎，那么我也没法提供更多的帮助，这个仓库可能不是那么适合你。

## 依赖

1. [Virtual-Hosts](https://github.com/x-falcon/Virtual-Hosts)
2. python3
   1. mitmproxy

## Android使用方法

**注意，部分机型和模拟器可能无法正确的安装证书，如果遇到这种情况请使用上面的替换文件方法**

**有任何问题先检查本地仓库有没有更新到最新版本，再使用搜索引擎排查，最后提issue**

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

## iOS + Surge 使用方法

理论上其他支持 MitM 和 Rewrite 的*网络调试工具*，例如 Shadowrocet 也可以用同样的方法。可以根据原理自行探索操作方法。

以下设置为一次性操作，只要游戏新版本不会覆盖 `internation.txt` 文件就无需在版本更新后重新进行。

1. 在电脑上安装 iMazing（macOS 和 Windows 都支持），使用 iMazing 备份交错战线的数据，找到其中的 `Container/Documents/internation.txt`，将其中的~~那个零~~ 0 修改为 1。这部分详细操作请自行参考 iMazing 官方文档，**务必注意最后在 iOS 上的操作，确保选择“保留部分设置并继续”，并且“不传输任何内容”（不从 iCloud 恢复数据），以免 iOS 设备数据被重置**。
2. 在 iOS 设备上安装 Surge，打开 MitM 和 Rewrite 功能。在 MitM 的配置界面里生成新证书，按提示操作安装和信任证书。
3. 在 Surge 的 MitM 界面主机名里增加 `cdn.megagamelog.com`。
4. 在 Surge 的 Rewrite 界面重定向里增加一条 HTTP 302 模式规则，正则表达式为 `^https://cdn.megagamelog.com/cross/release/ilist.txt$`，替代文本为 `https://raw.githubusercontent.com/AXiX-official/CrossCore-Internationalizer/main/ilist.txt`
5. 强行关闭并重启游戏即可自动更新国际服资源。

## 最后

如果有任何问题，欢迎提[issue](https://github.com/AXiX-official/CrossCore-Internationalizer/issues)。

如果你有更好的方法，欢迎提[PR](https://github.com/AXiX-official/CrossCore-Internationalizer/pulls)。
