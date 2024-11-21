############################################################
### use this file to implement the client-side in part 2 ###
############################################################

import socket
import xml.etree.ElementTree as ET
#client reads xml file

xml=input("Enter XML fil: ")

p = ET.parse(xml)
root=p.getroot()

host_name=socket.gethostname()
port=12345
client_socket=socket.socket()
