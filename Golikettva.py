import requests, os, time
from time import sleep
from prettytable import PrettyTable  # Import PrettyTable

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

# Headers and other functions here...

# Define PrettyTable for displaying account information
def print_accounts_table(data):
    table = PrettyTable()
    table.field_names = ["ID", "Nickname", "Status"]  # Table headers

    for i, account in enumerate(data):
        table.add_row([i + 1, account["nickname"], "Hoạt Động"])  # Add rows with account info

    print(table)

def dsacc():
    if chontktiktok["status"] != 200:
        print(f"{red}Authorization hoặc Token không hợp lệ!{e}")
        quit()

    print_accounts_table(chontktiktok["data"])  # Call the function to display accounts in a table format

dsacc()

# Other parts of the code...

# When checking errors, use PrettyTable to show job progress
def print_job_status(dem, tien, tong):
    table = PrettyTable()
    table.field_names = ["Job #", "Amount Earned", "Total Earned"]  # Table headers
    table.add_row([dem, tien, tong])  # Add job stats as a row

    print(table)

# Running the main task
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
            print_job_status(dem, tien, tong)  # Display the job status in a table
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
