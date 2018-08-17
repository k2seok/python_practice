from tkinter import *


class Bullet:
    bullet_list = []

    # 총알이 하나 생길때마다 이 list에 하나씩 append 시킬 것이다.
    def __init__(self, x, y, canvas):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.bullet_image = PhotoImage(file="image/bullet.png")
        self.me = self.canvas.create_image(self.x, self.y, image=self.bullet_image)
        Bullet.bullet_list.append(self)

    def move(self):
        self.canvas.move(self.me, 0, -5)
        self.y += -5
        # 윗칸으로 5씩 올라간다.
        if self.y < 10:
            self.canvas.delete(self.me)
            Bullet.bullet_list.remove(self)
        # 남은 칸이 10 이하면 bullet이 사라진다.


class Ship:
    def __init__(self, canvas):
        self.x = 385
        self.y = 560
        self.canvas = canvas
        self.ship_image = PhotoImage(file="image/ship.png")
        self.dx = 0
        # 이동값.. 키가 왼쪽 눌리면 -5 되고 오른쪽 눌리면 +5 되고
        self.me = self.canvas.create_image(self.x, self.y, image=self.ship_image)

    def move_left(self, event):
        self.canvas.move(self.me, -5, 0)
        self.x += -5

    def move_right(self, event):
        self.canvas.move(self.me, 5, 0)
        self.x += 5

    def shot(self, event):
        # print(self.x, self.y)
        Bullet(self.x, 550, self.canvas)

class Enemy():
    moveVal = 5;
    moveWayRight = True;

    def __init__(self, canvas, x, y):
        self.canvas = canvas;
        self.x = x;
        self.y = y;
        self.me = self.canvas.create_image(self.x, self.y, image=PhotoImage(file="image/enermy1.png"))

    def move(self):
        # 600 is maximum width I guess..
        if(self.moveWayRight) :
            # move right
            self.canvas.move(self.me, self.moveVal, 0)
            self.x += self.moveVal;
        else :
            # move left
            self.canvas.move(self.me, - self.moveVal, 0)
            self.x += self.moveVal;

        # 남은 칸이 10 이하면 bullet이 사라진다.
        # dead condition
        #     self.canvas.delete(self.me)
        #     Bullet.bullet_list.remove(self)

class App:
    enemies = [];
    enemyCount = 0;
    enemyArea_minX = 0;
    enemyArea_maxX = 800;
    enemyArea_minY = 0;
    enemyArea_maxY = 200;

    def makeEnemy(self, canvas, cnt):
        self.enemyCount = cnt;

        # TODO for loop make enemy
        #self.enemies.append(Enemy(canvas, 50, 50));

    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width=800, height=600)
        self.canvas.pack()
        self.ship = Ship(self.canvas);
        #self.makeEnemy(self.canvas, 1);

    def bind_event(self):
        self.window.bind('<Left>', self.ship.move_left)
        self.window.bind('<Right>', self.ship.move_right)
        self.window.bind('<space>', self.ship.shot)

    def loop(self):
        # bullet 이동 처리
        for bullet in Bullet.bullet_list:
            bullet.move()

        # enenmy 이동 처리
        # for enemy in self.enemies:
        #     enemy.move();

        self.window.after(10, self.loop)


game = App()
game.bind_event()
game.loop()
game.window.mainloop()
