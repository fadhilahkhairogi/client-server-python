import socket
import sys
#ini komen

def parse_input():
    try:
        server_host = sys.argv[1] 
        server_port = int(sys.argv[2])
        filename = sys.argv[3]

        return server_host,server_port,filename
    except Exception as e:
        print(f"Error: {e}")

def start_client():
    
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_host,server_port,filename =  parse_input()
        server_address = (server_host, server_port)
        print("Menghubungkan ke server...")
        client_socket.connect(server_address)

        request = f"GET {filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
        client_socket.send(request.encode())


        client_socket.send(request.encode('utf-8'))
        response = ''
        data = client_socket.recv(4096)
        if data:
            response += data.decode('utf-8', errors='ignore')
        print(f"Balasan dari server: {response}")

        print(response)
        client_socket.close()


    finally:
        client_socket.close()
        print("Connection to server closed")

if __name__ == "__main__":
    start_client()
