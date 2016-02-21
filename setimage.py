from PIL import Image
import sys
import socket

file = sys.argv[1]
ip = sys.argv[2]
port = int(sys.argv[3])

print "reading(" + file + ")"
image = Image.open(file)
data = image.getdata()

output = ""
value = 0
for i, bit in enumerate(data):
	value = (value << 1) | bit
	if (i + 1) % 8 == 0:
		output = output + chr(value)
		print str(bit) + ":" + bin(value) + ":" + str(ord(chr(value)))  + ":" + output
		value = 0
	else:		
		print str(bit) + ":" + bin(value)

	
def sendudp(message, ip, port):
	print "UDP target IP:", ip
	print "UDP target port:", port 
	print "message:", message
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print sock.sendto(bytes(message), (ip, port))

sendudp(output,ip,port)
