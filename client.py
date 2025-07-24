""" Client module to connect to the socket Server"""
import ssl
import socket

class SocketClient:
    """Socket client class"""
    def __init__(self, host='127.0.0.1', port=7053):
        self.host = host
        self.port = port
        self.context = ssl._create_unverified_context()
        # Here, AF_INET corresponds to IPv4 (AF_INET6 for IPv6),
        # SOCK_STREAM to TCP (SOCK_DGRAM for UDP)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn = self.context.wrap_socket(self.client_socket, server_hostname='localhost')

    def connect(self):
        """Connection to the defined server"""
        self.conn.connect((self.host, self.port))
        print(f"[*] Connected to server {self.host}:{self.port}")

    def send_message(self, message):
        """Send data to server"""
        self.conn.send(message.encode())
        response = self.conn.recv(1024).decode()
        return response

    def close(self):
        """Close socket connection"""
        self.conn.close()
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
