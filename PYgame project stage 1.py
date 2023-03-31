import pygame
import os

pygame.init()
# contant values
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("banana.png")),
      pygame.image.load(os.path.join("banana.png"))]
JUMPING = pygame.image.load(os.path.join("banana.png"))
OBSTACLE = [pygame.image.load(os.path.join("banana.png")),
       pygame.image.load(os.path.join("banana.png"))]      
     
class sprite:
       x_pos = 80
       y_pos = 210

       def __init__(self):
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.sprite_run = True
        self.sprite_jump = False

        self.step_index = 0
        self.image = self.run_img[0]
        self.sprite_rect = self.image.get_rect() 
        self.sprite_rect.y = self.y_pos
        self.sprite_rect.x = self.x_pos

def update(self, userInput):
       if self.sprite_run:
              self.run()
       if self.sprite_jump:
              self.jump()
       if self.step_index >= 10:
              self.step_index = 0

       if userInput[pygame.K_UP] and not self.sprite_jump:
              self.sprite_jump = True
              self.sprite_run = False
       elif not self.sprite_jump:
              self.sprite_jump = False
              self.sprite_run = True
def run(self):
       pass
def main() :
    run = True
    clock = pygame.time.Clock()
    player = sprite()

    while run:
        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("working")
        SCREEN.fill((255,255,255))
        pygame.display.flip()

main()
pygame.quit()