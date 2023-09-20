# Задание 3. Выполнить градиентное окрашивание произвольного треугольника,
# у которого все три вершины разного цвета, используя алгоритм растеризации треугольника.

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import math
import tkinter as tk
import sys
from tkinter import colorchooser
from tkinter import Tk, Frame, Button, BOTH, SUNKEN
from tkinter import colorchooser


def start_drawing(event):
    global prev_x, prev_y
    prev_x, prev_y = event.x, event.y


def draw(event):
    global fill1, vertexes
    if len(vertexes) < 3:
        x, y = event.x, event.y
        # color_code = colorchooser.askcolor(title="палитра цветов")
        # fill1 = color_code[1]

        canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill=fill1, outline='white')
        vertexes.append((x, y, fill1))
        # canvas.create_line(prev_x, prev_y, x, y, fill=fill1, width=2)
        # prev_x, prev_y = x, y
    else:
        draw_edges()


def draw_edges():
    global vertexes
    for i in range(-1, 2):
        dot1 = vertexes[i]
        dot2 = vertexes[i + 1]
        canvas.create_line(dot1[0], dot1[1], dot2[0], dot2[1], fill="black", width=1)


def on_button_click():
    global fill1
    (rgb, hx) = colorchooser.askcolor(title="палитра цветов")
    frame.config(bg=hx)
    fill1 = hx
    # return color_code


def choose_color(color):
    canvas.config(bg=color)

def gradient():
    return


root = tk.Tk()
root.title("Заливка серией пикселов")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

fill1 = 'blue'

vertexes = []



# Обработчики событий мыши
# canvas.bind("<Button-1>", start_drawing)  # Нажатие левой кнопки мыши
# canvas.bind("<B1-Motion>", draw)          # Движение мыши с нажатой кнопкой
canvas.bind("<Button-1>", draw)
button = tk.Button(root, text="Поменять текущий цвет", command=on_button_click)
button.pack(anchor="nw", padx=20, pady=30)

# button = tk.Button(root, text="Градиент", command=on_button_click)
# button.pack( padx=20, pady=30)

frame = Frame(border=1, relief=SUNKEN, width=100, height=100)
frame.place(x=30, y=400)
frame.config(bg=fill1)
root.mainloop()

#
#
#
# class Task3(Frame):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.master.title("Задание 3")
#         self.pack(fill=BOTH, expand=1)
#
#
#
#         self.btn = Button(self, text="            ", highlightcolor="blue", command=self.onChoose)
#         self.btn.place(x=20, y=30)
#
#         self.frame = Frame(self, border=1, relief=SUNKEN, width=100, height=100)
#         self.frame.place(x=160, y=30)
#
#     def onChoose(self):
#         (rgb, hx) = colorchooser.askcolor()
#         self.frame.config(bg=hx)
#
#
# def main():
#     root = Tk()
#     ex = Task3()
#     canvas = tk.Canvas(root, width=500, height=500)
#     canvas.pack()
#
#     #root.geometry("300x150+300+300")
#     root.mainloop()
#
#
# if __name__ == '__main__':
#     main()
