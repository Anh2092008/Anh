import requests,os,sys, time
from datetime import datetime
from time import sleep, strftime
import hashlib
from datetime import datetime, timedelta
lamd = "\033[1;34m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
xanhnhat = "\033[1;36m"
xanh = "\033[1;32m"
free = "\n"
baner = "          \033[1;37m██╗░░░██╗░█████╗░███╗░░░██╗░░░░░░░█████╗░███╗░░░██╗██╗░░██╗\n          \033[1;36m██║░░░██║██╔══██╗████╗░░██║░░░░░░██╔══██╗████╗░░██║██║░░██║\n          \033[1;35m██║░░░██║███████║██╔██╗░██║░░░░░░███████║██╔██╗░██║███████║\n          \033[1;34m╚██╗░██╔╝██╔══██║██║╚██╗██║░░░░░░██╔══██║██║╚██╗██║██╔══██║\n          \033[1;33m░╚████╔╝░██║░░██║██║░╚████║░░░░░░██║░░██║██║░╚████║██║░░██║\n          \033[1;32m░░╚═══╝░░╚═╝░░╚═╝╚═╝░░╚═══╝░░░░░░╚═╝░░╚═╝╚═╝░░╚═══╝╚═╝░░╚═╝\n          \033[1;31m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
het ="\033[0m"
dam ="\033[1m"
anh ="\033[1;37m[\033[1;33mN\033[1;32mV\033[1;31mA\033[1;37m]" 
ngan= "         \033[1;31m╠⁠\033[0m\033[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;31m╣\033[0m\n"
tren = "         \033[1;31m╔\033[0m\033[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;31m╗\033[0m\n"
duoi ="         \033[1;31m╚\033[0m\033[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;31m╝\033[0m\n"
thang = "\033[1;31m┗┫⁠┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓┣┛\033[0m"
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
mau = f"{anh} \x1b[38;5;46m➜ {trang}[ {xanh}{thu} {trang}] {trang}[ {xanh}Ngày {ngay} Tháng {thang} Năm {nam} {trang}]\n{anh} \x1b[38;5;46m➜ {trang}[ {xanh}Giờ {trang}] : {trang}[ {xanh}{gio} {trang}]\n"
def loading_animation(duration=5):
    end_time = time.time() + duration
    loading_chars = ['|', '/', '-', '\\']  
    while time.time() < end_time:
        for char in loading_chars:
            sys.stdout.write(f'\r{anh} \x1b[38;5;46m➜ \x1b[38;5;208mĐang Loading Vui Lòng Chờ [' + char+']')  
            sys.stdout.flush()  
            time.sleep(0.01)  

    print(f'\r{anh} \x1b[38;5;46m➜ Chào Mừng Bạn Đến Với Tool !', end='\r')
    sleep(2)
    print('                                                        ', end='\r')  # Hoàn thành loading

# Gọi hàm Để Loading hiện 
loading_animation()
for X in baner:
    sys.stdout.write(X)
    sys.stdout.flush()
    sleep(0.0025)
def genkey(ip):
    # Generate a unique key based on IP and current date
    return hashlib.md5(f"{ip}{datetime.now().strftime('%Y-%m-%d')}7535gydr".encode()).hexdigest()

FileLuuKey = 'keytoolnva.txt'  # File to store key
FileLuuTime = 'keytooltime.txt'  # File to store key generation time

getIP = requests.get('https://kiemtraip.com/raw.php').text
key = genkey(getIP)
url = f'https://flttnva.com/?key={key}'  # Destination URL
yeumoney = requests.get(f'https://link4m.co/api-shorten/v2?api=66cd182d82f1d87dd96f0210&url={url}').json()["shortenedUrl"]

def end_of_next_day():
    # Set expiration time to the end of the next day (23:59:59)
    tomorrow = datetime.now() + timedelta(days=1)
    return tomorrow.replace(hour=23, minute=59, second=59, microsecond=0)

def display_remaining_time(expiry_time):
    # Calculate the remaining time until expiry
    time_left = expiry_time - datetime.now()
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    #print(f"Thời gian còn lại: {hours} giờ {minutes} phút {seconds} giây")

# Set expiration time to end of the next day (23:59:59)
expiry_time = end_of_next_day()

