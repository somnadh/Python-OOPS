class Vehicles():
    def engine(self):
        return "Engine"

    def attribute(self):
        return "Vehicle"


class Helicopter(Vehicles):
    pass


class Submarine(Vehicles):
    pass


class Car(Vehicles):
    pass


v = Vehicles()
print(v.engine())
print(v.attribute())
print("\n")

h = Helicopter()
print(h.engine())
print(h.attribute())
print("\n")

s = Submarine()
print(s.engine())
print(s.attribute())
print("\n")

c = Car()
print(c.engine())
print(c.attribute())
print("\n")