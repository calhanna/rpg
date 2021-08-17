import pygame

SPEED = 5

class Player(pygame.sprite.Sprite):
    """ Player Class """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32,32))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)

    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]: self.rect.y -= SPEED
        if keys[pygame.K_a]: self.rect.x -= SPEED
        if keys[pygame.K_s]: self.rect.y += SPEED
        if keys[pygame.K_d]: self.rect.x += SPEED

