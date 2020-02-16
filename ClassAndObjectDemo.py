class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print(" config of cpu ram",self.cpu,self.ram)

com1=computer(12,85)
com2=computer(87,1000)
com1.config()
com2.config()
