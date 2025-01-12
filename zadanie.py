import tkinter as tk
class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Графический редактор")
        # Холст
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack()
        self.last_x, self.last_y = None, None
        # Мышь
        self.canvas.bind("<Button-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)

    def on_button_press(self, event):
        #начальные коорд
        self.last_x, self.last_y = event.x, event.y

    def on_mouse_drag(self, event):
        #линия при передвижении мыши
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, width=2, fill="black")
        self.last_x, self.last_y = event.x, event.y


def main():
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
