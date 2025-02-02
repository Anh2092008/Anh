import requests, os, time
from time import sleep
from prettytable import PrettyTable  # Thêm thư viện prettytable

# Màu sắc
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
n = "\033[1;3m\033[1;38m"
e = "\033[0m"

# Kiểm tra hoặc tạo file lưu Authorization và token
try:
    open("Authorization.txt", "x").close()
    open("token.txt", "x").close()
    open("cookie_linkedin.txt", "x").close()
except:
    pass

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/tiktok',
}

def chonacc():
    response = requests.get('https://gateway.golike.net/api/tiktok-account', headers=headers).json()
    return response

def nhannv(account_id):
    params = {'account_id': account_id, 'data': 'null'}
    response = requests.get('https://gateway.golike.net/api/advertising/publishers/tiktok/jobs', params=params, headers=headers).json()
    return response

def hoanthanh(ads_id, account_id):
    json_data = {
        'ads_id': ads_id,
        'account_id': account_id,
        'async': True,
        'data': None,
    }
    response = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs', headers=headers, json=json_data).json()
    return response

def baoloi(ads_id, object_id, account_id, loai):
    json_data1 = {
        'description': 'Tôi đã làm Job này rồi',
        'users_advertising_id': ads_id,
        'type': 'ads',
        'provider': 'tiktok',
        'fb_id': account_id,
        'error_type': 6,
    }
    requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1)

    json_data = {
        'ads_id': ads_id,
        'object_id': object_id,
        'account_id': account_id,
        'type': loai,
    }
    requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs', headers=headers, json=json_data)

loat = int(input(f"{trang}Nhập delay (giây): "))
thay = int(input(f"{trang}Nhập số lần lỗi để đổi tài khoản: "))
# Lấy danh sách tài khoản TikTok
chontktiktok = chonacc()

def dsacc():
    if chontktiktok["status"] != 200:
        print(f"{red}Authorization hoặc Token không hợp lệ!{e}")
        quit()

    # Hiển thị danh sách tài khoản bằng PrettyTable
    table = PrettyTable()
    table.field_names = ["STT", "Tên Tài Khoản", "Trạng Thái"]
    for i, acc in enumerate(chontktiktok["data"], start=1):
        table.add_row([i, acc["nickname"], "Hoạt Động"])
    print(table)

dsacc()

# Người dùng chọn tài khoản TikTok
while True:
    try:
        luachon = int(input(f"{vang}Chọn tài khoản để chạy: {e}"))
        while luachon > len(chontktiktok["data"]):
            luachon = int(input("Tài khoản không tồn tại. Hãy nhập lại: "))
        account_id = chontktiktok["data"][luachon - 1]["id"]
        break
    except:
        print(f"{red}Sai định dạng !{e}")

# Nhập thông số delay và số lần đổi tài khoản
while True:
    try:
        delay = loat
        break
    except:
        print(f"{red}Sai định dạng !{e}")

while True:
    try:
        doiacc = thay
        break
    except:
        print("Nhập một số hợp lệ!")

# Các biến khởi tạo
dem = 0
tong = 0
checkdoiacc = 0
dsaccloi = []

# Chạy nhiệm vụ
while True:
    if checkdoiacc == doiacc:
        dsaccloi.append(chontktiktok["data"][luachon - 1]["nickname"])
        print(f"Các tài khoản gặp lỗi: {dsaccloi}")
        dsacc()
        while True:
            try:
                luachon = int(input("Chọn tài khoản để chạy: "))
                while luachon > len(chontktiktok["data"]):
                    luachon = int(input("Tài khoản không tồn tại. Hãy nhập lại: "))
                account_id = chontktiktok["data"][luachon - 1]["id"]
                checkdoiacc = 0
                break
            except:
                print("Sai định dạng!")

    nhanjob = nhannv(account_id)
    if nhanjob["status"] == 200:
        ads_id = nhanjob["data"]["id"]
        link = nhanjob["data"]["link"]
        object_id = nhanjob["data"]["object_id"]

        if nhanjob["data"]["type"] != "follow":
            baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
            continue

        os.system(f"termux-open-url {link}")
        for i in range(delay, -1, -1):
            print(f"Đang đợi {i}s...", end="\r")
            sleep(1)

        nhantien = hoanthanh(ads_id, account_id)
        if nhantien["status"] == 200:
            dem += 1
            tien = nhantien["data"]["prices"]
            tong += tien
            print (Colorate.Diagonal(Colors.cyan_to_green, f"{dem}   +{tien}   {tong}"))
            checkdoiacc = 0
        else:
            baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
            checkdoiacc += 1


    # Menu after encountering an error
    if checkdoiacc >= doiacc:
        print(f"{red}Tài khoản {chontktiktok['data'][luachon - 1]['nickname']} đã gặp quá nhiều lỗi!{e}")
        while True:
            print(f"{trang}Nhập {luc}1 {trang}Để Chạy Lại Acc")
            print(f"{trang}Nhập {luc}2 {trang}Để Thay Acc")
            print(f"{trang}Nhập {luc}3 {trang}Để thoát Tool")
            choice = input(f"{trang}Lựa Chọn : {luc}")
            if choice == '1':
                print(f"{trang}Tiếp tục với tài khoản này...")
                checkdoiacc = 0  # Reset error count for this account
                break
            elif choice == '2':
                dsacc()  # List available accounts again
                while True:
                    try:
                        luachon = int(input(f"{vang}Chọn tài khoản để chạy: {e}"))
                        while luachon > len(chontktiktok["data"]):
                            luachon = int(input("Tài khoản không tồn tại. Hãy nhập lại: "))
                        account_id = chontktiktok["data"][luachon - 1]["id"]
                        checkdoiacc = 0  # Reset error count for new account
                        break
                    except:
                        print("Sai định dạng!")
                break
            elif choice == '3':
                print("Thoát tool...")
                quit()  # Exit the script
            else:
                print(f"{red}Lựa chọn không hợp lệ! Hãy nhập lại.{e}")
