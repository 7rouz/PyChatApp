# this file containes the connection handlers for client and server
import socket, select, string, sys


class Client:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.settimeout(2)

    def connect(self):
        try :
            self.soc.connect((self.server_ip, self.server_port))
        except :
            # TODO change all these prints to logs 
            print ("[Client] Unable to connect")
            sys.exit()

    def get_readable_socket(self, socket_list):
        return select.select(socket_list, [], [])

    def receive (self, sock):
        data = sock.recv(4096)
        if not data:
            print '\nDisconnected from chat server'
            sys.exit()
        else:
            # print data
            sys.stdout.write(data)

    def send (self):
        msg = sys.stdin.readline()
        client.soc.send(msg)