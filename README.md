##读我 (README.md)##
-此BOT源码已在Github开源
-需OneBot 11协议

开源地址:
https://github.com/xhong-org/qqbot

目前仍然开发中
QQ群:958732188

Github Updated 2025.10.25(Beta)
Local Updated 2025.10.25(Beta)

Tips:  本Bot不需要at机器人在输入指令,同时为了误触发,部分指令开头都加入了反斜杠"/"
还有"<text>"和"</text>"是表示开始和结束,没啥用处,我瞎几把写的
还有指令带参数的由"<arg>"或"[arg]"表示,分别为必选参数和可选参数.必选参数,字面意思,必须填入参数才能运行.可选参数,字面意思,可填可不填
如果你看到了一些指令的参数帮助为" ["text"[arg1]] " 这样的
可以理解为:这是一个可选参数,有需要填的话,你必须把可选参数里双引号括住的text写出来,然后你再考虑子可选参数要不要填
示例指令:
/xxx ["text"[arg1]]
/xxx ["ttt"<arg>]
/xxx <"emmm"[arg2]>
示例用法:
/xxx text114514abcd 或 /xxx text或 /xxx
/xxx ttt114514abcd 或 /xxx
/xxx emmm 或 /xxx emmm114514ahcd


##指令帮助##

Legacy(Main): 旧分支,但是主分支
<start>
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
- /info <address> #查询MCServer服务器信息和延迟(Tips: 部分SRV解析的域名可能无法获取或检测延迟)
- /2fa-bind <key> #绑定2FA秘钥,上限10个,当然你可以改
- /2fa-info #查看当前已经绑定的2FA秘钥,留意ID,这个是用来操作解绑秘钥和发送一次性验证码的参数
- /2fa-unbind <id> #解绑2FA秘钥,id是什么看看上面
- /2fa-getcode <id> #获取一次性验证码,有效时间为30秒,id是什么看看上面
</start>

Latest(Beta): 最新但是测试分支
保留了Main以下指令

Tips: "->"表示更改的指令名,作用不变
<rewrite>
- /bot-sign
- /bot-test
- /bot-status
- /bot-say
- /bot-info & 个人信息
- /info -> /mc-info
</rewrite>

<begin>
- 我要亿张神秘小图片 ["-R18-"<bool>] ["-AI-"<bool>] #随机获取P站作品.bool是布尔值,布尔值是什么网上搜,true为是,false为否,值得一提是,即使否定R18或AI仍然会有R18或AI成分.默认只发送"我要亿张神秘小图片"的话,否定R18和AI标签的.
- 摸头 [at] #生成摸头像表情包,默认不填生成发送者的头像
- 赞我 #给你点10个赞,记得回赞哦
- 个人信息 #字面意思
</begin>