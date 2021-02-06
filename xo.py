import pygame as pg
from pygame.constants import MOUSEBUTTONUP

quit = False
state = 0 # 0 -> Main menu , 1 -> Game , 2 -> End
turn = 0 # 0 -> x , 1 -> o
lock = [0] * 9 # 0 -> unlock , 1 -> lock
col = [2] * 9 # 0 -> x , 1 -> y , 2 -> None
SCREEN_WIDTH = 570
SCREEN_HEIGHT = 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_CAPTION = "XO" 

pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption(SCREEN_CAPTION)

font1 = pg.font.Font('freesansbold.ttf', 20)

start_two_mode_text = font1.render('Play two people mode', True, BLACK)
start_two_mode_text_rect = start_two_mode_text.get_rect()
start_two_mode_text_rect.center = (SCREEN_WIDTH / 2, 340)

main_exit_text = font1.render('Exit', True, BLACK)
main_exit_text_rect = main_exit_text.get_rect()
main_exit_text_rect.center = (SCREEN_WIDTH / 2, 400)

table = pg.image.load(r'res\\xo-table.png')
table = pg.transform.scale(table, (450, 380))

table_exit_text = font1.render('Back to main menu', True, BLACK)
table_exit_text_rect = table_exit_text.get_rect()
table_exit_text_rect.center = (SCREEN_WIDTH / 2, 470)

x_img = pg.image.load(r'res\\x.png')
x_img = pg.transform.scale(x_img, (144, 120))

o_img = pg.image.load(r'res\\o.png')
o_img = pg.transform.scale(o_img, (144, 120))

def main_menu():
    screen.fill(WHITE)
    screen.blit(x_img, (210, 150))
    screen.blit(o_img, (210, 150))
    screen.blit(start_two_mode_text, start_two_mode_text_rect)
    screen.blit(main_exit_text, main_exit_text_rect)

def game_space():
    screen.fill(WHITE)
    screen.blit(table, (60, 50))
    screen.blit(table_exit_text, table_exit_text_rect)

def check_win():
    global state

    if col[0] == 0 and col[1] == 0 and col[2] == 0:
        print('X win!')
        state = 2
    elif col[3] == 0 and col[4] == 0 and col[5] == 0:
        print('X win!')
        state = 2
    elif col[6] == 0 and col[7] == 0 and col[8] == 0:
        print('X win!')
        state = 2
    elif col[0] == 0 and col[3] == 0 and col[6] == 0:
        print('X win!')
        state = 2
    elif col[1] == 0 and col[4] == 0 and col[7] == 0:
        print('X win!')
        state = 2
    elif col[2] == 0 and col[5] == 0 and  col[8] == 0:
        print('X win!')
        state = 2
    elif col[0] == 0 and col[4] == 0 and col[8] == 0:
        print('X win!')
        state = 2
    elif col[2] == 0 and col[4] == 0 and col[6] == 0:
        print('X win!')
        state = 2
    elif col[0] == 1 and col[1] == 1 and col[2] == 1:
        print('O win!')
        state = 2
    elif col[3] == 1 and col[4] == 1 and col[5] == 1:
        print('O win!')
        state = 2
    elif col[6] == 1 and col[7] == 1 and col[8] == 1:
        print('O win!')
        state = 2
    elif col[0] == 1 and col[3] == 1 and col[6] == 1:
        print('O win!')
        state = 2
    elif col[1] == 1 and col[4] == 1 and col[7] == 1:
        print('O win!')
        state = 2
    elif col[2] == 1 and col[5] == 1 and  col[8] == 1:
        print('O win!')
        state = 2
    elif col[0] == 1 and col[4] == 1 and col[8] == 1:
        print('O win!')
        state = 2
    elif col[2] == 1 and col[4] == 1 and col[6] == 1:
        print('O win!')
        state = 2

def main_on_click():
    x, y = pg.mouse.get_pos()
    global state
    global quit

    if x >= 177 and x <= 394 and y >= 337 and y <= 350:
        game_space()
        state = 1
    elif x >= 265 and x <= 308 and y >= 388 and y <= 410:
        quit = True

