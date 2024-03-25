from math import pi
from figure import Figure


class Circle(Figure):

    def calc_area_of_figure(self):
        S = pi * self.side_figures ** 2
        return f'Радиус круга: {round(S, 2)}'