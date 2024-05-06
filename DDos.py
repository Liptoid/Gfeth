import os
def ping_ip(ip_address, count):
    """
    إرسال عدد محدد من طلبات الـ ping إلى عنوان IP معين.
    
    :param ip_address: عنوان IP المستهدف
    :param count: عدد طلبات الـ ping لإرسالها
    """
    # العدد الكلي للطلبات التي تم إرسالها بنجاح
    successful_pings = 0
    
    # إرسال الطلبات الـ ping باستخدام حلقة تكرارية
    for _ in range(count):
        response = os.system(f"ping -c 1 {ip_address}")  # يرسل طلب ping واحد فقط
        if response == 0:
            successful_pings += 1
    
    print(f"تم إرسال {successful_pings} من أصل {count} طلب ping بنجاح إلى {ip_address}")

def main():
    ip_address = "10.10.10.1"  # يمكنك تغيير هذا الرمز إلى العنوان المطلوب
    count = 50000  # عدد طلبات الـ ping المطلوبة
    ping_ip(ip_address, count)

if __name__ == "__main__":
    main()