xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
tim = '\033[1;39m'
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb = "\033[1;37m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
cyan = "\033[1;36]"
xanhd = "\033[0;34]"
cam= "\x1b[38;5;208m"
import requests, random
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
import socket
from pystyle import Write,Colors           
try :
    import random
    import time
    from colorama import Fore, Style
    import requests
    import time
    import os 
    from art import *
    from colorama import Fore
    import time
    import json
    import random
    from time import sleep
    import sys
    from tabulate import tabulate
except ImportError:
    os.system("pip install requests")
    os.system("pip install tabulate")
    os.system("pip install art")
    os.system("pip install colorama")
def countdown(time_sec):
    for remaining_time in range(time_sec, -1, -1):
        colors = [
            f"?",
            f"¿",
            f"?",
            f"¿",
            f"?",
            f"¿",
        ]
        for color in colors:
            print(f"\r{color} {trang}{luc}{remaining_time} {trang}giây ", end="")
            time.sleep(0.15)      
    print("\r                                   \r", end="") 
    print(f"{xnhac}Đang Nhận Tiền                  ",end = "\r")
def LINKEDIN():
    checkaccount = requests.get('https://gateway.golike.net/api/linkedin-account', headers=headers).json()
    # Khởi tạo danh sách chứa tên tài khoản, ID, và trạng thái
    user_linkedin1 = []
    account_id1 = []
    STT = []
    STATUS = []
    tong = 0
    dem = 0
    i = 1

    # Duyệt qua từng tài khoản trong dữ liệu nhận được
    for data in checkaccount['data']:
        usernametk = data['name']
        user_linkedin1.append(data['name'])
        account_id1.append(data['id'])
        STT.append(i)
        STATUS.append(f"{luc}Hoạt Động" + Fore.RESET)
        # In ra thông tin tài khoản mà không cần hiển thị dạng bảng
        print(f'{buom}█ {i}{trang}=> {den}NAME: {vang}{usernametk} {xanhd}=> {STATUS[-1]} {buom}█')
        
        i += 1
        print(f'{zuo}=============================================')
    # Yêu cầu người dùng chọn tài khoản bằng cách nhập số thứ tự
    choose = int(input(f'{lap}Nhập Tài Khoản : {zuo1}'))
    
    if choose >=1 or choose <= len(user_linkedin1) :
        user_tiktok1 = user_linkedin1[choose-1:choose]
        account_id1 = account_id1[choose-1:choose]
        user_tiktok = user_linkedin1[0] 
        account_id = account_id1[0]
        checkfile = os.path.isfile('cookie_linkedin.txt')
        if checkfile == False:
            createfile = open('cookie_linkedin.txt','w')
            createfile.write(COOKIELINK)
            createfile.close()
            readfile = open('cookie_linkedin.txt','r')
            COOKIELINK = readfile.read()
            readfile.close()
        else:
            readfile = open('cookie_linkedin.txt','r')
            COOKIELINK = readfile.read()
            
            readfile.close()     
        print(f'{zuo}=============================================')
        choose = int(input('\033[1;33mNhập Số Lượng Job : \033[1;90m'))
        DELAY = int(input('\033[1;33mNhập Delay : \033[1;90m'))
        NVA = int(input('\033[1;33mNhập Delay Nghỉ Khi Hết Job \033[1;31m(\033[1;32mgiây\033[1;31m) \033[1;33m: \033[1;90m'))
        print(f'{zuo}=============================================')
        for i in range(choose):
                url2 = 'https://gateway.golike.net/api/advertising/publishers/linkedin/jobs?account_id='+str(account_id)+'&data=null'
                checkurl2 = ses.get(url2,headers=headers).json()
                if checkurl2['status'] ==200:
                    linkjob = []
                    linkjob = str(checkurl2['data']['link'])
                    lenjob = len(checkurl2['data']['link'])
                    ads_id = checkurl2['data']['id']
                    object_id = checkurl2['data']['object_id']
                    type = checkurl2['data']['type']
                    countdown(DELAY)
                    if type == 'follow':
                        haeaders = {
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                            'cache-control': 'max-age=0',
                            'cookie':COOKIELINK ,
                            'priority': 'u=0, i',
                            'referer': 'https://app.golike.net/',
                            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'document',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-site': 'same-origin',
                            'sec-fetch-user': '?1',
                            'upgrade-insecure-requests': '1',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                            }

                        response = requests.get(str(linkjob),  headers=haeaders).text
                        if 'li:fsd_company' not in response and 'identityDashProfilesByMemberIdentity&quot;:{&quot;*elements&quot;:[&quot;urn:li:fsd_profile:' not in response:
                                    json_data2 = {
                                    'account_id': account_id,
                                    'ads_id': ads_id,
                                     }
                                    url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                                    check = requests.post(url,headers=headers,json=json_data2).json()
                                    # Khởi tạo biến tổng tiền nếu chưa có
                                    if check['success'] == True:
                                        dem += 1
                                        local_time = time.localtime()
                                        hour = local_time.tm_hour
                                        minute = local_time.tm_min
                                        second = local_time.tm_sec

                                        # Định dạng giờ, phút, giây
                                        h = f"{hour:02d}"
                                        m = f"{minute:02d}"
                                        s = f"{second:02d}"
                                        prices = check['data']['prices']

                                        # Cộng dồn giá trị prices vào tổng tiền
                                        tong += prices

                                        chuoi = (
                                            f"{trang}[   {zuo}{dem}\033[1;31m\033[1;97m   ] "
                                            f"\033[1;33m {h}:{m}:{s}\033[1;31m\033[1;97m  "
                                            f"{trang}success\033[1;31m\033[1;97m  "
f"{red} Theo Dõi\033[1;31m\033[1;32m\033[1;32m\033[1;97m "                                                                         
                                            f"{tim}  Ẩn ID\033[1;97m \033[1;97m \033[1;32m+{prices} \033[1;97m "
                                            f"{cyan}{tong}"
                                            
                                        )
                                        print(chuoi) 
                                    
                                    else:
                                            skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                            PARAMS = {
                                            'ads_id' : ads_id,
                                            'account_id' : account_id,
                                            'object_id' : object_id ,
                                            }
                                            checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                            if checkskipjob['status'] == 200:
                                                message = checkskipjob['message']
                                                print(Fore.RED+str(message))
                                                PARAMSr = {
                                                'ads_id' : ads_id,
                                                'account_id' : account_id,
                                                'object_id' : object_id ,
                                                }
                        else:
                            json_data = {
                            'patch': {
                                '$set': {
                                    'following': True,
                                },
                            },
                            }
                            json_data2 = {
                                    'account_id': account_id,
                                    'ads_id': ads_id,
                                }
                            try:
                                crft =  COOKIELINK.split('JSESSIONID="')[1].split('"')[0],
                                try:
                                    headersX = {
                                    'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                    'content-type': 'application/json; charset=UTF-8',
                                    'cookie': COOKIELINK,
                                    'csrf-token': COOKIELINK.split('JSESSIONID="')[1].split('"')[0],
                                    'origin': 'https://www.linkedin.com',
                                    'priority': 'u=1, i',
                                    'referer': 'https://www.linkedin.com/company/chatplayground-ai/posts/?feedView=all',
                                    'sec-fetch-dest': 'empty',
                                    'sec-fetch-mode': 'cors',
                                    'sec-fetch-site': 'same-origin',
                                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                    'x-li-lang': 'en_US',
                                    'x-li-page-instance': 'urn:li:page:companies_company_posts_index;7952eddd-435c-428e-9587-a2dd19a42e2f',
                                    'x-li-pem-metadata': 'Voyager - Organization - Member=organization-follow',
                                    'x-li-track': '{"clientVersion":"1.13.19938","mpVersion":"1.13.19938","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                    'x-restli-protocol-version': '2.0.0',
                                    }

                                    ID = response.split('li:fsd_company:')[1].split('&')[0]
                                    follow = requests.post('https://www.linkedin.com/voyager/api/feed/dash/followingStates/urn:li:fsd_followingState:urn:li:fsd_company:'+ID,headers=headersX,json=json_data)
                                    url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                                    time.sleep(2)
                                    check = requests.post(url,headers=headers,json=json_data2).json()
                                    if check['success'] == True:
                                        dem += 1
                                        local_time = time.localtime()
                                        hour = local_time.tm_hour
                                        minute = local_time.tm_min
                                        second = local_time.tm_sec

                                        # Định dạng giờ, phút, giây
                                        h = f"{hour:02d}"
                                        m = f"{minute:02d}"
                                        s = f"{second:02d}"
                                        prices = check['data']['prices']

                                        # Cộng dồn giá trị prices vào tổng tiền
                                        tong += prices

                                        chuoi = (
                                            f"{trang}[   {zuo}{dem}\033[1;31m\033[1;97m   ] "
                                            f"\033[1;33m {h}:{m}:{s}\033[1;31m\033[1;97m  "
                                            f"{trang}success\033[1;31m\033[1;97m  "
f"{red} Theo Dõi\033[1;31m\033[1;32m\033[1;32m\033[1;97m "                                                                         
                                            f"{tim}  Ẩn ID\033[1;97m \033[1;97m \033[1;32m+{prices} \033[1;97m "
                                            f"{cyan}{tong}"
                                            
                                        )
                                        print(chuoi) 
                                    else:
                                            skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                            PARAMS = {
                                            'ads_id' : ads_id,
                                            'account_id' : account_id,
                                            'object_id' : object_id ,
                                            }
                                            checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                            if checkskipjob['status'] == 200:
                                                message = checkskipjob['message']
                                                print(Fore.RED+str(message))
                                                PARAMSr = {
                                                'ads_id' : ads_id,
                                                'account_id' : account_id,
                                                'object_id' : object_id ,
                                                }
                                except IndexError:
                                    headersY = {
                                    'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                    'content-type': 'application/json; charset=UTF-8',
                                    'cookie':COOKIELINK,
                                    'csrf-token': COOKIELINK.split('JSESSIONID="')[1].split('"')[0],
                                    'origin': 'https://www.linkedin.com',
                                    'priority': 'u=1, i',
                                    'referer': 'https://www.linkedin.com/in/noman-chaudhary-52031148/',
                                    'sec-fetch-dest': 'empty',
                                    'sec-fetch-mode': 'cors',
                                    'sec-fetch-site': 'same-origin',
                                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                    'x-li-lang': 'en_US',
                                    'x-li-page-instance': 'urn:li:page:d_flagship3_profile_view_base;I6RhpcMURWuRvBmeIhl5BQ==',
                                    'x-li-pem-metadata': 'Voyager - Follows=follow-action,Voyager - Profile Actions=topcard-primary-follow-action-click',
                                    'x-li-track': '{"clientVersion":"1.13.19938","mpVersion":"1.13.19938","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                    'x-restli-protocol-version': '2.0.0',
                                    }
                                    try:
                                        ID = response.split('identityDashProfilesByMemberIdentity&quot;:{&quot;*elements&quot;:[&quot;urn:li:fsd_profile:')[1].split('&')[0]
                                        follow =  requests.post('https://www.linkedin.com/voyager/api/feed/dash/followingStates/urn:li:fsd_followingState:urn:li:fsd_profile:'+ID,headers=headersY,json=json_data) 
                                        time.sleep(2)
                                        url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                                        check = requests.post(url,headers=headers,json=json_data2).json()
                                        if check['success'] == True:
                                            dem += 1
                                            local_time = time.localtime()
                                            hour = local_time.tm_hour
                                            minute = local_time.tm_min
                                            second = local_time.tm_sec

                                            # Định dạng giờ, phút, giây
                                            h = f"{hour:02d}"
                                            m = f"{minute:02d}"
                                            s = f"{second:02d}"
                                            prices = check['data']['prices']

                                            # Cộng dồn giá trị prices vào tổng tiền
                                            tong += prices

                                            chuoi = (
                                            f"{trang}[   {zuo}{dem}\033[1;31m\033[1;97m   ] "
                                            f"\033[1;33m {h}:{m}:{s}\033[1;31m\033[1;97m  "
                                            f"{trang}success\033[1;31m\033[1;97m  "
f"{red} Theo Dõi\033[1;31m\033[1;32m\033[1;32m\033[1;97m "                                                                         
                                            f"{tim}  Ẩn ID\033[1;97m \033[1;97m \033[1;32m+{prices} \033[1;97m "
                                            f"{cyan}{tong}"
                                            
                                        )
                                            print(chuoi) 
                                        else:
                                                skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                                PARAMS = {
                                                'ads_id' : ads_id,
                                                'account_id' : account_id,
                                                'object_id' : object_id ,
                                                }
                                                checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                                if checkskipjob['status'] == 200:
                                                    message = checkskipjob['message']
                                                    print(Fore.RED+str(message))
                                                    PARAMSr = {
                                                    'ads_id' : ads_id,
                                                    'account_id' : account_id,
                                                    'object_id' : object_id ,
                                                    }
                                    except IndexError:
                                        print('COOKIE DIE')
                                        os.remove('cookie_linkedin.txt')
                                        return 0
                            except IndexError:
                                try:
                                    headersX = {
                                    'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                    'content-type': 'application/json; charset=UTF-8',
                                    'cookie': COOKIELINK,
                                    'csrf-token': COOKIELINK.split('JSESSIONID=')[1].split(';')[0],
                                    'origin': 'https://www.linkedin.com',
                                    'priority': 'u=1, i',
                                    'referer': 'https://www.linkedin.com/company/chatplayground-ai/posts/?feedView=all',
                                    'sec-fetch-dest': 'empty',
                                    'sec-fetch-mode': 'cors',
                                    'sec-fetch-site': 'same-origin',
                                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                    'x-li-lang': 'en_US',
                                    'x-li-page-instance': 'urn:li:page:companies_company_posts_index;7952eddd-435c-428e-9587-a2dd19a42e2f',
                                    'x-li-pem-metadata': 'Voyager - Organization - Member=organization-follow',
                                    'x-li-track': '{"clientVersion":"1.13.19938","mpVersion":"1.13.19938","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                    'x-restli-protocol-version': '2.0.0',
                                    }

                                    ID = response.split('li:fsd_company:')[1].split('&')[0]
                                    follow = requests.post('https://www.linkedin.com/voyager/api/feed/dash/followingStates/urn:li:fsd_followingState:urn:li:fsd_company:'+ID,headers=headersX,json=json_data)
                                    time.sleep(2)
                                    url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                                    check = requests.post(url,headers=headers,json=json_data2).json()
                                    if check['success'] == True:
                                        dem += 1
                                        local_time = time.localtime()
                                        hour = local_time.tm_hour
                                        minute = local_time.tm_min
                                        second = local_time.tm_sec

                                        # Định dạng giờ, phút, giây
                                        h = f"{hour:02d}"
                                        m = f"{minute:02d}"
                                        s = f"{second:02d}"
                                        prices = check['data']['prices']

                                        # Cộng dồn giá trị prices vào tổng tiền
                                        tong += prices

                                        chuoi = (
                                            f"{trang}[   {zuo}{dem}\033[1;31m\033[1;97m   ] "
                                            f"\033[1;33m {h}:{m}:{s}\033[1;31m\033[1;97m  "
                                            f"{trang}success\033[1;31m\033[1;97m  "
f"{red} Theo Dõi\033[1;31m\033[1;32m\033[1;32m\033[1;97m "                                                                         
                                            f"{tim}  Ẩn ID\033[1;97m \033[1;97m \033[1;32m+{prices} \033[1;97m "
                                            f"{cyan}{tong}"
                                            
                                        )
                                        print(chuoi) 
                                    else:
                                            skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                            PARAMS = {
                                            'ads_id' : ads_id,
                                            'account_id' : account_id,
                                            'object_id' : object_id ,
                                            }
                                            checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                            if checkskipjob['status'] == 200:
                                                message = checkskipjob['message']
                                                print(Fore.RED+str(message))
                                                PARAMSr = {
                                                'ads_id' : ads_id,
                                                'account_id' : account_id,
                                                'object_id' : object_id ,
                                                }
                                except IndexError:
                                    headersY = {
                                    'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                    'content-type': 'application/json; charset=UTF-8',
                                    'cookie':COOKIELINK,
                                    'csrf-token': COOKIELINK.split('JSESSIONID=')[1].split(';')[0],
                                    'origin': 'https://www.linkedin.com',
                                    'priority': 'u=1, i',
                                    'referer': 'https://www.linkedin.com/in/noman-chaudhary-52031148/',
                                    'sec-fetch-dest': 'empty',
                                    'sec-fetch-mode': 'cors',
                                    'sec-fetch-site': 'same-origin',
                                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                    'x-li-lang': 'en_US',
                                    'x-li-page-instance': 'urn:li:page:d_flagship3_profile_view_base;I6RhpcMURWuRvBmeIhl5BQ==',
                                    'x-li-pem-metadata': 'Voyager - Follows=follow-action,Voyager - Profile Actions=topcard-primary-follow-action-click',
                                    'x-li-track': '{"clientVersion":"1.13.19938","mpVersion":"1.13.19938","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                    'x-restli-protocol-version': '2.0.0',
                                    }
                                    try:
                                        ID = response.split('identityDashProfilesByMemberIdentity&quot;:{&quot;*elements&quot;:[&quot;urn:li:fsd_profile:')[1].split('&')[0]
                                        follow =  requests.post('https://www.linkedin.com/voyager/api/feed/dash/followingStates/urn:li:fsd_followingState:urn:li:fsd_profile:'+ID,headers=headersY,json=json_data) 
                                        time.sleep(2)
                                        url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                                        check = requests.post(url,headers=headers,json=json_data2).json()
                                        if check['success'] == True:
                                            dem += 1
                                            local_time = time.localtime()
                                            hour = local_time.tm_hour
                                            minute = local_time.tm_min
                                            second = local_time.tm_sec

                                            # Định dạng giờ, phút, giây
                                            h = f"{hour:02d}"
                                            m = f"{minute:02d}"
                                            s = f"{second:02d}"
                                            prices = check['data']['prices']

                                            # Cộng dồn giá trị prices vào tổng tiền
                                            tong += prices

                                            chuoi = (
                                            f"{trang}[   {zuo}{dem}\033[1;31m\033[1;97m   ] "
                                            f"\033[1;33m {h}:{m}:{s}\033[1;31m\033[1;97m  "
                                            f"{trang}success\033[1;31m\033[1;97m  "
f"{red} Thả Like\033[1;31m\033[1;32m\033[1;32m\033[1;97m "                                                                         
                                            f"{tim}  Ẩn ID\033[1;97m \033[1;97m \033[1;32m+{prices} \033[1;97m "
                                            f"{cyan}{tong}"
                                            
                                        )
                                            print(chuoi) 
                                        else:
                                                skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                                PARAMS = {
                                                'ads_id' : ads_id,
                                                'account_id' : account_id,
                                                'object_id' : object_id ,
                                            
                                                }
                                                checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                                if checkskipjob['status'] == 200:
                                                    message = checkskipjob['message']
                                                    print(Fore.RED+str(message))
                                                    PARAMSr = {
                                                    'ads_id' : ads_id,
                                                    'account_id' : account_id,
                                                    'object_id' : object_id ,
                                                    
                                                    }
                                    except IndexError:
                                        print(f'{do}COOKIE DIE!')
                                        os.remove(f'cookie_linkedin.txt')
                                        return 0
                    elif type == 'like':
                        try:
                            crft =  COOKIELINK.split('JSESSIONID')[1].split(';')[0],

                            headersL = {
                                'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                'content-type': 'application/json; charset=UTF-8',
                                'cookie': COOKIELINK,
                                'csrf-token': COOKIELINK.split('JSESSIONID=')[1].split(';')[0],
                                'origin': 'https://www.linkedin.com',
                                'priority': 'u=1, i',
                                'referer': 'https://www.linkedin.com/feed/update/urn:li:activity:7219700822467575808/',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                'x-li-lang': 'en_US',
                                # 'x-li-page-instance': 'urn:li:page:d_flagship3_detail_base;T3jRBiYHTZqgLY+qsIgtkg==',
                                'x-li-track': '{"clientVersion":"1.13.20142","mpVersion":"1.13.20142","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                'x-restli-protocol-version': '2.0.0',
                            }

                            params = {
                                'action': 'execute',
                                'queryId': 'voyagerSocialDashReactions.b731222600772fd42464c0fe19bd722b',
                            }

                            json_data = {
                                'variables': {
                                    'entity': {
                                        'reactionType': 'LIKE',
                                    },
                                    'threadUrn': 'urn:li:activity:'+str(object_id),
                                },
                                'queryId': 'voyagerSocialDashReactions.b731222600772fd42464c0fe19bd722b',
                                'includeWebMetadata': True,
                            }

                            response = requests.post(
                                'https://www.linkedin.com/voyager/api/graphql',
                                params=params,
                                headers=headersL,
                                json=json_data
                            )
                        except IndexError:
                            headersN = {
                                'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                'content-type': 'application/json; charset=UTF-8',
                                'cookie': COOKIELINK,
                                'csrf-token': COOKIELINK.split('JSESSIONID="')[1].split('"')[0],
                                'origin': 'https://www.linkedin.com',
                                'priority': 'u=1, i',
                                'referer': 'https://www.linkedin.com/feed/update/urn:li:activity:7219700822467575808/',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                'x-li-lang': 'en_US',
                                # 'x-li-page-instance': 'urn:li:page:d_flagship3_detail_base;T3jRBiYHTZqgLY+qsIgtkg==',
                                'x-li-track': '{"clientVersion":"1.13.20142","mpVersion":"1.13.20142","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                'x-restli-protocol-version': '2.0.0',
                            }

                            params = {
                                'action': 'execute',
                                'queryId': 'voyagerSocialDashReactions.b731222600772fd42464c0fe19bd722b',
                            }

                            json_data = {
                                'variables': {
                                    'entity': {
                                        'reactionType': 'LIKE',
                                    },
                                    'threadUrn': 'urn:li:activity:'+str(object_id),
                                },
                                'queryId': 'voyagerSocialDashReactions.b731222600772fd42464c0fe19bd722b',
                                'includeWebMetadata': True,
                            }

                            response = requests.post(
                                'https://www.linkedin.com/voyager/api/graphql',
                                params=params,
                                headers=headersN,
                                json=json_data
                            )
                        json_data2 = {
                                'account_id': account_id,
                                'ads_id': ads_id,
                            }
                        time.sleep(2)
                        url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                        check = requests.post(url,headers=headers,json=json_data2).json()
                        if check['success'] == True:
                                        dem += 1
                                        local_time = time.localtime()
                                        hour = local_time.tm_hour
                                        minute = local_time.tm_min
                                        second = local_time.tm_sec

                                        # Định dạng giờ, phút, giây
                                        h = f"{hour:02d}"
                                        m = f"{minute:02d}"
                                        s = f"{second:02d}"
                                        prices = check['data']['prices']

                                        # Cộng dồn giá trị prices vào tổng tiền
                                        tong += prices

                                        chuoi = (
                                            f"{trang}[   {zuo}{dem}\033[1;31m\033[1;97m   ] "
                                            f"\033[1;33m {h}:{m}:{s}\033[1;31m\033[1;97m  "
                                            f"{trang}success\033[1;31m\033[1;97m  "
f"{red} Thả Like\033[1;31m\033[1;32m\033[1;32m\033[1;97m "                                                                         
                                            f"{tim}  Ẩn ID\033[1;97m \033[1;97m \033[1;32m+{prices} \033[1;97m "
                                            f"{cyan}{tong}"
                                            
                                        )
                                        print(chuoi) 
                        else:
                                skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                PARAMS = {
                                'ads_id' : ads_id,
                                'account_id' : account_id,
                                'object_id' : object_id ,
                                }
                                checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                if checkskipjob['status'] == 200:
                                    message = checkskipjob['message']
                                    print(Fore.RED+str(message))
                                    PARAMSr = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }   
                else:       
                    print(f'{zuo}Hết Job Cho nghỉ 30 phút !')
                    
                    countdown(NVA)

checkfile = os.path.isfile('Authorization.txt')
if checkfile == False:
    createfile = open('Authorization.txt','w')
    createfile.write(author)
    createfile.close()
    readfile = open('Authorization.txt','r')
    file = readfile.read()
    readfile.close()
else:
             
            print(f'                 {z3}Danh Sách Tài Khoản ')
            print(f'{zuo}=============================================')
            LINKEDIN()
                
