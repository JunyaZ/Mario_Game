import pyglet
from pyglet.window import key
from GameObject import GameObject
from BackgroundObject import BackgroundObject
from enemies import Enemies
class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(400, 100)
        self.frame_rate = 1/60.0
        self.player = GameObject( posx = 200, posy = 200 ,image = "Mario_Super.png")
        self.enemie1 = Enemies(posx=500, posy=200, image="goomba_1.png")
        self.enemie2 = Enemies(posx=300, posy=200, image="goomba_1.png")
        self.background = BackgroundObject(posx = 0, posy = 0, image ='background_0.jpg')
        self.brick = BackgroundObject(posx=0, posy=0, image='brick.png')


    def on_key_press(self, symbol, modifiers):
        if symbol == key.RIGHT:
            self.player.velx = 150
            self.background.velx = -150
        if symbol == key.LEFT:
            self.player.velx = -150
            self.background.velx = 150
        if symbol == key.UP:
            self.player.vely = 150
        if symbol == key.DOWN:
            self.player.vely = -150
        if symbol == key.A:
            self.player.imageList = self.player.image_list_attack
        if symbol == key.W:
            self.player.imageList = self.player.image_list_walk
            self.background.velx = -150
        if symbol == key.S:
            self.player.imageList = self.player.image_list_swim
        if symbol == key.D:
            self.player.imageList = self.player.image_list_dash
        if symbol == key.J:
            self.player.imageList = self.player.image_list_jump
        if symbol == key.C:
            self.player.imageList = self.player.image_list_climb

    def on_key_release(self, symbol, modifiers):
        if symbol in (key.RIGHT, key.LEFT):
            self.player.velx = 0
            self.background.velx = 0
        if symbol in (key.UP, key.DOWN, key.C):
            self.player.vely =0
        if symbol in (key.A, key.W, key.S, key.D, key.J, key.C):
            self.player.imageList = self.player.image_list_default
            self.background.velx = 0

    def on_draw(self):
        self.clear()
        self.background.draw()
        self.brick.draw()
        self.player.draw()
        self.enemie1.draw()
        self.enemie2.draw()

    def update(self, dt):
        self.player.update(dt)
        self.background.update()


if __name__ == "__main__":
    window = GameWindow(1024, 768, "Mario", resizable=True)
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()