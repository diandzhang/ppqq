import os
import re
file_path="adguard_rules.txt"
def geturl(msg):
    msgs=msg.split("'")
    for line in msgs:
        if "0.html" in line :
            # print(line)
            protocodl =re.findall(r'(?<=://)[^/]+', line)
            for linez in protocodl: 
               return linez
lines = set()
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            lines.add(line.strip())

with open("e.xml", encoding='utf-8') as markup_file:
    for line in markup_file:
        lines.add("||" +geturl(line) + "^")

with open(file_path, 'w') as file:
    file.write('\n'.join(lines))



      
