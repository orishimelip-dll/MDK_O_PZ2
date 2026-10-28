class Parallelepiped:
    def __init__(self, first=1.0, second=1.0, height=1.0):
        self.first = first
        self.second = second
        self.height = height

    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self, value):
        if value <= 0:
            raise ValueError("Длина не может быть меньше или равна 0")
        self.__first = value

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, value):
        if value <= 0:
            raise ValueError("Ширина не может быть меньше или равна 0")
        self.__second = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Высота не может быть меньше или равна 0")
        self.__height = value

    def read(self):
        print("Ввод данных о параллелепипеде")
        try:
            self.first = float(input("Введите длину: "))
            self.second = float(input("Введите ширину: "))
            self.height = float(input("Введите высоту: "))
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Установлены значения по умолчанию (1.0).")
            self.first = 1.0
            self.second = 1.0
            self.height = 1.0

    def display(self):
        print("\nХарактеристики параллелепипеда")
        print(f"Длина: {self.first}")
        print(f"Ширина: {self.second}")
        print(f"Высота: {self.height}")

    def volume(self):
        return self.first * self.second * self.height

    def surface_area(self):
        return 2 * (self.first * self.second + self.first * self.height + self.second * self.height)


if __name__ == "__main__":
    p = Parallelepiped()
    p.read()
    p.display()
    try:
        print(f"Объем: {p.volume():.2f}")
        print(f"Площадь поверхности: {p.surface_area():.2f}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка при вычислении: {e}")

    print("Проверка валидации (попытка задать отрицательное значение)")
    try:
        p.first = -5
    except ValueError as e:
        print(f"Перехвачено исключение: {e}")