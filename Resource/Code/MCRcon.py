import mcrcon
def mc_send_cmd(cmd):
    host = "cn-qz-plc-1.ofalias.net"  # 地址
    port = 53467  # 端口
    password = "2118181145141414"  # 密码
    
    try:
        # 连接到RCON
        with mcrcon.MCRcon(host, password, port) as mcr:
            # 指令
            print(f"已发送指令\n{cmd}")
            res = mcr.command(cmd)
            return(res)
    except ConnectionRefusedError as e:
        return(f"连接被拒绝\n错误信息：{e}")
    except TimeoutError:
        return("连接超时")
    except mcrcon.MCRconException as e:
        return(f"RCON连接错误:{e}")
    except Exception as e:
        return(f"发生未知错误:{e}")
