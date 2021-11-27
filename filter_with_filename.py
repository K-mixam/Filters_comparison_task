from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
rgb_table = np.array(img)
height = len(rgb_table)
width = len(rgb_table[1])
mosaic_size = 10
grayscale_value = 50


def count_average_brightness(_i: int, _j: int, _mosaic_size: int) -> float:
    """
    Считает среднее значение яркости пикселей из области [_i: _i + _mosaic_size, _j: _j + _mosaic_size]
    :param _i: индекс, с которого начинаеется отчет области вычислений по высоте массива
    :param _j: индекс, с которого начинаеется отчет области вычислений по ширине массива
    :param _mosaic_size: размер области вычислений
    :return: среднее значение яркости пикселей из квадрата со стороной _mosaic_size

    >>> count_average_brightness(0, 0, 10)
    0.0
    >>> count_average_brightness(100, 100, 10)
    200.0
    """
    return np.average(rgb_table[_i: _i + mosaic_size, _j: _j + mosaic_size])


def applying_the_filter(_i: int, _j: int, _average_brightness: float, _mosaic_size: int):
    """
    Изменяет пиксели в квадрате [_i: _i + _mosaic_size, _j: _j + _mosaic_size] массива rgb_table
    :param _i: индекс, с которого начинаеется отчет области изменений по высоте массива
    :param _j: индекс, с которого начинаеется отчет области изменений по ширине массива
    :param _average_brightness: среднее значение яркости пикселей
    :param _mosaic_size: размер области изменений
    :return: изменяет пиксели в заданной области массива rgb_table
    """
    rgb_table[_i: _i + mosaic_size, _j: _j + mosaic_size] = \
        int(_average_brightness // grayscale_value) * grayscale_value


for i in range(0, height, mosaic_size):
    for j in range(0, width, mosaic_size):
        applying_the_filter(i, j, count_average_brightness(i, j, mosaic_size), mosaic_size)
res = Image.fromarray(rgb_table)
res.save("res.jpg")
