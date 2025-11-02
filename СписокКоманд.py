#pyton

a = 1

#ДОП:
#l = x.split(" ")
#l = list(x)

#БЛОКИ:
#x = lambda a: a*a
#print(x(4))
#----------------------------
#def add(a, b):
#   return a + b
#x = add(3, 5)



#СПИСКИ:
#x = {1, 2, 2, 3}
#x.add(4)
#-----------------------------
#x = {"a": "абв", "b": 123}
#print(x["a"])
#x["a"] = "вба"
#-----------------------------
#x = [1, 2, 3]
#print(x[0])
#x.append(4)


#ЦИКЛЫ:
#while x < 5:
#for i in range(0):
#----------------------------
#if x < y:
#elif x > y:
#else:

#or and

#x = input("??? ")
#x += 1 / x -= 1
#x = "Привет!" / x = 5 
#type(x)
#y = int(x)   -в число
#y = str(x)   -в слово
#y = float(x) -в ?
#len(x)
#print(x)



levels = [
    {
        "name": "Level 1",
        "backroud_image": "Pr/backround_level1.png",
        "questions": [
            {
                "text": "Как меня зовут?",
                "answers": [
                    {"text": "Миша", "correct": True},
                    {"text": "Masha", "correct": False},
                    {"text": "Vova", "correct": False},
                    {"text": "Ivan", "correct": False},
                ],
            },
            {
                "text": "Vopros 2?",
                "answers": [
                    {"text": "Миша", "correct": True},
                    {"text": "Masha", "correct": True},
                    {"text": "Vova", "correct": True},
                    {"text": "Ivan", "correct": False},
                ],
            },
        ],
    },
    {
        "name": "Level 2",
        "questions": [
            {
                "text": "Как меня зовут?",
                "answers": [
                    {"text": "Миша", "correct": True},
                    {"text": "Masha", "correct": True},
                    {"text": "Vova", "correct": True},
                    {"text": "Ivan", "correct": False},
                ],
            }
        ],
    },
]

print(levels[0]["questions"][0]["answers"][0]["text"])



pygame

import pygame #импортируем pygame
pygame.init() #запускаем pygame

screen = pygame.display.set_mode((a, a)) #задаём размер окна
pygame.display.set_caption("a") #задаём название окна
pygame.display.set_icon(pygame.image.load('t/a.png')) #задаём иконку окна

a = pygame.image.load('t/a.png').convert_alpha() #загрузка абекта
pygame.mixer.Sound('t/a.mp3').play() #включение музыки

pygame.display.update() #атрисовка картинки окна
screen.blit(pygame.image.load('t/a.png').convert_alpha(), (a, a)) #отресовка абекта
pygame.time.Clock().tick(10) #тик задержки

a = a.get_rect(topleft=(a, a)) #задаёт хитбокс (картинка.get_rect(topleft=(координата х, координата у)))
if a.colliderect(a): #проверка саприкосновения хитбоксов
    print("a") #пишит сообщение

keys = pygame.key.get_pressed() #переменная, проверяющая нажатость клавиш
if keys[pygame.K_LEFT]: #проверка нажатости
    print("a") #пишит сообщение

if pygame.key.get_pressed()[pygame.K_LEFT]:
    print("a") #пишит сообщение


screen.fill((255, 255, 255)) #изменение цвета фона
cub = pygame.Surface((50, 50))
cub.fill((0, 255, 0))
screen.blit(pygame.Surface((50, 50)), (100, 100))
pygame.draw.circle(screen, (0, 0, 0), (250, 150), 30)

font = pygame.font.Font(None, 48)
text_surface = font.render("Привет, Pygame!", True, (0, 0, 0))

#X_b = pygame.Rect(0, 0, 500, 500)
#    if X_b.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
#        print("да")
#        elif X_b.collidepoint(mouse_pos):
#        print("возможно")
#    else:
#        print("нет")



run = True
for event in pygame.event.get(): #блок по выключению программы
        if event.type == pygame.QUIT:
            run = False

pygame.quit() #выключение игры