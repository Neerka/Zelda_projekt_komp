import pygame
pygame.init()

win_width = 1280
win_height = 780

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Zedla - projekt')


class player(object):
    def __init__(self, x, y, char_width, char_heigth):
        self.x = x
        self.y = y
        self.char_width = char_width
        self.char_heigth = char_heigth
        self.velocity = 3
        self.d_con = win_width - char_width
        self.s_con = win_height - char_heigth
        self.isRoll = False
        self.rollCount = 9
        self.sprintCount = 100

    def move(self):
        if keys[pygame.K_LSHIFT]:
            self.velocity = 6
        else:
            self.velocity = 3
        if keys[pygame.K_d] and self.x < self.d_con:
            self.x += self.velocity
        if keys[pygame.K_a] and self.x > 0:
            self.x -= self.velocity
        if keys[pygame.K_w] and self.y > 0:
            self.y -= self.velocity
        if keys[pygame.K_s] and self.y < self.s_con:
            self.y += self.velocity

    def roll(self):
        if self.rollCount >= 0:
            if (keys[pygame.K_d] and self.x < self.d_con) or (keys[pygame.K_a]
                                                              and self.x > 0):
                if keys[pygame.K_d]:
                    course = 1
                if keys[pygame.K_a]:
                    course = -1
                if keys[pygame.K_a] and keys[pygame.K_d]:
                    course = 0
                self.x += (self.rollCount**2)*0.2*course
            if (keys[pygame.K_w] and self.y > 0) or (keys[pygame.K_s]
                                                     and self.y < self.s_con):
                if keys[pygame.K_w]:
                    course = -1
                if keys[pygame.K_s]:
                    course = 1
                if keys[pygame.K_w] and keys[pygame.K_s]:
                    course = 0
                self.y += (self.rollCount**2)*0.2*course
            self.rollCount -= 1
        else:
            self.isRoll = False
            self.rollCount = 9


run = True
gracz = player(608, 328, 48, 48)
while run:
    pygame.time.delay(16)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    gracz.move()
    if not gracz.isRoll:
        if keys[pygame.K_SPACE]:
            gracz.isRoll = True
    else:
        gracz.roll()
    if keys[pygame.K_ESCAPE]:
        run = False

    win.fill((40, 40, 65))
    pygame.draw.rect(win, (100, 200, 0), (gracz.x, gracz.y,
                     gracz.char_width, gracz.char_heigth))
    pygame.display.update()

pygame.quit()
