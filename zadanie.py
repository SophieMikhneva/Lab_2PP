import tkinter as tk
from tkinter import messagebox


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Графический редактор")
        # Холст
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack()
        self.last_x, self.last_y = None, None

        self.create_menu()

        # Мышь
        self.canvas.bind("<Button-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        # Меню
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Новый", command=self.new_file)
        file_menu.add_command(label="Выход", command=self.exit_program)
        menu_bar.add_cascade(label="Файл", menu=file_menu)
        self.root.config(menu=menu_bar)

    def on_button_press(self, event):
        # начальные коорд
        self.last_x, self.last_y = event.x, event.y

    def on_mouse_drag(self, event):
        # линия при передвижении мыши
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, width=2, fill="black")
        self.last_x, self.last_y = event.x, event.y

    def new_file(self):
        self.canvas.delete("all")

    def exit_program(self):
        self.root.quit()


def main():
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