while True:
    # Check if the key file exists
    if os.path.exists(FileLuuKey) and os.path.exists(FileLuuTime):
        # Read the stored key and time from file
        with open(FileLuuKey, "r") as file:
            file_key = file.read().strip()
        with open(FileLuuTime, "r") as time_file:
            stored_time = datetime.fromisoformat(time_file.read().strip())
        
        # Set expiry time to 23:59:59 of the day after the key was generated
        expiry_time = stored_time + timedelta(days=1)
        expiry_time = expiry_time.replace(hour=23, minute=59, second=59, microsecond=0)
        
        # Check if the stored key is valid and not expired
        if file_key == key and datetime.now() < expiry_time:
            display_remaining_time(expiry_time)
            #print(f"Hạn sử dụng key đến: {expiry_time.strftime('%Y-%m-%d ')}")
            #print("Hết Thời Gian Ae Chuẩn Bị Key Mới")
            break
        else:
            # Key is expired or invalid; remove files to prompt re-entry
            os.remove(FileLuuKey)
            os.remove(FileLuuTime)
            continue

    print("\033[1;31mKey là sau từ 'key=' của URL")
    print("Ko hiểu liên hệ Zalo: https://zaloapp.com/qr/p/1dvbslht1vl1r?src=qr")
    print(f"{anh} \x1b[38;5;46m➜ \033[1;37m[ \033[1;32mKey \033[1;37m]\033[1;35m :\033[1;36m {key}")
    print(f"{anh} \x1b[38;5;46m➜ \033[1;37m[ \033[1;32mKey Link \033[1;37m]\033[1;35m :\033[1;36m {yeumoney}")

    inputkey = input(f'{anh} \x1b[38;5;46m➜ \033[1;37m[ \033[1;32mNhập key \033[1;37m]\033[1;35m : \033[1;36m').strip()

    # Check if the entered key matches
    if inputkey == key:
        print(f'{anh} \x1b[38;5;46m➜ \033[1;37m[ \033[1;32mKey Đúng \033[1;37m] ', end='\r')
        sleep(1)
        print(' ' * 60, end='\r')
        
        # Write the key and the current time to file
        with open(FileLuuKey, "w") as file:
            file.write(inputkey)
        with open(FileLuuTime, "w") as time_file:
            time_file.write(datetime.now().isoformat())
        
        # Set expiry time to 23:59:59 of the next day and display it
        expiry_time = end_of_next_day()
        display_remaining_time(expiry_time)
        #print(f"Hạn sử dụng key đến: {expiry_time.strftime('%Y-%m-%d ')}")
        break
    else:
        print(f'{anh} \x1b[38;5;46m➜ \033[1;37m[ \033[1;31mKey Sai \033[1;37m] ', end='\r')
        sleep(1)
        print(' ' * 60, end='\r')

        
        os.system("clear")
        for X in baner:
            sys.stdout.write(X)
            sys.stdout.flush()
            sleep(0.0125)
os.system("clear")
time_left = expiry_time - datetime.now()
hours, remainder = divmod(time_left.seconds, 3600)
minutes, seconds = divmod(remainder, 60)
display_remaining_time(expiry_time)
thu_dic = {
    "Monday": "Thứ Ba",
    "Tuesday": "Thứ Tư",
    "Wednesday": "Thứ Năm",
    "Thursday": "Thứ Sáu",
    "Friday": "Thứ Bảy",
    "Saturday": "Chủ Nhật",
    "Sunday": "Thứ Hai"
}
thuu = thu_dic[current_date.strftime("%A")]
            #♪⁠┌⁠║⁠∵⁠║⁠┘⁠♪║⁠ ⁠”⁠ ⁠⊚⁠ ͟⁠ʖ⁠ ⁠⊚⁠ ⁠”⁠ ⁠╏♥⁠╣⁠[⁠-⁠_⁠-⁠]⁠╠⁠♥
for X in baner:
    sys.stdout.write(X)
    sys.stdout.flush()
    sleep(0.0025)
for X in free:
    sys.stdout.write(X)
    sys.stdout.flush()
    sleep(0.0025)
