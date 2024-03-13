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