from utils.detector_figures import detector
from utils.command_interface import Commander


def main():

    try:
        params = Commander.parse_command()
        if params:
            print(detector(len(params), params))
    except TypeError:
        print('Что то пошло не так...')


if __name__ == '__main__':
    main()
