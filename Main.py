from ManagerAnimal import ManagerAnimal


def main():
    animal_manager = ManagerAnimal()

    while True:
        print("1. Tạo con chó")
        print("2. Tạo con mèo")
        print("3. Liệt kê thú cưng")
        print("4. Cập nhật tên thú cưng")
        print("5. Xóa thú cưng")
        print("0. Thoát")
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            name = input("Nhập tên cho con chó: ")
            animal_manager.createDog(name)

        elif choice == "2":
            name = input("Nhập tên cho con mèo: ")
            animal_manager.createCat(name)

        elif choice == "3":
            animal_manager.list_animals()

        elif choice == "4":
            old_name = input("Nhập tên hiện tại của thú cưng: ")
            new_name = input("Nhập tên mới của thú cưng: ")
            animal_manager.updateAnimal(old_name, new_name)

        elif choice == "5":
            name = input("Nhập tên thú cưng cần xóa: ")
            animal_manager.deleteAnimal(name)

        elif choice == "0":
            print("Đang thoát khỏi chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lựa chọn hợp lệ.")


if __name__ == "__main__":
    main()
