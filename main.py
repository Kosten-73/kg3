from PIL import Image, ImageTk
import tkinter as tk

# Создаем главное окно
root = tk.Tk()
root.title("Пример работы с холстом")

# Создаем холст
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Рисуем на холсте
canvas.create_rectangle(50, 50, 200, 200, fill="blue")

# Преобразуем холст в изображение
canvas.postscript(file="canvas_image.ps", colormode="color")

# Открываем изображение с использованием Pillow
image = Image.open("canvas_image.ps")

# Получаем цвет пикселя по координатам (x, y)
x, y = 100, 100  # Пример координат
if 0 <= x < 500 and 0 <= y < 500:
    pixel_color = image.getpixel((x, y))
else:
    # Обработка случая, когда координаты (x, y) находятся за пределами изображения
    pixel_color = None  # или другое значение по умолчанию

# Выводим цвет в формате (R, G, B)
print("Цвет пикселя на координатах ({}, {}): {}".format(x, y, pixel_color))

# Запускаем главный цикл
root.mainloop()
