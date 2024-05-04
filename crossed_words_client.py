import sys, socket
import echo_util

HOST = sys.argv[-1] if len(sys.argv) > 1 else '127.0.0.1'
PORT = echo_util.PORT

if __name__ == '__main__':
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))  
        data = echo_util.recv_msg(sock)
        
    except ConnectionError:
        print('Socket error on connection')
        sys.exit(1)

    print('\nConnected to {}:{}'.format(HOST, PORT))
    print("Type word, enter to send, 'q' to quit")

    print(data)

    while True:
        
        msg = input()
        if not msg:
            continue

        if msg == 'q': break
        try:
            echo_util.send_msg(sock, msg) 
            print('Sent message: {}'.format(msg))
            msg = echo_util.recv_msg(sock)
            print(msg)
            if msg == "Corect!":
                break;
        except ConnectionError:
            print('Socket error during communication')
            sock.close()
            print('Closed connection to server\n')
            break

    print("Closing connection")
    sock.close()