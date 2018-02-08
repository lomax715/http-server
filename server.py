import socket

debug = 0

def server():
    """ server side """
    s = socket.socket()
    if debug == 0: print(s)

    host = socket.gethostname()
    if debug == 0: print(host)
    s.bind((host, 12345))

    s.listen(5)

    while True:
        conn, addr = s.accept()
        message = b''

        while True:
            data = conn.recv(1)

            if data == b'':
                break

            if data == b'\n':
                break

        conn.send(message)
        conn.close()

        if (message.decode() == 'q'):
            break

server()
