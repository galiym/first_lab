import math

# Класс, представляющий прямоугольник
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Метод для вычисления периметра прямоугольника
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    # Метод для вычисления площади прямоугольника
    def calculate_area(self):
        return self.width * self.height

    # Метод для вычисления длины диагонали прямоугольника
    def calculate_diagonal_length(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

# Основная программа
if __name__ == "__main__":
    print("Введите ширину прямоугольника:")
    width = float(input())

    print("Введите высоту прямоугольника:")
    height = float(input())

    # Создание объекта прямоугольника
    my_rectangle = Rectangle(width, height)

    # Вычисление и вывод параметров прямоугольника
    print(f"Периметр прямоугольника: {my_rectangle.calculate_perimeter()}")
    print(f"Площадь прямоугольника: {my_rectangle.calculate_area()}")
    print(f"Длина диагонали прямоугольника: {my_rectangle.calculate_diagonal_length()}")
