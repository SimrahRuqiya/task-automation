############################################################
### use this file to implement the client-side in part 2 ###
############################################################

import socket
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
#client reads xml file

xml=input("Enter XML file name: ")
with open(xml,'r') as f:
    data=f.read()

p = ET.parse(xml)
root=p.getroot()

host_name=socket.gethostname()
port=12345
client_socket=socket.socket()
