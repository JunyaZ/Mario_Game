import pyglet

class BackgroundObject:
    def __init__(self, posx, posy, image = None):
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0

        self.image_list_default = ['mushroom_sky.png', 'ppbgs.png']

        self.imageList =  self.image_list_default
        if image is not None:
            image = pyglet.image.load('../sprites/backgrounds/new_back_img/'+image)
            self.sprite = pyglet.sprite.Sprite(image, x = self.posx, y = self.posy)

    def draw(self):
        self.sprite.draw()

    def update(self, dt):

        self.sprite.x += self.velx * dt
        self.sprite.y += self.vely * dt

