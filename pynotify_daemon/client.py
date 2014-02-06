import sys
import socket
import json


def doit(host, port, title, msg):
    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server and send data
        sock.connect((host, port))
        data = json.dumps({
            'title': title,
            'msg': msg,
        })
        sock.sendall(data + "\n")
        # received = sock.recv(4096)
    finally:
        sock.close()


def main(argv=sys.argv):
    HOST, PORT = "localhost", 9999
    title = sys.argv[1]
    msg = sys.argv[2]
    doit(HOST, PORT, title, msg)

if __name__ == '__main__':
    main()
