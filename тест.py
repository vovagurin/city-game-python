import pygame #импортируем pygame
clock = pygame.time.Clock() #задаём време
pygame.init() #запускаем pygame

info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
print(info)

screen = pygame.display.set_mode((1555, 886), pygame.RESIZABLE) #задаём размер окна
pygame.display.set_caption("тест") #задаём название окна
pygame.display.set_icon(pygame.image.load('test/книга.png')) #задаём иконку окна


bg = pygame.image.load('test/фон тест.png').convert_alpha() #загрузка мадэли фона
bol = pygame.image.load('test/шар.png').convert_alpha() #загрузка мадэли шара
#player = pygame.image.load('test/pers/+0.png')
#списки анимации персонажа
walk_left = [
    pygame.image.load('test/pers/{0.png').convert_alpha(),
    pygame.image.load('test/pers/{1.png').convert_alpha(),
    pygame.image.load('test/pers/{2.png').convert_alpha()
]
walk_right = [
    pygame.image.load('test/pers/}0.png').convert_alpha(),
    pygame.image.load('test/pers/}1.png').convert_alpha(),
    pygame.image.load('test/pers/}2.png').convert_alpha()
]
walk_up = [
    pygame.image.load('test/pers/^0.png').convert_alpha(),
    pygame.image.load('test/pers/^1.png').convert_alpha(),
    pygame.image.load('test/pers/^2.png').convert_alpha()
]
walk_dawn = [
    pygame.image.load('test/pers/+0.png').convert_alpha(),
    pygame.image.load('test/pers/+1.png').convert_alpha(),
    pygame.image.load('test/pers/+2.png').convert_alpha()
]




player_walk = 0 #переменная(номер идущей кортинки анимации)
bg_x = 0 #переменная(координата х фона)
player_speed = 10 #переменная(скорость перса)
player_x = 200 #переменная(координата х перса)
player_y = 500 #переменная(координата у перса)
bol_x = 1100 #переменная(координата х шара)
is_jump = False #переменная(прыгает ли)
jump_count = 7 #переменная(сила прыжка)



bg_saunds = pygame.mixer.Sound('test/saunds/музло.mp3') #загрузка музыки
bg_saunds.play() #включение музыки




run = True #вспомагательная переменная, обозначающая работу программы
while run: #цикл программы

    pygame.display.update() #атрисовка картинки окна
    clock.tick(10) #тик задержки

    keys = pygame.key.get_pressed() #переменная, проверяющая нажатость клавиш



    player_rect = walk_left[0].get_rect(topleft=(player_x, player_y)) #задаёт хитбокс перса (картинка.get_rect(topleft=(координата х, координата у)))
    bol_rect = bol.get_rect(topleft=(bol_x, 500)) #задаёт хитбокс шара (картинка.get_rect(topleft=(координата х, координата у)))

    if player_rect.colliderect(bol_rect): #проверка саприкосновения перса и шара
        print("ты проиграл") #пишит сообщение

    screen.blit(bg, (bg_x, 0)) #отресовка фона
    screen.blit(bg, (bg_x + 1555, 0)) #отресовка доп фона
    if keys[pygame.K_LEFT]: #если нажата стрелка в лева
        screen.blit(walk_left[player_walk], (player_x, player_y)) #отресовка перса (список[номер картинки],(координата х, координата у))
    elif keys[pygame.K_RIGHT]: #если нажата стрелка в право
        screen.blit(walk_right[player_walk], (player_x, player_y)) #отресовка перса (список[номер картинки],(координата х, координата у))
    else:
        screen.blit(walk_right[player_walk], (player_x, player_y)) #отресовка перса (список[номер картинки],(координата х, координата у))
    screen.blit(bol, (bol_x, 500)) #отресовка шара


    
    if keys[pygame.K_LEFT] and player_x > 50: #перемещение
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 1500:
        player_x += player_speed

    if not is_jump: #прыжок
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -7:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -=1
        else:
            is_jump = False
            jump_count = 7


    if player_walk == 2: #переключение слайдов анимации перса
        player_walk = 0
    else:
        player_walk += 1

    bg_x -= 5
    if bg_x == -1555: #перемещение фона
        bg_x = 0


    for event in pygame.event.get(): #блок по выключению программы
        if event.type == pygame.QUIT:
            run = False
            pygame.quit() #выключение игры


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                screen.fill((227, 73, 7)) #изменение цвета фона
            
            elif event.key == pygame.K_x:
                screen.fill((66, 135, 245)) #изменение цвета фона
            
            elif event.key == pygame.K_c:
                screen.fill((127, 25, 38)) #изменение цвета фона


                












