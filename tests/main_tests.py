import unittest
from src.Figures.FiguresLib.circle import Circle
from src.Figures.FiguresLib.triangle import Triangle


class TestCircle(unittest.TestCase):
    def test_calc_area_of_figure(self):
        corner_case = [
            ([2], 12.57),
        ]

        for params, expected in corner_case:
            with self.subTest(params=params, expected=expected):
                circle_instance = Circle(params)
                actual = circle_instance.calc_area_of_figure()
                self.assertEqual(actual, expected)


class TestTriangle(unittest.TestCase):
    def test_calc_area_of_triangle(self):
        corner_case = [
            ([1, 2, 3], 'Треугольник с заданными параметрами не существует', 'Неизвестный'),
            ([3, 4, 5], 6.0, 'Треугольник прямоугольный'),
            ([5, 5, 6], 15.0, 'Треугольник равнобедренный'),
            ([2, 3, 4], 2.9, 'Треугольник тупоугольный'),
            ([5, 6, 7], 14.7, 'Треугольник остроугольный'),
        ]

        for params, expected, triangle_type in corner_case:
            with self.subTest(params=params, expected=expected, triangle_type=triangle_type):
                triangle_instance = Triangle(params)
                actual = triangle_instance.calc_area_of_figure()
                t_type = triangle_instance.type_triangle
                self.assertEqual(t_type, triangle_type)
                self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
