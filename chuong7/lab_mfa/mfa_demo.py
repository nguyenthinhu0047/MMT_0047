import pyotp
import qrcode
import os

# Sinh secret key
secret = pyotp.random_base32()
print("Secret key:", secret)

# Ghi secret key vào file
with open("secret.txt", "w") as f:
    f.write(secret)

# Tạo URI chuẩn otpauth
totp = pyotp.TOTP(secret)
uri = totp.provisioning_uri(name="nhu@example.com", issuer_name="MyMFAApp")
print("URI:", uri)

# Tạo mã QR
img = qrcode.make(uri)

# Lưu mã QR vào file với xử lý lỗi
output_path = "D:\Ki6\mang may tinh\chuong7\lab_mfa\otp_qr.png"
try:
    img.save(output_path)
    if os.path.exists(output_path):
        print(f"Mã QR đã được lưu vào {output_path}")
    else:
        print("Lỗi: File không được tạo!")
except Exception as e:
    print(f"Lỗi khi lưu file: {e}")
# In mã QR      
img.show()