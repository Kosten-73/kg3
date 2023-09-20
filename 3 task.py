# Задание 3. Выполнить градиентное окрашивание произвольного треугольника,
# у которого все три вершины разного цвета, используя алгоритм растеризации треугольника.

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import math
import tkinter as tk
from tkinter import *

# importing the choosecolor package
from tkinter import colorchooser


def start_drawing(event):
    global prev_x, prev_y
    prev_x, prev_y = event.x, event.y


def draw(event):
    global prev_x, prev_y
    x, y = event.x, event.y
    canvas.create_line(prev_x, prev_y, x, y, fill="black", width=2)
    prev_x, prev_y = x, y

# Function that will be invoked when the
# button will be clicked in the main window
def choose_color():
    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title="Choose color")
    return color_code


root = Tk()
button = Button(root, text="Select color",
                command=choose_color)
button.pack()
root.geometry("600x600")
#root.mainloop()

#root = tk.Tk()
root.title("Заливка серией пикселов")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Обработчики событий мыши
canvas.bind("<Button-1>", start_drawing)  # Нажатие левой кнопки мыши
canvas.bind("<B1-Motion>", draw)          # Движение мыши с нажатой кнопкой
# canvas.Button()
root.mainloop()
