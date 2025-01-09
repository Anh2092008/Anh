import requests
import os
import time
from prettytable import PrettyTable

# Màu sắc terminal
colors = {
    "reset": "\033[0m",
    "red": "\033[1;31m",
    "green": "\033[1;32m",
    "yellow": "\033[1;33m",
    "blue": "\033[1;34m",
    "magenta": "\033[1;35m",
    "cyan": "\033[1;36m",
    "white": "\033[1;37m",
}

# Hiển thị banner
def display_banner():
    banner = f"{colors['green']}== TikTok Account Manager ==" + colors['reset']
    os.system("clear")
    print(banner)

# Lấy thông tin từ file hoặc yêu cầu nhập từ người dùng
def get_credentials():
    try:
        with open("Authorization.txt", "r") as f_auth, open("token.txt", "r") as f_token:
            author = f_auth.read().strip()
            token = f_token.read().strip()
    except FileNotFoundError:
        author = input(f"{colors['cyan']}Nhập Authorization: {colors['reset']}")
        token = input(f"{colors['cyan']}Nhập Token: {colors['reset']}")
        with open("Authorization.txt", "w") as f_auth, open("token.txt", "w") as f_token:
            f_auth.write(author)
            f_token.write(token)
    return author, token

# Gửi yêu cầu danh sách tài khoản TikTok
def fetch_accounts(headers):
    url = "https://gateway.golike.net/api/tiktok-account"
    response = requests.get(url, headers=headers)
    return response.json()

# Hiển thị danh sách tài khoản với PrettyTable
def display_accounts(accounts):
    table = PrettyTable()
    table.field_names = ["STT", "Tên Tài Khoản", "ID"]
    for index, acc in enumerate(accounts, start=1):
        table.add_row([index, acc["nickname"], acc["id"]])
    print(table)

# Lấy nhiệm vụ từ API
def fetch_job(headers, account_id):
    url = "https://gateway.golike.net/api/advertising/publishers/tiktok/jobs"
    params = {"account_id": account_id, "data": "null"}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# Hoàn thành nhiệm vụ
def complete_job(headers, ads_id, account_id):
    url = "https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs"
    data = {
        "ads_id": ads_id,
        "account_id": account_id,
        "async": True,
        "data": None,
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Báo lỗi nhiệm vụ
def report_job(headers, ads_id, object_id, account_id, job_type):
    url = "https://gateway.golike.net/api/report/send"
    data = {
        "description": "Tôi đã làm Job này rồi",
        "users_advertising_id": ads_id,
        "type": "ads",
        "provider": "tiktok",
        "fb_id": account_id,
        "error_type": 6,
    }
    requests.post(url, headers=headers, json=data)

    url_skip = "https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs"
    data_skip = {
        "ads_id": ads_id,
        "object_id": object_id,
        "account_id": account_id,
        "type": job_type,
    }
    requests.post(url_skip, headers=headers, json=data_skip)

# Main logic
def main():
    display_banner()
    author, token = get_credentials()
    headers = {
        "Authorization": author,
        "t": token,
        "User-Agent": "Mozilla/5.0",
    }

    accounts = fetch_accounts(headers)
    if accounts.get("status") != 200:
        print(f"{colors['red']}Authorization hoặc Token không hợp lệ!{colors['reset']}")
        return

    accounts_list = accounts["data"]
    display_accounts(accounts_list)

    try:
        choice = int(input(f"{colors['yellow']}Chọn tài khoản để chạy: {colors['reset']}"))
        account_id = accounts_list[choice - 1]["id"]
    except (ValueError, IndexError):
        print(f"{colors['red']}Lựa chọn không hợp lệ!{colors['reset']}")
        return

    delay = int(input(f"{colors['cyan']}Nhập delay (giây): {colors['reset']}"))
    while True:
        job = fetch_job(headers, account_id)
        if job.get("status") == 200:
            ads_id = job["data"]["id"]
            link = job["data"]["link"]
            os.system(f"termux-open-url {link}")
            time.sleep(delay)
            result = complete_job(headers, ads_id, account_id)
            if result.get("status") == 200:
                print(f"{colors['green']}Nhiệm vụ hoàn thành!{colors['reset']}")
            else:
                print(f"{colors['red']}Lỗi khi hoàn thành nhiệm vụ!{colors['reset']}")
        else:
            print(f"{colors['yellow']}Không có nhiệm vụ nào khả dụng!{colors['reset']}")
            time.sleep(10)

if __name__ == "__main__":
    main()
