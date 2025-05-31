import pyshark

# Đường dẫn đến file .pcapng
path= r"D:/Ki6/mạng máy tính/chuong_3/data_nhu_mtien_16a2.pcapng"


# Mở file pcapng
cap = pyshark.FileCapture(path, use_json=True)


# Danh sách lưu thông tin tầng 2 và 3
layer2_3_info = []

for packet in cap:
    try:
        # Lấy thông tin tầng 2 (MAC)
        eth_src = packet.eth.src if hasattr(packet, 'eth') else 'N/A'
        eth_dst = packet.eth.dst if hasattr(packet, 'eth') else 'N/A'
        
        # Lấy thông tin tầng 3 (IP)
        ip_src = packet.ip.src if hasattr(packet, 'ip') else 'N/A'
        ip_dst = packet.ip.dst if hasattr(packet, 'ip') else 'N/A'

        layer2_3_info.append({
            'eth_src': eth_src,
            'eth_dst': eth_dst,
            'ip_src': ip_src,
            'ip_dst': ip_dst
        })
    except AttributeError:
        continue

cap.close()

# In ra 10 dòng đầu tiên
for i, info in enumerate(layer2_3_info[:10], start=1):
    print(f"Gói {i}:")
    print(f"  MAC nguồn: {info['eth_src']}")
    print(f"  MAC đích:  {info['eth_dst']}")
    print(f"  IP nguồn:  {info['ip_src']}")
    print(f"  IP đích:   {info['ip_dst']}\n")


