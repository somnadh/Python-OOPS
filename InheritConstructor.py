class Ishitha:

    def __init__(self):
        print("parent Constructor invoked")

    def Ishu_method(self):
        print("Ishitha's First Method")


class Somnadh(Ishitha):

    def __init__(self):
        super().__init__()
        print("child Constructor invoked")

    def feature(self):
        super().Ishu_method()



obj=Somnadh()
obj.feature()