import requests,os,sys, time
from datetime import datetime
from time import sleep, strftime
import hashlib
lamd = "\033[1;34m"
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
xanhnhat = "\033[1;36m"
xanh = "\033[1;32m"
baner ="??????????\n"
het ="\033[0m"
ngan= "┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫⁠\n"
tren = "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n"
duoi ="┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n"
os.system("clear")
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
mau = f"{thu} Ngày {ngay} Tháng {thang} Năm {nam}\nGiờ : {gio}\n"
def loading_animation(duration=10):
    end_time = time.time() + duration
    loading_chars = ['|', '/', '-', '\\']  
    while time.time() < end_time:
        for char in loading_chars:
            sys.stdout.write('\rĐang Loading Vui Lòng Chờ ' + char+'')  
            sys.stdout.flush()  
            time.sleep(0.01)  

    print('\rChào Mừng Bạn Đến Với Tool !', end='\r')
    sleep(2)
    print('                                                        ', end='\r')  # Hoàn thành loading

# Gọi hàm Để Loading hiện 
loading_animation()
for X in baner:
    sys.stdout.write(X)
    sys.stdout.flush()
    sleep(0.25)
def genkey(ip):
    return hashlib.md5(f"{ip}{datetime.now().strftime('%Y-%m-%d')}7535gydr".encode()).hexdigest()

FileLuuKey = 'keytoolnva.txt' # Bạn có thể thay tùy thích:v

getIP = requests.get('https://kiemtraip.com/raw.php').text

key = genkey(getIP)
url = f'https://flttnva.com/?key={key}'  # Trang đích 
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
    print("\033[1;31mChú ý : Key là bắt đầu từ Sau key= của url")
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
os.system("clear")
for X in baner:
    sys.stdout.write(X)
    sys.stdout.flush()
    sleep(0.25)
for X in mau:
    sys.stdout.write(X)
    sys.stdout.flush()
    sleep(0.25)
for X in tren:
    sys.stdout.write(X)
    sys.stdout.flush()
    sleep(0.025)
print("\033[1;37m➩ Nhập Số [1] Tool Buff follow Tik Tok\033[0m")
for X in ngan:
    sys.stdout.write(X)
    sys.stdout.flush()
    sleep(0.025)
print("\033[1;37m➩ Nhập Số [2] Tool Buff Tik Tok Zefoy\033[0m")
for X in duoi:
    sys.stdout.write(X)
    sys.stdout.flush()
    sleep(0.025)
chon = str(input(' Nhập Lựa Chọn : '))


if chon == '1':
    exec(requests.get('https://raw.githubusercontent.com/Anh2092008/Anh/refs/heads/main/Bufffltt').text)
#    
elif chon == '2':
    exec(requests.get('https://raw.githubusercontent.com/Anh2092008/Anh/refs/heads/main/Zefoy').text)
else:
    print("Sai Lựa Chọn")
    exit()
