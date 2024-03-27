# FiguresLib

## Что это такое? ##
Этот модуль считывает данные пользователя и вычисляет радиус круга или треугольника(в дальнейшем будут и другие фигуры).

## Немного гайда ##
Основной модуль запуска имеет следующую структуру:

	params = Commander.parse_command()
    if params:
        print(detector(len(params), params))


Сначала считываются входные параметры, если параметр существует то передаются дальше в функцию-детектор,
где реализована логика определения фигуры и вызова соответствующего метода класса фигуры.


----------



### Использование ###

В консоли прописываем команду:

	python runner.py

Следуем дальнейшим указаниям.