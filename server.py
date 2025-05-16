import socket
import sys
import threading


def handle_client(connectionSocket):

    try:
        file = process_request(connectionSocket)
        print(f'file: {file}')
        with open(file, 'r', encoding='utf-8') as f:
            output = f.read().encode()
        
        response = b"HTTP/1.1 200 OK\r\n\r\n" + output
        
    except IOError:
        response = b"HTTP/1.1 404 Not Found\r\n\r\nFile Not Found"
    
    except Exception as e:
        print(f"Error: {e}")

    finally:
        connectionSocket.sendall(response)
        connectionSocket.close()
        
        
    
    


def process_request(connectionSocket):
    try:
        request = connectionSocket.recv(4096).decode()
        file = request.split()[1]
        file = file.lstrip('/')
        return file
    except Exception as e:
        print(f"Error: {e}")
        


def start_server():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Port = 6543
    server_address = '127.0.0.1'
    serverSocket.bind((server_address, Port))
    serverSocket.listen(1)

    print(f'Server is running on port {Port}')
    while True:
        connectionSocket, addr = serverSocket.accept()
        client_thread = threading.Thread(target=handle_client, args=(connectionSocket,))
        client_thread.start()

    serverSocket.close()
    sys.exit()

if __name__ == "__main__":
    start_server()
