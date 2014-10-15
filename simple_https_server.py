import BaseHTTPServer, SimpleHTTPServer
import ssl
import sys
from SimpleHTTPServer import SimpleHTTPRequestHandler
import base64

key = ""

class AuthHandler(SimpleHTTPRequestHandler):
    ''' Main class to present webpages and authentication. '''
    def do_HEAD(self):
        print "send header"
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
 
    def do_AUTHHEAD(self):
        print "send header"
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"Test\"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()
 
    def do_GET(self):
        global key
        ''' Present frontpage with user authentication. '''
        if self.headers.getheader('Authorization') == None:
            self.do_AUTHHEAD()
            self.wfile.write('no auth header received')
            pass
        elif self.headers.getheader('Authorization') == 'Basic '+key:
            SimpleHTTPRequestHandler.do_GET(self)
            pass
        else:
            self.do_AUTHHEAD()
            self.wfile.write(self.headers.getheader('Authorization'))
            self.wfile.write('not authenticated')
            pass

if len(sys.argv) < 4:
    print "usage SimpleAuthServer.py [host:port] [username:password] [certfile]"
    sys.exit()

host = sys.argv[1].split(":")[0]
port = int(sys.argv[1].split(":")[1])
key = base64.b64encode(sys.argv[2])
httpd = BaseHTTPServer.HTTPServer((host, port), AuthHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile=sys.argv[3], server_side=True)
httpd.serve_forever()
