############################################################
### use this file to implement the server-side in part 2 ###
############################################################

import socket
import xml.etree.ElementTree as ET
import csv

# Load employee dataset from CSV (Assuming 'directory.csv' exists in the same directory)
data = []
try:
    with open('directory.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
except Exception as e:
    print(f"Error reading 'directory.csv': {e}")
    exit(1)

# Create a socket and listen for client connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 65432))
server_socket.listen()
print("Server is running and waiting for client connections...")

while True:
    # Accept incoming client connection
    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    try:
        # Receive the query XML from the client
        query_xml = conn.recv(4096).decode()
        print(f"Received query XML: {query_xml}")  # Debug log

        # Parse the received XML query
        query_tree = ET.fromstring(query_xml)
        conditions = query_tree.findall('condition')

        # Apply the filtering conditions to the dataset
        filtered_data = data
        for condition in conditions:
            column = condition.find('column').text.strip()  # Strip whitespace
            value = condition.find('value').text.strip()   # Strip whitespace
            print(f"Filtering by: {column} = {value}")  # Debug log

            # Ensure column exists and filter
            filtered_data = [row for row in filtered_data if row.get(column) and row[column].strip() == value]
            print(f"Filtered data: {filtered_data}")  # Debug log

        # Create the response XML
        response = ET.Element('result')
        if filtered_data:
            ET.SubElement(response, 'status').text = 'success'
            data_elem = ET.SubElement(response, 'data')
            for row in filtered_data:
                row_elem = ET.SubElement(data_elem, 'row')
                for key, value in row.items():
                    ET.SubElement(row_elem, key.lower()).text = value
        else:
            ET.SubElement(response, 'status').text = 'failure'
            ET.SubElement(response, 'message').text = 'No data found matching the conditions.'

        # Send the response XML to the client
        response_xml = ET.tostring(response, encoding='utf-8')
        conn.send(response_xml)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        conn.close()
