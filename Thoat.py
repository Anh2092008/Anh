import requests
import time
import os
import sys
from time import sleep, strftime
import hashlib
from datetime import datetime

os.system("cls" if os.name == "nt" else "clear")

# Lấy thời gian hiện tại
current_date = datetime.now()
ngay = current_date.strftime('%d')
thang = current_date.month
nam = current_date.year
gio = current_date.strftime('%H : %M : %S')
thu_dict = {
    "Monday": "Thứ Hai",
    "Tuesday": "Thứ Ba",
    "Wednesday": "Thứ Tư",
    "Thursday": "Thứ Năm",
    "Friday": "Thứ Sáu",
    "Saturday": "Thứ Bảy",
    "Sunday": "Chủ Nhật"
}
thu = thu_dict[current_date.strftime("%A")]

# Hàm loading animation
def loading_animation(duration=10):
    end_time = time.time() + duration
    loading_chars = ['|', '/', '-', '\\']  
    while time.time() < end_time:
        for char in loading_chars:
            sys.stdout.write('\rĐang Loading Vui Lòng Chờ ' + char)  
            sys.stdout.flush()  
            time.sleep(0.01)  

    print('\rChào Mừng Bạn Đến Với Tool !', end='\r')
    sleep(2)
    print('                                                        ', end='\r')  # Hoàn thành loading

# Gọi hàm Để Loading hiện 
loading_animation()

def genkey(ip):
    return hashlib.md5(f"{ip}{datetime.now().strftime('%Y-%m-%d')}7535gydr".encode()).hexdigest()

FileLuuKey = 'keytoolnva.txt' # Bạn có thể thay tùy thích:v

getIP = requests.get('https://kiemtraip.com/raw.php').text

key = genkey(getIP)
url = f'https://huongdev.com/?key={key}'  # Trang đích 
yeumoney = requests.get(f'https://link4m.co/api-shorten/v2?api=66cd182d82f1d87dd96f0210&url={url}').json()["shortenedUrl"]

while True:
    if os.path.exists(FileLuuKey):
        with open(FileLuuKey, "r") as file:
            file_key = file.read().strip()
        if file_key == key:
            break
        else:
            os.remove(FileLuuKey)
            continue

    #print(f"{thu} Ngày {ngay} Tháng {thang} Năm {nam}")
    #print(f'Giờ : {gio}')
    print("Chú ý : Key là bắt đầu từ key= của url")
    print("Nếu ko hiểu liên hệ Zalo : https://zaloapp.com/qr/p/1dvbslht1vl1r?src=qr")
    print(f"\033[1;33mLink Key Ngày \033[1;32m:\033[1;36m {yeumoney}")

    inputkey = input('\033[1;33mNhập key \033[1;35m: \033[1;94m').strip()

    if inputkey == key:
        print('\033[1;32m Key đúng rồi bú thôi!\033[0;m', end='\r')
        sleep(1)
        print('                                                        ', end='\r')
        with open(FileLuuKey, "w") as file:
            file.write(inputkey)
        break
    else:
        print('\033[1;31m Key Sai Mẹ rồi', end='\r')
        sleep(1)
        print('                                                        ', end='\r')
        
        os.system("clear")

# In thời gian và thông báo
print(f'{thu} Ngày {ngay} Tháng {thang} Năm {nam}')
print(f'Giờ : {gio} ')
print('\033[1;31mChú ý\033[0m : Nguồn lỏ nhiều khi Thành Công Nhưng FL ko tăng')

username = input('\033[1;36mNhập Username Tik Tok ( Sau @ ) : ')
me = f"\033[1;36mUsername\033[0m  : {username}\n"
for X in me:
    sys.stdout.write(X)
    sys.stdout.flush()
    sleep(0.25)
print('----------------------------------------')

while True:
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }
    
    access = requests.get('https://tikfollowers.com/free-tiktok-followers', headers=headers)
    try:
        session = access.cookies['ci_session']
        headers.update({'cookie': f'ci_session={session}'})
        token = access.text.split("csrf_token = '")[1].split("'")[0]
        data = '{"type":"follow","q":"@' + username + '","google_token":"t","token":"' + token + '"}'
        
        search = requests.post('https://tikfollowers.com/api/free', headers=headers, data=data).json()
        if search['success'] == True:
            data_follow = search['data']
            data = '{"google_token":"t","token":"' + token + '","data":"' + data_follow + '","type":"follow"}'
            send_follow = requests.post('https://tikfollowers.com/api/free/send', headers=headers, data=data).json()
            if send_follow['o'] == 'Success!' and send_follow['success'] == True and send_follow['type'] == 'success':
                print(f'\033[1;32mThành Công\033[0m : Tăng Follow Tik Tok')
                print(f'\033[1;36mUsername\033[0m  : {username}')
                print('----------------------------------------')
                continue
            elif send_follow['o'] == 'Oops...' and send_follow['success'] == False and send_follow['type'] == 'info':
                try:
                    thoigian = send_follow['message'].split('You need to wait for a new transaction. : ')[1].split('.')[0]
                    phut = thoigian.split(' Minutes')[0]
                    giay = int(phut) * 60
                    for i in range(giay, 0, -1):
                        print(f'\033[1;36mVui Lòng Chờ {i} Giây\033[0m ', end='\r')
                        time.sleep(1)
                    continue
                except:
                    print(f'\033[1;31mThất Bại\033[0m : Tăng Follow Tik Tok')
                print(f'\033[1;36mUsername\033[0m  : {username}')
                print('----------------------------------------')
                continue
    except:
        print('Lỗi Không Xác Định               ', end='\r')
        sleep(1)
        print('                                                        ', end='\r')
        continue
