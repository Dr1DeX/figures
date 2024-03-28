import math

from Figures.FiguresLib.BaseFigure import BaseFigure


class Triangle(BaseFigure):
    type_triangle = 'Неизвестный'

    def calc_area_of_figure(self):
        return self.__utils_triangle_determinant()

    def print_info_triangle(self):
        return self.type_triangle

    def __utils_right_triangle(self, a, b):
        return 0.5 * a * b

    def __utils_isosceles_triangle(self, a, b, c):
        h = math.sqrt(c ** 2 - ((a - b) ** 2) / 4)
        return round(0.5 * b * h, 2)

    def __utils_geron_triangle(self, a, b, c):
        # Formula Heron
        s = (a + b + c) / 2
        return round(math.sqrt(s * (s - a) * (s - b) * (s - c)), 2)

    def __utils_triangle_determinant(self):
        a, b, c = sorted(self.side_figures)
        if a + b <= c or a + c <= b or b + c <= a:
            return 'Треугольник с заданными параметрами не существует'
        elif a ** 2 + b ** 2 == c ** 2:
            self.type_triangle = 'Треугольник прямоугольный'
            return self.__utils_right_triangle(a, b)
        elif a == b or a == c or b == c:
            self.type_triangle = 'Треугольник равнобедренный'
            return self.__utils_isosceles_triangle(a, b, c)
        elif (a ** 2 + b ** 2 < c ** 2) or (a ** 2 + c ** 2 < b ** 2) or \
                (c ** 2 + b ** 2 < a ** 2):
            self.type_triangle = 'Треугольник тупоугольный'
            return self.__utils_geron_triangle(a, b, c)
        else:
            self.type_triangle = 'Треугольник остроугольный'
            return self.__utils_geron_triangle(a, b, c)
