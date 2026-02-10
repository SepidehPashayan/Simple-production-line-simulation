import random
import time
import threading

inventory = []

inventory_lock = threading.Lock()

production_failed = False
production_lock = threading.Lock()

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
        global production_failed
        x = random.randint(1,100)
        if x in self.list:
            self.state = "broken"
            with production_lock:
                production_failed = True
            print(f"machine {self.n} is broken")
            print("production failed")
            return True
        return False

    def can_start(self):
        if self.state == "broken":
            return False
        with inventory_lock:
            for y in self.ip:
                if y not in inventory:
                    return False
            for y in self.ip:
                inventory.remove(y)
            return True

    def run(self):
        global production_failed
        while True:
            with production_lock:
                if production_failed:
                        break
            if self.can_start():
                if self.check_failure():
                    break
                self.state = "working"
                print(f"machine {self.n} is working")
                time.sleep(self.t)
                with inventory_lock:
                    inventory.append(self.op)
                    print(f"machine {self.n} produced {self.op}")
                
                if self.n == "D" and self.op:
                    print("The production was completed successfully")
                break
            time.sleep(0.1)

            
m1 = Machine("A", 3, 1, [], "Piece1")
m2 = Machine("B", 4, 3, [], "Piece2")
m3 = Machine("C", 2, 5, ["Piece1", "Piece2"], "Piece3")
m4 = Machine("D", 2, 2, ["Piece3"], "FinalProduct")


m1.start()
m2.start()
m3.start()
m4.start()

m1.join()
m2.join()
m3.join()
m4.join()