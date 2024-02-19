import os
import re
file_path="adguard_rules.txt"
lines = set()
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
