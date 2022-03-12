import http.server
import urllib.request
import socketserver
import sys

from aiohttp import Payload

if len(sys.argv) < 3:
    print('Usage: python3 mitm.py <port> <payload file>')
    exit(1)
class MaliciousProxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print('[*] Got request for: {}'.format(self.path))
        # Your code will go here
        req = urllib.request.Request(self.path)
        print(req)
        print("test")
        req += Payload
        self.send_response(200)
        self.end_headers()
        self.wfile.write(req)
port = int(sys.argv[1])
server = socketserver.ThreadingTCPServer(('', port), MaliciousProxy)
print("[*] Serving on port {}".format(port))
server.serve_forever()