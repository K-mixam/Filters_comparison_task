
from PIL import Image
import numpy as np
file_name = input("Enter the file name ")
file_name_updated = input("Save as... ")
mosaic_size = int(input("Enter the mosaic size "))
grayscale_value = int(input("Enter the grayscale value "))

img = Image.open(file_name)
rgb_table = np.array(img)
height = len(rgb_table)
width = len(rgb_table[1])


def count_average_brightness(_i: int, _j: int, _mosaic_size: int) -> float:
    return np.average(rgb_table[_i: _i + mosaic_size, _j: _j + mosaic_size])


def applying_the_filter(_i: int, _j: int, _average_brightness: float, _mosaic_size: int):
    rgb_table[_i: _i + mosaic_size, _j: _j + mosaic_size] = \
        int(_average_brightness // grayscale_value) * grayscale_value


for i in range(0, height, mosaic_size):
    for j in range(0, width, mosaic_size):
        applying_the_filter(i, j, count_average_brightness(i, j, mosaic_size), mosaic_size)

res = Image.fromarray(rgb_table)
res.save(file_name_updated)
