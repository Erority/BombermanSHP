import pygame
from pygame.locals import *

# Game Initialization
pygame.init()


# Game Resolution
screen_width=1280
screen_height=720
screen=pygame.display.set_mode((screen_width, screen_height))

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText


# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(5, 77, 18)
blue=(0, 0, 255)
yellow=(230, 211, 9)
orange=(209, 107, 4)
light_orange=(237, 198, 97)

# Game Fonts
font = "Retro.ttf"


# Game Framerate
clock = pygame.time.Clock()
FPS=30

# Main Menu
def main_menu():

    menu=True
    selected="start"

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        print("Start")
                    if selected=="quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.fill(green)
        title=text_format("Bomberman", font, 150, orange)
        if selected=="start":
            text_start=text_format("START", font, 100, yellow)
        else:
            text_start = text_format("START", font, 100, light_orange)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 100, yellow)
        else:
            text_quit = text_format("QUIT", font, 100, light_orange)

        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 380))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Bomberman")

#Initialize the Game
main_menu()
pygame.quit()
quit()