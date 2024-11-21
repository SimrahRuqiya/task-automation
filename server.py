############################################################
### use this file to implement the server-side in part 2 ###
############################################################

import socket

host_name=socket.gethostname()
port=12345
server_socket=socket.socket()
server_socket.bind(host_name,port)
server_socket.listen()
