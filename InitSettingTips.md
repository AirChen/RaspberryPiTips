###烧制系统
准备好树莓派用的系统，和系统的烧卡工具。这些在[官网](https://www.raspberrypi.org/)上都可以找得到。
准备一张16G大小的TF卡和读卡器，接入电脑，我们就可以开始烧制树莓派的系统了。

系统烧制好后，还需处理两件事情：

    1.默认的系统存储空间很小，我们需要将其扩大一些，推荐在一台安装了GParted软件的Ubuntu电脑上进行调整。
    2.如果本地路由使用的静态IP，需要给树莓派设置一个IP，这时需要对烧好系统的TF卡中的cmdline文件进行修改。（加入一个键值对ip=172.16.xxxx即可）

完成上面这些步骤之后，就可以将准备好的TF卡插入树莓派开发板的卡槽，接入电源，启动树莓派了。

将树莓派接入局域网（网线接入），可以用ssh登录工具进行登录，用户名和密码默认为：pi raspberry
运行vncserver可以启动vnc远程桌面，使用vnc客户端可以登录，用户名和密码同上，支持文件传输。

###更新源
    sudo vi  /etc/apt/sources.list 
将之前的源注释掉，添加下面的源

    deb http://mirrordirector.raspbian.org/raspbian/ jessie main contrib non-free rpi
    deb http://archive.raspbian.org/raspbian jessie main contrib non-free rpi
保存后，执行 

    sudo apt-get install update 
    sudo apt-get install upgrade(更新软件)
参考：http://www.shumeipaiba.com/wanpai/jiaocheng/16.html

###配置网卡
当前树莓派具备网线，和无线网络这两个部分的网卡，所以在打算使用无线网接入wlan的时候，需要对网络的配置文件进行一下配置。

    sudo vi /etc/network/interfaces
写入

    allow-hotplug wlan0
    auto wlan0
    iface wlan0 inet dhcp  
    pre-up wpa_supplicant -B w -D wext -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf 
    post-down killall -q wpa_supplicant
用vnc登录远程桌面，在界面上设置一下接入的无线网络即可。
参考：http://www.cnblogs.com/imapla/p/5532993.html

###其它
[安装opencv](https://pypi.python.org/pypi/opencv-python)

[opencv调用原装摄像头](http://blog.csdn.net/leeyunj/article/details/53482265)

[树莓派串口](http://blog.csdn.net/yangqicong11/article/details/26571787)

[max7219库](https://max7219.readthedocs.io/en/latest/)
