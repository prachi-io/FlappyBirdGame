# We will import packages
import pygame , random
# pygame has many modules , we need to initialize all modules
pygame.init()

# color for background
SKY_BLUE = (80, 164, 217)

# screen has dimensions
w,h = 300 , 500
# we need to create the screen
screen = pygame.display.set_mode((w,h))

# To set the caption
pygame.display.set_caption("FLAPPY BIRD")

# we need to set icon/logo of our game
# we need to load the image then only we will be able to set it
icon = pygame.image.load("Images/bird.png")
#  now we set it on our screen
pygame.display.set_icon(icon)

# we will load our background image
bg = pygame.image.load("Images/intro.png")
# now we want to bring this bg on our main screen
# We dont want it in full screen , We want it in center

# we are running a loop for closing the game window when it is completed
run = True
while run :

    # As background color is black but i want a different color
    screen.fill(SKY_BLUE)

    # we want to set background image in center
    screen.blit(bg,(50,100))

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False

    # aapki screen pe jo bhi changes aa rahe h unhe unpade karne ke liye
    pygame.display.update()



