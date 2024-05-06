from scapy.all import *

def send_pings(ip, count):
    for _ in range(count):
        send(IP(dst=ip)/ICMP(), verbose=False)

target_ip = "192.168.0.169"
ping_count = 5000000

# حلقة تكرارية لإرسال الـ ping
for _ in range(5):  # إرسال 10,000 ping في كل دورة
    send_pings(target_ip, 10000)
