# Задание 1. Заливка и выделение границы.
#
# 1а) Рекурсивный алгоритм заливки на основе серий пикселов (линий) заданным цветом.
#
# 1б) Рекурсивный алгоритм заливки на основе серий пикселов (линий) рисунком из графического файла.
# Файл можно загрузить встроенными средствами и затем считывать точки изображения для использования в заливке.
# Рассмотреть случаи когда файл небольшого размера и заливается циклически и когда большой.
# Масштабировать не нужно.  Область рисуется мышкой. Область произвольной формы. Внутри могут быть отверстия.
# Точка, с которой начинается заливка, задается щелчком мыши.
#
# 1в) Выделение границы связной области. На вход подается изображение.
# Граница связной области задается одним цветом.
# Имея начальную точку границы организовать ее обход, занося точки в список в порядке обхода.
# Начальную точку границы можно получать любым способом.
# Для контроля полученную границу прорисовать поверх исходного изображения.
# import tkinter as tk
# from tkinter import ttk
# import matplotlib.pyplot as plt
# import math
# import sys
# from tkinter import colorchooser
# def start_drawing(event):
#     global prev_x, prev_y
#     prev_x, prev_y = event.x, event.y
#
#
# def draw(event):
#     global prev_x, prev_y
#     x, y = event.x, event.y
#     canvas.create_line(prev_x, prev_y, x, y, fill=fill1, width=2)
#     prev_x, prev_y = x, y
#
# def pour(event):
#     global prev_x, prev_y
#     x, y = event.x, event.y
#     print(x, y)
#
# def on_button_click():
#     global fill1
#     color_code = colorchooser.askcolor(title="палитра цветов")
#     fill1 = color_code[1]
#     return color_code
#
# root = tk.Tk()
# root.title("Заливка серией пикселов")
#
# canvas = tk.Canvas(root, width=500, height=500)
# canvas.pack()
#
# fill1 = 'black'
#
# # Обработчики событий мыши
# canvas.bind("<Button-1>", start_drawing)  # Нажатие левой кнопки мыши
# canvas.bind("<B1-Motion>", draw)          # Движение мыши с нажатой кнопкой
# button = tk.Button(root, text="палитра цветов", command=on_button_click)
# button.pack()
# button1 = tk.Button(root, text="залить", command=pour)
# button1.pack()
# root.mainloop()
import tkinter as tk
from tkinter import colorchooser
import tkinter as tk
from tkinter import PhotoImage
def start_drawing(event):
    global prev_x, prev_y
    prev_x, prev_y = event.x, event.y

def draw(event):
    global prev_x, prev_y
    x, y = event.x, event.y
    canvas.create(prev_x, prev_y, x, y, fill=fill1, width=2)
    # Обновляем цвет пикселей в массиве
    for i in range(prev_x, x + 1):
        for j in range(prev_y, y + 1):
            if 0 <= i < 500 and 0 <= j < 500:  # Убедитесь, что координаты в пределах холста
                pixel_colors[j][i] = fill1  # Устанавливаем цвет пикселя

    prev_x, prev_y = x, y

def pour(event):
    x, y = event.x, event.y
    color = pixel_colors[y][x]
    fill_area(x, y, color)

def fill_area(x, y, color):
    global prev_x, prev_y

    canvas.create_line(prev_x, prev_y, x, y, fill=fill1, width=2)

    if (0 <= x < 500 & 0 <= y < height & color != fill1):
        pixel_colors[x][y] = fill1
        color = pixel_colors[y][x]
        fill_area(x + 1, y, color)
        fill_area(x - 1, y, color)
        fill_area(x, y + 1, color)
        fill_area(x, y - 1, color)
    prev_x, prev_y = x, y
def on_button_click():
    global fill1
    color_code = colorchooser.askcolor(title="палитра цветов")
    fill1 = color_code[1]
    return color_code



root = tk.Tk()
root.title("Заливка серией пикселов")
width = 500
height = 500
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

fill1 = 'black'
pixel_colors = [['white' for _ in range(500)] for _ in range(500)]
# Обработчики событий мыши
canvas.bind("<Button-1>", start_drawing)  # Нажатие левой кнопки мыши
canvas.bind("<B1-Motion>", draw)          # Движение мыши с нажатой кнопкой

button = tk.Button(root, text="палитра цветов", command=on_button_click)
button.pack()

button1 = tk.Button(root, text="заливка", command=lambda: canvas.bind("<Button-1>", pour))
button1.pack()

root.mainloop()
