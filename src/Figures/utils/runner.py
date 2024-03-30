from src.Figures.utils.command_interface import Commander
from src.Figures.utils.detector_figures import detector


def runner():

    try:
        params = Commander.parse_command()
        if params:
            print(detector(len(params), params))
    except TypeError:
        print('Что то пошло не так...')

