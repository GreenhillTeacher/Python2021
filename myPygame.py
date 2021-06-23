#Maria Suarez
#C:\Users\suarezm\Documents\python\Python2021
# K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow
# K_LEFT                left arrow
import time, sys, pygame
print(sys.path)
pygame.init() #Initialize the game
pygame.time.delay(100)  #delay in milliseconds
WIDTH=500
HEIGHT=600
#create the object with images
bg=pygame.image.load("Images/backGr.png")
some=pygame.image.load("Images/robot.png")
white=[255,255,255]
purple=[200,190,0]
green=[50,25,255]
blue=[0,0,255]
#create object to open window

screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(purple)
screen.blit(bg,(0,0)) #place image oevrlaping
pygame.display.set_caption('My Game') #Chanhe title onn the screen and you can also change icon
pygame.display.update() #command to actually do something
#you must always ....ALWAYS
check = True
x=10
y=10
xR=50
yR=70
x1=40
y1=50
rad=30
hbox, wbox =20,20
rect=pygame.Rect(x,y,wbox,hbox) #this creates a rectangle
rect1=pygame.Rect(x1,y1,wbox,hbox)
JumpCheck=False
jump=10
while check:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            check = False
    speed=5
    keyBoardKey=pygame.key.get_pressed()  #checking what key ispressed
    if keyBoardKey[pygame.K_LEFT]:   #Moving left on x (-)
        rect.x -=speed
        xR -= speed   
    if keyBoardKey[pygame.K_RIGHT]: #Moving right on x (+)
        rect.x += speed
        xR += speed
#is to check if we are going to jump

    if not JumpCheck:
        if keyBoardKey[pygame.K_UP]:        #Moving up on y (-)
            rect.y -= speed 
            yR -= speed
        if keyBoardKey[pygame.K_DOWN]:        #Moving down on y (+)
            rect.y += speed
            yR += speed
        if keyBoardKey[pygame.K_SPACE]:
            JumpCheck=True
    else:
        if jump >=-10:
            rect.y -=(jump*abs(jump))/2
            yR -=(jump*abs(jump))/2
            jump-=1
        else:
            jump = 10
            JumpCheck=False
    if keyBoardKey[pygame.K_s]:
        rad -= speed
    if keyBoardKey[pygame.K_f]:
        rad += speed
    if keyBoardKey[pygame.K_a]:   #Moving left on x (-)
        rect1.x -=speed       
    if keyBoardKey[pygame.K_d]: #Moving right on x (+)
        rect1.x += speed
    if keyBoardKey[pygame.K_w]:        #Moving up on y (-)
        rect1.y -= speed
    if keyBoardKey[pygame.K_x]:        #Moving down on y (+)
        rect1.y += speed
    if rect.x < 0: rect.x=0
    if rect.x > WIDTH-wbox: rect.x = WIDTH-wbox
    if rect.y < 0: rect.y=0
    if rect.y > HEIGHT - hbox: rect.y=HEIGHT - hbox
    if rad < 0: rad=1
    if rad > WIDTH-x: rad = WIDTH-x
    if rect.colliderect(rect1):
        rect.x -=3
        rect1.x +=3
    screen.fill(purple)
    screen.blit(bg,(0,0))
    screen.blit(some, (x,y))
    pygame.draw.rect(screen,(blue),rect1)
    pygame.draw.rect(screen,(green),rect)
    pygame.draw.circle(screen,(white),(x+300,y+200),rad,2)
    pygame.display.flip()
    pygame.time.delay(30)
pygame.quit()


