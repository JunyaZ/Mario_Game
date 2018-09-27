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
        self.player = GameObject( posx = 200, posy = 185 ,image = "Mario_Super.png")
        self.background = BackgroundObject(posx = 0, posy = 0, image = "background_3.jpg")
        #self.brick1 = BackgroundObject(posx=0, posy=0, image="brick1.png")
        #self.brick2 = BackgroundObject(posx=862, posy=0, image="brick1.png")
        #self.water = BackgroundObject(posx=625, posy=0, image="water.png")

        self.enemie1 = Enemies(posx=random.randint(0, 300), posy=185, velx=random.randint(30, 50), vely=0,
                               image="goomba_1.png")
        self.enemie2 = Enemies(posx=random.randint(0, 300), posy=185, velx=random.randint(-50, -30), vely=0,
                               image="goomba_1.png")
        ememies_list.append(self.enemie1)
        ememies_list.append(self.enemie2)

        self.toggle = False


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

    def on_draw(self):
        self.clear()
        self.background.draw()
        #self.brick1.draw()
        #self.brick2.draw()
        self.player.draw()
        #self.water.draw()

        for enemy in ememies_list:
            enemy.draw()

    def update(self, dt):
        self.player.update(dt)
        self.background.update(dt)
        eneme_out_of_window = []
        for enemieObj in ememies_list:

            if (enemieObj.getX() < 10 or enemieObj.getX() > 500):
                print(enemieObj.getX())
                eneme_out_of_window.append(enemieObj)

            enemieObj.update(dt)
        for removeEneme in eneme_out_of_window:
            ememies_list.remove(removeEneme)
            # ememies_list.remove(enemieObj)
            start = 0
            end = 0
            if (self.toggle == True):
                start = 20
                end = 40
                self.toggle = False
            else:
                start = -40
                end = -20
                self.toggle = True

            enemie = Enemies(posx=random.randint(0, 300), posy=185, velx=random.randint(start, end), vely=0,
                             image="goomba_1.png")
            ememies_list.append(enemie)

            # print(enemieObj.getX())



if __name__ == "__main__":
    window = GameWindow(1434,574, "Mario", resizable=False)
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.lib.load_library('avbin64')
    pyglet.have_avbin = True
    music = pyglet.resource.media('backgroundMusic.mp3')
    music.play()
    pyglet.app.run()