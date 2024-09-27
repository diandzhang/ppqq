import os
import re
import time
import requests
import random
file_path="adguard_rules.txt"
lines = set()
fruit_list = [
'http://47.103.223.194/jlp?m=',
'http://139.224.2.227:38880/jlp?m=',
'http://47.102.192.248:38880/jlp?m=',
'http://47.102.201.163:38880/jlp?m=',
'http://47.103.12.187:38880/jlp?m=',
'http://47.103.64.143:38880/jlp?m=',
'http://139.196.11.180:38880/jlp?m=',
'http://47.101.65.122:38880/jlp?m=',
'http://47.102.216.197:38880/jlp?m=',
'http://47.101.185.223:38880/jlp?m=',
'http://47.102.101.220:38880/jlp?m=',
'http://git.1fmall.cn:38880/jlp?m=',
'http://47.102.114.25:38880/jlp?m=',
'http://47.103.158.47:18089/jlp?m=',
'http://47.243.245.27:18089/jlp?m=',
'http://47.101.133.213/jlp?m=',
'http://106.15.181.208/jlp?m=',
'http://47.100.194.171/jlp?m=',
'http://139.196.236.218/jlp?m=',
'http://101.132.113.35/jlp?m=',
'http://101.132.223.12/jlp?m=',
'http://47.101.186.10/jlp?m=',
'http://47.123.7.103/jlp?m=',
'http://update-test.youshui.ren:38880/jlp?m=',
'https://139.196.202.168:28888/jlp?m=',
'http://47.100.52.43/jlp?m=',
'http://47.103.66.25/jlp?m=',
'http://101.132.61.123/jlp?m=',
'http://101.132.81.231/jlp?m=',
'http://101.132.61.22/jlp?m=',
'http://101.132.83.74/jlp?m=',
'http://139.196.146.238:38880/jlp?m=',
'http://47.100.31.221:38880/jlp?m=',
'http://139.196.159.43:38880/jlp?m=',
'http://106.14.2.180:38880/jlp?m=',
'http://47.102.124.25:38880/jlp?m=',
'http://47.102.114.145:38880/jlp?m=',
'http://47.103.214.197:38880/jlp?m='
  ]

def getraw(url):
    html = ""
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    try:
        resp = requests.get(url, headers=header, timeout=15)
        html = resp.text
    except Exception as e:
        print(url, e)
    #    print("end getraw",url)
    return html

def geturl(msg):
    msgs=msg.split(";")
    for line in msgs:
        if "0.html" in line :
            urls=line.split("'")
            for url in urls:
               if "http"  in url:
                    protocodl =re.findall(r'(?<=://)[^/]+', url)
                    for linez in protocodl: 
                      lines.add("||" +linez + "^")

with open("e.xml", 'w') as file:
    for item in fruit_list:
        item=item+str(random.randint(1000, 10000))
        print(item)
        file.write(item +":\n")
        file.write(getraw(item))
        time.sleep(1)


if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            lines.add(line.strip())

with open("e.xml", encoding='utf-8') as markup_file:
    for line in markup_file:
        geturl(line)
        
with open(file_path, 'w') as file:
    file.write('\n'.join(sorted(lines)))

# https://mirror.ghproxy.com/https://raw.githubusercontent.com/diandzhang/ppqq/main/adguard_rules.txt
# https://raw.githubusercontent.com/diandzhang/ppqq/main/adguard_rules.txt
# https://cdn.jsdelivr.net/gh/diandzhang/ppqq@main/adguard_rules.txt
