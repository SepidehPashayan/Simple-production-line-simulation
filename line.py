import random
import time

class Machine:
    def __init__(self,name,time,possibility_of_failure,input_piece,output_piece):
        self.state = "idle"
        self.n = name
        self.t = time
        self.pf = possibility_of_failure
        self.ip = input_piece
        self.op = output_piece

        self.list = [i+1 for i in range(self.pf)]

    def check_failure(self):
        x = random.randint(1,100)
        if x in self.list:
            self.state = "broken"

    def can_start(self):
        while True:
            if self.state == "idle":
                if self.ip in self.IO:
                    break
        time.sleep(1)

    def start_working(self):
        self.state = "working"
        self.IO.append(self.op)
        time.sleep(self.t)

            

