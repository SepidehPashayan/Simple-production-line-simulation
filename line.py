import random
import time
import threading

inventory = []

inventory_lock = threading.Lock()

class Machine(threading.Thread):
    def __init__(self,name,time,possibility_of_failure,input_piece,output_piece):
        super().__init__()
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
            print(f"machine {self.n} is broken")
            return True
        return False

    def can_start(self):
        if self.check_failure() == False:
            with inventory_lock:
                for y in self.ip:
                    if y not in inventory:
                        return False
                for y in self.ip:
                    inventory.remove(y)
                return True

    def start_working(self):
        if self.can_start():
            self.state = "working"
            print(f"machine {self.n} is working")
            time.sleep(self.t)
            with inventory_lock:
                inventory.append(self.op)
                print(f"machine {self.n} produced {self.op}")
            
            if self.name == "4" and self.op:
                print("The production was completed successfully")

            
m1 = Machine("1", 3, 1, [], "Piece1")
m2 = Machine("2", 4, 3, [], "Piece2")
m3 = Machine("3", 2, 5, ["Piece1", "Piece2"], "Piece3")
m4 = Machine("4", 2, 2, ["Piece3"], "FinalProduct")


m1.start()
m2.start()
m3.start()
m4.start()

m4.join()