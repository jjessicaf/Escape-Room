import pygame
pygame.init()

screenw = 450
screenh = 450
win = pygame.display.set_mode((screenw, screenh))
pygame.display.set_caption("The Escape Room")
gameIcon = pygame.image.load('boi.png')
pygame.display.set_icon(gameIcon)

#colors
black = (0, 0 ,0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
grey = (100,100,100)

#images
background_image = pygame.image.load("bg.png")
one = pygame.image.load('box1.png')
two = pygame.image.load('box2.png')
three = pygame.image.load('box3.png')
underlay = pygame.image.load('underlay.png')
d1 = pygame.image.load('decor1.png')
d2 = pygame.image.load('decor2.png')
d3 = pygame.image.load('decor3.png')
d4 = pygame.image.load('decor4.png')
d5 = pygame.image.load('decor5.png')
boy = pygame.image.load('boi3.png')
dor = pygame.image.load('door.png')

clock = pygame.time.Clock()
beg=True
run=False

s_smallText = pygame.font.Font('freesansbold.ttf',17)
smallText = pygame.font.Font('freesansbold.ttf',23)
mediumText = pygame.font.Font('freesansbold.ttf',45)
largeText = pygame.font.Font('freesansbold.ttf',70)

def text_objects(text, color, size):
    if size == "s_small":
        textSurface = s_smallText.render(text, True, color)
    elif size == "small":
        textSurface = smallText.render(text, True, color)
    elif size == "medium":
        textSurface = mediumText.render(text, True, color)
    elif size == "large":
        textSurface = largeText.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, color, x=0, y=0, size="small"):
    TextSurf, TextRect = text_objects(text, color, size)
    #TextRect.x = 20
    #TextRect.y = 20
    TextRect.center = (screenw/2)+x, (screenh/2)+y
    win.blit(TextSurf, TextRect)

def message_bisplay(text, color, size="small"):
    TextSurf, TextRect = text_objects(text, color, size)
    TextRect.x = 20
    TextRect.y = 20
    win.blit(TextSurf, TextRect)

grid = 5

x = 150
y = 150
x_move = False
y_move = False

class boi():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self, win, img):
        win.blit(img, [self.x, self.y])

class box():
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
  def draw(self, win, img):
    win.blit(img, [self.x, self.y])

class decor():
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
  def draw(self, win, img):
    win.blit(img, [self.x, self.y])

class exitt():
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
  def draw(self, win, img):
    win.blit(img, [self.x, self.y])
  
class wall():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self, win):
        pygame.draw.rect (win, black, (self.x, self.y, self.width, self.height))
class mazeboi():
    def __init__(self, x, y, width, height):
        self.x = mx
        self.y = my
        self.width = width
        self.height = height
    def draw(self, win):
        pygame.draw.rect (win, red, (self.x, self.y, self.width, self.height))
def drawMaze():
    win.fill(white)
    pygame.draw.rect (win, grey, (380, 380, 30, 30))
    mb.draw(win)
    
    w1.draw(win)
    w2.draw(win)
    w3.draw(win)
    w4.draw(win)
    w5.draw(win)
    w6.draw(win)
    w7.draw(win)
    w8.draw(win)
    w9.draw(win)
    w10.draw(win)
    w11.draw(win)
    w12.draw(win)
    w13.draw(win)
    w14.draw(win)
    w15.draw(win)
    w16.draw(win)
    pygame.display.update()

mx = 35
my = 35
mb = mazeboi(mx,my,30,30)
w1 = wall(0, 0, 30, 450)
w2 = wall(420, 0, 30, 450)
w3 = wall(30, 0, 490, 30)
w4 = wall(30, 420, 390, 30)
w5 = wall(30, 80, 70, 30)
w6 = wall(100, 80, 30, 90)
w7 = wall(180, 80, 30, 190)
w8 = wall(210, 80, 160, 30)
w9 = wall(340, 110, 30, 110)
w10 = wall(100, 220, 30, 130)
w11 = wall(180, 270, 240, 30)
w12 = wall(100, 350, 120, 30)
w13 = wall(260, 170, 30, 100)
w14 = wall(220, 300, 30, 80)
w15 = wall(300, 350, 70, 30)
w16 = wall(340, 380, 30, 80)

