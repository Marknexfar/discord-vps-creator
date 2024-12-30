import gdown

# URL file Google Drive
url = "https://drive.google.com/uc?id=1EVZcL9WoWXnfU_vmmn72TAQnwNjA811G"

# Đường dẫn lưu file sau khi tải
output = "/mnt/win10.zip"  # Đổi tên file tùy ý

# Tải file
gdown.download(url, output, quiet=False)

print(f"File đã được tải về và lưu tại: {output}")
