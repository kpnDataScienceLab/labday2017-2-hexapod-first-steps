#!/usr/bin/env python3

import socketserver
import json
import struct
import time
from collections import namedtuple
from binascii import hexlify

RemoteControl=namedtuple('RemoteControl', 'rv rh lv lh b0 b1 b2 b3 b4 b5 b6 b7')

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        data = self.request.recv(1024).strip()
        try:
            command_json = json.loads(data.decode('utf-8'))

            print("{} wrote: {}".format(self.client_address[0], command_json))
            command = RemoteControl(**command_json)
            self.sendToHexapod(command)
            self.request.sendall("OK".encode('utf-8'))
            time.sleep(0.033)
        except Exception as e:
            self.request.sendall(str(e).encode('utf-8'))



        # just send back the same data, but upper-cased


    def sendToHexapod(self, c):
        """ translate RemoteControl into hexapod remote control values packet """

        buttons = int(('{}'*8).format(c.b7, c.b6, c.b5, c.b4, c.b3, c.b2, c.b1, c.b0), 2)
        print(buttons)
        cksum = 255 - ((c.rv + c.rh + c.lv + c.lh + buttons) & 0xFF)
        print(cksum)
        packet = struct.pack('BBBBBBBB',
                0xFF, c.rv, c.rh, c.lv, c.lh, buttons, 0, cksum)

        print("Sending {} to robot".format(hexlify(packet)))
        with open("/dev/ttyUSB0","wb") as _f:
            _f.write(packet)
            _f.flush()


def main():
    HOST, PORT = "0.0.0.0", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

if __name__ == "__main__":
    main()
