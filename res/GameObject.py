import pyglet
import os


class GameObject:
    def __init__(self, posx, posy, image = None):
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0

        self.imageIndex = 0
        self.update_time = 0

        self.image_list_attack = ['attack_0.png', 'attack_m_00.png','attack_1.png', 'attack_m_01.png',
                                  'attack_2.png', 'attack_m_02.png', 'attack_3.png', 'attack_m_03.png',
                                  'attack_4.png', 'attack_m_04.png', 'attack_5.png', 'attack_m_05.png',
                                  'attack_6.png', 'attack_m_06.png', 'attack_7.png', 'attack_m_07.png',
                                  'attack_8.png', 'attack_m_08.png', 'attack_9.png', 'attack_m_09.png',
                                  'attack_10.png', 'attack_m_10.png',]
        self.image_list_walk = ['walk_0.png', 'walk_m_00.png', 'walk_1.png', 'walk_m_01.png',
                                'walk_2.png', 'walk_m_02.png', 'walk_3.png', 'walk_m_03.png',
                                'walk_4.png',  'walk_m_04.png', 'walk_5.png', 'walk_m_05.png',
                                'walk_6.png', 'walk_m_06.png', 'walk_7.png', 'walk_m_07.png']

        self.image_list_swim = ['swim_0.png', 'swim_m_0.png', 'swim_1.png', 'swim_m_1.png',
                                'swim_2.png', 'swim_m_2.png', 'swim_3.png', 'swim_m_3.png',
                                'swim_4.png', 'swim_m_4.png', 'swim_5.png', 'swim_m_5.png', 'swim_6.png', 'swim_m_6.png']

        self.image_list_dash = ['dash_0.png', 'dash_m_0.png', 'dash_1.png', 'dash_m_1.png',
                                'dash_2.png', 'dash_m_2.png', 'dash_3.png', 'dash_m_3.png',
                                'dash_4.png', 'dash_m_4.png', 'dash_5.png', 'dash_m_5.png',
                                'dash_6.png', 'dash_m_6.png', 'dash_7.png', 'dash_m_7.png']

        self.image_list_climb = ['climb_0.png', 'climb_1.png']
        self.image_list_jump = ['jump_0.png', 'jump_m_0.png']

        self.image_list_default = ['Mario_Super.png', "Super_Mario_m.png"]
        self.state = 0

        self.imageList =  self.image_list_default
        self.imageList_mirror = self.image_list_default
        if image is not None:
            image = pyglet.image.load((os.getcwd())[:-3]+'sprites/heroes/mario/super/'+image)
            self.sprite = pyglet.sprite.Sprite(image, x = self.posx, y = self.posy)

    def draw(self):
        self.sprite.draw()

    def update(self, dt):
        self.update_time += 1;
        self.sprite.x += self.velx * dt
        self.sprite.y += self.vely * dt
        if(self.update_time%10 == 0 ):
            self.imageIndex += 2
            self.imageIndex = self.imageIndex % len(self.imageList)
            image = self.imageList[self.imageIndex]


            #print(image)
            image = pyglet.image.load((os.getcwd())[:-3]+'/sprites/heroes/mario/super/' + image)
            self.sprite = pyglet.sprite.Sprite(image, x=self.sprite.x, y=self.sprite.y)
            self.update_index = 0
