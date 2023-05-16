import socket as sck
import time

class Client:
    def __init__(self, address: str, port: int) -> None:
        self.address = (address, port)
        self.client = sck.create_connection(self.address)
    
    def send(self, msg: str):
        my_str_as_bytes = str.encode(msg)
        sent = self.client.send(my_str_as_bytes)
        if sent == 0:
            raise RuntimeError("socket connection broken")

    def receive(self, len_msg: int) -> str:
        time.sleep(1)
        amount = 0
        rec = b''
        msgs = []
        while amount < len_msg:
            rec = self.client.recv(4)
            msgs.append(rec)
            amount += len(rec)
        return b''.join(msgs).decode()



def main():
    client = Client("127.0.0.1", 2446)
    message = "educational socket project"
    while 1:
        client.send(message)
        rcv_message = client.receive(len(message))
        print(rcv_message)
        assert message == rcv_message
        time.sleep(0.5)


if __name__ == "__main__":
    main()

