class Human():
    # __private - переменная
    __privateVar = "this is __private variable"

    def __init__(self):
        self.className = "Human class constructor"
        self.__privateVar = "this is redefined __private variable"

    # public - доступен везде
    def showName(self, name):
        self.name = name
        return self.__privateVar + " " + name

    # __private - Доступен только в базовом классе
    def __privateMethod(self):
        return "Private method"

    # _protected - Доступен в классах - наследниках
    def _protectedMethod(self):
        return "Protected method"

    # __private - Доступен ТОЛЬКО из базового класса
    def showPrivate(self):
        return self.__privateMethod()

    def showProtecded(self):
        return self._protectedMethod()


class Male(Human):
    def showClassName(self):
        return "Male"

    def showPrivate(self):
        return self.__privateMethod()

    def showProtected(self):
        return self._protectedMethod()


class Female(Human):
    def showClassName(self):
        return "Female"

    def showPrivate(self):
        return self.__privateMethod()

    def showProtected(self):
        return self._protectedMethod()


h = Human()
print(h.className)
print(h.showName("Vasya"))
print(h.showPrivate())
print(h.showProtecded())
# print(h.privateMethod())
# print(h.protectedMethod())
print("\n")

m = Male()
print(m.className)
print(m.showClassName())
# print(m.showPrivate())
print(m.showProtected())
print("\n")

f = Female()
print(f.className)
print(f.showClassName())
print(f.showProtected())
print("\n")