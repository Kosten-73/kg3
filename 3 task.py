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

        canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill=get_rgb(fill1), outline='white')
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

    #print(vertexes[0][2], vertexes[1][2], vertexes[2][2])
    gradient()


def on_button_click():
    global fill1
    (rgb, hx) = colorchooser.askcolor(title="палитра цветов")
    frame.config(bg=hx)
    #fill1 = hx
    #print(hx, rgb, rgb[0], rgb[1], rgb[2])
    # frame.config(bg=hx)
    fill1 = rgb
    # return color_code


def choose_color(color):
    canvas.config(bg=color)


#
# def interpolateColor(c1, c2, alpha):
#     r = int(c1.getRed() * (1 - alpha) + c2.getRed() * alpha)
#     g = int(c1.getGreen() * (1 - alpha) + c2.getGreen() * alpha)
#     b = int(c1.getBlue() * (1 - alpha) + c2.getBlue() * alpha)
#     return (r, g, b)
#
#
# def repaintImage(p1, p2, p3): #BufferedImage image,
#     totalHeight = p3.y - p1.y
#
#     for y in range(p1.y, p2.y + 1):
#         segmentHeight = p2.y - p1.y + 1
#         alpha = float(y - p1.y) / totalHeight
#         beta = float(y - p1.y) / segmentHeight
#
#         x1 = int(p1.x + (p3.x - p1.x) * alpha)
#         x2 = int(p1.x + (p2.x - p1.x) * beta)
#
#         color1 = vertexes[0][2]
#         color2 = vertexes[1][2]
#         color3 = vertexes[2][2]
#
#         colorA = interpolateColor(color1, color3, alpha)
#         colorB = interpolateColor(color1, color2, beta)
#
#         for x in range(x1, x2 + 1):
#             phi = (x1 == x2) ? 1.0f : (float) (x - x1) / (x2 - x1)
#             blendedColor = interpolateColor(colorA, colorB, phi)
#             image.setRGB(x, y, blendedColor.getRGB())
#
#
#
#     for y in range(p2.y + 1, p3.y + 1):
#         segmentHeight = p3.y - p2.y + 1
#         alpha = (float) (y - p1.y) / totalHeight
#         beta = (float) (y - p2.y) / segmentHeight
#
#         x1 = (int) (p1.x + (p3.x - p1.x) * alpha)
#         x2 = (int) (p2.x + (p3.x - p2.x) * beta)
#
#         colorA = interpolateColor(color1, color3, alpha)
#         colorB = interpolateColor(color2, color3, beta)
#
#         for x in range(x1, x2 + 1):
#             phi = (x1 == x2) ? 1.0f : (float) (x - x1) / (x2 - x1)
#             blendedColor = interpolateColor(colorA, colorB, phi)
#             image.setRGB(x, y, blendedColor.getRGB())
def get_rgb(rgb):
    return "#%02x%02x%02x" % rgb
def gradient():
    global vertexes
    x1, y1, c1 = vertexes[0][0], vertexes[0][1], vertexes[0][2]
    x2, y2, c2 = vertexes[1][0], vertexes[1][1], vertexes[1][2]
    x3, y3, c3 = vertexes[2][0], vertexes[2][1], vertexes[2][2]

    xmin = min(x1, x2, x3)
    xmax = max(x1, x2, x3)
    ymin = min(y1, y2, y3)
    ymax = max(y1, y2, y3)

    for x in range(xmin-1, xmax + 1):
        for y in range(ymin-1, ymax+1):
            l1 = float(((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / ((y2 - y3) * (x1 - x3) * (x3 - x2) * (y1 - y3)))
            l2 = float(((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)))
            l3 = 1 - l1 - l2

            flag = True
            l123 = [l1, l2, l3]
            for l in l123:
                if ((0 > l) or (l > 1)):
                    #print("!!!!!!!!!!!!!!!!!!!!", l)
                    flag = False
            if flag:
                # print(c1, type(c1), c1[0], type(c1[0]))
                # print(c2, type(c2), c2[0], type(c2[0]))
                # print(c3, type(c3), c3[0], type(c3[0]))
                # r = int(l1 * int(c1[0]& 0x00FF0000) + l2 * int(c2[0]& 0x00FF0000) + l3 * int(c3[0]& 0x00FF0000))
                # g = int(l1 * int(c1[1]& 0x0000FF00) + l2 * int(c2[1]& 0x0000FF00) + l3 * int(c3[1]& 0x0000FF00))
                # b = int(l1 * int(c1[2]& 0x000000FF) + l2 * int(c2[2]& 0x000000FF) + l3 * int(c3[2]& 0x000000FF))

                r = int(l1 * int(c1[0]) + l2 * int(c2[0]) + l3 * int(c3[0]))
                g = int(l1 * int(c1[1]) + l2 * int(c2[1]) + l3 * int(c3[1]))
                b = int(l1 * int(c1[2]) + l2 * int(c2[2]) + l3 * int(c3[2]))

                # r = l1 * c1 + l2 * (c2) + l3 * (c3)
                # g = l1 * (c1) + l2 * (c2) + l3 * (c3)
                # b = l1 * (c1) + l2 * (c2) + l3 * (c3)
                print(x,y, r,g,b)
                canvas.create_oval(x-1, y-1, x, y, fill="#%02x%02x%02x"%(r,g,b))

    return


root = tk.Tk()
root.title("Заливка серией пикселов")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

fill1 = (0, 255, 0)

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
frame.config(bg=get_rgb(fill1))
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
