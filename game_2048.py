from tkinter import *;
from random import *

SIZE_GAME = 500  # 초기 사이즈
GRID_LENGTH = 4  # 크기 (N * N)
GRID_PADDING = 10   # 셀 간격

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
BACKGROUND_COLOR_DICT = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563", \
                         32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61", \
                         512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"}
CELL_COLOR_DICT = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2", \
                   32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", 256: "#f9f6f2", \
                   512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"}
FONT = ("Verdana", 40, "bold")

KEY_UP_ALT = "\'\\uf700\'"
KEY_DOWN_ALT = "\'\\uf701\'"
KEY_LEFT_ALT = "\'\\uf702\'"
KEY_RIGHT_ALT = "\'\\uf703\'"

KEY_UP = "'w'"
KEY_DOWN = "'s'"
KEY_LEFT = "'a'"
KEY_RIGHT = "'d'"


class GameGrid(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        # self.master.title('2048')
        # self.master.bind("<Key>", self.key_down)

        self.grid_cells = []
        self.init_grid()
        # self.init_matrix()
        # self.update_grid_cells()

        self.mainloop()

    def init_grid(self):
        # background를 grid로 구현, color, size 입력
        background = Frame(self, bg=BACKGROUND_COLOR_GAME, width=SIZE_GAME, height=SIZE_GAME)
        background.grid()

        for i in range(GRID_LENGTH):
            grid_row = []
            for j in range(GRID_LENGTH):
                cell = Frame(background, bg=BACKGROUND_COLOR_CELL_EMPTY, width=SIZE_GAME / GRID_LENGTH,
                             height=SIZE_GAME / GRID_LENGTH)
                cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
                # font = Font(size=FONT_SIZE, family=FONT_FAMILY, weight=FONT_WEIGHT)
                t = Label(master=cell, text="", bg=BACKGROUND_COLOR_CELL_EMPTY, justify=CENTER, font=FONT, width=4,
                          height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)


game = GameGrid();
