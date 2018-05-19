##bot test
import socket
from getkeys import key_check

class bot_control:

    def __init__(self):
        self.pos = [0,0,0]
        self.deltaPos = [0,0,0]
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect(("localhost",25005))
        self.transmit()
        print("CONNECTED TO BOT")
    def transmit(self):
        sent = ",".join(map(str,self.deltaPos))
        self.s.sendall(sent.encode("utf-8"))
        returned= self.s.recv(1024).decode("utf-8")
        self.deltaPos = [0,0,0]
        if returned == sent:
            return "Everything is fine"
        else:
            return "not good"

    def left(self, step=0.1):
        self.deltaPos[2] -= step
        self.transmit()

    def right(self, step=0.1):
        self.deltaPos[2] += step
        self.transmit()

    def hit(self, force=1):
        self.deltaPos[0] -= force
        self.transmit()
        self.deltaPos[0] += force
        time.sleep(0.3)
        self.transmit()

    def destroy(self):
        self.s.close()

if __name__ == "__main__":
    try:
        import time
        b1 = bot_control()
        lastKeys = []
        while True:
            keys = key_check()
            if "A" in keys:
                b1.left(1)
            elif "D" in keys:
                b1.right(1)
            elif "W" in keys:
                b1.hit()
            time.sleep(0.1)
            lastKeys = keys
    finally:
        b1.destroy()
