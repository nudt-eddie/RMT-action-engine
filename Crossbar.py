from PHV import PHV
from ALU import ALU

'''
define 
    0000 send container 0 1 to Alu1
    0001 send container 0 1 to Alu2

'''
Alu1 = ALU()
Alu2 = ALU()
class Crossbar:
    def __init__(self,phv,command ='' ):
        self.Phv = phv
        Alu1 = ALU()
        Alu2 = ALU()
        self.ALU = [Alu1,Alu2]
    def run(self,op,fun):
        if(op == "0000011"):
            if fun == '000':
                containers = [self.Phv.containers[0],self.Phv.containers[1]]
                containers = Alu1.operate(op,'000',containers)
                self.Phv.containers[0] = containers[0]
                self.Phv.containers[1] = containers[1]
            elif fun == '011':
                containers = [self.Phv.containers[0],self.Phv.containers[1]]
                containers = Alu1.operate(op,'011',containers)
                self.Phv.containers[0] = containers[0]
                self.Phv.containers[1] = containers[1]
            elif fun == '110':
                containers = [self.Phv.containers[2],self.Phv.containers[3]]
                containers = Alu2.operate(op,'110',containers)
                self.Phv.containers[2] = containers [0]
                self.Phv.containers[3] = containers[1]
            elif fun == '100':
                containers = [self.Phv.containers[2],self.Phv.containers[3]]
                containers = Alu2.operate(op,'100',containers)
                self.Phv.containers[3] = containers[1]
            elif fun == '0100':
                containers = [self.Phv.containers[0]]
                containers = Alu2.operate(op,'0100',containers)
                self.Phv.containers[0] = containers[0]
            elif fun == '0101':
                containers = [self.Phv.containers[0]]
                containers = Alu2.operate(op,'0101',containers)
                self.Phv.containers[0] = containers[0]
            elif fun == '111':
                containers = [self.Phv.containers[0]]
                containers = Alu2.operate(op,'111',containers)
                self.Phv.containers[0] = containers[0]
            else:
                print("无该fun操作，请重新输入！")
        elif(op == "0010011"):
                try:
                    containers = [self.Phv.containers[0]]
                    containers = Alu2.operate(op,fun,containers)
                    self.Phv.containers[0] = containers[0]
                except:
                    print("无该fun操作，请重新输入！")

    def show(self):
        self.Phv.show()


