import http.server
import socketserver
import urllib.parse
import json

PORT = 8000
AUTH_TOKEN = "9828522814"

class AuthHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)
        token = query.get('token', [None])[0]

        if token != AUTH_TOKEN:
            self.send_response(401)
            self.send_header("Content-type", "text/html")
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b"You are not authenticated")
            return

        self.send_header('Access-Control-Allow-Origin', '*')
        super().do_GET()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        token = data.get('token')

        if token == AUTH_TOKEN:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response = {'status': 'success', 'message': 'Authenticated'}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(401)
            self.send_header("Content-type", "application/json")
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response = {'status': 'failure', 'message': 'Authentication failed'}
            self.wfile.write(json.dumps(response).encode('utf-8'))

with socketserver.TCPServer(("", PORT), AuthHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
