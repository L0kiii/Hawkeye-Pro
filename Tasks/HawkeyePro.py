"""
@usage: 任务名为markdown对应的标题/ip需修改为自己的
@author: L0ki
@blog: https://l0ki.top
"""
import requests
import json
import random

burp_url = 'http://ip:port/api/setting/query'
burp_header = {
    'Host': 'ip:port',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.28 Safari/537.36 OPR/61.0.3298.6 (Edition developer)',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json;charset=utf-8'
}

namesDict = {}
with open(file="urls.txt", mode="r", encoding="utf-8") as f:
    n=0
    for line in f.readlines():
        n=n+1
        line = line.strip()
        if line.startswith("###"):
            value = line[4:]
        else:
            namesDict[line] = value + str(n)

"""
随机命名
with open(file="urls.txt", mode="r", encoding="utf-8") as f:
    for line in f.readlines():
        line = line.strip()
        if line.startswith("###"):
            value = line[4:] + str(random.randint(0, 200))
        else:
            namesDict[line] = value + str(random.randint(0, 9))

"""


def getName(domain):
    if domain.startswith("###"):
        return None
    return namesDict[domain]


def send_data():
    with open(file="urls.txt", mode="r", encoding="utf-8") as f:
        domains = f.readlines()

        for do in domains:
            domain = do.strip("\n")
            if getName(domain) is None:
                continue
            data = {"tag": getName(domain), "keyword": domain, "enabled": "False"}
            burp_data = json.dumps(data)
            try:
                response = requests.post(url=burp_url, headers=burp_header, data=burp_data)
                # 打印请求状态
                if response:
                    print(burp_data)
                    print("[+]Add Task Success!")
                response.close()
            except EOFError:
                print("[*]time out!")


if __name__ == '__main__':
    print(
        """    
████████╗ █████╗ ███████╗██╗  ██╗███████╗
╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝██╔════╝
   ██║   ███████║███████╗█████╔╝ ███████╗
   ██║   ██╔══██║╚════██║██╔═██╗ ╚════██║
   ██║   ██║  ██║███████║██║  ██╗███████║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
@author: L0ki
@blog: https://l0ki.top                                                                          
        """
    )
    send_data()
