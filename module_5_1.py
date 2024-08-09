# 1. Создайте класс House.
class House:

    # 2.Внутри класса House определите метод __init__, в который передадите название и кол-во этажей.
    def __init__(self, name, number_of_floors):

        # 3. Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
        self.name = name
        self.number_of_floors = number_of_floors

    # 4. Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
    def go_to(self, new_floor):

        # Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
        # Если же new_floor больше чем self.number_of_floors или меньше 1,
        # то вывести строку "Такого этажа не существует".
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            print('-'.join([str(num) for num in range(1, new_floor+1)]))


# 5. Создайте объект класса House с произвольным названием и количеством этажей.
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# 6. Вызовите метод go_to у этого объекта с произвольным числом.
h1.go_to(5)
h2.go_to(10)


