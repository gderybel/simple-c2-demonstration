""" Client module to connect to the socket Server"""
import socket

class SocketClient:
    """Socket client class"""
    def __init__(self, host='127.0.0.1', port=7053):
        self.host = host
        self.port = port
        # Here, AF_INET corresponds to IPv4 (AF_INET6 for IPv6),
        # SOCK_STREAM to TCP (SOCK_DGRAM for UDP)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """Connection to the defined server"""
        self.client_socket.connect((self.host, self.port))
        print(f"[*] Connected to server {self.host}:{self.port}")

    def send_message(self, message):
        """Send data to server"""
        self.client_socket.send(message.encode())
        response = self.client_socket.recv(1024).decode()
        return response

    def close(self):
        """Close socket connection"""
        self.client_socket.close()
        print("[*] Connection closed")


if __name__ == "__main__":
    client = SocketClient()
    client.connect()

    try:
        msg = 'my-encryption-key'
        reply = client.send_message(msg)
        print("Server:", reply)
    finally:
        client.close()
