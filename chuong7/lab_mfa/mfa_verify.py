import pyotp
#đọc secret key từ file     
'''with open("secret.txt", "r") as f:
    secret = f.read().strip()

totp = pyotp.TOTP(secret)
# in mã OTP'''

secret= "OWDSPQRFEXFLVDPGVHLACAI2U43MLRPU"

totp = pyotp.TOTP(secret)
# nhập mât khẩu
paassword = input("Nhập mật khẩu: ")
if paassword != "nhu2624@":
    print("Mật khẩu không đúng!")       
    exit()

# Nhập mã otp
otp_input = input("Nhập mã OTP từ google authenticator: ")
if totp.verify(otp_input):
    print("Xác thực thành công!")
else:   
    print("Xác thực thất bại!")
