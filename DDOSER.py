import socket
import time

def read_packet_from_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def send_packet(target_ip, target_port, packet, interval):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(packet.encode())
            print("Packet sent to", target_ip, "on port", target_port)
            s.close()
        except Exception as e:
            print("Error:", e)
        time.sleep(interval)

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    target_port = int(input("Enter target port number: "))
    packet_file = input("Enter packet file name (e.g., pkg.txt): ")
    packet = read_packet_from_file(packet_file)
    interval = 1 / 3  # 3 packets per second
    send_packet(target_ip, target_port, packet, interval)