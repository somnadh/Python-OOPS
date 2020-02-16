class A:
    def show(self):
        print("show in A")

class B(A):
    def show1(self):
       pass



s=B()
s.show()