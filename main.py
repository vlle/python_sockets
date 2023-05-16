import socket as sck

class Srvr:
    def __init__(self, address: str, host: int) -> None:
        self.server = sck.socket()
        self.address = (address, host)
        self.server.bind(self.address)

    def listen(self):
        self.server.listen()

    def accept_messages(self):
       conn, addr = self.server.accept()
       with conn:
           msg = conn.recv(4096)
           while msg != b'': 
               print(f"msg? {msg}")
               print(f"got connection from {addr}")
               print("sending back")
               if msg == b'':
                   break
               conn.send(msg)
               msg = conn.recv(4096)



def main():
    server = Srvr("127.0.0.1", 2445)
    server.listen()
    while True is True:
        server.accept_messages()

if __name__ == "__main__":
    main()
