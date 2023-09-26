import tkinter as tk
from tkinter import colorchooser

def start_drawing(event):
    global prev_x, prev_y, drawing
    if not drawing:
        prev_x, prev_y = event.x, event.y
        drawing = True
    else:
        x, y = event.x, event.y
        draw_line(prev_x, prev_y, x, y, fill1)
        prev_x, prev_y = x, y
        drawing = False

def draw_line(x1, y1, x2, y2, color):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while x1 != x2 or y1 != y2:
        canvas.create_line(x1, y1, x1 + sx, y1 + sy, fill=color, width=2)
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

def on_button_click():
    global fill1
    color_code = colorchooser.askcolor(title="Палитра цветов")
    fill1 = color_code[1]
    return color_code

root = tk.Tk()
root.title("Рисование линий (алгоритм Брезенхема)")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

fill1 = 'black'
prev_x, prev_y = None, None
drawing = False

# Обработчики событий мыши
canvas.bind("<Button-1>", start_drawing)  # Нажатие левой кнопки мыши
button = tk.Button(root, text="Палитра цветов", command=on_button_click)
button.pack()

root.mainloop()
