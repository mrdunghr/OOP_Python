from Cat import Cat
from Dog import Dog


class ManagerAnimal:
    def __init__(self):
        self.animals = []

    def createDog(self, name):
        dog = Dog(name)
        self.animals.append(dog)
        print("Đã tạo thành công 1 con chó với tên của nó là", name)

    def createCat(self, name):
        cat = Cat(name)
        self.animals.append(cat)
        print("Đã tạo thành công 1 con chó với tên của nó là", name)

    def list_animals(self):
        for animal in self.animals:
            print(animal.name)

    def updateAnimal(self, oldName, newName):
        for animal in self.animals:
            if animal.name == oldName:
                animal.name = newName
                print("Đã cập nhập thành công tên của con này: ", newName)

    def deleteAnimal(self, name):
        for animal in self.animals:
            if animal.name == name:
                self.animals.remove(animal)
                print("Đã xóa con này rồi!")
                return
        print("Không tìm thấy con nào như này")
