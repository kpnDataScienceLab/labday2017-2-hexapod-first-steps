#!/usr/bin/env python3

import time
from http.server import BaseHTTPRequestHandler, HTTPServer

import serportserver

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself

        try:
            command=serportserver.bytesToRc(post_data)
            serportserver.sendToHexapod(command)
            self.send_response(200)
            time.sleep(0.033)
            self.wfile.write(bytes("OK", "utf8"))
        except Exception as e:
            self.send_response(500)
            self.wfile.write("exception: {}".format(e).encode("utf8"))



def run():
      print('starting server...')

      # Server settings
      # Choose port 8080, for port 80, which is normally used for a http server, you need root access
      server_address = ('0.0.0.0', 9100)
      httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
      print('running server...')
      httpd.serve_forever()


if __name__ == '__main__':
    run()

# vim:ts=4:expandtab