print(f"\033[1;31m╔━━━━━━━━╦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
print(f"\033[1;31m║⁠{anh} \x1b[38;5;46m➜ \033[1;31m║⁠ \033[1;37m[\033[1;32m Thông Tin Key \033[1;37m]")
print(f"\033[1;31m║⁠{anh} \x1b[38;5;46m➜ \033[1;31m║⁠ \033[1;37m[ \033[1;32m{thuu} \033[1;37m] {expiry_time.strftime('\033[1;37m[ \033[1;32mNgày %d Tháng %m Năm %Y \033[1;37m]')}")
print(f"\033[1;31m║⁠{anh} \x1b[38;5;46m➜ \033[1;31m║⁠ \033[1;37m[ \033[1;32mThời gian còn lại \033[1;37m] : \033[1;37m[\033[1;32m {hours} : {minutes} : {seconds} \033[1;37m ]")
print(f"\033[1;31m╠⁠━━━━━━━━╩━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
print(f"\033[1;31m╠⁠━━━━━━━━╦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
print(f"\033[1;31m║⁠{anh} \x1b[38;5;46m➜ \033[1;31m║ {trang}[ {xanh}Hôm Nay {trang}] {trang}[ {xanh}vs {trang}] {trang}[ {xanh}Thời Gian {trang}]")
print(f"\033[1;31m║⁠{anh} \x1b[38;5;46m➜ \033[1;31m║⁠ {trang}[ {xanh}{thu} {trang}] {trang}[ {xanh}Ngày {ngay} Tháng {thang} Năm {nam} {trang}]")
print(f"\033[1;31m║⁠{anh} \x1b[38;5;46m➜ \033[1;31m║ {trang}[ {xanh}Thời Gian Vô Tool{trang} ] : {trang}[ {xanh}{gio} {trang}]⁠")
print(f"\033[1;31m╚━━━━━━━━╩━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
for X in tren:
    sys.stdout.write(X)
    sys.stdout.flush()
    sleep(0.025)
print(f" {anh} \x1b[38;5;46m➜   \033[1;37m[\033[1;32m 1 \033[1;37m] Tool Buff follow Tik Tok [Đểu]\033[0m")
for X in ngan:
    sys.stdout.write(X)
    sys.stdout.flush()
    sleep(0.025)
print(f" {anh} \x1b[38;5;46m➜   \033[1;37m[\033[1;32m 2 \033[1;37m] Tool Buff Tik Tok Zefoy [Capcha ko giải đc]\033[0m")
for X in ngan:
    sys.stdout.write(X)
    sys.stdout.flush()
    sleep(0.025)
print(f" {anh} \x1b[38;5;46m➜   \033[1;37m[\033[1;32m 3 \033[1;37m] Tool Golike Linkedin\033[0m")
for X in ngan:
    sys.stdout.write(X)
    sys.stdout.flush()
    sleep(0.025)
print(f" {anh} \x1b[38;5;46m➜   \033[1;37m[\033[1;32m 4 \033[1;37m] Tool Share Ảo Bài viết Fb [Ổn]\033[0m")
for X in duoi:
    sys.stdout.write(X)
    sys.stdout.flush()
    sleep(0.025)
chon = str(input(f' {anh} \x1b[38;5;46m➜   \033[1;37m[ \033[1;33mNhập \033[1;32mLựa \033[1;31mChọn \033[1;37m] \033[1;35m: \033[1;32m'))


if chon == '1':
    exec(requests.get('https://raw.githubusercontent.com/Anh2092008/Anh/refs/heads/main/Bufffltt').text)
#    
elif chon == '2':
    exec(requests.get('https://raw.githubusercontent.com/Anh2092008/Anh/refs/heads/main/Zefoy').text)
elif chon == '3':
    exec(requests.get('').text)
elif chon == '4':
    exec(requests.get('https://raw.githubusercontent.com/Anh2092008/Anh/refs/heads/main/Share%20Ao').text)
else:
    print(f" {anh} \x1b[38;5;46m➜ \033[1;37m[ \033[1;31mSai Lựa Chọn \033[1;37m]")
    print(f" {anh} \x1b[38;5;46m➜ \033[1;37m[ \033[1;31mChạy Lại Tools \033[1;37m]")
    exit()
