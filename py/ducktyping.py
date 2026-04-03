class dog:
    def sound(self):
        print("bow bow")

class car:
    def sound(self):
        print("brrrrrrr")

def make_sound(obj):
    obj.sound()

make_sound(dog())
make_sound(car())
