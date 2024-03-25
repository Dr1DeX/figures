import abc


class Figure(abc.ABC):
    side_figures: list[int] # type hint


    def __init__(self, side_figures) -> None:
        self.side_figures = side_figures
    
    @abc.abstractmethod
    def calc_area_of_figure(self):
        pass
