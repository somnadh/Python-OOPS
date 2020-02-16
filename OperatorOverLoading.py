class Demo:
    def addition(self,*somu):
        s=0
        for i in somu:
            s=s+i
        return s


d=Demo()
print(d.addition(6,7,8))
print(d.addition(8.5,7,8))