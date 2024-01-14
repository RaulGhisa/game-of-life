import tkinter as tk

HEIGHT = 15
WIDTH = 15


class CAGui(tk.Tk):
    def __init__(self, rows, columns, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=columns * WIDTH + 1, height=rows * HEIGHT + 1, borderwidth=0, highlightthickness=0)
        self.canvas.pack(padx=20, pady=20)
        self.rows = rows
        self.columns = columns
        self.cellwidth = WIDTH
        self.cellheight = HEIGHT

    def draw_state(self, state: list):
        assert len(state) == self.columns

        self.canvas.delete('all')

        self.rect = {}
        self.oval = {}

        for column in range(self.columns):
            for row in range(self.rows):
                x1 = column * self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight

                colour = 'white' if not state[row][column] else 'black'
                self.rect[row, column] = self.canvas.create_rectangle(x1, y1, x2, y2, fill=colour, tags="rect")

        self.update()
