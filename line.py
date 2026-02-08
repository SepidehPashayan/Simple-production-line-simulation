import random

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

            