def game_on_click():
    x, y = pg.mouse.get_pos()
    global state
    global turn
    
    if state != 2:
        if x >= 60 and x <= 204 and y >= 50 and y <= 170:
            if turn == 0 and lock[0] == 0:
                screen.blit(x_img, (60, 50))
                turn = 1
                lock[0] = 1
                col[0] = 0
            elif turn == 1 and lock[0] == 0:
                screen.blit(o_img, (60, 50))
                turn = 0
                lock[0] = 1
                col[0] = 1
        elif x >= 214 and x <= 366 and y >= 50 and y <= 170:
            if turn == 0 and lock[1] == 0:
                screen.blit(x_img, (214, 50))
                turn = 1
                lock[1] = 1
                col[1] = 0
            elif turn == 1 and lock[1] == 0:
                screen.blit(o_img, (214, 50))
                turn = 0
                lock[1] = 1
                col[1] = 1
        elif x >= 374 and x <= 510 and y >= 50 and y <= 170:
            if turn == 0 and lock[2] == 0:
                screen.blit(x_img, (374, 50))
                turn = 1
                lock[2] = 1
                col[2] = 0
            elif turn == 1 and lock[2] == 0:
                screen.blit(o_img, (374, 50))
                turn = 0
                lock[2] = 1
                col[2] = 1
        elif x >= 60 and x <= 204 and y >= 182 and y <= 306:
            if turn == 0 and lock[3] == 0:
                screen.blit(x_img, (60, 182))
                turn = 1
                lock[3] = 1
                col[3] = 0
            elif turn == 1 and lock[3] == 0:
                screen.blit(o_img, (60, 182))
                turn = 0
                lock[3] = 1
                col[3] = 1
        elif x >= 214 and x <= 366 and y >= 182 and y <= 306:
            if turn == 0 and lock[4] == 0:
                screen.blit(x_img, (212, 182))
                turn = 1
                lock[4] = 1
                col[4] = 0
            elif turn == 1 and lock[4] == 0:
                screen.blit(o_img, (212, 182))
                turn = 0
                lock[4] = 1
                col[4] = 1
        elif x >= 374 and x <= 510 and y >= 182 and y <= 306:
            if turn == 0 and lock[5] == 0:
                screen.blit(x_img, (374, 182))
                turn = 1
                lock[5] = 1
                col[5] = 0
            elif turn == 1 and lock[5] == 0:
                screen.blit(o_img, (374, 182))
                turn = 0
                lock[5] = 1
                col[5] = 1
        elif x >= 60 and x <= 204 and y >= 316 and y <= 430:
            if turn == 0 and lock[6] == 0:
                screen.blit(x_img, (60, 316))
                turn = 1
                lock[6] = 1
                col[6] = 0
            elif turn == 1 and lock[6] == 0:
                screen.blit(o_img, (60, 316))
                turn = 0
                lock[6] = 1
                col[6] = 1
        elif x >= 214 and x <= 366 and y >= 316 and y <= 430:
            if turn == 0 and lock[7] == 0:
                screen.blit(x_img, (214, 316))
                turn = 1
                lock[7] = 1
                col[7] = 0
            elif turn == 1 and lock[7] == 0:
                screen.blit(o_img, (214, 316))
                turn = 0
                lock[7] = 1
                col[7] = 1
        elif x >= 374 and x <= 510 and y >= 316 and y <= 430:
            if turn == 0 and lock[8] == 0:
                screen.blit(x_img, (374, 316))
                turn = 1
                lock[8] = 1
                col[8] = 0
            elif turn == 1 and lock[8] == 0:
                screen.blit(o_img, (374, 316))
                turn = 0
                lock[8] = 1
                col[8] = 1
    
    a = 0
    b = 0
    for i in range(9):
        if col[i] == 0:
            a += 1
        if col[i] == 1:
            b += 1

    if a == 3:
        check_win()
        a = 0
        b = 0
    if b == 3:
        check_win()
        a = 0
        b = 0
    if (a + b) == 9 and state != 2:
        print('Draw')
        state = 2
        a = 0
        b = 0

main_menu()

while not quit:
    for event in pg.event.get():
        x, y = pg.mouse.get_pos()

        if event.type == pg.QUIT:
            quit = True
        elif event.type == pg.MOUSEBUTTONUP:
            if state == 0:
                main_on_click()
            elif state == 1 and state != 2:
                game_on_click()
            elif state == 2:
                if x >= 192 and x <= 380 and y >= 458 and y <= 478:
                    state = 0
                    for i in range(9):
                        lock[i] = 0
                        col[i] = 2
                    main_menu()
    
    pg.display.update()
    CLOCK.tick(fps)