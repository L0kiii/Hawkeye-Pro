"""
@usage: 在username.txt和password.txt中添加对应的账户
@author: L0ki
@blog: https://l0ki.top
"""
import requests
import json

burp_url = 'http://ip:8002/api/setting/github'
burp_header = {
    'Host': 'ip:8002',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.28 Safari/537.36 OPR/61.0.3298.6 (Edition developer)',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json;charset=utf-8'
}


def sent_data():
    userName = []
    passWord = []
    with open(file="username.txt", mode="r", encoding="utf-8") as f:
        usernames = f.readlines()
        for ur in usernames:
            username = ur.strip("\n")
            userName.append(username)
    with open(file="password.txt", mode="r", encoding="utf-8") as p:
        passwords = p.readlines()
        for pa in passwords:
            password = pa.strip("\n")
            passWord.append(password)
    for i in range(0, len(userName)):
        u = userName[i]
        p = passWord[i]
        data = {"username": u, "password": p}
        burp_data = json.dumps(data)

        try:
            response = requests.post(url=burp_url, headers=burp_header, data=burp_data)
            if response:
                print(burp_data)
                print("[+]Add Token Success!")
            response.close()
        except EOFError:
            print("[*]Time Out!")


if __name__ == '__main__':
    print(
        """
        
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗███████╗
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║██╔════╝
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║███████╗
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║╚════██║
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║███████║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝
@author: L0ki
@blog: https://l0ki.top   
        """
    )
    sent_data()
