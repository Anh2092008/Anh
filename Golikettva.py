import os
import time
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

# Sample initialization of chontktiktok (Replace this with real API call or data loading logic)
chontktiktok = {
    "status": 200,
    "data": [
        {"id": 1, "nickname": "Account1"},
        {"id": 2, "nickname": "Account2"},
        {"id": 3, "nickname": "Account3"}
    ]
}

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

# Main logic
def main():
    dsacc()  # Display the accounts initially

    # Variables for account switching and error handling
    checkdoiacc = 0
    doiacc = 3  # Max error attempts before switching account
    dsaccloi = []  # List to store failed accounts
    account_id = None
    luachon = 1  # Default choice for account selection

    while True:
        # Simulate a process that may encounter errors
        if checkdoiacc == doiacc:
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

        # Simulating an action on an account (e.g., fetching job)
        try:
            # For demonstration purposes, simulate receiving a job for the selected account
            account_data = chontktiktok["data"][luachon - 1]
            print(f"Processing job for account: {account_data['nickname']}")

            # Simulate the process of checking job status
            sleep(2)  # Simulate delay for the job process
            print(f"Job completed for account {account_data['nickname']}")

            # After job completion, reset error count
            checkdoiacc = 0

        except Exception as e:
            print(f"An error occurred: {e}")
            checkdoiacc += 1  # Increment error count if something goes wrong

# Running the main logic
main()
