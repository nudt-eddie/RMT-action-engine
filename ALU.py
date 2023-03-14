from argparse import Action
from container import container
import time


class ALU:
    def __init__(self):
        self.state = 0
    def operate(self,op,fun,containers):
        if self.state == 1 :
            time.sleep(2)
        self.state == 1
        if(op == "0000011"):
            if fun == '000':
                print("**********正在交换原地址和目的地址**********")
                time.sleep(1)
                containers[0].data,containers[1].data = containers[1].data,containers[0].data
            if fun == '011':
                print("**********set目的地址**********")
                time.sleep(1)
                containers[1].data = input("***输入修改的目的ip***")
            if fun == '100':
                print("**********正在修改Vlan id**********")
                time.sleep(1)
                containers[1].data = '{}'.format(eval(containers[1].data)+1)
            if fun == '110':
                print("**********正在修改端口号**********")
                time.sleep(1)
                tmp = input("***输入修改的端口***")
                containers[0].data = tmp
            if fun == '0101':
                print("**********load************")
                tmp = input("load contain:")
                if(tmp in containers[0].mem):
                    containers[0].mem.remove(tmp)
                else:
                    print("********mem中不存在该内容*********")
            if fun == "0100":
                print("**********store************")
                tmp = input("store contain:")
                containers[0].mem.append(tmp)
            if fun == "111":
                print("**********丢弃当前报文********")
        if(op == "0010011"):
            if fun == '000':
                print("**********addi********")
                tmp1,tmp2 = map(eval,input("输入两个被操作数" + '\n').split())
                tmp = tmp1 + tmp2
                containers[0].mem.append(tmp)
            if fun == '010':
                print("*********subi*********")
                tmp1,tmp2 = map(eval,input("输入两个被操作数" + '\n').split())
                tmp = tmp1 - tmp2
                containers[0].mem.append(tmp)
            if fun == '100':
                print("*********xori*********")
                tmp1,tmp2 = map(eval,input("输入两个被操作数" + '\n').split())
                tmp = tmp1 ^ tmp2
                containers[0].mem.append(tmp)
            if fun == '110':
                print("*********ori*********")
                tmp1,tmp2 = map(eval,input("输入两个被操作数" + '\n').split())
                tmp = tmp1 or tmp2
                containers[0].mem.append(tmp)
            if fun == '111':
                print("*********andi*********")
                tmp1,tmp2 = map(eval,input("输入两个被操作数" + '\n').split())
                tmp = tmp1 and tmp2
                containers[0].mem.append(tmp)
            if fun == '001':
                print("*********muli*********")     
                tmp1,tmp2 = map(eval,input("输入两个被操作数" + '\n').split())
                tmp = tmp1 * tmp2
                containers[0].mem.append(tmp)                             

        self.state == 0
        return containers

#仿真器中值类似部署了加减和异或同或操作