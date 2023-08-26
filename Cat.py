from Animal import Animal


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, species="Cat")

    def make_sound(self):
        return "Meow!"
