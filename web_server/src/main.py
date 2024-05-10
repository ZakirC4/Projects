import os
import sys
import socket as sock
import time

ABS_DIR_PATH = os.getcwd()
INDEX_HTML_PATH = os.path.join(ABS_DIR_PATH, "web", "index.html")

ADDR = ('localhost', 8080)
HOST, PORT = ADDR

def get_html_content():
    with open(INDEX_HTML_PATH, 'r') as file:
        return file.read()

def send_html_response(conn):
    html_content = get_html_content()
    http_response = f"HTTP/1.1 200 OK Content-Type: text/html {html_content}"
    conn.sendall(http_response.encode())

if not os.path.exists(INDEX_HTML_PATH):
    print("[ERROR] index.html not found")
    sys.exit(1)

last_modified = os.path.getmtime(INDEX_HTML_PATH)
active_connections = []

with sock.socket(sock.AF_INET, sock.SOCK_STREAM) as server:
    server.bind(ADDR)
    server.listen(5)
    print(f"[LISTENING] listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        print(f"[CONNECTED] {addr} connected")

        if os.path.getmtime(INDEX_HTML_PATH) > last_modified:
            print("HTML file updated, reloading content")
            last_modified = os.path.getmtime(INDEX_HTML_PATH)
        
        send_html_response(conn)
        active_connections.append(conn)

        for conn in active_connections:
            try:
                conn.setblocking(False)
                data = conn.recv(1024)
                if not data:
                    print(f"[DISCONNECTED] {conn.getpeername()} disconnected")
                    active_connections.remove(conn)
                    conn.close()
            except BlockingIOError:
                pass
