from math import pi

from Figures.FiguresLib.BaseFigure import BaseFigure


class Circle(BaseFigure):

    def calc_area_of_figure(self):
        s = pi * self.side_figures[0] ** 2
        return round(s, 2)
