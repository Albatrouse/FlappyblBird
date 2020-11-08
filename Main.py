from tkinter import *
import time
import random

root = Tk()
root.geometry("800x600+0+0")
root.title("Flappy Cube")
root.config(bg='lightblue')
root.resizable(False, False)

x = 380
y=280

cube = Canvas(root, bg="green", width=40, height=40)

is_jump = False
range = 50

def jump(event):
    global is_jump
    is_jump = True

enemy1H = random.randint(200, 400)
enemy1 = Canvas(root, bg='red', height = enemy1H, width=50)
enemy1X = 800
enemy1Y = 0
enemy1_2 = Canvas(root, bg='red', height = (600-enemy1H-80), width=50)


enemy2H = random.randint(200, 400)
enemy2 = Canvas(root, bg='red', height = enemy2H, width=50)
enemy2X = 1200
enemy2Y = 0
enemy2_2 = Canvas(root, bg='red', height = (600-enemy2H-80), width=50)


root.bind('<Button-1>', jump)

score = 0
scoreL = Label(root, bg="lightblue", text='Score: '+str(score))

inside = False
run = True

while run:
    time.sleep(0.005)
    if root.quit():
        run = False
    
    if(is_jump):
        if range == 0:
            is_jump = False
            range = 50
        else:
            y -= 2
            range -= 2
    else: y+=2

    cube.place(x=x, y=y)

    enemy1X -= 1
    enemy1.place(x=enemy1X, y=enemy1Y)
    enemy1_2.place(x=enemy1X, y=(enemy1H+120))
    if enemy1X < -50:
        enemy1X = 800
        enemy1H = random.randint(200, 400)
        enemy1.config(height = enemy1H)
        enemy1_2.config(height = (600-enemy1H-120))

    if((x+40 >= enemy1X and x <= enemy1X+50) and (y <= enemy1Y+enemy1H or y+40 >= enemy1H+120)):
        print("Game Over")
    

    enemy2X -= 1
    enemy2.place(x=enemy2X, y=enemy2Y)
    enemy2_2.place(x=enemy2X, y=(enemy2H+120))
    if enemy2X < -50:
        enemy2X = 800
        enemy2H = random.randint(200, 400)
        enemy2.config(height = enemy2H)
        enemy2_2.config(height = (600-enemy2H-120))

    if((x+40 >= enemy2X and x <= enemy2X+50) and (y <= enemy2Y+enemy2H or y+40 >= enemy2H+120)):
        print("Game Over")

    

    if((x+40 >= enemy1X and x <= enemy1X+50)or(x+40 >= enemy2X and x <= enemy2X+50)):
        if(inside == False): 
            score += 1
        inside = True
        scoreL.config(text="Score: "+str(score))
    else: inside = False

    scoreL.place(x=0, y=0)

    root.update()
