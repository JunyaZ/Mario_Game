import pyglet
from pyglet.window import  key
from GameObject import GameObject
from BackgroundObject import BackgroundObject
from enemies import Enemies
import os
import random


ememies_list=[]

class GameWindow(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(400, 100)
        self.frame_rate = 1/60.0
        self.player = GameObject( posx = 200, posy = 40 ,image = "Mario_Super.png")
        self.background = BackgroundObject(posx = 0, posy = 0, image = "background_3.jpg")

        self.enemie1 = Enemies(posx=random.randint(0, 300), posy=40, velx=random.randint(10, 30), vely=0,
                               image="goomba_1.png")
        self.enemie2 = Enemies(posx=random.randint(0, 300), posy=40, velx=random.randint(-30, -10), vely=0,
                               image="goomba_1.png")
        ememies_list.append(self.enemie1)
        ememies_list.append(self.enemie2)

        #self.background = BackgroundObject(posx=0, posy=0, image='background_0.jpg')
        #self.brick = BackgroundObject(posx=0, posy=0, image='brick.png')

        self.toggle = False
        self.score = pyglet.text.Label('Score : 0',
                                  font_name='Times New Roman',
                                  font_size=36,
                                  x=100, y=550,
                                  anchor_x='center', anchor_y='center')


    def on_key_press(self, symbol, modifiers):
        if symbol == key.RIGHT:
            self.player.velx = 25
            self.background.velx = -25
            self.player.imageIndex = 0
            if(self.player.state == 0):
                self.player.imageList = self.player.image_list_walk
            elif(self.player.state == 1):
                self.player.imageList = self.player.image_list_swim
            elif(self.player.state == 2):
                self.player.imageList = self.player.image_list_dash
            elif (self.player.state == 3):
                self.player.imageList = self.player.image_list_jump
            else:
                self.player.imageList = self.player.image_list_walk
        if symbol == key.LEFT:
            self.player.velx = -25
            self.background.velx = 25
            self.player.imageIndex = 1
            if(self.player.state == 0):
                self.player.imageList = self.player.image_list_walk
            elif(self.player.state == 1):
                self.player.imageList = self.player.image_list_swim
            elif (self.player.state == 2):
                self.player.imageList = self.player.image_list_dash
            elif (self.player.state == 3):
                self.player.imageList = self.player.image_list_jump
            else:
                self.player.imageList = self.player.image_list_walk



        if symbol == key.A:
           self.player.imageList = self.player.image_list_attack
           self.player.state = 4
           self.player.attack_status = 1
        if symbol == key.W:
            self.player.state = 0
            self.player.imageList = self.player.image_list_walk

            #self.background.velx = -150
        if symbol == key.S:
            self.player.state = 1
            self.player.imageList = self.player.image_list_swim
        if symbol == key.D:
            self.player.state = 2
            self.player.imageList = self.player.image_list_dash
        if symbol == key.J:
            self.player.state = 3
            self.player.imageList = self.player.image_list_jump

        if symbol == key.C:
            self.player.imageList = self.player.image_list_climb



    def on_key_release(self, symbol, modifiers):
        if symbol in (key.RIGHT, key.LEFT):
            self.player.velx = 0
            self.background.velx = 0
            self.player.imageList = self.player.image_list_default
        if symbol in (key.UP, key.DOWN, key.C):
            self.player.vely = 0
        if symbol in (key.A, key.W, key.S, key.D, key.J, key.C):
            self.player.imageList = self.player.image_list_default
            self.background.velx = 0
            self.player.state = 0
            self.player.attack_status = 0

    def on_draw(self):
        self.clear()
        self.background.draw()
        self.player.draw()
        #self.brick.draw()
        for enemy in ememies_list:
            enemy.draw()
        self.score.draw()

    def update(self, dt):
        eneme_out_of_window = []
        self.player.update(dt)
        self.background.update(dt)

        if(self.player.attack_status == 2):

            for enemy in ememies_list:
                if(abs(self.player.getX()-enemy.getX()) < 10):
                    print("killed")
                    self.player.score += 10
                    self.score = pyglet.text.Label('Score : ' + str(self.player.score ),
                                                   font_name='Times New Roman',
                                                   font_size=36,
                                                   x=100, y=550,
                                                   anchor_x='center', anchor_y='center')
                    eneme_out_of_window.append(enemy)

        for enemieObj in ememies_list:
            if (enemieObj.getX() < 10 or enemieObj.getX() > 500):
                #print(enemieObj.getX())
                eneme_out_of_window.append(enemieObj)
            enemieObj.update(dt)

        for removeEneme in eneme_out_of_window:
            ememies_list.remove(removeEneme)
            # ememies_list.remove(enemieObj)
            start = 0
            end = 0
            if (self.toggle == True):
                start = 10
                end = 30
                self.toggle = False
            else:
                start = -30
                end = -10
                self.toggle = True

            enemie = Enemies(posx=random.randint(0, 300), posy=40, velx=random.randint(start, end), vely=0,
                             image="goomba_1.png")
            ememies_list.append(enemie)

            # print(enemieObj.getX())



if __name__ == "__main__":
    window = GameWindow(1430, 574, "Mario", resizable=False)
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()