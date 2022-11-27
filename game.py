# Circle Tic-Tac-Toe
import random
import time
import turtle

'''
This program was inteded to create a functional circle tic-tac-toe
game. The game was modeled after the Math Field Day event, Triathlon,
in which participants play circle tic-tac-toe in the first round.
The same rules apply, but there are some variations made to make it
more stylistic and customizable.
'''

# lists and variables:
coordinates = {
    'tm1': [0, 60],
    'tm2': [0, 120],
    'tm3': [0, 170],
    'tm4': [0, 220],
    'tl1': [-60, 30],
    'tl2': [-105, 60],
    'tl3': [-150, 85],
    'tl4': [-195, 110],
    'tr1': [60, 30],
    'tr2': [105, 60],
    'tr3': [150, 85],
    'tr4': [195, 110],

    'bm1': [0, -60],
    'bm2': [0, -120],
    'bm3': [0, -170],
    'bm4': [0, -220],
    'bl1': [-60, -30],
    'bl2': [-105, -60],
    'bl3': [-150, -85],
    'bl4': [-195, -110],
    'br1': [60, -30],
    'br2': [105, -60],
    'br3': [150, -85],
    'br4': [195, -110] 
}

win_conditions = {
    # vertical conditions:
    'tl': ['tl1', 'tl2', 'tl3', 'tl4'],
    'tm': ['tm1', 'tm2', 'tm3', 'tm4'],
    'tr': ['tr1', 'tr2', 'tr3', 'tr4'],
    'bl': ['bl1', 'bl2', 'bl3', 'bl4'],
    'bm': ['bm1', 'bm2', 'bm3', 'bm4'],
    'br': ['br1', 'br2', 'br3', 'br4'],

    # horizontal conditions:
    '1-1': ['tl1', 'tm1', 'tr1', 'br1'],
    '1-2': ['tm1', 'tr1', 'br1', 'bm1'],
    '1-3': ['tr1', 'br1', 'bm1', 'bl1'],
    '1-4': ['br1', 'bm1', 'bl1', 'tl1'],
    '1-5': ['bm1', 'bl1', 'tl1', 'tm1'],
    '1-6': ['bl1', 'tl1', 'tm1', 'tr1'],

    '2-1': ['tl2', 'tm2', 'tr2', 'br2'],
    '2-2': ['tm2', 'tr2', 'br2', 'bm2'],
    '2-3': ['tr2', 'br2', 'bm2', 'bl2'],
    '2-4': ['br2', 'bm2', 'bl2', 'tl2'],
    '2-5': ['bm2', 'bl2', 'tl2', 'tm2'],
    '2-6': ['bl2', 'tl2', 'tm2', 'tr2'],

    '3-1': ['tl3', 'tm3', 'tr3', 'br3'],
    '3-2': ['tm3', 'tr3', 'br3', 'bm3'],
    '3-3': ['tr3', 'br3', 'bm3', 'bl3'],
    '3-4': ['br3', 'bm3', 'bl3', 'tl3'],
    '3-5': ['bm3', 'bl3', 'tl3', 'tm3'],
    '3-6': ['bl3', 'tl3', 'tm3', 'tr3'],

    '4-1': ['tl4', 'tm4', 'tr4', 'br4'],
    '4-2': ['tm4', 'tr4', 'br4', 'bm4'],
    '4-3': ['tr4', 'br4', 'bm4', 'bl4'],
    '4-4': ['br4', 'bm4', 'bl4', 'tl4'],
    '4-5': ['bm4', 'bl4', 'tl4', 'tm4'],
    '4-6': ['bl4', 'tl4', 'tm4', 'tr4'],

    # spirals:
    'rtl': ['tl1', 'tm2', 'tr3', 'br4'],
    'rtm': ['tm1', 'tr2', 'br3', 'bm4'],
    'rtr': ['tr1', 'br2', 'bm3', 'bl4'],
    'rbr': ['br1', 'bm2', 'bl3', 'tl4'],
    'rbm': ['bm1', 'bl2', 'tl3', 'tm4'],
    'rbl': ['bl1', 'tl2', 'tm3', 'tr4'],

    'ltl': ['tl1', 'bl2', 'bm3', 'br4'],
    'ltm': ['tm1', 'tl2', 'bl3', 'bm4'],
    'ltr': ['tr1', 'tm2', 'tl3', 'bl4'],
    'lbr': ['br1', 'tr2', 'tm3', 'tl4'],
    'lbm': ['bm1', 'br2', 'tr3', 'tm4'],
    'lbl': ['bl1', 'bm2', 'br3', 'tr4']
}

