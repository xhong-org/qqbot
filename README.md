##读我 (README.md)##
-此BOT源码已在Github开源
-需OneBot 11协议

https://github.com/xhong-org/qqbot

目前仍然开发中
Updated 2025.10.21(Beta)

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

Latest(Beta): 最新但是测试分支
保留了Main以下指令

Tips: "->"表示更改的指令名,作用不变
<rewrite>
- /bot-sign
- /bot-test
- /bot-status
- /bot-say
- /bot-info
- /mc-ping -> /mc-ping
</rewrite>

<begin>
- 我要亿张神秘小图片 ["-R18-"<bool>] ["-AI-"<bool>] #随机获取P站作品.bool是布尔值,布尔值是什么网上搜,true为是,false为否,值得一提是,即使否定R18或AI仍然会有R18或AI成分.默认只发送"我要亿张神秘小图片"的话,否定R18和AI标签的.
- 摸头 [at] #生成摸头像表情包,默认不填生成发送者的头像
- 赞我 #给你点10个赞,记得回赞哦
</begin>