def drawTrivia():
    win.fill(blue)
    w1.draw(win)
    w2.draw(win)
    w3.draw(win)
    w4.draw(win)
    message_display("TRIVIA", white, 0, -150, size="medium")
    message_display("1. Unscramble RCIVATOAT", white, 0, -70, size="small")
    message_display("a. TRASISTOR", white, 0, -20, size="s_small")
    message_display("b. ACTIVATOR", white, 0, 30, size="s_small")
    message_display("c. VITRACATOR", white, 0, 80, size="s_small")
    pygame.display.update()

def drawTrivia2():
    win.fill(blue)
    w1.draw(win)
    w2.draw(win)
    w3.draw(win)
    w4.draw(win)
    message_display("TRIVIA", white, 0, -150, size="medium")
    message_display("2. What element helps to keep", white, 0, -80, size="small")
    message_display("bones strong?", white, 0, -50, size="small")
    message_display("a. calcium", white, 0, 0, size="s_small")
    message_display("b. potassium", white, 0, 50, size="s_small")
    message_display("c. magnesium", white, 0, 100, size="s_small")
    pygame.display.update()

def drawTrivia3():
    win.fill(blue)
    w1.draw(win)
    w2.draw(win)
    w3.draw(win)
    w4.draw(win)
    message_display("TRIVIA", white, 0, -150, size="medium")
    message_display("3. What country produces the", white, 0, -80, size="small")
    message_display("most coffee?", white, 0, -50, size="small")
    message_display("a. Bolivia", white, 0, 0, size="s_small")
    message_display("b. Britain", white, 0,50, size="s_small")
    message_display("c. Brazil", white, 0, 100, size="s_small")
    pygame.display.update()

def Incorrect():
    win.fill(blue)
    w1.draw(win)
    w2.draw(win)
    w3.draw(win)
    w4.draw(win)
    message_display("Incorrect, try again.", white, 0, -40, size="small")
    message_display("Press 'f' to continue", white, 0, 50, size="s_small")
    pygame.display.update()

def endD():
    win.fill(grey)
    message_display("Congrats on", white, 0, -60, size="medium")
    message_display("Escaping.", white, 0, 0, size="medium")
    message_display("boomer", white, 180, 200, size="s_small")
    pygame.display.update()
     
#collisions
def collisions(object, pp):
    if object.x < pp.x - grid < object.x + object.width and object.y <= pp.y < object.y + object.height:
        pp.x += grid
    if object.x < pp.x + pp.width + grid < object.x + object.width and object.y <= pp.y < object.y + object.height:
        pp.x -= grid
    if object.y < pp.y - grid < object.y+ object.height and object.x <= pp.x < object.x + object.width:
        pp.y += grid
    if object.y < pp.y + pp.height + grid < object.y+ object.height and object.x <= pp.x < object.x + object.width:
        pp.y -= grid
    if object.x < pp.x - grid < object.x + object.width and object.y <= pp.y + pp.height < object.y + object.height:
        pp.x += grid
    if object.x < pp.x + pp.width + grid < object.x + object.width and object.y <= pp.y + pp.height < object.y + object.height:
        pp.x -= grid
    if object.y < pp.y - grid < object.y+ object.height and object.x <= pp.x + pp.width < object.x + object.width:
        pp.y += grid
    if object.y < pp.y + pp.height + grid < object.y+ object.height and object.x <= pp.x + pp.width < object.x + object.width:
        pp.y -= grid

