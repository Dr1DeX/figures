from FiguresLib.circle import Circle
from FiguresLib.triangle import Triangle
from utils.exceptions import IncorrectParams


def detector(len_figures, params):
    try:
        if len_figures == 0:
            raise IncorrectParams
        if len_figures == 1:
            square_circle = Circle(params)
            return square_circle.calc_area_of_figure()
        elif len_figures == 3:
            triangle = Triangle(params)
            square_triangle = triangle.calc_area_of_figure()
            triangle_type = triangle.print_info_triangle()
            return f'Площадь треугольника: {square_triangle}\nТип треугольника: {triangle_type}'
        else:
            raise IncorrectParams
    except IncorrectParams:
        return 'Введены некорректные параметры'
        # other logic figures....
