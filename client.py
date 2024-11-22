############################################################
### use this file to implement the client-side in part 2 ###
############################################################

#Names: Leen Abhari, Simrah Shabandri
import socket
import xml.etree.ElementTree as ET
import sys

# Check that the user provided two arguments
if len(sys.argv) != 3:
    print("Usage: python client.py <query_file> <output_file>")
    sys.exit(1)

# Get the input query file and output file from command-line arguments
query_file = sys.argv[1]
output_file = sys.argv[2]

# Read the query from the provided XML file
with open(query_file, 'r') as file:
    query_xml = file.read()

# Create a socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 65432))

# Send the XML query to the server
client_socket.send(query_xml.encode())

# Receive the response from the server
response_xml = client_socket.recv(4096).decode()

# Parse the response XML
response_tree = ET.ElementTree(ET.fromstring(response_xml))
root = response_tree.getroot()

# Print the status of the response
status = root.find('status').text
print(f"Response Status: {status}")

# If the status is success, print the data rows
if status == "success":
    data = root.find('data')
    for row in data.findall('row'):
        name = row.find('name').text
        title = row.find('title').text
        email = row.find('email').text
        print(f"Name: {name}, Title: {title}, Email: {email}")
elif status == "failure":
    message = root.find('message').text
    print(f"Message: {message}")

# Save the response XML to the specified output file
with open(output_file, 'w') as file:
    file.write(response_xml)

# Close the socket connection
client_socket.close()
