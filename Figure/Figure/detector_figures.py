from circle import Circle
from triangle import Triangle

def detector(len_figures, params):
    if len_figures == 0:
        raise TypeError('Введены некорректные параметры')
    if len_figures == 1:
        square_circle = Circle(*params)
        return square_circle.calc_area_of_figure()
    elif len_figures <= 3:
        square_triangle = Triangle(params)
        return square_triangle.print_info_triangle()
    else:
        return 'Других фигур пока не завезли, но обещаем честно причестно это исправить!'
        
    # other logic figures....
