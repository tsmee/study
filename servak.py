import socket
import threading

HOST = ''
PORT = 9999

def create_connection(conn, addr):
    print('Connected by', addr)
    while 1:
        data = conn.recv(1024)
        txt_data = data.decode("UTF-8").strip()
        print(txt_data)
        if not data:
            break
        elif txt_data == 'close':
            conn.send('dosvidos \n'.encode())
            break
        else:
            rev_data = ""
            for i in range(len(txt_data)):
                rev_data += txt_data[-1 - i]
            conn.send((rev_data + '\n').encode())
    conn.close()
    print("Connection from ", addr, " was closed")
    return

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)


while True:
    conn, addr = s.accept()
    th = threading.Thread(target=create_connection, args=(conn,addr))
    th.start()
