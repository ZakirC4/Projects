import sys
import socket
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QFileDialog

class FileTransferServer:
    def __init__(self, port):
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', self.port))
        self.connections = []

    def start(self):
        self.server_socket.listen(5)
        print(f"[LISTENING] listening on localhost:{self.port}")
        while True:
            conn, addr = self.server_socket.accept()
            self.connections.append((conn, addr))
            threading.Thread(target=self.handle_client, args=(conn, addr)).start()

    def handle_client(self, conn, addr):
        print(f"[CONNECTED] Client {addr} connected.")
        while True:
            data = conn.recv(5000)
            if not data:
                print(f"[DISCONNECTED] Client {addr} disconnected.")
                conn.close()
                self.connections.remove((conn, addr))
                break
            print(f"[RECEIVED] Received from {addr}")
            with open('received_file.txt', 'wb') as file:
                file.write(data)

    def stop(self):
        for conn, _ in self.connections:
            conn.close()
        self.server_socket.close()

class FileTransferApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('File Sharing')
        self.setGeometry(100, 100, 500, 350)
        self.setFixedSize(500, 350)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Set background color of central widget to black
        self.central_widget.setStyleSheet("background-color: black;")

        layout = QVBoxLayout()

        self.ip_entry = QLineEdit()
        self.ip_entry.setPlaceholderText("ip address")
        self.ip_entry.setStyleSheet("border: 2px solid gray; border-radius: 15px; padding: 10px; width: 200px; color: white;")
        layout.addWidget(self.ip_entry)

        self.file_btn = QPushButton("Choose a File")
        self.file_btn.setStyleSheet("background-color: gray; border: none; border-radius: 20px; padding: 10px 20px; margin-top: 20px;")
        self.file_btn.clicked.connect(self.open_file)
        layout.addWidget(self.file_btn)

        self.send_btn = QPushButton("Send")
        self.send_btn.setStyleSheet("background-color: blue; border: none; border-radius: 20px; padding: 10px 20px; margin-top: 20px;")
        self.send_btn.clicked.connect(self.send_file)
        layout.addWidget(self.send_btn)

        # Add stretch to center the widgets vertically
        layout.addStretch(1)

        # Set layout margin to center the widgets horizontally
        layout.setContentsMargins(150, 0, 150, 0)

        self.central_widget.setLayout(layout)

    def open_file(self):
        global FILE
        filename, _ = QFileDialog.getOpenFileName(None, "Choose a File")
        if filename:
            FILE = filename

    def send_file(self):
        try:
            if FILE:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((self.ip_entry.text(), PORT))
                with open(FILE, 'rb') as file:
                    while True:
                        chunk = file.read(1024)
                        if not chunk:
                            break
                        client_socket.sendall(chunk)
                print("File sent successfully!")
                client_socket.close()
            else:
                print("Please select a file first.")
        except Exception as e:
            print(f"Client Error: {e}")

if __name__ == "__main__":
    FILE = None
    PORT = 50000

    app = QApplication(sys.argv)
    file_transfer_app = FileTransferApp()
    file_transfer_app.show()

    server = FileTransferServer(PORT)
    threading.Thread(target=server.start).start()

    sys.exit(app.exec_())
