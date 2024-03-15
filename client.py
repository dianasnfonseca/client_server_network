import socket
import pickle

class Client:
    """
    A simple client class for sending data to a server using sockets.
    """

    def __init__(self, host='localhost', port=12345):
        """
        Initializes the Client object with the specified host and port.
        
        Args:
            host (str): The hostname or IP address of the server. Defaults to 'localhost'.
            port (int): The port number on which the server is listening. Defaults to 12345.
        """
        self.host = host
        self.port = port

    def send_data(self, data):
        """
        Sends the provided data to the server.

        Args:
            data: The data to be sent to the server.
        """
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.host, self.port))
        client_socket.send(data)
        client_socket.close()

def main():
    """
    Main function to demonstrate the usage of the Client class.
    """
    client = Client()
    data_dict = {"key": "value"}
    serialized_data = pickle.dumps(data_dict)
    client.send_data(serialized_data)

if __name__ == "__main__":
    main()