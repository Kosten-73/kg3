# Задание 2. Реализовать рисование отрезка: целочисленным алгоритмом Брезенхема  и алгоритмом ВУ
import tkinter as tk

# Функция, которая будет вызываться при выборе цвета
def choose_color(color):
    canvas.config(bg=color)  # Устанавливаем цвет фона canvas

root = tk.Tk()
root.title("Палитра цветов")

# Создаем палитру цветов
colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown"]

# Создаем кнопки для каждого цвета
for color in colors:
    button = tk.Button(root, text=color, bg=color, width=10, height=2, command=lambda c=color: choose_color(c))
    button.pack(side=tk.LEFT, padx=5, pady=5)

canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

root.mainloop()
