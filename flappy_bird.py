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
print(type(bg)) # Surface object
# now we want to bring this bg on our main screen
# We dont want it in full screen , We want it in center

# We will load the image for base
base = pygame.image.load("Images/base.png")

# We will make a bird class and write its attributes
class Bird :

    #  Here we are making constructor(can say)
    def __init__(self , pos):
        # Load the iamge of bird
        self.image = pygame.image.load("Images/bird.png")
        # Load function returns the surface object
        # We want rectangle around it
        self.rect = self.image.get_rect()
        # It will return rect kind of object and its x , y is by default 0
        # We want to change its x and y according to our provided position
        self.rect.x , self.rect.y = pos
        # Velocity will be there
        self.vel = 3
        # jab tak hum space press nahi karenge by default bird niche aaegi
        self.fly = False

    # Drawing our bird on screen
    def draw(self  ,screen) :
        screen.blit(self.image , (self.rect.x , self.rect.y))

# Game Start
def gamestart(screen) :

    # We will make instance of Bird class
    b = Bird((50,300))

    # Why we need to write loop -> beacuse this is something we want to do continuously till user apne aap cut karde ya game over ho jae
    run = True
    while run :

        screen.fill(SKY_BLUE)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False

        # Want to draw bird so calling function of draw
        b.draw(screen)

        # place Base image
        screen.blit(base , (0,400))

        pygame.display.update()


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


        # Now as we can see according to image , on tapping on screen , the game should start
        # If we give any input from our kewboard or mouse so that is event(it means we are tring to interact) for our game
        # Now question is how to detect tap
        # here MOUSEBUTTONDOWN , means mouse ko dabana
        # MOUSEBUTTONUP , means mouse ko release karna
        # event.button == 1 to check left click h ki nahi
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            print("START THE GAME")
            gamestart(screen)

    # aapki screen pe jo bhi changes aa rahe h unhe unpade karne ke liye
    pygame.display.update()





