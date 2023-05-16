import socket as sck
import select
import time

class Client:
    def __init__(self, address: str, port: int) -> None:
        self.address = (address, port)
        self.client = sck.create_connection(self.address)
        self.client.setblocking(False)
        self.amount = 0

    def select(self):
        potential_readers = [self.client]
        potential_writers = [self.client]
        potential_errs = []
        timeout = 60
        self.ready_to_read, self.ready_to_write, self.in_error = \
               select.select(
                  potential_readers,
                  potential_writers,
                  potential_errs,
                  timeout)
    
    def send(self, msg: str):
        my_str_as_bytes = str.encode(msg)
        if self.client in self.ready_to_write:
            sent = self.client.send(my_str_as_bytes)


    def receive(self, len_msg: int) -> str:
        rec = b''
        self.msgs = []
        if self.client in self.ready_to_read:
            rec = self.client.recv(4096)
            self.msgs.append(rec)
            return b''.join(self.msgs).decode()
        return "None"



def main():
    client = Client("127.0.0.1", 2447)
    message = "educational socket project"
    try:
        while 1:
            client.select()
            client.send(message)
            rcv_message = client.receive(len(message))
            print(rcv_message)
            time.sleep(0.1)
    except KeyboardInterrupt:
        client.client.close()


if __name__ == "__main__":
    main()

