import requests, os, time
from time import sleep
from prettytable import PrettyTable

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
e = "\033[0m"

# Kiểm tra hoặc tạo file lưu Authorization và token
try:
    open("Authorization.txt", "x").close()
    open("token.txt", "x").close()
    open("cookie_linkedin.txt", "x").close()
except:
    pass

# Đọc Authorization và token từ file
try:
    with open("Authorization.txt", "r") as auth_file:
        author = auth_file.read().strip()
    with open("token.txt", "r") as token_file:
        token = token_file.read().strip()
except:
    print(f"{red}Không tìm thấy file Authorization hoặc Token. Vui lòng kiểm tra lại!{e}")
    quit()

# Kiểm tra nếu Authorization hoặc token rỗng
if not author or not token:
    print(f"{red}Authorization hoặc Token không được để trống!{e}")
    quit()

# Headers API
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,  # Giá trị Authorization
    't': token,  # Giá trị token
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/tiktok',
}

# Hàm lấy danh sách tài khoản TikTok
def chonacc():
    try:
        response = requests.get('https://gateway.golike.net/api/tiktok-account', headers=headers)
        if response.status_code != 200:
            print(f"{red}API trả về lỗi: {response.status_code}. Nội dung: {response.json()}{e}")
            quit()
        return response.json()
    except Exception as ex:
        print(f"{red}Lỗi khi gọi API: {ex}{e}")
        quit()

# Lấy danh sách tài khoản
chontktiktok = chonacc()

# Hàm hiển thị danh sách tài khoản TikTok
def dsacc():
    if chontktiktok.get("status") != 200:
        print(f"{red}Authorization hoặc Token không hợp lệ!{e}")
        quit()

    # Tạo bảng sử dụng PrettyTable
    table = PrettyTable()
    table.field_names = ["STT", "Tên Tài Khoản", "Trạng Thái"]
    table.align = "l"

    # Thêm dữ liệu vào bảng với định dạng màu sắc
    for i, account in enumerate(chontktiktok["data"], start=1):
        nickname = account.get("nickname", "Chưa xác định")
        status = "Hoạt động" if account.get("status") == "active" else "Không hoạt động"
        
        # Định dạng màu sắc cho tên tài khoản
        nickname_colored = f"{vang}{nickname}{e}"
        status_colored = f"{luc}{status}{e}" if status == "Hoạt động" else f"{red}{status}{e}"
        
        table.add_row([f"{luc}{i}{e}", nickname_colored, status_colored])

    # Hiển thị bảng
    print(f"{lam}Danh sách tài khoản TikTok:{e}")
    print(table)

# Hiển thị danh sách tài khoản
dsacc()

# Người dùng chọn tài khoản TikTok
while True:
    try:
        luachon = int(input(f"{vang}Chọn tài khoản để chạy: {e}"))
        if 1 <= luachon <= len(chontktiktok["data"]):
            account_id = chontktiktok["data"][luachon - 1]["id"]
            break
        else:
            print(f"{red}Tài khoản không tồn tại. Hãy nhập lại!{e}")
    except ValueError:
        print(f"{red}Sai định dạng! Vui lòng nhập số.{e}")

# Các biến khởi tạo
loat = int(input("Nhập delay (giây): "))
thay = int(input("Nhập số lần lỗi để đổi tài khoản: "))
dem = 0
tong = 0
checkdoiacc = 0
dsaccloi = []

# Chạy nhiệm vụ
while True:
    if checkdoiacc >= thay:
        dsacc()
        while True:
            try:
                luachon = int(input(f"{vang}Chọn tài khoản mới để chạy: {e}"))
                if 1 <= luachon <= len(chontktiktok["data"]):
                    account_id = chontktiktok["data"][luachon - 1]["id"]
                    checkdoiacc = 0
                    break
                else:
                    print(f"{red}Tài khoản không tồn tại. Hãy nhập lại!{e}")
            except ValueError:
                print(f"{red}Sai định dạng! Vui lòng nhập số.{e}")

    nhanjob = nhannv(account_id)
    if nhanjob["status"] == 200:
        ads_id = nhanjob["data"]["id"]
        link = nhanjob["data"]["link"]
        object_id = nhanjob["data"]["object_id"]

        if nhanjob["data"]["type"] != "follow":
            baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
            continue

        os.system(f"termux-open-url {link}")
        for i in range(loat, -1, -1):
            print(f"Đang đợi {i}s...", end="\r")
            sleep(1)

        nhantien = hoanthanh(ads_id, account_id)
        if nhantien["status"] == 200:
            dem += 1
            tien = nhantien["data"]["prices"]
            tong += tien
            print(f"{luc}{dem}. Nhận: {tien} - Tổng: {tong}{e}")
            checkdoiacc = 0
        else:
            baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
            checkdoiacc += 1
