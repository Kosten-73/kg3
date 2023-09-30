import tkinter as tk
from tkinter import colorchooser


def start_drawing(event):
    global prev_x, prev_y, drawing
    if not drawing:
        prev_x, prev_y = event.x, event.y
        drawing = True
    else:
        x, y = event.x, event.y
        draw_wu_line(prev_x, prev_y, x, y, fill1)
        prev_x, prev_y = x, y
        drawing = False

def draw_wu_line(x0, y0, x1, y1, color):
    dx = x1 - x0
    dy = y1 - y0

    if abs(dx) > abs(dy):
        if x0 > x1:
            x0, x1, y0, y1 = x1, x0, y1, y0

        gradient = dy / dx
        y = y0 + gradient

        for x in range(x0, x1):
            intensity1 = 1 - (y - int(y))
            intensity2 = y - int(y)
            draw_point(x, int(y), intensity1)
            draw_point(x, int(y) + 1, intensity2)
            y += gradient

    else:
        if y0 > y1:
            y0, y1, x0, x1 = y1, y0, x1, x0

        gradient = dx / dy
        x = x0 + gradient

        for y in range(y0, y1+1):
            intensity1 = 1 - (x - int(x))
            intensity2 = x - int(x)
            draw_point(int(x), y, intensity1)
            draw_point(int(x) + 1, y, intensity2)
            x += gradient

def draw_point(x, y, intensity):
    r = int(fill1[0] * intensity)
    g = int(fill1[1] * intensity)
    b = int(fill1[2] * intensity)
    color_str = "#{:02x}{:02x}{:02x}".format(r, g, b)
    canvas.create_line(x, y, x + 1, y + 1, fill=color_str)

def on_button_click():
    global fill1
    color_code = colorchooser.askcolor(title="Палитра цветов")
    fill1 = color_code[1]

root = tk.Tk()
root.title("Рисование линий (алгоритм У Сяолиня)")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

fill1 = (0, 0, 0)  # Черный цвет (RGB)
prev_x, prev_y = None, None
drawing = False

# Обработчики событий мыши
canvas.bind("<Button-1>", start_drawing)  # Нажатие левой кнопки мыши

button = tk.Button(root, text="Палитра цветов", command=on_button_click)
button.pack()

root.mainloop()
