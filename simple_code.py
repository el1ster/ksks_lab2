import tkinter as tk


def clear_display(color):
    canvas.delete("all")
    canvas.configure(bg=color)


def draw_pixel(x, y, color):
    canvas.create_rectangle(x, y, x + 1, y + 1, fill=color, outline=color)


def draw_line(x0, y0, x1, y1, color):
    canvas.create_line(x0, y0, x1, y1, fill=color)


def draw_rectangle(x0, y0, w, h, color):
    canvas.create_rectangle(x0, y0, x0 + w, y0 + h, fill=color, outline=color)


def fill_rectangle(x0, y0, w, h, color):
    canvas.create_rectangle(x0, y0, x0 + w, y0 + h, fill=color, outline=color)


def draw_ellipse(x0, y0, radius_x, radius_y, color):
    canvas.create_oval(x0 - radius_x, y0 - radius_y, x0 + radius_x, y0 + radius_y, fill=color, outline=color)


def fill_ellipse(x0, y0, radius_x, radius_y, color):
    canvas.create_oval(x0 - radius_x, y0 - radius_y, x0 + radius_x, y0 + radius_y, fill=color, outline=color)


def draw_circle(x0, y0, radius, color):
    canvas.create_oval(x0 - radius, y0 - radius, x0 + radius, y0 + radius, fill=color, outline=color)


def fill_circle(x0, y0, radius, color):
    canvas.create_oval(x0 - radius, y0 - radius, x0 + radius, y0 + radius, fill=color, outline=color)


def draw_rounded_rectangle(x0, y0, w, h, radius, color):
    canvas.create_rectangle(x0, y0, x0 + w, y0 + h, fill=color, outline=color)
    canvas.create_arc(x0, y0, x0 + 2 * radius, y0 + 2 * radius, start=90, extent=90, fill=color, outline=color)
    canvas.create_arc(x0 + w - 2 * radius, y0, x0 + w, y0 + 2 * radius, start=0, extent=90, fill=color, outline=color)
    canvas.create_arc(x0, y0 + h - 2 * radius, x0 + 2 * radius, y0 + h, start=180, extent=90, fill=color, outline=color)
    canvas.create_arc(x0 + w - 2 * radius, y0 + h - 2 * radius, x0 + w, y0 + h, start=270, extent=90, fill=color,
                      outline=color)


def fill_rounded_rectangle(x0, y0, w, h, radius, color):
    canvas.create_rectangle(x0, y0, x0 + w, y0 + h, fill=color, outline=color)
    canvas.create_arc(x0, y0, x0 + 2 * radius, y0 + 2 * radius, start=90, extent=90, fill=color, outline=color)
    canvas.create_arc(x0 + w - 2 * radius, y0, x0 + w, y0 + 2 * radius, start=0, extent=90, fill=color, outline=color)
    canvas.create_arc(x0, y0 + h - 2 * radius, x0 + 2 * radius, y0 + h, start=180, extent=90, fill=color, outline=color)
    canvas.create_arc(x0 + w - 2 * radius, y0 + h - 2 * radius, x0 + w, y0 + h, start=270, extent=90, fill=color,
                      outline=color)


def draw_text(x0, y0, color, font_number, length, text):
    font = ("Arial", font_number)
    canvas.create_text(x0, y0, fill=color, font=font, text=text)


def execute_command():
    command = command_entry.get()
    try:
        exec(command)
    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()

    command_entry = tk.Entry(root, width=50)
    command_entry.pack()

    execute_button = tk.Button(root, text="Виконати", command=execute_command)
    execute_button.pack()

    root.mainloop()
