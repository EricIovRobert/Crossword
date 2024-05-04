import echo_util
import random
HOST = echo_util.HOST
PORT = echo_util.PORT


WORD_LIST = ['casa', 'masina', 'telefon', 'tableta', 'laptop']
def choose_word():
	return random.choice(WORD_LIST)

def scramble_word(word):
	return ''.join(random.sample(word,len(word)))


def handle_client(sock, addr, word):
    
    while True:
        try:
            
            msg = echo_util.recv_msg(sock) 
            print('{}: {}'.format(addr, msg))
            if (msg == word):
                 echo_util.send_msg(sock, "Corect!")
                 break
            elif (msg != word):
                 echo_util.send_msg(sock, "Incorect, incearca din nou!")
            
        except (ConnectionError, BrokenPipeError):
            print('Closed connection to {}'.format(addr))
            sock.close()
            break


if __name__ == '__main__':
    listen_sock = echo_util.create_listen_socket(HOST, PORT)
    addr = listen_sock.getsockname()
    print('Listening on {}'.format(addr))
    word = choose_word()
    word1 = scramble_word(word)
    client_sock, addr = listen_sock.accept()
    echo_util.send_msg(client_sock, word1)
    print('Connection from {}'.format(addr))     
    handle_client(client_sock, addr, word)