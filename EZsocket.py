import socket
import threading


def startserver(ip, port, max_connections):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(max_connections)
    print(f'[info]server is start as {ip}:{port},max connections is {max_connections}')
    return s


def mainloop(server_object, conn_object):
    # server_object is too fxxkin long!
    so = server_object
    print(f'[info]server is looping')
    while True:
        conn, addr = so.accept()
        with conn:
            print(f'[info]Connected by {addr[0]}:{addr[1]}')
            try:
                conn_object(conn, addr)
            except Exception as e:
                print(f'[warn]Connection {addr[0]}:{addr[1]} Exception detected.')
                print(f'[warn]Exception:{e}')
            print(f'[info]{addr[0]}:{addr[1]} is Disconnected')

def ezrecv(conn,byteslong=1024):
    return conn.recv(byteslong).decode()
