# server.py
import socket
import pickle
import json
import xml.etree.ElementTree as ET

class Server:
    def _init_(self, host='localhost', port=12345):
        self.host = host
        self.port = port

    def receive_data(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(1)
        print("Server is listening...")
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established.")
        data = client_socket.recv(4096)
        return data

    def handle_data(self, data):
        # Handle received data
        # Implement decryption if applicable
        # Implement serialization format based on the user's choice
        pass

def main():
    server = Server()
    data = server.receive_data()
    server.handle_data(data)

if __name__ == "__main__":
    main()


# client.py
import socket
import pickle

class Client:
    def _init_(self, host='localhost', port=12345):
        self.host = host
        self.port = port

    def send_data(self, data):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.host, self.port))
        client_socket.send(data)
        client_socket.close()

def main():
    client = Client()
    data_dict = {"key": "value"}
    serialized_data = pickle.dumps(data_dict)
    client.send_data(serialized_data)

if __name__ == "__main__":
    main()

# For handling encryption and other functionalities, you can add appropriate functions/classes.
# Write unit tests to test various functionalities.