class Dog(object):
    def sound(self):
        print("Barking")

class Bird(object):
    def sound(self):
        print("Chirping")


def makeSound(obj):
    obj.sound()

if __name__ == "__main__":
    d = Dog()
    b = Bird()
    makeSound(d)
    makeSound(b)