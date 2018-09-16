import pyglet
from pyglet.window import  key
from GameObject import GameObject
from BackgroundObject import BackgroundObject

class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(400, 100)
        self.frame_rate = 1/60.0
        self.player = GameObject( posx = 200, posy = 225 ,image = "Mario_Super.png")
        self.background = BackgroundObject(posx = 0, posy = 0, image = "background_0.jpg")


    def on_key_press(self, symbol, modifiers):
        if symbol == key.RIGHT:
            self.player.velx = 15
        if symbol == key.LEFT:
            self.player.velx = -15

        if symbol == key.UP:
            self.player.vely = 15
        if symbol == key.DOWN:
            self.player.vely = -15

        if symbol == key.A:
            self.player.imageList = self.player.image_list_attack
        if symbol == key.W:
            self.player.imageList = self.player.image_list_walk
            self.background.velx = -15
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
        if symbol in (key.UP, key.DOWN, key.C):
            self.player.vely = 0
        if symbol in (key.A, key.W, key.S, key.D, key.J, key.C):
            self.player.imageList = self.player.image_list_default
            self.background.velx = 0

    def on_draw(self):
        self.clear()
        self.background.draw()
        self.player.draw()

    def update(self, dt):
        self.player.update(dt)
        self.background.update(dt)



if __name__ == "__main__":
    window = GameWindow(1200, 900, "Mario", resizable=False)
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()