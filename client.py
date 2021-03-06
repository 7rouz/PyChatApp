# Chat Client Script

import sys
from network.connection import Client

def prompt() :
    sys.stdout.write('<You> ')
    sys.stdout.flush()

#main function
if __name__ == "__main__":

    if(len(sys.argv) < 3) :
        print 'Usage : python telnet.py hostname port'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    client = Client(host, port)

    # Connect client to the server
    client.connect()

    print 'Connected to remote host. Start sending messages'
    prompt()

    s = client.soc 

    while 1:
        socket_list = [sys.stdin, s]

        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = client.get_readable_socket(socket_list)

        for sock in read_sockets:
            #incoming message from remote server
            if sock == s:
                client.receive(sock)
                prompt()

            #user entered a message
            else :
                client.send()
                prompt()
