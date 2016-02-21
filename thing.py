import socket
import time

UDP_IP = "198.84.230.106"
UDP_PORT = 26001
MESSAGE = "1"

while True :
    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    print "message:", MESSAGE
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print sock.sendto(bytes(MESSAGE), (UDP_IP, UDP_PORT))
    time.sleep(5)
