
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class Gabriel(BaseHTTPRequestHandler):
    def _send_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._send_headers()
        self.wfile.write("<html><body><h1>Get hi!</h1></body></html>")

    def do_HEAD(self):
        self._send_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._send_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")


def run(port=80):
    server_address = ('localhost', port)
    httpd = HTTPServer(server_address, Gabriel)
    print '* Starting httpd...'
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()