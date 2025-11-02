import pygame

_pygame_image_load_orig = pygame.image.load
def _pygame_image_load_conv(path):
    surf = _pygame_image_load_orig(path)
    try:
        return surf.convert_alpha()
    except Exception:
        return surf
    
pygame.image.load = _pygame_image_load_conv

#фоны
F_N = pygame.image.load('Pr/f/F_N.png')
F_K = pygame.image.load('Pr/f/F_K.png')
F_L_1 = pygame.image.load('Pr/f/F_L_1.png')
F_L_2 = pygame.image.load('Pr/f/F_L_2.png')
F_L_3 = pygame.image.load('Pr/f/F_L_3.png')
F_L_4 = pygame.image.load('Pr/f/F_L_4.png')
F_L_5 = pygame.image.load('Pr/f/F_L_5.png')
F_L_6 = pygame.image.load('Pr/f/F_L_6.png')
F_L_7 = pygame.image.load('Pr/f/F_L_7.png')
F_L_8 = pygame.image.load('Pr/f/F_L_8.png')
F_L_9 = pygame.image.load('Pr/f/F_L_9.png')
F_L_10 = pygame.image.load('Pr/f/F_L_10.png')
F_L_P = [
    pygame.image.load('Pr/f/F_L_1.png'),
    pygame.image.load('Pr/f/F_L_2.png'),
    pygame.image.load('Pr/f/F_L_3.png'),
    pygame.image.load('Pr/f/F_L_4.png'),
    pygame.image.load('Pr/f/F_L_5.png'),
    pygame.image.load('Pr/f/F_L_6.png'),
    pygame.image.load('Pr/f/F_L_7.png'),
    pygame.image.load('Pr/f/F_L_8.png'),
    pygame.image.load('Pr/f/F_L_9.png'),
    pygame.image.load('Pr/f/F_L_10.png')
]

font_1 = pygame.font.Font(None, 48)
font_2 = pygame.font.Font(None, 48)
font_3 = pygame.font.Font(None, 48)

#print(lvL[0-9]["q"][0-4]["an"][0-3]["t"]) - ответ
#print(lvL[0-9]["q"][0-4]["an"][0-3]["cor"]) - правильность ответа
#print(lvL[0-9]["q"][0-4]["t"]) - вапрос
#print(lvL[0-9]["n"]) - номер Level
#print(lvL[0-9]["g"]) - пройденость
#print(lvL[0-9]["b"]) - балл

