import socket as sck
import select

class Srvr:
    def __init__(self, address: str, host: int) -> None:
        self.server = sck.socket()
        self.address = (address, host)
        self.server.bind(self.address)
        self.server.setblocking(False)

        self.potential_readers = [self.server]
        self.potential_writers = []
        self.potential_errs = []

    def listen(self):
        self.server.listen()

    def accept_messages(self):
        timeout = 60
        ready_to_read, ready_to_write, in_error = \
               select.select(
                  self.potential_readers,
                  self.potential_writers,
                  self.potential_errs,
                  timeout)
        for sock in ready_to_read:
            if sock is self.server:
                conn, addr = self.server.accept()
                self.potential_readers.append(conn)
            else:
                try:
                    msg = sock.recv(4096)
                    if len(msg) != 0:
                        sock.send(msg)
                    else:
                        sock.close()
                        self.potential_readers.remove(sock)
                except sck.error as e:
                    print(e)
                    self.potential_readers.remove(sock)
                    sock.close()


def main():
    server = Srvr("127.0.0.1", 2447)
    server.listen()
    while True is True:
        server.accept_messages()


if __name__ == "__main__":
    main()
