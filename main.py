import pyglet
from pyglet.window import key
from random import randint, choice


window = pyglet.window.Window(width=1200, height=900, resizable=False)
window.set_location(400, 100)
main_batch = pyglet.graphics.Batch()


# when creating a new enemy, it will choose a random direction from the list below
directions = [1, -1]
player_speed = 300
left = False
right = False
destroyed_enemies = 0
next_wave = 0
score = 0
fire = False
player_fire_rate = 0
enemy_fire_rate = 0
enemy_falling = 0
enemy_falling_count = 1
preloaded = False
player_health = 5
player_is_alive = True
enemy_death = False
time = 0
game = False
flash_time = 1
player_flash = False



# loading images
background = pyglet.image.load('res/sprites/background.jpg')
brick = pyglet.image.load('res/sprites/brick.png')
playerImage = pyglet.image.load('res/sprites/mario.png') # space_ship.png
playerShoot = pyglet.image.load('res/sprites/bullet.png')
goomba = pyglet.image.load('res/sprites/goomba.png')

# loading sprite sheet for the enemy
enemy = pyglet.image.load('res/sprites/enemy.png')
enemy_seq = pyglet.image.ImageGrid(enemy, 1, 8, item_width=100, item_height=100)
enemy_texture = pyglet.image.TextureGrid(enemy_seq)
enemy_anim = pyglet.image.Animation.from_image_sequence(enemy_texture[0:], 0.1, loop=True)


# creating a labels
text1 = pyglet.text.Label("Enemies Destroyed", x=1000 , y=850, batch=main_batch)
text1.font_size = 10
text2 = pyglet.text.Label("Score", x=1000 , y=750, batch=main_batch)
text2.font_size = 10
text3 = pyglet.text.Label("Players", x=1000 , y=650, batch=main_batch)
text3.font_size = 10


# creating a label to display labels
num_enemies_destroyed = pyglet.text.Label(str(0), x=1100, y=800, batch=main_batch)
num_enemies_destroyed.font_size = 22
num_score = pyglet.text.Label(str(0), x=1100, y=700, batch=main_batch)
num_score.font_size = 22
numb_player_health = pyglet.text.Label(str(5), x=1100, y=600, batch=main_batch)
numb_player_health.font_size = 22

game_over_text = pyglet.text.Label("Game Over", x=600, y=500)
game_over_text.anchor_x = "center"
game_over_text.anchor_y = "center"
game_over_text.font_size = 60

reload_text = pyglet.text.Label("r : Restart", x=600 , y=350)
reload_text.anchor_x = "center"
reload_text.anchor_y = "center"
reload_text.font_size = 20

intro_text = pyglet.text.Label("Welcome Mario Game ", x=600 , y=450)
intro_text.anchor_x = "center"
intro_text.anchor_y = "center"
intro_text.font_size = 60

player = pyglet.sprite.Sprite(playerImage, x=500, y=100, batch=main_batch)

# add the  sound
explosion = pyglet.media.load('res/sounds/fire.wav', streaming=False)
player_gun_sound = pyglet.media.load('res/sounds/flagpole.wav', streaming=False)

playerShoot_list = []
goomba_list = []
enemy_list = []
bg_list = []

@window.event
def on_draw():
    window.clear()
    if not preloaded:
        preload()
    for bg in bg_list:
        bg.draw()
    if game:
        main_batch.draw()
    else:
        intro_text.draw()
    if not player_is_alive:
        game_over_text.draw()
        reload_text.draw()

def reload():
    global player_is_alive, next_wave, score, destroyed_enemies, player_fire_rate, enemy_fire_rate, explode_time
    global enemy_falling, enemy_falling_count, player_health
    global enemy_death, shake_time, high_score
    next_wave = 0
    score = 0
    player_health = 5
    player_fire_rate = 0
    enemy_fire_rate = 0
    enemy_falling = 0
    enemy_falling_count = 1
    enemy_death = False
    shake_time = 0
    destroyed_enemies = 0
    player_is_alive = True
    player.x, player.y = 500, 100
    player.batch = main_batch

    num_enemies_destroyed.text = str(destroyed_enemies)
    num_score.text = str(score)
    numb_player_health.text = str(player_health)

    for obj in enemy_list:
        obj.batch = None
    for obj in goomba_list:
        obj.batch = None
    enemy_list.clear()
    goomba_list.clear()

@window.event
def on_key_press(symbol, modifiers):
    global  right, left, fire, game
    if symbol == key.RIGHT:
        right = True
    if symbol == key.LEFT:
        left = True
    if symbol == key.SPACE:
        fire = True
        if not game:
            game = True
            fire = False # to prevent firing when the game starts
    if symbol == key.R:
        reload()

@window.event
def on_key_release(symbol, modifiers):
    global right, left, fire
    if symbol == key.RIGHT:
        right = False
    if symbol == key.LEFT:
        left = False
    if symbol == key.SPACE:
        fire = False

def player_move(entity, dt):
    if right and entity.x < 1000:
        entity.x += player_speed * dt
    if left and entity.x > 100:
        entity.x -= player_speed * dt

