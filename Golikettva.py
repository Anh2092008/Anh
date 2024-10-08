
#

import requests,os,time
from time import sleep

den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
n ="\033[1;3m\033[1;38m"
e ="\033[0m"
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
\033[1;97m[\033[1;91m⑉⁠\033[1;97m]\033[1;97m Tool\033[1;33m     : \033[1;97m \033[1;31mGolike-Tiktok\033[1;33m \033[1;97m
\033[1;97m[\033[1;91m⑉⁠\033[1;97m]\033[1;97m Youtube\033[1;33m  : \033[1;97m \033[1;36m\033[1;31m \033[1;97m
\033[1;97m[\033[1;91m⑉⁠\033[1;97m]\033[1;97m Tik Tok\033[1;33m  : \033[1;33m\033[1;32m\033[1;31m
\033[1;97m[\033[1;91m⑉⁠\033[1;97m]\033[1;97m Zalo\033[1;33m     : 
\033[1;97m[\033[1;91m⑉⁠\033[1;97m]\033[1;97m Telegram\033[1;33m : 
\033[97m════════════════════════════════════════════════
\n\n"""

os.system("clear")
for x in banner:
  print(x,end = "")
  sleep(0.001)
try:
  Authorization = open("Authorization.txt","x")
  t = open("token.txt","x")
except:
  pass
Authorization = open("Authorization.txt","r")
t = open("token.txt","r")
author = Authorization.read()
token = t.read()
if author == "":
  author = input("\033[1;31mNHẬP \033[1;33mAUTHORIZATION : \033[1;36m")
  token = input("\033[1;31mNHẬP \033[1;33mT :\033[1;36m ")
  Authorization = open("Authorization.txt","w")
  t = open("token.txt","w")
  Authorization.write(author)
  t.write(token)
else:
  select = input("\033[1;97m║ ĐĂNG\033[1;96m NHẬP \033[1;95mTÀI \033[1;94mKHOẢN \033[1;93m \033[1;92m\033[1;91m ( ENTER ĐỂ BỎ QUA ,NHẬP AUTHORIZATION TẠI ĐÂY \033[1;97m\n║                              \033[1;91m           ĐỂ ĐỔI )  \n\033[1;97m╚⟩⟩⟩\033[1;93m ")
  os.system("clear")
for x in banner:
  print(x,end = "")
  sleep(0.001)

  if select != "":
    author = select
    token = input("\033[1;36mNhập \033[1;33mT :\033[1;36m ")
    Authorization = open("Authorization.txt","w")
    t = open("token.txt","w")
    Authorization.write(author)
    t.write(token)
Authorization.close()
t.close()
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/tiktok',
}


def chonacc():
  json_data = {}

  response = requests.get('https://gateway.golike.net/api/tiktok-account', headers=headers, json=json_data).json()
  return response
def nhannv(account_id):

  params = {
    'account_id': account_id,
    'data': 'null',
  }

  json_data = {}

  response = requests.get('https://gateway.golike.net/api/advertising/publishers/tiktok/jobs',params=params,headers=headers,json=json_data,).json()
  return response
def hoanthanh(ads_id,account_id):
  json_data = {
    'ads_id': ads_id,
    'account_id': account_id,
    'async': True,
    'data': None,
  }

  response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
    headers=headers,
    json=json_data,
  ).json()
  return response
def baoloi(ads_id,object_id,account_id,loai):
  json_data1 = {
    'description': 'Tôi đã làm Job này rồi',
    'users_advertising_id': ads_id,
    'type': 'ads',
    'provider': 'tiktok',
    'fb_id': account_id,
    'error_type': 6,
  }

  response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1).json()

  json_data = {
    'ads_id': ads_id,
    'object_id': object_id,
    'account_id': account_id,
    'type': loai,
  }

  response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
    headers=headers,
    json=json_data,
  ).json()  
chontktiktok = chonacc()  
def dsacc():
  if(chontktiktok["status"]!=200):
    print("{n}\033[1;37mAuthorization \033[1;36mhoặc \033[1;35mT \033[1;34msai \033[1;33mhãy \033[1;32mnhập \033[1;31mlại\033[1;30m!\033[1;37m!\033[1;36m!{e}")
    quit()
    os.system("clear")

  for i in range(len(chontktiktok["data"])):
    print(f'\033[1;93m╠⁠\033[1;36m[{i+1}] \033[1;35m➩ \033[1;97mTên Tài Khoản┊\033[1;32m :\033[1;93m {chontktiktok["data"][i]["nickname"]}  ')
   
dsacc() 
while True:
  try:
    luachon = int(input(f"\033[1;35m\033[1;93m║{n}\033[1;97m CHỌN \033[1;96mTÀI \033[1;95mKHOẢN \033[1;94mĐỂ \033[1;93mCHẠY {e}\n\033[1;93m╠⁠\033[1;96m⟩\033[1;95m⟩\033[1;94m⟩ "))
    while luachon > len((chontktiktok)["data"]):
      luachon = int(input("\033[1;37mACC \033[1;36mNÀY \033[1;35mKHÔNG \033[1;34mCÓ \033[1;33mTRONG \033[1;32mDANH \033[1;31mSÁCH\033[1;30m, \033[1;37mHÃY \033[1;36mNHẬP \033[1;35mLẠI\033[1;3rm :\033[1;33m "))
    account_id = chontktiktok["data"][luachon - 1]["id"]
    break  
  except:
    print("\033[1;93m╠⁠\033[1;37m SAI \033[1;36mĐỊNH \033[1;35mDẠNG !!!") 
while True:
  try:
    delay = int(input(f"\033[1;93m║ {n}\033[1;35mNHẬP\033[1;91m DELAY{e} \n\033[1;93m╠⁠\033[1;96m⟩\033[1;95m⟩\033[1;94m⟩ "))
    break
  except:
    print("\033[1;93m╠⁠\033[1;37m SAI \033[1;36mĐỊNH \033[1;35mDẠNG !!!")
while True:
  try: 
    doiacc = int(input(f"\033[1;93m║ {n}\033[1;99mNHẬN\033[1;91m TIỀN\033[1;96m THẤT\033[1;95m BẠI\033[1;94m BAO\033[1;93m NHIU\033[1;92m LẦN\033[1;91m THÌ\033[1;96m DỪNG\033[1;93m{e} \n\033[1;93m╚\033[1;96m⟩\033[1;95m⟩\033[1;94m⟩ "))
    break
  except:
    print(f"{n}\033[1;37mNHẬP \033[1;36mVÀO \033[1;35m1 \033[1;34mSỐ \033[1;33m!\033[1;32m!\033[1;31m!{e}")    
os.system("clear")
dem = 0
tong = 0
checkdoiacc = 0
dsaccloi = []
accloi = ""

            
os.system("clear")

for x in banner:
  print(x,end = "")
  sleep(0.001)
while True:
  if checkdoiacc == doiacc:
    dsaccloi.append(chontktiktok["data"][luachon - 1]["nickname"])
    print(f"\033[1;37mCÁC \033[1;36mACC \033[1;35mTIKTOK \033[1;34m{dsaccloi} \033[1;33mCÓ \033[1;32mVẺ \033[1;31mGẶP \033[1;30mVẤN \033[1;37mĐỀ \033[1;36mNÊN \033[1;35mĐỔI\033[1;34m ACC \033[1;33mCHẠY \033[1;32mĐÊ ")
    dsacc()
    while True:
      try:
        luachon = int(input(f"\033[1;35m\033[1;93m║ {n}\033[1;97mCHỌN \033[1;96mTÀI \033[1;95mKHOẢN \033[1;94mĐỂ \033[1;93mCHẠY{e} \n\033[1;93m╚\033[1;96m⟩\033[1;95m⟩\033[1;94m⟩  "))
        while luachon > len((chontktiktok)["data"]):
          luachon = int(input(f"{n}\033[1;37mACC \033[1;36mNÀY \033[1;35mKHÔNG \033[1;34mCÓ \033[1;33mTRONG \033[1;32mDANH \033[1;31mSÁCH, \033[1;30mHÃY \033[1;37mNHẬP \033[1;36mLẠI\033[1;35m{e} : \033[1;36m"))
        account_id = chontktiktok["data"][luachon - 1]["id"]
        checkdoiacc = 0
        break  
      except:
        print(f"{n}\033[1;37mSAI \033[1;36mĐỊNH \033[1;35mDẠNG \033[1;34m!\033[1;33m!\033[1;32m!{e}")
        os.system("clear")

     
  print(f'{n}\033[1;97mĐANG \033[1;96mLẤY \033[1;95mNHIỆM \033[1;94mVỤ\033[1;93m FOLLOW{e}',end="\r")    
  while True:
    try:  
      nhanjob = nhannv(account_id)
      break
    except:
      pass
  if(nhanjob["status"] == 200):
    ads_id = nhanjob["data"]["id"]
    link = nhanjob["data"]["link"]
    object_id = nhanjob["data"]["object_id"]
    if(nhanjob["data"]["type"] != "follow"):
      baoloi(ads_id,object_id,account_id,nhanjob["data"]["type"])
      continue
    os.system(f"termux-open-url {link}")
    for i in range(delay,-1,-1):
      print('                                             ',end = '\r')
      for j in [".","..","..."]:
    	
                        print(f"{n}\r\033[1;37mn\033[1;36mv\033[1;35ma\033[1;32m\033[1;31mc\033[1;34mu\033[1;33mt\033[1;36mo\033[1;37m\033[1;36m\033[1;31m\033[1;32m\033[1;37m\033[1;35m {e}\033[1;37m╏⁠\033[1;31m{i}\033[1;37m╏⁠ ", end='')
                        sleep(0.1)
                        print(f"{n}\r\033[1;34mN\033[1;31mv\033[1;37ma\033[1;36m\033[1;32mc\033[1;35mu\033[1;37mt\033[1;33mo\033[1;34m\033[1;32m\033[1;32m\033[1;33m\033[1;36m\033[1;35m \033[1;37m╏\033[1;31m⁠{i}\033[1;37m╏⁠{e} ", end='')
                        sleep(0.1)
                        print(f"{n}\r\033[1;31mN\033[1;37mV\033[1;36ma\033[1;33m\033[1;35mc\033[1;32mu\033[1;34mt\033[1;35mo\033[1;31m\033[1;37m\033[1;33m\033[1;34m\033[1;35m\033[1;34m {e}\033[1;37m╏\033[1;31m⁠{i}\033[1;37m╏⁠ ", end='')
                        sleep(0.1)
                        print(f"{n}\r\033[1;32mN\033[1;33mV\033[1;34mA\033[1;35m\033[1;36mc\033[1;37mu\033[1;36mt\033[1;31mo\033[1;33m\033[1;34m\033[1;34m\033[1;35m\033[1;34m\033[1;97m \033[1;37m╏\033[1;31m⁠{i}\033[1;37m╏⁠{e} ", end='')
                        sleep(0.1)
                        print(f"{n}\r\033[1;37mN\033[1;34mV\033[1;35mA\033[1;36m\033[1;32mC\033[1;33mu\033[1;31mt\033[1;37mo\033[1;35m\033[1;34m\033[1;35m\033[1;36m\033[1;33m\033[1;32m {e}\033[1;37m╏\033[1;31m⁠{i}\033[1;37m╏⁠ ", end='')
                        sleep(0.1)
                        print(f"{n}\r\033[1;37mN\033[1;34mV\033[1;35mA\033[1;36m\033[1;32mC\033[1;33mU\033[1;31mt\033[1;37mo\033[1;35m\033[1;34m\033[1;35m\033[1;36m\033[1;33m\033[1;33m \033[1;37m╏⁠\033[1;31m{i}\033[1;37m╏⁠{e} ", end='')
                        sleep(0.1)
                        print(f"{n}\r\033[1;37mN\033[1;34mV\033[1;35mA\033[1;36m\033[1;32mC\033[1;33mU\033[1;31mT\033[1;37mo\033[1;35m\033[1;34m\033[1;35m\033[1;36m\033[1;33m\033[1;36m {e}\033[1;37m╏\033[1;31m⁠{i}\033[1;37m╏⁠ ", end='')
                        sleep(0.1)
                        print(f"{n}\r\033[1;37mN\033[1;36mV\033[1;35mA\033[1;33m\033[1;31mC\033[1;33mU\033[1;37mT\033[1;35mO\033[1;35m\033[1;34m\033[1;35m\033[1;36m\033[1;33m\033[1;36m \033[1;37m╏⁠\033[1;31m{i}\033[1;37m╏⁠{e} ", end='')
                        sleep(0.1)
                        
                        
    print("                                                ",end = "\r")    
    print(f"{n}\033[1;36mĐANG \033[1;35mNHẬN \033[1;34mTIỀN{e}         ",end = "\r")
    while True:    
      try:    
        nhantien = hoanthanh(ads_id,account_id)
        break
      except:
        pass
    if(nhantien["status"] == 200):
      dem += 1
      tien = nhantien["data"]["prices"]
      tong += tien
      local_time = time.localtime()
      hour = local_time.tm_hour
      minute = local_time.tm_min
      second = local_time.tm_sec
      h = hour
      m = minute
      s = second
      if(hour < 10):
        h = "0"+str(hour)
      if(minute < 10):
        m = "0"+str(minute)
      if(second < 10):
        s = "0"+str(second)
      chuoi = f"\033[1;36m{dem}\033[1;35m | \033[1;33m{h}:{m}:{s}\033[1;31m\033[1;35m | \033[1;31m{nhantien['data']['type']}\033[1;35m |\033[1;97m \033[1;33m+{tien} \033[1;35m| \033[1;32m{tong} vnđ"  
      print("                                                    ",end = "\r")
      
      print(chuoi)
    
      checkdoiacc = 0  
    else:
     
      while True:
        try:  
          baoloi(ads_id,object_id,account_id,nhanjob["data"]["type"])
          print("                                              ",end = "\r")
          print("\033[1;37mBỎ \033[1;36mQUA \033[1;35mNHIỆM \033[1;34mVỤ ",end = "\r")
          sleep(1)
          checkdoiacc+=1
          break
        except:
          qua = 0
          pass