ai_turn = True
location = 'n/a'
turn = 'x'
crosses = []
circles = []
winning_moves = []
preserved_coordinates = dict(coordinates)
button_pressed = False
players = [-168, 217, 'black']
cross_or_circles = [-168, 128, 'black', 'x']
cross_color = [-231, -16, 'red']
circle_color = [140, -16, 'red']

# screen and turtle setup:
wn = turtle.Screen()
wn.tracer(False)
wn.setup(width=720, height=720) # dimensions of the screen
wn.addshape('cross.gif')
wn.addshape('circle.gif')
wn.bgpic('title.gif')
wn.title('Circle Tic-Tac-Toe')

# create writer turtle
writer = turtle.Turtle()
writer.ht()
writer.pencolor('black')
writer.up()

# create turtle for crosses and circles:
shaper = turtle.Turtle()
shaper.ht()
shaper.up()
shaper.shape('cross.gif')

# create turtle for drawing winning moves:
lines = turtle.Turtle()
lines.ht()
lines.up()
lines.pensize(5)

# create a turtle for managing the optionsL
opturt = turtle.Turtle()
opturt.ht()
opturt.up()
opturt.shape('turtle')
opturt.seth(90)
opturt.shapesize(.8)


# functions:
def coor_locator(x,y):
    print(x, y)

def displays(screen): # displays different screens depending on the parameter
    global button_pressed
    button_pressed = True
    if screen == 'play':
        wn.bgpic('board.gif')
    elif screen == 'help':
        writer.goto(0, 285)
        writer.write('Click on any of the different win conditions for more information.' , font=('Arial', 11, 'normal'), align='center')
        wn.bgpic('help-screen.gif')
    elif screen == 'options':
        wn.bgpic('options-screen.gif')
    elif screen == 'info':
        wn.bgpic('information-screen.gif')

def option_selection():
    global circle_color, cross_color, cross_or_circles
    opturt.clear()
    opturt.goto(players[0], players[1])
    opturt.color(players[2])
    opturt.stamp()
    opturt.goto(cross_or_circles[0], cross_or_circles[1])
    opturt.color(cross_or_circles[2])
    opturt.stamp()
    opturt.goto(circle_color[0], circle_color[1])
    opturt.color(circle_color[2])
    opturt.stamp()
    opturt.goto(cross_color[0], cross_color[1])
    opturt.color(cross_color[2])
    opturt.stamp()

