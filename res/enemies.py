import pyglet
path = r"C:/Users/1x8le/Documents/MSU course/CSC745/project_pyglet/Mario_Game-master/picture/goomba/"
class Enemies:
    def __init__(self, posx, posy, image = None):
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0

        self.imageIndex = 0
        self.update_time = 0
        self.goomba_list = ['goomba_1.png', 'goomba_2.png', 'goomba_3.png',
                            'goomba_4.png','goomba_5.png', 'goomba_6.png']
        self.image_list_default = ['goomba_1.png']
        self.imageList =self.image_list_default
        if image is not None:
            image = pyglet.image.load(path+image)
            self.sprite = pyglet.sprite.Sprite(image, x = self.posx, y = self.posy)

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
