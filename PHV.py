from container import container
class PHV:
    def __init__(self,list1):
        self.containers = [] 
        container1 = container(list1[0])
        container2 = container(list1[1])
        container3 = container(list1[2])
        container4 = container(list1[3])
        self.containers.append(container1)
        self.containers.append(container2)
        self.containers.append(container3)
        self.containers.append(container4)

    def show(self):
        print("原ip："+ self.containers[0].data)
        print("目的ip："+ self.containers[1].data)
        print("端口号："+ self.containers[2].data)
        print("Vlan Id："+ self.containers[3].data)
        print("mem contain:" + str(self.containers[0].mem))


#初步定义  container1  原ip  container2   目的ip     container3  端口号      container4   vlan id