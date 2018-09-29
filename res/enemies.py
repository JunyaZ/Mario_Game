import pyglet
import os

class Enemies:
    def __init__(self, posx, posy, velx, vely, image = None):
        self.posx = posx
        self.posy = posy
        self.velx = velx
        self.vely = vely

        self.imageIndex = 0
        self.update_time = 0
        self.goomba_list = ['goomba_1.png', 'goomba_2.png', 'goomba_3.png',
                            'goomba_4.png','goomba_5.png', 'goomba_6.png']
        self.imageList = self.goomba_list
        if image is not None:
            image = pyglet.image.load((os.getcwd())[:-3]+"picture/goomba/"+image)
            self.sprite = pyglet.sprite.Sprite(image, x = self.posx, y = self.posy)

    def getX(self):
        return self.sprite.x
    def getY(self):
        return self.sprite.y

    def getVelX(self):
        return self.velx
    def getVelY(self):
        return self.vely


    def update(self, dt):
        self.update_time += 1
        self.sprite.x += self.velx * dt
        self.sprite.y += self.vely * dt
        if (self.update_time % 10 == 0):
            self.imageIndex += 1
            self.imageIndex = self.imageIndex % len(self.imageList)
            image = self.imageList[self.imageIndex]
            # print(image)
            image = pyglet.image.load((os.getcwd())[:-3]+"picture/goomba/" + image)
            self.sprite = pyglet.sprite.Sprite(image, x=self.sprite.x, y=self.sprite.y)
            self.update_index = 0

    def set_velocity(self):
        """Sets velocity vector based on direction"""
        if self.direction == 'left':
            self.x_vel = -2
        else:
            self.x_vel = 2

        self.y_vel = 0

    def walking(self):
        """Default state of moving sideways"""
        if (self.current_time - self.animate_timer) > 125:
            if self.frame_index == 0:
                self.frame_index += 1
            elif self.frame_index == 1:
                self.frame_index = 0
            self.animate_timer = self.current_time

    def falling(self):
        """For when it falls off a ledge"""
        if self.y_vel < 10:
            self.y_vel += self.gravity

    def jumped_on(self):
        """Placeholder for when the enemy is stomped on"""
        pass

    def death_jumping(self):
        """Death animation"""
        self.rect.y += self.y_vel
        self.rect.x += self.x_vel
        self.y_vel += self.gravity

        if self.rect.y > 600:
            self.kill()

    def start_death_jump(self, direction):
        """Transitions enemy into a DEATH JUMP state"""
        self.y_vel = -8
        if direction == 'right':
            self.x_vel = 2
        else:
            self.x_vel = -2
        self.gravity = .5
        self.frame_index = 3
        self.image = self.frames[self.frame_index]
        self.state = 'death jump'

    def handle_state(self):
        """Enemy behavior based on state"""
        if self.state == 'walk':
            self.walking()
        elif self.state == 'fall':
            self.falling()
        elif self.state == 'jumped on':
            self.jumped_on()
        elif self.state == 'shell slide':
            self.shell_sliding()
        elif self.state == 'death jump':
            self.death_jumping()

    def draw(self):
        self.sprite.draw()

