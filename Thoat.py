import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
banner = """\033[1;3m\033[1;38m   
               \033[1;31m███╗   ██╗██╗   ██╗ █████╗ 
               ████╗  ██║██║   ██║██╔══██╗
               ██╔██╗ ██║██║   ██║███████║
               \033[1;37m██║╚██╗██║╚██╗ ██╔╝██╔══██║
               ██║ ╚████║ ╚████╔╝ ██║  ██║
               ╚═╝  ╚═══╝  ╚═══╝  ╚═╝  ╚═╝                                  
\033[0m\n
\033[1;97mTool : \033[1;32m Thầy Ông nội               
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m⑉⁠\033[1;97m]\033[1;97m Tool\033[1;31m     : \033[1;97m \033[1;31mThoat Tool\033[1;33m \033[1;97m
\033[1;97m[\033[1;91m⑉⁠\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m \033[1;36m\033[1;31m \033[1;97m
\033[1;97m[\033[1;91m⑉⁠\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33m\033[1;32m\033[1;31m
\033[1;97m[\033[1;91m⑉⁠\033[1;97m]\033[1;97m Zalo\033[1;31m     : 
\033[1;97m[\033[1;91m⑉⁠\033[1;97m]\033[1;97m Telegram\033[1;31m : 
\033[97m════════════════════════════════════════════════
\n"""
os.system("cls" if os.name == "nt" else "clear")

for x in banner:
  print(x,end = "")
  sleep(0.001)
print(f"\033[1;3m\033[1;38m\033[1;37m╔═════════════════════════════════════════════════╗")
print(f"\033[1;37m║   \033[1;97m[\033[1;91m⑉⁠\033[1;97m] \033[1;36m✈  \033[1;37mCảm \033[1;36mƠn \033[1;35mBạn \033[1;34mĐã \033[1;33mThoát \033[1;32mTool \033[1;31mNhé\033[1;30m.\033[1;37m.\033[1;36m.\033[1;35m.\033[1;31m!      \033[1;37m║")
print(f"\033[1;37m╚═════════════════════════════════════════════════╝\033[0m\n\n")
