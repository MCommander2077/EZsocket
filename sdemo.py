from EZsocket import *


def loopobj(conn, addr):
    msg = ezrecv(conn, 1024)
    if not msg:
        conn.close()
        return 0
    print(msg)
    conn.close()
    return 0


if __name__ == '__main__':
    s = startserver('0.0.0.0', 5000, 5)
    mainloop(s, loopobj)
