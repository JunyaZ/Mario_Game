import pyglet
from pyglet.window import key
from game import resources

game_window = pyglet.window.Window(800, 600)
start_bg = resources.start_bg

score_label = pyglet.text.Label(text="Score: 0", x=10, y=575)
greeting_label = pyglet.text.Label(text="Welcome To Mario World!", 
                                x=400, y=375, anchor_x='center',color=(255, 209, 26, 255), bold=True, font_size=40)
start_label = pyglet.text.Label(text="Press Enter to START game", 
                                x=400, y=275, anchor_x='center',color=(255, 77, 136, 255), bold=True, font_size=30)

@game_window.event
def on_draw():
    game_window.clear()
 
    start_bg.width = 800
    start_bg.height = 600
    start_bg.blit(0,0)
    greeting_label.draw()
    score_label.draw()
    start_label.draw()

@game_window.event
def on_key_press(symbol, modifiers):
    if symbol == key.ENTER:
         game_window.clear()
         start_label.delete()
         start_bg.delete()
         greeting_label.delete()
         print('loading next page')

if __name__ == '__main__':
   
    pyglet.app.run()