lvL = [
    {
        "n": [pygame.font.Font(None, 38).render("общественный", False, (255, 255, 255)), pygame.font.Font(None, 38).render("транспорт", False, (255, 255, 255))],
        "g": 1,
        "b": 0,
        "q": [
            {
                "t": font_2.render("V-1", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-2", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-3", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-4", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-5", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            }
        ]
    },
        {
        "n": font_3.render("школа", False, (255, 255, 255)),
        "g": 0,
        "b": 0,
        "q": [
            {
                "t": font_2.render("V-1", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-2", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-3", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-4", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-5", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            }
        ]
    },
        {
        "n": font_3.render("дом", False, (255, 255, 255)),
        "g": 0,
        "b": 0,
        "q": [
            {
                "t": font_2.render("V-1", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-2", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-3", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-4", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-5", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            }
        ]
    },
        {
        "n": font_3.render("на воде", False, (255, 255, 255)),
        "g": 0,
        "b": 0,
        "q": [
            {
                "t": font_2.render("V-1", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-2", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-3", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-4", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-5", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            }
        ]
    },
        {
        "n": font_3.render("религия", False, (255, 255, 255)),
        "g": 0,
        "b": 0,
        "q": [
            {
                "t": font_2.render("V-1", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-2", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-3", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-4", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-5", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            }
        ]
    },
        {
        "n": pygame.font.Font(None, 35).render("электричество", False, (255, 255, 255)),
        "g": 0,
        "b": 0,
        "q": [
            {
                "t": font_2.render("V-1", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-2", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-3", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-4", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-5", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            }
        ]
    },
        {
        "n": font_3.render("экскурсия", False, (255, 255, 255)),
        "g": 0,
        "b": 0,
        "q": [
            {
                "t": font_2.render("V-1", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-2", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-3", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-4", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-5", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            }
        ]
    },
        {
        "n": font_3.render("улица", False, (255, 255, 255)),
        "g": 0,
        "b": 0,
        "q": [
            {
                "t": font_2.render("V-1", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-2", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-3", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-4", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-5", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            }
        ]
    },
        {
        "n": font_3.render("город", False, (255, 255, 255)),
        "g": 0,
        "b": 0,
        "q": [
            {
                "t": font_2.render("V-1", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-2", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-3", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-4", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-5", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            }
        ]
    },
        {
        "n": font_3.render("на природе", False, (255, 255, 255)),
        "g": 0,
        "b": 0,
        "q": [
            {
                "t": font_2.render("V-1", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-2", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-3", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-4", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("V-5", False, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("o-1", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-2", False, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("o-3", False, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("o-4", False, (0, 0, 0)), "cor": False},
                ],
            }
        ]
    }
]



#уровни
U_lev = [
    [
        pygame.image.load('Pr/k/U/lev/lev_0_1.png'),
        pygame.image.load('Pr/k/U/lev/lev_0_2.png'),
        pygame.image.load('Pr/k/U/lev/lev_0_3.png'),
        pygame.image.load('Pr/k/U/lev/lev_0_4.png'),
        pygame.image.load('Pr/k/U/lev/lev_0_5.png')
    ],
    [
        pygame.image.load('Pr/k/U/lev/lev_1_1.png'),
        pygame.image.load('Pr/k/U/lev/lev_1_2.png'),
        pygame.image.load('Pr/k/U/lev/lev_1_3.png'),
        pygame.image.load('Pr/k/U/lev/lev_1_4.png'),
        pygame.image.load('Pr/k/U/lev/lev_1_5.png')
    ],
    [
        pygame.image.load('Pr/k/U/lev/lev_2_1.png'),
        pygame.image.load('Pr/k/U/lev/lev_2_2.png'),
        pygame.image.load('Pr/k/U/lev/lev_2_3.png'),
        pygame.image.load('Pr/k/U/lev/lev_2_4.png'),
        [
            pygame.image.load('Pr/k/U/lev/lev_2_5_0.png'),
            pygame.image.load('Pr/k/U/lev/lev_2_5_1.png'),
            pygame.image.load('Pr/k/U/lev/lev_2_5_2.png'),
            pygame.image.load('Pr/k/U/lev/lev_2_5_3.png'),
            pygame.image.load('Pr/k/U/lev/lev_2_5_4.png')
        ]
    ],
    [
        pygame.image.load('Pr/k/U/lev/lev_3_1.png'),
        pygame.image.load('Pr/k/U/lev/lev_3_2.png'),
        pygame.image.load('Pr/k/U/lev/lev_3_3.png'),
        pygame.image.load('Pr/k/U/lev/lev_3_4.png'),
        pygame.image.load('Pr/k/U/lev/lev_3_5.png')
    ]
]
U_pra = [
    [
        pygame.image.load('Pr/k/U/pra/pra_0_1.png'),
        pygame.image.load('Pr/k/U/pra/pra_0_2.png'),
        pygame.image.load('Pr/k/U/pra/pra_0_3.png'),
        pygame.image.load('Pr/k/U/pra/pra_0_4.png'),
        pygame.image.load('Pr/k/U/pra/pra_0_5.png')
    ],
    [
        pygame.image.load('Pr/k/U/pra/pra_1_1.png'),
        pygame.image.load('Pr/k/U/pra/pra_1_2.png'),
        pygame.image.load('Pr/k/U/pra/pra_1_3.png'),
        pygame.image.load('Pr/k/U/pra/pra_1_4.png'),
        pygame.image.load('Pr/k/U/pra/pra_1_5.png')
    ],
    [
        pygame.image.load('Pr/k/U/pra/pra_2_1.png'),
        pygame.image.load('Pr/k/U/pra/pra_2_2.png'),
        pygame.image.load('Pr/k/U/pra/pra_2_3.png'),
        pygame.image.load('Pr/k/U/pra/pra_2_4.png'),
        [
            pygame.image.load('Pr/k/U/pra/pra_2_5_0.png'),
            pygame.image.load('Pr/k/U/pra/pra_2_5_1.png'),
            pygame.image.load('Pr/k/U/pra/pra_2_5_2.png'),
            pygame.image.load('Pr/k/U/pra/pra_2_5_3.png'),
            pygame.image.load('Pr/k/U/pra/pra_2_5_4.png')
        ]
    ],
    [
        pygame.image.load('Pr/k/U/pra/pra_3_1.png'),
        pygame.image.load('Pr/k/U/pra/pra_3_2.png'),
        pygame.image.load('Pr/k/U/pra/pra_3_3.png'),
        pygame.image.load('Pr/k/U/pra/pra_3_4.png'),
        pygame.image.load('Pr/k/U/pra/pra_3_5.png')
    ]
]


#другие модэли
Con = pygame.image.load('Pr/k/Con_.png')
Con_a_p = pygame.image.load('Pr/k/Con_a_p.png')
Con_b_p = pygame.image.load('Pr/k/Con_b_p.png')
Con_c_p = pygame.image.load('Pr/k/Con_c_p.png')
Con_d_p = pygame.image.load('Pr/k/Con_d_p.png')

K_nocl_p =  pygame.image.load('Pr/k/K_nocl.png')
K_nocl = pygame.image.load('Pr/k/K_nocl_p.png')

Krest = pygame.image.load('Pr/k/K_nocl_p.png')
Krest_p = pygame.image.load('Pr/k/K_nocl_p.png')
buk = pygame.image.load('Pr/k/K_nocl_p.png')
buk_p = pygame.image.load('Pr/k/K_nocl_p.png')

Ben = [
    pygame.image.load('Pr/k/Ben_b.png'),
    pygame.image.load('Pr/k/Ben_g.png'),
    pygame.image.load('Pr/k/Ben_n.png'),
    pygame.image.load('Pr/k/Ben_n_B.png')
]



le = [
    [
        pygame.image.load('Pr/k/le/le_1_1.png'),
        pygame.image.load('Pr/k/le/le_1_2.png'),
        pygame.image.load('Pr/k/le/le_1_3.png')
    ],
    [
        pygame.image.load('Pr/k/le/le_2_1.png'),
        pygame.image.load('Pr/k/le/le_2_2.png'),
        pygame.image.load('Pr/k/le/le_2_3.png'),
        pygame.image.load('Pr/k/le/le_2_4.png')
    ],
    [
        pygame.image.load('Pr/k/le/le_3_1.png'),
        pygame.image.load('Pr/k/le/le_3_2.png'),
        pygame.image.load('Pr/k/le/le_3_3.png')
    ],
    [
        pygame.image.load('Pr/k/le/le_4_1.png'),
        pygame.image.load('Pr/k/le/le_4_2.png'),
        pygame.image.load('Pr/k/le/le_4_3.png'),
        pygame.image.load('Pr/k/le/le_4_4.png')
    ],
    [
        pygame.image.load('Pr/k/le/le_5_1.png'),
        pygame.image.load('Pr/k/le/le_5_2.png'),
        pygame.image.load('Pr/k/le/le_5_3.png'),
        pygame.image.load('Pr/k/le/le_5_4.png'),
        pygame.image.load('Pr/k/le/le_5_5.png')
    ]
]



#хитбоксы
X_Con_a = pygame.Rect(0, 35, 640, 70)
X_Con_b = pygame.Rect(0, 135, 640, 70)
X_Con_c = pygame.Rect(0, 235, 640, 70)
X_Con_d = pygame.Rect(0, 335, 640, 70)


X_L_1 = pygame.Rect(620, 575, 75, 60)
X_L_2 = pygame.Rect(679, 368, 75, 60)
X_L_3 = pygame.Rect(390, 435, 75, 60)
X_L_4 = pygame.Rect(435, 510, 75, 60)
X_L_5 = pygame.Rect(770, 450, 75, 60)
X_L_6 = pygame.Rect(755, 240, 75, 60)
X_L_7 = pygame.Rect(610, 65, 75, 60)
X_L_8 = pygame.Rect(526, 225, 75, 60)
X_L_9 = pygame.Rect(360, 175, 75, 60)
X_L_10 = pygame.Rect(370, 25, 75, 60)

X_L_1_p = pygame.Rect(600, 555, 275, 100)
X_L_2_p = pygame.Rect(659, 348, 275, 100)
X_L_3_p = pygame.Rect(370, 415, 275, 100)
X_L_4_p = pygame.Rect(415, 490, 275, 100)
X_L_5_p = pygame.Rect(590, 430, 275, 100)
X_L_6_p = pygame.Rect(575, 220, 275, 100)
X_L_7_p = pygame.Rect(590, 45, 275, 100)
X_L_8_p = pygame.Rect(346, 205, 275, 100)
X_L_9_p = pygame.Rect(340, 155, 275, 100)
X_L_10_p = pygame.Rect(350, 5, 275, 100)


X_L_1_k = pygame.Rect(800, 575, 60, 60)
X_L_2_k = pygame.Rect(859, 368, 60, 60)
X_L_3_k = pygame.Rect(570, 435, 60, 60)
X_L_4_k = pygame.Rect(615, 510, 60, 60)
X_L_5_k = pygame.Rect(610, 450, 60, 60)
X_L_6_k = pygame.Rect(595, 240, 60, 60)
X_L_7_k = pygame.Rect(790, 65, 60, 60)
X_L_8_k = pygame.Rect(366, 225, 60, 60)
X_L_9_k = pygame.Rect(540, 175, 60, 60)
X_L_10_k = pygame.Rect(550, 25, 60, 60)


X_K_nocl = pygame.Rect(252, 415, 390, 200)
X_K_Krest = pygame.Rect(0, 0, 500, 500)



#переменные
Log_Fon = F_K
nL = 1
nV = 1
Fon = F_N
le_yp = [0, 0, 0, 0, 0,]
U_yp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
lvL_komplit = [3, 2, 2, 2, 2]
#nE = [[60, 60], [119, -157], [-170, -90], [-125, -15], [60, 0], [45, -210], [50, -460], [-184, -225], [-200, -350], [-190, -500]]
