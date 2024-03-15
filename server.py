# server.py
import socket
from decryption import Decryption
from printing import Printing

class Server:
    def _init_(self, host='localhost', port=12345, print_to_screen=True, print_to_file=False, file_path=None):
        """
        Initialize the Server object.

        :param host: Host address to bind the server socket (default: 'localhost')
        :param port: Port number to bind the server socket (default: 12345)
        :param print_to_screen: Flag to indicate whether to print data to the screen (default: True)
        :param print_to_file: Flag to indicate whether to print data to a file (default: False)
        :param file_path: Path of the file to print data (required if print_to_file is True)
        """
        self.host = host
        self.port = port
        self.print_to_screen = print_to_screen
        self.print_to_file = print_to_file
        self.file_path = file_path

    def receive_data(self):
        """
        Receive data from the client.

        :return: Received data
        """
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(1)
        print("Server is listening...")
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established.")
        data = client_socket.recv(4096)
        return data

    def handle_data(self, data):
        """
        Handle received data.

        :param data: Received data
        """
        decrypted_data = Decryption.decrypt(data)
        if self.print_to_screen:
            Printing.print_to_screen(decrypted_data)
        if self.print_to_file and self.file_path:
            Printing.print_to_file(decrypted_data, self.file_path)

def main():
    """
    Main function to run the server.
    """
    server = Server(print_to_screen=True, print_to_file=True, file_path="received_data.txt")
    data = server.receive_data()
    server.handle_data(data)

if _name_ == "_main_":
    main()


