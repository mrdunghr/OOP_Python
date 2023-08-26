from Animal import Animal


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, species="Dog")

    def make_sound(self):
        return "Woof!"