def click(x, y): # locates where the cursor is and what space to place x/o
    global ai_turn, button_pressed, circle_color, cross_color, cross_or_circles, location, players, turn
    # home button:
    if x >= -340 and x <= -305 and y >= -340 and y <= -305:
        reset_game()
        button_pressed = False
        wn.bgpic('title.gif')


    # play button:
    elif button_pressed == False and x >= -165 and x <= 165 and y >= 75 and y <= 170:
        turn = cross_or_circles[3]
        displays('play')


    # help button:
    elif button_pressed == False and x >= -165 and x <= 165 and y >= -50 and y <= 50:
        displays('help')
    # screen:
    elif button_pressed == True and wn.bgpic() == 'help-screen.gif':
        writer.clear()
        if x >= -255 and x <= -55 and y >= 0 and y <= 185: # left
            writer.write('The player wins when four crosses/circles are connected vertically. This does not apply across the center.' , font=('Arial', 11, 'normal'), align='center')
        elif x >= 55 and x <= 255 and y >= 0 and y <= 185: # right
            writer.write('The player wins when four crosses/circles are connected horizontally in a circle.' , font=('Arial', 11, 'normal'), align='center')
        elif x >= -100 and x <= 100 and y >= -250 and y <= -65: # bottom
            writer.write('The player wins when four crosses/circles are connected in a spiral.' , font=('Arial', 11, 'normal'), align='center')
            writer.goto(writer.xcor(), writer.ycor() - 15)
            writer.write('A spiral is formed by moving outward one circle and over left/right until the outermost circle.' , font=('Arial', 11, 'normal'), align='center')
            writer.goto(writer.xcor(), writer.ycor() + 15)


    # options button:
    elif button_pressed == False and x >= -165 and x <= 165 and y >= -170 and y <= -70:
        displays('options')
        option_selection()
    # screen:
    elif button_pressed == True and wn.bgpic() == 'options-screen.gif':
        # players:
        if x >= -185 and x <= -155 and y >= 205 and y <= 235: # cross selection
            players = [-168, 217, 'black']
            ai_turn = True
        elif x >= 40 and x <= 70 and y >= 205 and y <= 235: # circle selection
            players = [53, 217, 'black']
            ai_turn = False
        # crosses or circles:
        if x >= -185 and x <= -155 and y >= 115 and y <= 145: # cross selection
            cross_or_circles = [-168, 128, 'black', 'x']
            turn = 'x'
        elif x >= 40 and x <= 70 and y >= 115 and y <= 145: # circle selection
            cross_or_circles = [53, 128, 'black', 'o']
            turn = 'o'
        # cross colors:
        if x >= -250 and x <= -215 and y >= -30 and y <= 5: # red circles
            cross_color = [-231, -16, 'red']
        elif x >= -250 and x <= -215 and y >= -80 and y <= -45: # orange circles
            cross_color = [-231, -66, 'orange']
        elif x >= -250 and x <= -215 and y >= -130 and y <= -95: # yellow circles
            cross_color = [-231, -116, 'yellow']
        elif x >= -250 and x <= -215 and y >= -180 and y <= -145: # green circles
            cross_color = [-231, -166, 'green']
        elif x >= -250 and x <= -215 and y >= -230 and y <= -195: # blue circles
            cross_color = [-231, -216, 'blue']
        elif x >= -250 and x <= -215 and y >= -280 and y <= -245: # violet circles
            cross_color = [-231, -266, 'blueviolet']
        # circle colors:
        if x >= 125 and x <= 155 and y >= -30 and y <= 5: # red circles
            circle_color = [140, -16, 'red']
        elif x >= 125 and x <= 155 and y >= -80 and y <= -45: # orange circles
            circle_color = [140, -66, 'orange']
        elif x >= 125 and x <= 155 and y >= -130 and y <= -95: # yellow circles
            circle_color = [140, -116, 'yellow']
        elif x >= 125 and x <= 155 and y >= -180 and y <= -145: # green circles
            circle_color = [140, -166, 'green']
        elif x >= 125 and x <= 155 and y >= -230 and y <= -195: # blue circles
            circle_color = [140, -216, 'blue']
        elif x >= 125 and x <= 155 and y >= -280 and y <= -245: # violet circles
            circle_color = [140, -266, 'blueviolet']
        option_selection()


    # information button:
    elif button_pressed == False and x >= 305 and x <= 340 and y >= -340 and y <= -305:
        displays('info')


    # play button:
    elif button_pressed == True and wn.bgpic() == 'board.gif':
        # top middle:
        if x >= -40 and x <= 40 and y >= 0 and y <= 80: # the first, top-half middle column
            location = 'tm1'
        elif x >= -40 and x <= 40 and y >= 80 and y <= 160: # the second, top-half, middle column
            location = 'tm2'
        elif x >= -40 and x <= 40 and y >= 160 and y <= 200: # the third, top-half, middle column
            location = 'tm3'
        elif x >= -40 and x <= 40 and y >= 200 and y <= 260: # the fourth, top-half, middle column
            location = 'tm4'
        # top left:
        if x >= -70 and x <= -35 and y >= 20 and y <= 55: # the first, top-half, left column
            location = 'tl1'
        elif x >= -115 and x <= -95 and y >= 50 and y <= 70: # the second, top-half, left column
            location = 'tl2'
        elif x >= -170 and x <= -130 and y >= 80 and y <= 100: # the third, top-half, left column, x >= -160 and x <= -140
            location = 'tl3'
        elif x >= -220 and x <= -160 and y >= 80 and y <= 130: # the fourth, top-half, left column, x >= -205 and x <= -185 and 
            location = 'tl4'
        # top right:
        if x >= 35 and x <= 70 and y >= 20 and y <= 55: # the first, top-half, right column
            location = 'tr1'
        elif x >= 95 and x <= 115 and y >= 50 and y <= 70: # the second, top-half, right column
            location = 'tr2'
        elif x >= 130 and x <= 170 and y >= 80 and y <= 100: # the third, top-half, right column
            location = 'tr3'
        elif x >= 160 and x <= 220 and y >= 80 and y <= 130: # the fourth, top-half, right column
            location = 'tr4'
        # bottom middle:
        if x >= -40 and x <= 40 and y >= -80 and y <= 0: # the first, bottom-half middle column
            location = 'bm1'
        elif x >= -40 and x <= 40 and y >= -160 and y <= -80: # the second, bottom-half, middle column
            location = 'bm2'
        elif x >= -40 and x <= 40 and y >= -200 and y <= -160: # the third, bottom-half, middle column
            location = 'bm3'
        elif x >= -40 and x <= 40 and y >= -260 and y <= -200: # the fourth, bottom-half, middle column
            location = 'bm4'
        # bottom left:
        if x >= -70 and x <= -35 and y >= -55 and y <= -20: # the first, bottom-half, left column
            location = 'bl1'
        elif x >= -115 and x <= -95 and y >= -70 and y <= -50: # the second, bottom-half, left column
            location = 'bl2'
        elif x >= -170 and x <= -130 and y >= -100 and y <= -80: # the third, bottom-half, left column
            location = 'bl3'
        elif x >= -220 and x <= -160 and y >= -130 and y <= -80: # the fourth, bottom-half, left column
            location = 'bl4'
        # bottom right:
        if x >= 35 and x <= 70 and y >= -55 and y <= -20: # the first, bottom-half, right column
            location = 'br1'
        elif x >= 95 and x <= 115 and y >= -70 and y <= -50: # the second, bottom-half, right column
            location = 'br2'
        elif x >= 130 and x <= 170 and y >= -100 and y <= -80: # the third, bottom-half, right column
            location = 'br3'
        elif x >= 160 and x <= 220 and y >= -130 and y <= -80: # the fourth, bottom-half, right column
            location = 'br4'
        # restart button:
        elif x >= 305 and x <= 340 and y >= -340 and y <= -305:
            turn = 'restart'
        placing_shapes()
        win_test()

