import pyglet
path= r"C:/Users/1x8le/Documents/Mario_Game-master/picture/backgrounds/"
class BackgroundObject:
    def __init__(self, posx, posy, image = None):
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0
        self.image_list_default = ['title.png']
        self.backgroud_list = ['goomba_1.png', 'goomba_2.png', 'goomba_3.png',
                            'goomba_4.png','goomba_5.png', 'goomba_6.png']
        self.imageList =  self.image_list_default

        if image is not None:
            image = pyglet.image.load(path+image)
            self.sprite = pyglet.sprite.Sprite(image, x = self.posx, y = self.posy)

    def draw(self):
        self.sprite.draw()

    def update(self):
        self.sprite.x += self.velx
        self.sprite.y += self.vely
