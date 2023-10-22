import tkinter as tk


class DrawingApp:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=800, height=600)
        self.canvas.pack()

        self.command_entry = tk.Entry(master, width=50)
        self.command_entry.pack()

        self.execute_button = tk.Button(master, text="Виконати", command=self.execute_command)
        self.execute_button.pack()

    def clear_display(self, color):
        self.canvas.delete("all")
        self.canvas.configure(bg=color)

    def draw_pixel(self, x, y, color):
        self.canvas.create_rectangle(x, y, x + 1, y + 1, fill=color, outline=color)

    def draw_line(self, x0, y0, x1, y1, color):
        self.canvas.create_line(x0, y0, x1, y1, fill=color)

    def draw_rectangle(self, x0, y0, w, h, color):
        self.canvas.create_rectangle(x0, y0, x0 + w, y0 + h, fill=color, outline=color)

    def fill_rectangle(self, x0, y0, w, h, color):
        self.canvas.create_rectangle(x0, y0, x0 + w, y0 + h, fill=color, outline=color)

    def draw_ellipse(self, x0, y0, radius_x, radius_y, color):
        self.canvas.create_oval(x0 - radius_x, y0 - radius_y, x0 + radius_x, y0 + radius_y, fill=color, outline=color)

    def fill_ellipse(self, x0, y0, radius_x, radius_y, color):
        self.canvas.create_oval(x0 - radius_x, y0 - radius_y, x0 + radius_x, y0 + radius_y, fill=color, outline=color)

    def draw_circle(self, x0, y0, radius, color):
        self.canvas.create_oval(x0 - radius, y0 - radius, x0 + radius, y0 + radius, fill=color, outline=color)

    def fill_circle(self, x0, y0, radius, color):
        self.canvas.create_oval(x0 - radius, y0 - radius, x0 + radius, y0 + radius, fill=color, outline=color)

    def draw_rounded_rectangle(self, x0, y0, w, h, radius, color):
        self.canvas.create_rectangle(x0, y0, x0 + w, y0 + h, fill=color, outline=color)
        self.canvas.create_arc(x0, y0, x0 + 2 * radius, y0 + 2 * radius, start=90, extent=90, fill=color, outline=color)
        self.canvas.create_arc(x0 + w - 2 * radius, y0, x0 + w, y0 + 2 * radius, start=0, extent=90, fill=color,
                               outline=color)
        self.canvas.create_arc(x0, y0 + h - 2 * radius, x0 + 2 * radius, y0 + h, start=180, extent=90, fill=color,
                               outline=color)
        self.canvas.create_arc(x0 + w - 2 * radius, y0 + h - 2 * radius, x0 + w, y0 + h, start=270, extent=90,
                               fill=color, outline=color)

    def fill_rounded_rectangle(self, x0, y0, w, h, radius, color):
        self.canvas.create_rectangle(x0, y0, x0 + w, y0 + h, fill=color, outline=color)
        self.canvas.create_arc(x0, y0, x0 + 2 * radius, y0 + 2 * radius, start=90, extent=90, fill=color, outline=color)
        self.canvas.create_arc(x0 + w - 2 * radius, y0, x0 + w, y0 + 2 * radius, start=0, extent=90, fill=color,
                               outline=color)
        self.canvas.create_arc(x0, y0 + h - 2 * radius, x0 + 2 * radius, y0 + h, start=180, extent=90, fill=color,
                               outline=color)
        self.canvas.create_arc(x0 + w - 2 * radius, y0 + h - 2 * radius, x0 + w, y0 + h, start=270, extent=90,
                               fill=color, outline=color)

    def draw_text(self, x0, y0, color, font_number, length, text):
        font = ("Arial", font_number)
        self.canvas.create_text(x0, y0, fill=color, font=font, text=text)

    def execute_command(self):
        command = self.command_entry.get()
        try:
            exec(command)
        except Exception as e:
            print(f"Помилка: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()