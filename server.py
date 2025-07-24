""" Server socket module to handle connections from clients"""
import socket
import threading


class ClientHandler(threading.Thread):
    """Handling multiple clients at the same time, and returns responses"""
    def __init__(self, client_socket, address):
        super().__init__()
        self.client_socket = client_socket
        self.address = address

    def run(self):
        print(f"[+] New connection from {self.address}")
        try:
            while True:
                data = self.client_socket.recv(1024).decode()
                if not data:
                    break
                print(f"[{self.address}] {data}")
                self.client_socket.send("Message received.".encode())
        except ConnectionResetError:
            print(f"[-] Connection lost from {self.address}")
        finally:
            self.client_socket.close()
            print(f"[+] Connection closed for {self.address}")


class SocketServer:
    """Handling server side"""
    def __init__(self, host='127.0.0.1', port=7053):
        self.host = host
        self.port = port
        # Here, AF_INET corresponds to IPv4 (AF_INET6 for IPv6),
        # SOCK_STREAM to TCP (SOCK_DGRAM for UDP)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        """Start server"""
        self.server_socket.bind((self.host, self.port))
        # Here, the integer corresponds of the max client queue size for the socket
        self.server_socket.listen(10)
        print(f"[*] Server listening on {self.host}:{self.port}")

        try:
            while True:
                client_sock, addr = self.server_socket.accept()
                handler = ClientHandler(client_sock, addr)
                handler.start()
        except KeyboardInterrupt:
            print("\n[!] Server shutting down...")
        finally:
            self.server_socket.close()


if __name__ == "__main__":
    server = SocketServer()
    server.start()
