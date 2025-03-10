import socket
import json

# Define the UDP IP address and port to listen on
UDP_IP = "127.0.0.1"
UDP_PORT_READ = 8080
UDP_PORT_WRITE = 8081

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT_READ))

send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)






while True:
    inputData = {
        "thrusters_throttle": [
            {"throttle": 1, "x_dir": 1,"z_dir": 1}
        ],
        "rotator_throttle" : [
            {"x_dir" : 1, "y_dir" : 0}
        ]
    }


    data, addr = sock.recvfrom(4096)
    send_sock.sendto(json.dumps(inputData).encode(), (UDP_IP, UDP_PORT_WRITE))
    print(data.decode())