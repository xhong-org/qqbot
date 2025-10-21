##读我 (README.md)##
-此BOT源码已在Github开源
https://github.com/xhong-org/qqbot
目前仍然开发中
Updated 2025.10.21(Beta)

##指令帮助##
Legacy(Main): 旧分支,现在依然当做主分支来用
- /bot-sign #签到,可获取硬币,但是在Legacy分支毫无作用,你可以自主开发
- /bot-info #查看个人信息.获取当前硬币数以及其他信息,但是不包括QQ个人信息(因为我忘了写
- /bot-say <text> #可以让bot发送消息,但是并没有屏蔽违禁词,简单来说,text有什么就发什么
- /bot-help #用于查看指令用法
- /bot-op <qq_num | at> #授予某人bot管理权限,可以输入QQ号或者在群里at某人授予
- /bot-deop <qq_num | at> #撤销某人bot权限,同上
- /bot-status #查看主机状态
- /bot-test #测试用的
- /bot-reload #重新读取档案文件
- /bot-save #保存配置文件
- /bot-update #重启bot用的
- /mc-cmd <command> #通过Rcon向发送MCServer命令
- /tps #查看$mc_address变量的地址的Minecraft服务器当前tps,仅适合用于Forge端服务器
- /list #查看$mc_address变量的地址的Minecraft服务器当前人数
- /s <message> #查看$mc_address变量的地址的Minecraft服务器发送游戏消息
- /2fa-bind <key> #绑定2FA秘钥,上限10个,当然你可以改
- /2fa-info #查看当前已经绑定的2FA秘钥,留意ID,这个是用来操作解绑秘钥和发送一次性验证码的参数
- /2fa-unbind <id> #解绑2FA秘钥,id是什么看看上面
- /2fa-getcode <id> #获取一次性验证码,有效时间为30秒,id是什么看看上面
