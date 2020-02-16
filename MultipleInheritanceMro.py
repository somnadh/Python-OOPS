class Ishitha:
    def __init__(self):
        print("parent Constructor invoked")
    def Ishu_method(self):
        print("Ishitha's First Method")
class Somnadh:
    def __init__(self):
        super().__init__()
        print("child Constructor invoked")
    def Ishu_method(self):
        super().Ishu_method()
        print("somu's First Method")
class Arya(Somnadh,Ishitha):#mro==> left to right it will go
    def __init__(self):
        super().__init__()
        print(" Arya Constructor invoked")
    def feature(self):
        super().Ishu_method()
obj=Arya()
obj.feature()