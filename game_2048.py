from builtins import range
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

CELL_VALUE_EMPTY = 0

KEYCODE_LEFT = (37, 65)
KEYCODE_UP = (38, 87)
KEYCODE_RIGHT = (39, 68)
KEYCODE_DOWN = (40, 83)


class Game2048(Frame):
    nowValues = [[CELL_VALUE_EMPTY]*GRID_LENGTH for i in range(GRID_LENGTH)]; # game cell value
    def __init__(self):
        # TODO check frame is valuable
        self.frame = Frame.__init__(self);

        self.grid();
        self.game = self.master;
        # self.master.title('2048')
        # self.master.bind("<Key>", self.key_down)

        self.grid_cells = []
        self.bindEvent_KEY();
        self.init_board()
        self.init_values(2);
        self.mainloop()

    def init_board(self):
        # background를 grid로 구현, color, size 입력
        background = Frame(self, bg=BACKGROUND_COLOR_GAME, width=SIZE_GAME, height=SIZE_GAME)
        background.grid()

        # N*N board에 cell init
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

    def update_grid_cells(self):
        for i in range(GRID_LENGTH):
            for j in range(GRID_LENGTH):
                new_number = self.nowValues[i][j]
                if new_number == CELL_VALUE_EMPTY:
                    self.grid_cells[i][j].configure(text="", bg=BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number), bg=BACKGROUND_COLOR_DICT[new_number],
                                                    fg=CELL_COLOR_DICT[new_number])

    def move(self, inputKey):
        code = inputKey.keycode;
        #test
        ##print('input', inputKey);
        ##print('input', code);


        # TODO cal move value
        ## calMove();
        if(code in KEYCODE_UP) :

            print('up');
        elif(code in KEYCODE_LEFT) :
            print('left');
        elif(code in KEYCODE_RIGHT) :
            print('right');
        elif (code in KEYCODE_DOWN):
            print('down');

        pass;

    def bindEvent_KEY(self):
        self.game.bind("<Up>", self.move);
        self.game.bind("<Down>", self.move);
        self.game.bind("<Left>", self.move);
        self.game.bind("<Right>", self.move);
        self.game.bind("<w>", self.move);
        self.game.bind("<a>", self.move);
        self.game.bind("<d>", self.move);
        self.game.bind("<s>", self.move);
        pass

    def init_values(self, value):
        # default value into 0,0
        self.nowValues[0][0] = value;

        self.update_grid_cells();
        pass;


game = Game2048();
