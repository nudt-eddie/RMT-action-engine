
from PHV import PHV
from Crossbar import Crossbar

class Action_Engine:
    def __init__(self,phv):
        
        self.Cs_bar = Crossbar(phv)


    def run(self):
        while (True):
            try:
                command = input("*****请输入指令：op fun****"+"\n").split()
                self.Cs_bar.run(command[0],command[1])
                self.Cs_bar.Phv.show()
            except:
                print("****格式输入错误，重新输入！****")
a = ['192.168.0.1','192.168.0.2','3','0']
phv = PHV(a)   
phv.show() 
RMT = Action_Engine(phv)
RMT.run()