def drawUpdate():
    win.blit(background_image, [0, 0])
    message_bisplay("keys: " + str(len(inventory)), white, size="small")
    bb.draw(win, boy)
    box1.draw(win, one)
    box2.draw(win, two)
    box3.draw(win, three)
    decor1.draw(win, d1)
    decor2.draw(win, d2)
    decor3.draw(win, d3)
    decor4.draw(win, d4)
    decor5.draw(win, d5)
    door.draw(win, dor)
    pygame.display.update()

inventory = []

bb=boi(x,y,30,45)
box1 = box(120,0,110,50)
box2 = box(410, 40, 40, 100)
box3 = box(0, 410, 70, 40)
decor1 = decor(0, 150, 55,200)
decor2 = decor(250, 0, 200, 40)
decor3 = decor(400, 210, 50, 240)
decor4 = decor(300, 410, 100, 40)
decor5 = decor(70, 425, 140, 30)
door = exitt(0,60, 15, 60)

trivia1 = False
trivia2 = False
trivia3 = False
incorrect = False
end = False

while beg:
    clock.tick(5)
    win.fill(grey)
    message_display("The Escape Room", white, 0, -20, size="medium")
    message_display("Press 'p' to Play", white, 0, 40, size="small")
    message_display("when in-game, press 'e' to interact with objects", white, 0, 150, size="s_small")
    message_display("use the arrow keys to move", white, 0, 175, size="s_small")
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            beg = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                beg = False
                intro = True

while intro:
    clock.tick(5)
    win.fill(grey)
    message_display("Solve clues around the room to", white, 0, -60, size="small")
    message_display("obtain keys.", white, 0, -30, size="small")
    message_display("When you get 2 keys, find the door", white, 0, 10, size="small")
    message_display("to escape!", white, 0, 40, size="small")
    message_display("(press 'p' to continue)", white, 0, 150, size="s_small")
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            intro = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                intro = False
                run = True
    
