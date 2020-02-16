class Student:
    def __init__(self,m1,m2):
        print(m1+m2)

    def sum(self,a=None,b=None,c=None):
            s=0
            if(a!=None and b!=None and c!=None):
                s=a+b+c
            elif(a!=None and b!=None):
                s=a+b
            else:
                s=a

            return s

s=Student(14,12)
print(s.sum(12,12,12))
print(s.sum(12.5,12.9))
print(s.sum(1200,15.5,25))
print(s.sum())
print(s.sum("somu  sarat"," kiran"," kumar"))
