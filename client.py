import sys
import socket

debug = 0

def client(eom, message):
    s = socket.socket()

    if debug == 0: print(s)
    host = socket.gethostname()

    if debug == 0: print(host)

    try:
        s.connect((host, 12345))

    except:
        print("Connection failed")

    else:
        msg = str.encode(message)
        s.sendall(msg)

        if eom == "close":
            s.close()
            return

        elif eom == "LF":
            s.send(str.encode("\n"))

        raw = s.recv(len(message))
        result = raw.decode()
        s.close()

        if result == message:
            print("OK")
            return True
        else:
            print("Failed")
            return False

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print("Usage: client message")
    else:
        client(sys.argv[1], sys.argv[2])
