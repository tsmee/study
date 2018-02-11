import socket
import threading

HOST = ''
PORT = 2222

def create_connection(conn, addr):
    print('Connected by', addr, ' active clients: ', threading.active_count()-1)
    while 1:
        data = conn.recv(1024)
        txt_data = data.decode("UTF-8").strip()
        print(txt_data)
        if not data:
            break
        elif txt_data.lower() == 'close':
            conn.send('dosvidos \n'.encode())
            break
        else:
            conn.send(data)
    conn.close()
    print("Connection from ", addr, " was closed")
    return

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)


while threading.active_count() < 12:
    conn, addr = s.accept()
    th = threading.Thread(target=create_connection, args=(conn,addr))
    th.start()