# this function runs only once, it loads two background images at the start
def preload():
    global preloaded
    for i in range(2):
        bg_list.append(pyglet.sprite.Sprite(background, x=0, y=i*1200))
    preloaded = True

def bg_move(dt):
    for bg in bg_list:
        bg.y -= 50*dt
        if bg.y <= -1300:
            bg_list.remove(bg)
            bg_list.append(pyglet.sprite.Sprite(background, x=0, y=1100))

def enemy_move(enemies, yspeed, dt):
    global score
    for enemy in enemies:
        if enemy.x >= 1000:
            enemy.x = 1000
            enemy.speed *= -1
        if enemy.x <= 100:
            enemy.x = 100
            enemy.speed *= -1
        enemy.y -= yspeed*dt
        enemy.x += enemy.speed * dt
        if enemy.y <= 450 and enemy.y >= 449.4 and player_is_alive:
            score -= 1
            num_score.text = str(score)
        if enemy.y <= -100:
            enemies.remove(enemy)

def enemyFalling(dt):
    global enemy_falling, player_is_alive, enemy_falling_count
    global next_wave
    enemy_falling -= dt
    if player_is_alive:
        if enemy_falling <= 0:
            enemy_list.append(pyglet.sprite.Sprite(enemy_anim, x=600, y=950, batch=main_batch))
            enemy_list[-1].speed = randint(100, 300) * choice(directions) # last spawned entity in entity list
            enemy_list[-1].hit_count = 0
            enemy_list[-1].MAX_HIT = 2
            enemy_falling += enemy_falling_count
    if next_wave >= 20:
        enemy_falling_count -= 0.05
        next_wave = 0

def enemy_shoot(dt):
    global enemy_fire_rate
    enemy_fire_rate -= dt
    if enemy_fire_rate <= 0:
        for enemy in enemy_list:
            if randint(0, 10) >= 5:
                goomba_list.append(pyglet.sprite.Sprite(goomba, enemy.x + 50, enemy.y, batch=main_batch))
        enemy_fire_rate += 5

def update_enemy_shoot(dt):
    for item in goomba_list:
        item.y -= 400 * dt
        if item.y < -50: # if the goomba y position is below -100 it gets removed from the goomba list
            goomba_list.remove(item)

def player_shoot(dt):
    global player_fire_rate
    player_fire_rate -= dt
    if player_fire_rate <= 0:
        playerShoot_list.append(pyglet.sprite.Sprite(playerShoot, player.x + 32, player.y + 96, batch=main_batch))
        player_fire_rate += 0.2
        if player_is_alive:
            player_gun_sound.play()

def update_player_shoot(dt):
    for bullet in playerShoot_list:
        bullet.y += 400 * dt
        if bullet.y > 950: # if the bullet y position is above 950 it gets removed from the playshoot list
            playerShoot_list.remove(bullet)

def screen():
    global time, enemy_death
    time -= 0.1
    x = randint(-10, 10)
    if time <= 0:
        bg_list[0].x = x
        bg_list[1].x = x
        time += 0.11
    elif time >= 0:
        bg_list[0].x = 0
        bg_list[1].x = 0
        enemy_death = False

def Hitenemy(entity):
    global destroyed_enemies, score, next_wave, enemy_death
    entity.hit_count += 1
    if entity.hit_count >= entity.MAX_HIT and player_is_alive:
        enemy_death = True
        enemy_list.remove(entity)  # remove the enemy from enemy list when shot two times
        entity.delete()
        explosion.play()
        destroyed_enemies += 1 # is only for displaying
        next_wave += 1
        score += 1
        num_enemies_destroyed.text = str(destroyed_enemies)
        num_score.text = str(score)

def player_hit():
    global player_health, numb_player_health, player_flash
    player_health -= 1
    numb_player_health.text = str(player_health)
    player_flash = True
    if player_health <= 0:
        player.batch = None
        game_over()

def update_flash():
    global flash_time, player_flash
    flash_time -= 0.2
    player.color = (255, 0, 0)
    if flash_time <= 0:
        player.color = (255, 255, 255)
        flash_time = 1
        player_flash = False

def game_over():
    global player_is_alive
    player_is_alive = False

def bullet_collision(entity, bullet_list):
    for bullet in bullet_list:
        if bullet.x < entity.x + entity.width and bullet.x + bullet.width > entity.x \
                and bullet.y < entity.y + entity.height and bullet.height + bullet.y > entity.y:
            bullet_list.remove(bullet)  # remove the bullet from bullet list when colliding with an enemy
            return True

def update(dt):
    if game:
        player_move(player, dt)
        enemy_move(enemy_list, 30, dt)
        if fire:
            player_shoot(dt)
        update_player_shoot(dt)
        enemy_shoot(dt)
        update_enemy_shoot(dt)
        for entity in enemy_list:
            if bullet_collision(entity, playerShoot_list):
                Hitenemy(entity)
        if bullet_collision(player, goomba_list) and player_is_alive:
            player_hit()
        if player_flash:
            update_flash()
        enemyFalling(dt)
        if enemy_death:
            screen()
    bg_move(dt)

if __name__ == "__main__":

    pyglet.clock.schedule_interval(update, 1.0/80)
    pyglet.app.run()
