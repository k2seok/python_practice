# from builtins import range
from tkinter import *;
from random import randrange;

SIZE_GAME = 500  # 초기 사이즈
GRID_LENGTH = 4  # 크기 (N * N)
GRID_PADDING = 10  # 셀 간격

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
BACKGROUND_COLOR_DICT = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563", \
                         32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61", \
                         512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"}
CELL_COLOR_DICT = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2", \
                   32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", 256: "#f9f6f2", \
                   512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"}
FONT = ("Verdana", 40, "bold")

CELL_DEFAULT_VALUE = 2
CELL_VALUE_EMPTY = 0

KEYCODE_LEFT = (37, 65)
KEYCODE_UP = (38, 87)
KEYCODE_RIGHT = (39, 68)
KEYCODE_DOWN = (40, 83)

GAME_LOSE = -1;
GAME_WIN = 1;
GAME_RUNNING = 0;

class Game2048(Frame):
    CELL_MAX_VALUE = CELL_DEFAULT_VALUE;
    nowValues = [[CELL_VALUE_EMPTY] * GRID_LENGTH for i in range(GRID_LENGTH)];  # game cell value

    def start(self):
        self.frame = Frame.__init__(self);
        self.grid();
        self.game = self.master;
        self.master.title('2048')
        self.bindEvent_KEY();

        self.status = GAME_RUNNING;
        self.grid_cells = []
        self.init_board()
        self.init_values(CELL_DEFAULT_VALUE);
        self.mainloop()
        pass;
    # def main(self):
    #     pass;

    def __init__(self):
        self.status = GAME_LOSE;

        self.start();
        # self.window = Tk();
        # self.main = Canvas(self.window, width=SIZE_GAME, height=SIZE_GAME);
        # self.main.create_image(0, 0, image=PhotoImage(file="image/ship.png"))
        # self.main.pack();






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

    def changeMaximum(self, value):
        self.CELL_MAX_VALUE = value if value > self.CELL_MAX_VALUE else self.CELL_MAX_VALUE;
        pass;

    '''action : 1차원배열을 한칸씩 밀면서, merge or move 해준다.'''
    def push(self, arg):
        idx = 0;

        # 1번부터 순서대로 밀어준다.
        for i in range(1, GRID_LENGTH):
            if (arg[i] < 1):
                continue;

            if (arg[idx] > CELL_VALUE_EMPTY):
                # merge
                if (arg[idx] == arg[i]):
                    arg[idx] *= CELL_DEFAULT_VALUE;
                    arg[i] = CELL_VALUE_EMPTY;

                    self.changeMaximum(arg[idx]);
                    idx+=1;
                else:  # move
                    canPush = False;
                    # move direct
                    for j in range(idx + 1, i):
                        if (arg[j] == CELL_VALUE_EMPTY):
                            idx = j;
                            canPush = True;
                            break;
                        pass;
                    if (not canPush):
                        idx += 1;
                    else:
                        arg[idx] = arg[i];
                        arg[i] = CELL_VALUE_EMPTY;
                # idx += 1;
            # 0(Move)
            else:
                arg[idx] = arg[i];
                arg[i] = CELL_VALUE_EMPTY;
        return arg;

    nextValues = [];

    def push_cells(self, isUporDown, isReverse):
        self.nextValues = [[CELL_VALUE_EMPTY] * GRID_LENGTH for i in range(GRID_LENGTH)];
        for i in range(GRID_LENGTH):
            # init
            nextRow = list(self.nowValues[i]);

            # up down 은 i j 변경해서 1차원배열로 변환
            if (isUporDown):
                for j in range(GRID_LENGTH):
                    nextRow[j] = self.nowValues[j][i];

            if (isReverse):
                nextRow.reverse();

            nextRow = self.push(nextRow);

            if (isReverse):
                nextRow.reverse();

            # up down 은 i j 변경해서 1차원배열로 재변환
            if (isUporDown):
                for j in range(GRID_LENGTH):
                    self.nextValues[j][i] = nextRow[j];
            else:
                self.nextValues[i] = nextRow;

        self.nowValues = self.nextValues;


    def move(self, inputKey):
        # # TODO game status 에 따른 move : game 시작전이면 start
        # if(self.status != GAME_RUNNING):
        #     self.start();
        #     print('restart game...')
        #
        #     return;
        #     pass;

        code = inputKey.keycode;
        # test
        ##print('input', inputKey);
        ##print('input', code);

        if (code in KEYCODE_LEFT):
            print('left');
            self.push_cells(isUporDown=False, isReverse=False);
        elif (code in KEYCODE_RIGHT):
            print('right');
            self.push_cells(isUporDown=False, isReverse=True);
        elif (code in KEYCODE_UP):
            print('up');
            self.push_cells(isUporDown=True, isReverse=False);
        elif (code in KEYCODE_DOWN):
            print('down');
            self.push_cells(isUporDown=True, isReverse=True);
        pass

        # TODO need end check : 움직인 후, endcheck(high value win or 칸이 꽉차서 lose)
        self.checkEnd();

        if (self.status != GAME_RUNNING):
            self.end();
            return;

        self.make_new_cell();
        self.update_grid_cells();


    def bindEvent_KEY(self):
        self.game.bind("<Up>", self.move);
        self.game.bind("<Down>", self.move);
        self.game.bind("<Left>", self.move);
        self.game.bind("<Right>", self.move);
        self.game.bind("<w>", self.move);
        self.game.bind("<a>", self.move);
        self.game.bind("<d>", self.move);
        self.game.bind("<s>", self.move);
        pass;

    def init_values(self, value):
        # default value into 0,0
        self.nowValues[0][0] = value;
        self.make_new_cell();

        self.update_grid_cells();
        pass;

    def make_new_cell(self):
        #TODO : Empty cell check & default Value Up
        # self.checkEnd();
        # if(self.status != GAME_RUNNING):
        #     self.end();
        #     return;

        # 확률로 변경 -> 무한 루프 방지, 게임 방향 변경
        # (가끔 움직여도 새 cell이 나타나지 않음)
        for i in range(10):
            pos = [randrange(0, GRID_LENGTH), randrange(0, GRID_LENGTH)];
            if (self.nowValues[pos[0]][pos[1]] == CELL_VALUE_EMPTY):
                self.nowValues[pos[0]][pos[1]] = CELL_DEFAULT_VALUE;
                break;



    def checkEnd(self):
        cnt = 0;
        for i in range(GRID_LENGTH):
            for j in range(GRID_LENGTH):
                if(self.nowValues[i][j] > CELL_VALUE_EMPTY) :
                    cnt+=1;
        if(cnt >= GRID_LENGTH * GRID_LENGTH):
            self.status = GAME_LOSE;
        pass;

    def end(self):
        print('gmae end:' , 'win' if self.status == GAME_WIN else 'lose');
        pass;

game = Game2048();