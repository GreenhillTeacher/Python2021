#MAria Suarez
#learn how change colors
#LEarn to draw shapes
#Lear ho to control objects on the screen with key
# K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow
# K_LEFT                left arrow
import time, sys, pygame, os
os.system('cls')
pygame.init() #Initialize the game
purple=[200,0,200]
white=[255,255,255]
red=[200,25,0]
green=[0,200,50]
WIDTH=500
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))  #declare our screen or window
screen.fill(purple)
BG=pygame.image.load("Images2\\BackGround.jpg")
Andy=pygame.image.load("Images2\\robotico.png")
pygame.time.delay(100)  #delay in milliseconds
pygame.display.set_caption("My game")
xa=10
yb=10
x1=40
y1=50
wbox=20
hbox=20
rect1=pygame.Rect(xa,yb,wbox,hbox)
rect2=pygame.Rect(x1,y1,wbox,hbox)
#VAriables to control our rect 
speed=5
jump = 10
rad=30
check=True
JumpCheck=False
while check:       
     # ALL YOUR PROGRAMS WITH PYGAME MUST HAVE THIS PART
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            check = False
    #================================================
    KB=pygame.key.get_pressed() #Checking is a key has been pressed
    if KB[pygame.K_RIGHT]:
        rect1.x +=speed  #move rectangle two pixels to the right
        xa +=(speed)
        rad += speed
    if KB[pygame.K_LEFT]:
        rect1.x -=speed  #move rectangle two pixels to the left
        xa -= speed
        rad -= speed
    #Code for Jumping
    if not JumpCheck:
        if KB[pygame.K_UP]:
            rect1.y -=speed  #move rectangle two pixels up
            yb -=speed
        if KB[pygame.K_DOWN]:
            rect1.y +=speed  #move rectangle two pixels down
            yb +=speed
        if KB[pygame.K_SPACE]:
            JumpCheck= True
    else:
        if jump >= -10:
            rect1.y -= (jump*abs(jump))/2
            yb -=(jump*abs(jump))/2
            jump -=1
        else:
            jump=10
            JumpCheck=False
        #Control Limits
    
    if KB[pygame.K_a]:   #Moving left on x (-)
        rect2.x -=speed       
    if KB[pygame.K_d]: #Moving right on x (+)
        rect2.x += speed
    if KB[pygame.K_w]:        #Moving up on y (-)
        rect2.y -= speed
    if KB[pygame.K_x]:        #Moving down on y (+)
        rect2.y += speed
        #Control borders for the 1st rect
    if rect1.x <0: rect1.x=0      #control left value of x
    if rect1.x> WIDTH-wbox: rect1.x=WIDTH-wbox  #control right value of x
    if rect1.y <0: rect1.y=0       # control the y up value 
    if rect1.y >HEIGHT-hbox: rect1.y=HEIGHT-hbox
    #Control borders for 2nd rect
    if rect2.x <0: rect2.x=0      #control left value of x
    if rect2.x> WIDTH-wbox: rect2.x=WIDTH-wbox  #control right value of x
    if rect2.y <0: rect2.y=0       # control the y up value 
    if rect2.y >HEIGHT-hbox: rect2.y=HEIGHT-hbox

    if rad <0: rad = 1
    if rad > WIDTH/2: rad=250-xa
    if rect1.colliderect(rect2):
        rect1.x -= 10
        rect2.x += 10
    
    
    screen.fill(purple)
    screen.blit(BG,(0,0))
    screen.blit(Andy,(xa+10,yb+10))
    pygame.draw.rect(screen, red, rect1)
    pygame.draw.rect(screen, white, rect2)
    pygame.draw.circle(screen, (white),(xa+240,yb+300), rad, 2)
    pygame.display.update()
    pygame.time.delay(30)
print("Goodbye")
pygame.time.delay(100)  #delay in milliseconds

pygame.quit()