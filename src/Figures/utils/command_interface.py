from src.Figures.utils.exceptions import UnknownCommand


class AcceptMethod:
    SquareTriangle = 1
    RadiusCircle = 2


class MsgScriptMethod:
    @staticmethod
    def square_triangle_cmd():
        try:
            msg = 'Введите три стороны для треугольника: '
            print(msg, end='')
            params = list(map(int, input().split()))
            return params
        except ValueError:
            print('Значения должны быть целыми числами')

    @staticmethod
    def radius_circle_cmd():
        try:
            msg = 'Введите радиус окружности: '
            print(msg, end='')
            params = list(map(int, input().split()))
            return params
        except ValueError:
            print('Значения должны быть целыми числами')


class Commander:
    @staticmethod
    def parse_command():
        msg = """
Список доступных методов:

[1] Найти площадь треугольника и определить его тип
[2] Найти радиус круга

З.Ы Других методов пока не завезли, но обещаем честно причестно это исправить!
"""

        print(msg)
        print()
        try:
            cmd = int(input('Ввод команды: '))
            if cmd == AcceptMethod.SquareTriangle:
                return MsgScriptMethod.square_triangle_cmd()
            elif cmd == AcceptMethod.RadiusCircle:
                return MsgScriptMethod.radius_circle_cmd()
            else:
                raise UnknownCommand
        except ValueError:
            print('Ожидалось целое число')
        except UnknownCommand:
            print('Я не знаю такой команды, давай попробуем ещё раз.')