while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.KEYUP:
            x_move = True
            y_move = True

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        bb.x -= grid
        x_move = True
    elif keys[pygame.K_RIGHT]:
        bb.x += grid
        x_move = True
    elif keys[pygame.K_UP]:
        bb.y -= grid
        y_move = True
    elif keys[pygame.K_DOWN]:
        bb.y += grid
        y_move = True
    elif keys[pygame.K_e]:
        pygame.event.get()
        if (box1.x <= bb.x - grid <= box1.x + box1.width and box1.y <= bb.y - grid <= box1.y + box1.height) or (box1.x <= bb.x + bb.width + grid <= box1.x + box1.width and box1.y <= bb.y + bb.height + grid <= box1.y + box1.height):         
            if 'Key_1' not in inventory:
                pygame.event.get()
                print("hi")
                trivia1 = True
                while trivia1:
                    clock.tick(20)
                    drawTrivia()
                    events = pygame.event.get()
                    for event in events:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_a:
                                print("hi")
                                trivia1 = False
                                incorrect = True
                            if event.key == pygame.K_b:
                                print("ih")
                                trivia1 = False
                                trivia2 = True
                            if event.key == pygame.K_c:
                                print("ih")
                                trivia1 = False
                                incorrect = True
                    while incorrect:
                        clock.tick(20)
                        Incorrect()
                        events = pygame.event.get()
                        for event in events:
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_f:
                                    print("df")
                                    pygame.event.get()
                                    incorrect = False
                                    trivia1 = True

                while trivia2:
                    clock.tick(20)
                    drawTrivia2()
                    events = pygame.event.get()
                    for event in events:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_b:
                                print("hi")
                                trivia2 = False
                                incorrect = True
                                if event.key == pygame.K_SPACE:
                                    drawTrivia()
                            if event.key == pygame.K_a:
                                print("ih")
                                trivia2 = False
                                trivia3 = True
                            if event.key == pygame.K_c:
                                print("ih")
                                trivia2 = False
                                incorrect = True
                    while incorrect:
                        clock.tick(20)
                        Incorrect()
                        events = pygame.event.get()
                        for event in events:
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_f:
                                    print("df")
                                    pygame.event.get()
                                    incorrect = False
                                    trivia2 = True
                while trivia3:
                    clock.tick(20)
                    drawTrivia3()
                    events = pygame.event.get()
                    for event in events:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_a:
                                print("hi")
                                trivia2 = False
                                incorrect = True
                                if event.key == pygame.K_SPACE:
                                    drawTrivia()
                            if event.key == pygame.K_c:
                                print("ih")
                                trivia3 = False
                                inventory.append('Key_1')
                                print(len(inventory))
                            if event.key == pygame.K_b:
                                print("ih")
                                trivia2 = False
                                incorrect = True
                    while incorrect:
                        clock.tick(20)
                        Incorrect()
                        events = pygame.event.get()
                        for event in events:
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_f:
                                    print("df")
                                    pygame.event.get()
                                    incorrect = False
                                    trivia3 = True

        elif (box2.x <= bb.x + grid <= box2.x + box2.width and box2.y <= bb.y + grid <= box2.y + box2.height) or (box2.x <= bb.x + bb.width + grid <= box2.x + box2.width and box2.y <= bb.y + bb.height + grid <= box2.y + box2.height):
            if 'Key_1' in inventory and 'Key_2' not in inventory:
                pygame.event.get()
                print("bi")
                maze = True
                while maze:
                    clock.tick(20)
                    drawMaze()
                    pygame.event.get()
                    if (mb.x + mb.width) > 420:
                        mb.x -= (grid*3)/3 
                    elif mb.x < 30:
                        mb.x += (grid*3)/3 
                    elif (mb.y + mb.height) > 420:
                        mb.y -= (grid*3)/3  
                    elif mb.y < 30:
                        mb.y += (grid*3)/3 
                    keys = pygame.key.get_pressed()
                    pygame.event.get()
                    if keys[pygame.K_LEFT]:
                        mb.x -= (grid*3)/3 
                        x_move = True
                    elif keys[pygame.K_RIGHT]:
                        mb.x += (grid*3)/3 
                        x_move = True
                    elif keys[pygame.K_UP]:
                        mb.y -= (grid*3)/3 
                        y_move = True
                    elif keys[pygame.K_DOWN]:
                        mb.y += (grid*3)/3 
                        y_move = True

                    collisions(w1, mb)
                    collisions(w2, mb)
                    collisions(w3, mb)
                    collisions(w4, mb)
                    collisions(w5, mb)
                    collisions(w6, mb)
                    collisions(w7, mb)
                    collisions(w8, mb)
                    collisions(w9, mb)
                    collisions(w10, mb)
                    collisions(w11, mb)
                    collisions(w12, mb)
                    collisions(w13, mb)
                    collisions(w14, mb)
                    collisions(w15, mb)
                    collisions(w16, mb)
    
                    if mb.x + mb.width >= 410 and mb.y + mb.height >= 410:
                        inventory.append('Key_2')
                        print(len(inventory))
                        maze = False
        if 'Key_1' in inventory and 'Key_2' in inventory:
            if (door.x <= bb.x - grid <= door.x + door.width and door.y <= bb.y + grid <= door.y + door.height) or (door.x <= bb.x + bb.width - grid <= door.x + door.width and door.y <= bb.y + bb.height + grid <= door.y + box2.height):
                end = True
                while end:
                    clock.tick(20)
                    endD()
                    
                    

  #edges          
    if (bb.x + bb.width) > screenw -1:
        bb.x -= grid 
    elif bb.x < 1:
        bb.x += grid 
    elif (bb.y + bb.height) > screenh - 1:
        bb.y -= grid 
    elif bb.y < 1:
        bb.y += grid 

    collisions(box1, bb)
    collisions(box2, bb)
    collisions(box3, bb)
    collisions(decor1, bb)
    collisions(decor2, bb)
    collisions(decor3, bb)
    collisions(decor4, bb)
    collisions(decor5, bb)
    collisions(door, bb)
        
    drawUpdate()

pygame.quit()
quit()

  
