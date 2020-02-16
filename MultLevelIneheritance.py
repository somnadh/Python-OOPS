class Ishitha:
    def Ishu_method(self):
        print("Ishitha's First Method")
    def Ishu_method2(self):
        print("Ishitha's Second Method")
    def Ishu_method3(self):
        print("Ishitha's Third Method")


class Somnadh:
    def Somnadh_method(self):
        print("somu's First Method")
    def Somnadh_method2(self):
        print("somu's Second Method")
    def Somnadh_method3(self):
        print("somu's Third Method")

class Arya(Somnadh,Ishitha):
    def Arya_method(self):
        print("Arya's First Method")
    def Arya_method2(self):
        print("Arya's Second Method")
    def Arya_method3(self):
        print("Arya's Third Method")

obj=Arya()
obj.Ishu_method()
obj.Ishu_method2()
obj.Ishu_method3()
obj.Somnadh_method()
obj.Somnadh_method2()
obj.Somnadh_method3()
obj.Arya_method()
obj.Arya_method2()
obj.Arya_method3()