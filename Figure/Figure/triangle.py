import figure


class Triangle(figure.Figure):
    __type_triangle = ''

    def calc_area_of_figure(self):
        pass

    def __utils_triangle_determinant(self):
        a, b, c = sorted(self.side_figures)
        if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (c*c + b*b == a*a):
            self.__type_triangle = 'Треугольник равнобедренный'
        elif (a*a + b*b < c*c) or (a*a + c*c < b*b) or (c*c + b*b < a*a):
            self.__type_triangle = 'Треугольник тупоугольный'
        else:
            self.__type_triangle = 'Треугольник остроугольный'

    def print_info_triangle(self):
        self.__utils_triangle_determinant()
        return self.__type_triangle