# places x/o respectively, based on click
def placing_shapes():
    global ai_turn, circles, coordinates, crosses, cross_or_circles, location, turn
    if location in coordinates:
        xy = coordinates[location]
        if turn == 'x':
            shaper.shape('cross.gif')
            crosses.append(location)
            turn = 'o'
        elif turn == 'o':
            shaper.shape('circle.gif')
            circles.append(location)
            turn = 'x'
        coordinates.pop(location)
        shaper.goto(xy[0], xy[1])
        shaper.stamp()
        if ai_turn == True and turn != cross_or_circles[3]:
            location = random.choice(list(coordinates.keys()))
            placing_shapes()

    elif turn == 'restart':
        reset_game()
        turn = cross_or_circles[3]
    else:
        writer.goto(0, 290)
        writer.write('Please click in an available space. This space might be occupied.' , font=('Arial', 14, 'bold'), align='center')
        time.sleep(1.25)
        writer.clear()

# testing for win conditions
def win_test():
    global winning_moves, circle_color, cross_color
    if len(coordinates) > 0:
        for conditions in win_conditions:
            testing_conditions = win_conditions[conditions]
            check_crosses = all(i in crosses for i in testing_conditions) # checks lists to see if they contain win conditions
            check_circles = all(i in circles for i in testing_conditions)
            if check_crosses == True:
                writer.goto(0, 290)
                writer.write('Crosses win!' , font=('Arial', 14, 'bold'), align='center')
                winning_moves = testing_conditions
                drawing_lines(cross_color[2])
            elif check_circles == True:
                writer.goto(0, 290)
                writer.write('Circles win!' , font=('Arial', 14, 'bold'), align='center')
                winning_moves = testing_conditions
                drawing_lines(circle_color[2])
    else:
        writer.write('It\'s a tie!' , font=('Arial', 14, 'bold'), align='center')

def drawing_lines(color):
    global winning_moves
    wn.tracer(True)
    lines.up()
    lines.pencolor(color)
    for i in winning_moves:
        xy = preserved_coordinates[i]
        lines.goto(xy[0], xy[1])
        lines.down()
    wn.tracer(False)

def reset_game():
    global circles, coordinates, crosses, turn
    lines.clear()
    shaper.clear()
    opturt.clear()
    writer.clear()
    crosses = []
    circles = []
    coordinates = dict(preserved_coordinates)

# function calls and events:
wn.onscreenclick(click)
wn.listen()
wn.mainloop()