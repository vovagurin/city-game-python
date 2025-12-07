import pygame
import helper

_pygame_image_load_orig = pygame.image.load
def _pygame_image_load_conv(path):
    surf = _pygame_image_load_orig(path)
    try:
        return surf.convert_alpha()
    except Exception:
        return surf
    
pygame.image.load = _pygame_image_load_conv

#фоны
F_N = pygame.image.load(helper.resource_path('Pr/f/F_N.png'))
F_K = pygame.image.load(helper.resource_path('Pr/f/F_K.png'))
F_L_1 = pygame.image.load(helper.resource_path('Pr/f/F_L_1.png'))
F_L_2 = pygame.image.load(helper.resource_path('Pr/f/F_L_2.png'))
F_L_3 = pygame.image.load(helper.resource_path('Pr/f/F_L_3.png'))
F_L_4 = pygame.image.load(helper.resource_path('Pr/f/F_L_4.png'))
F_L_5 = pygame.image.load(helper.resource_path('Pr/f/F_L_5.png'))
F_L_6 = pygame.image.load(helper.resource_path('Pr/f/F_L_6.png'))
F_L_7 = pygame.image.load(helper.resource_path('Pr/f/F_L_7.png'))
F_L_8 = pygame.image.load(helper.resource_path('Pr/f/F_L_8.png'))
F_L_9 = pygame.image.load(helper.resource_path('Pr/f/F_L_9.png'))
F_L_10 = pygame.image.load(helper.resource_path('Pr/f/F_L_10.png'))
F_L_P = [
    pygame.image.load(helper.resource_path('Pr/f/F_L_P_1.png')),
    pygame.image.load(helper.resource_path('Pr/f/F_L_P_2.png')),
    pygame.image.load(helper.resource_path('Pr/f/F_L_P_3.png')),
    pygame.image.load(helper.resource_path('Pr/f/F_L_P_4.png')),
    pygame.image.load(helper.resource_path('Pr/f/F_L_P_5.png')),
    pygame.image.load(helper.resource_path('Pr/f/F_L_P_6.png')),
    pygame.image.load(helper.resource_path('Pr/f/F_L_P_7.png')),
    pygame.image.load(helper.resource_path('Pr/f/F_L_P_8.png')),
    pygame.image.load(helper.resource_path('Pr/f/F_L_P_9.png')),
    pygame.image.load(helper.resource_path('Pr/f/F_L_P_10.png'))
]


shrift = helper.resource_path('Pr/p/mister_brush.ttf')
font_1 = pygame.font.Font(shrift, 37)
font_1_1 = pygame.font.Font(shrift, 25)
font_1_2 = pygame.font.Font(shrift, 16)
font_2 = pygame.font.Font(shrift, 37)
font_3 = pygame.font.Font(shrift, 37)

#print(lvL[0-9]["q"][0-4]["an"][0-3]["t"]) - ответ
#print(lvL[0-9]["q"][0-4]["an"][0-3]["cor"]) - правильность ответа
#print(lvL[0-9]["q"][0-4]["t"]) - вапрос
#print(lvL[0-9]["n"]) - номер Level
#print(lvL[0-9]["g"]) - пройденость
#print(lvL[0-9]["b"]) - балл

lvL = [
    {
        "n": [pygame.font.Font(shrift, 27).render("общественный", True, (255, 255, 255)), pygame.font.Font(shrift, 27).render("транспорт", True, (255, 255, 255))],
        "g": 1,
        "b": 0,
        "q": [
            {
                "t": font_2.render("Что необходимо сделать при входе в автобус?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("приложить проездной билет", True, (0, 0, 0)), "cor": True},
                    {"t": font_1_1.render("поздороваться со всеми пассажирами", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("закрыть за собой двери", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("занять место", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("Что нельзя делать в общественном транспорте?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("сидеть на сиденье", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("разговаривать с другом", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("высовываться из окна", True, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("смотреть в окно", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("Что нельзя провозить в общественном транспорте?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("коляску", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("смехоопасные вещества", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("еду", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("взрывоопасные вещества", True, (0, 0, 0)), "cor": True},
                ],
            },
            {
                "t": font_2.render("Если ты забыл вещь в транспорте, что делать?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("бежать за автобусом", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("позвонить в службу перевозчика", True, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("подать в суд", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("пожаловаться друзьям", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("Автобус попал в ДТП, Что тебе делать?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("выбежать наружу", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("снять всё на видео", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("узнать кто виноват в аварии", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("дождаться указаний водителя", True, (0, 0, 0)), "cor": True},
                ],
            }
        ]
    },
        {
        "n": font_3.render("школа", True, (255, 255, 255)),
        "g": 0,
        "b": 0,
        "q": [
            {
                "t": font_2.render("Что нужно сделать, когда звенит звонок на урок?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1_1.render("продолжать бегать по коридору", True, (0, 0, 0)), "cor": False},
                    {"t": pygame.font.Font(shrift, 20).render("спрятаться в шкаф, чтобы не идти на математику", True, (0, 0, 0)), "cor": False},
                    {"t": pygame.font.Font(shrift, 18).render("спокойно зайти в класс и приготовиться к занятию", True, (0, 0, 0)), "cor": True},
                    {"t": pygame.font.Font(shrift, 18).render("позвонить другу и рассказать, какой звонок громкий", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("Что нужно сделать, если опоздал на урок?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1_1.render("Тихо войти, извиниться и занять место", True, (0, 0, 0)), "cor": True},
                    {"t": pygame.font.Font(shrift, 18).render("литература не самый нужный урок, можно и прогулять", True, (0, 0, 0)), "cor": False},
                    {"t": pygame.font.Font(shrift, 20).render("ворваться со словами, А вот и звезда пришла!", True, (0, 0, 0)), "cor": False},
                    {"t": pygame.font.Font(shrift, 14).render("предъявить претензию учителю, почему тот не разбудил вас вовремя", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": [
                    font_2.render("Что нужно делать, если случайно пролил воду", True, (0, 0, 0)),
                    font_2.render("на парту или пол?", True, (0, 0, 0))
                ],
                "an": [
                    {"t": font_1_1.render("сделать вид, что ничего не произошло", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("Убежать до прихода учителя", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("сказать, что это эксперимент по физике", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("протереть и извиниться", True, (0, 0, 0)), "cor": True},
                ],
            },
            {
                "t": [
                    pygame.font.Font(shrift, 32).render("Во время пожара в школе кто-то предлагает выбежать", True, (0, 0, 0)),
                    pygame.font.Font(shrift, 32).render("через окно с первого этажа. Как лучше поступить?", True, (0, 0, 0)),
                ],
                "an": [
                    {"t": font_1_1.render("сразу выпрыгнуть, быстрее выберешься", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("действовать по указанию учителя", True, (0, 0, 0)), "cor": True},
                    {"t": pygame.font.Font(shrift, 19).render("пусть сначала сам прыгнет, а там уже и я решу", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("предложить начертить план", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("Что нужно делать, если не сделал домашнее задание?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1_2.render("постараться сделать домашнее задание на перемене", True, (0, 0, 0)), "cor": True},
                    {"t": font_1_2.render("сказать, что сегодня Луна в Водолее - домашку нельзя делать", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_2.render("предложить принести домашнее задание на следующий урок", True, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("признаться честно", True, (0, 0, 0)), "cor": True},
                ],
            }
        ]
    },
        {
        "n": font_3.render("дом", True, (255, 255, 255)),
        "g": 0,
        "b": 0,
        "q": [
            {
                "t": font_2.render("Что делать, если к тебе стучаться в дверь?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("сказать родителям", True, (0, 0, 0)), "cor": True},
                    {"t": font_1_1.render("притвориться что никого нету дома", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("поговорить с человеком за дверью", True, (0, 0, 0)), "cor": False},
                    {"t": pygame.font.Font(shrift, 23).render("припугнуть того кто находится за дверью", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("Что нельзя делать, когда выходишь из дома?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("выключать утюг", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("закрывать дверь", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("открывать окно", True, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("мыть руки", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("Гроза застала тебя дома, как ты поступишь?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1_2.render("гроза страшная вещь, спрячусь под кровать", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_2.render("отключу электроприборы, закрою дверь и окна", True, (0, 0, 0)), "cor": True},
                    {"t": font_1_2.render("открою окна, пусть свежий воздух проникает в дом", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_2.render("гулять в грозу страшно, буду смотреть телевизор", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("Как действовать при пожаре в многоэтажном здании?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("спуститься на лифте", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("спуститься на парашюте", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("спуститься по лестнице", True, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("подняться наверх", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("Что можно делать на открытом балконе?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1_1.render("запускать бумажные самолётики", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("высовываться с балкона", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("кидать снежки в соседей", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("ходить по балкону", True, (0, 0, 0)), "cor": True},
                ],
            }
        ]
    },
        {
        "n": font_3.render("на воде", True, (255, 255, 255)),
        "g": 0,
        "b": 0,
        "q": [
            {
                "t": font_2.render("Почему нельзя заплывать за буйки?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("за ними зона акул", True, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("так сказал сосед на пляже", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("дальше может быть течение и глубина", True, (0, 0, 0)), "cor": True},
                    {"t": font_1_1.render("чтобы не мешать рыбакам ловить рыбу", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("Как понять что человек тонет?", True, (0, 0, 0)),
                "an": [
                    {"t": pygame.font.Font(shrift, 23).render("он громко зовёт на помощь и машет руками", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("он спокойно опускается на дно", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("он плывёт в сторону берега", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("он молчит, судорожно двигает руками", True, (0, 0, 0)), "cor": True},
                ],
            },
            {
                "t": font_2.render("На пляже повесили красный флаг. Что это значит?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1_1.render("конкурс по плаванию начинается", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("купание запрещено", True, (0, 0, 0)), "cor": True},
                    {"t": font_1_1.render("все спасатели ушли на перерыв", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("кто-то тонет", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("Что делать, если начался шторм или гроза у воды?", True, (0, 0, 0)),
                "an": [
                    {"t": pygame.font.Font(shrift, 21).render("лечь плашмя на берег, подальше от деревьев", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("укрыться под деревом", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("забежать в воду подальше от берега", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("отойти подальше от берега", True, (0, 0, 0)), "cor": True},
                ],
            },
            {
                "t": font_2.render("Что делать если ты тонешь?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1_2.render("лечь на спину, сделать глубокий вдох и звать на помощь", True, (0, 0, 0)), "cor": True},
                    {"t": font_1_1.render("начать быстро грести руками и ногами", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("нырнуть под воду", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("применить технику дельфин", True, (0, 0, 0)), "cor": False},
                ],
            }
        ]
    },
        {
        "n": font_3.render("культура", True, (255, 255, 255)),
        "g": 0,
        "b": 0,
        "q": [
            {
                "t": font_2.render("Что такое культура?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1_2.render("духовные и материальные ценности, созданные человеком", True, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("коллекция любимых мемов", True, (0, 0, 0)), "cor": False},
                    {"t": pygame.font.Font(shrift, 22).render("умение не пролить чай, когда здороваешься", True, (0, 0, 0)), "cor": False},
                    {"t": pygame.font.Font(shrift, 21).render("то что показывают по телевизору после 23:00", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("Что относится к культурным ценностям?", True, (0, 0, 0)),
                "an": [
                    {"t": pygame.font.Font(shrift, 23).render("любой предмет которому уже больше 100 лет", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("любимая кружка с котиком", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("картины художников", True, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("дружба", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": [
                    font_2.render("Почему важно сохранять памятники", True, (0, 0, 0)),
                    font_2.render("истории и культуры?", True, (0, 0, 0))
                ],
                "an": [
                    {"t": font_1.render("в них скрыто золото", True, (0, 0, 0)), "cor": False},
                    {"t": pygame.font.Font(shrift, 22).render("они украшают города и привлекают туристов", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("старые здания стоят дешевле, чем новые", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_2.render("чтобы передать будущим поколениям знания о прошлом", True, (0, 0, 0)), "cor": True},
                ],
            },
            {
                "t": font_2.render("Что относится к нематериальной культуре?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("ваза из музея", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("народные танцы", True, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("новый айфон", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("любовь к чаю и сериалам", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("Почему важно уважать культуру других народов?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1_2.render("потому что это помогает лучше понимать и ценить друг друга", True, (0, 0, 0)), "cor": True},
                    {"t": font_1_2.render("чтобы не попасть в неловкую ситуацию за границей", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("потому что так велели древние мудрецы", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("чтобы звучать умно на вечеринках", True, (0, 0, 0)), "cor": False},
                ],
            }
        ]
    },
        {
        "n": pygame.font.Font(shrift, 28).render("электричество", True, (255, 255, 255)),
        "g": 0,
        "b": 0,
        "q": [
            {
                "t": [
                    font_2.render("Какое минимальное напряжение электрического тока", True, (0, 0, 0)),
                    font_2.render("может быть опасно для человека?", True, (0, 0, 0))
                ],
                "an": [
                    {"t": font_1.render("220 В", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("6 В", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("400 В", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("36 В", True, (0, 0, 0)), "cor": True},
                ],
            },
            {
                "t": [
                    font_2.render("Почему нельзя перегружать удлинители и розетки", True, (0, 0, 0)),
                    font_2.render("множеством приборов?", True, (0, 0, 0))
                ],
                "an": [
                    {"t": pygame.font.Font(shrift, 21).render("электричество будет тратиться в разы больше", True, (0, 0, 0)), "cor": False},
                    {"t": pygame.font.Font(shrift, 21).render("может произойти короткое замыкание и пожар", True, (0, 0, 0)), "cor": True},
                    {"t": font_1_1.render("приборы будут работать медленнее", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("розетка может устать и уйти в отпуск", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": [
                    font_2.render("Можно ли пользоваться электроприбором", True, (0, 0, 0)),
                    font_2.render("с оголенным проводом?", True, (0, 0, 0))
                ],
                "an": [
                    {"t": font_1.render("можно", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("вдали от воды можно", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("нельзя", True, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("можно но сторожно", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": [
                    font_2.render("почему птицы могут сидеть на проводах", True, (0, 0, 0)),
                    font_2.render("под напряжением и не получают удар током?", True, (0, 0, 0))
                ],
                "an": [
                    {"t": pygame.font.Font(shrift, 23).render("обе их лапки касаются одного проводника", True, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("у них перьевая изоляция", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("ток уважает пернатых", True, (0, 0, 0)), "cor": False},
                    {"t": pygame.font.Font(shrift, 23).render("у них от природы есть защитный механизм", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": [
                    font_2.render("Почему при касании к корпусу некоторых", True, (0, 0, 0)),
                    font_2.render("старых стиральных машин щекочет током?", True, (0, 0, 0))
                ],
                "an": [
                    {"t": font_1_1.render("машина приветствует хозяина", True, (0, 0, 0)), "cor": False},
                    {"t": pygame.font.Font(shrift, 18).render("барабан крутясь создаёт статическое электричество", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("нарушено заземление", True, (0, 0, 0)), "cor": True},
                    {"t": pygame.font.Font(shrift, 19).render("в стиральной машине живёт дух электричества", True, (0, 0, 0)), "cor": False},
                ],
            }
        ]
    },
        {
        "n": font_3.render("экскурсия", True, (255, 255, 255)),
        "g": 0,
        "b": 0,
        "q": [
            {
                "t": font_2.render("Что нужно сделать перед началом экскурсии?", True, (0, 0, 0)),
                "an": [
                    {"t": pygame.font.Font(shrift, 22).render("проверить, есть ли у тебя с собой телефон", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("выслушать инструктаж учителя", True, (0, 0, 0)), "cor": True},
                    {"t": font_1_2.render("поспорить с друзьями, кто первый займёт место в автобусе", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("спросить у гида, будет ли Wi-Fi", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": [
                    font_2.render("Почему важно надевать удобную одежду и обувь", True, (0, 0, 0)),
                    font_2.render("на экскурсию?", True, (0, 0, 0))
                ],
                "an": [
                    {"t": font_1_1.render("чтобы в случае чего можно было убежать", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_2.render("потому что учителя всегда оценивают внешний вид", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("чтобы совпасть по стилю с гидом", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_2.render("чтобы не устать и избежать травм во время переходов", True, (0, 0, 0)), "cor": True},
                ],
            },
            {
                "t": [
                    font_2.render("Почему нельзя подходить слишком близко", True, (0, 0, 0)),
                    font_2.render("к историческим памятникам?", True, (0, 0, 0))
                ],
                "an": [
                    {"t": font_1.render("они прокляты", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("камеры всё равно следят", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("даже лёгкое касание может повредить их", True, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("вдруг памятник оживёт", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": [
                    font_2.render("Что делать, если тебе стало плохо", True, (0, 0, 0)),
                    font_2.render("во время экскурсии?", True, (0, 0, 0))
                ],
                "an": [
                    {"t": pygame.font.Font(shrift, 22).render("потихоньку уйти, чтобы никого не тревожить", True, (0, 0, 0)), "cor": False},
                    {"t": pygame.font.Font(shrift, 22).render("сообщить учителю или сопровождающему", True, (0, 0, 0)), "cor": True},
                    {"t": pygame.font.Font(shrift, 20).render("лечь на пол и надеяться, что кто-нибудь заметит", True, (0, 0, 0)), "cor": False},
                    {"t": pygame.font.Font(shrift, 23).render("сделать вид, что это часть перформанса", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("Что нужно сделать после экскурсии?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1_1.render("уйти домой без предупреждения", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("оставаться на следующею экскурсию", True, (0, 0, 0)), "cor": False},
                    {"t": pygame.font.Font(shrift, 22).render("возвращаться в класс вместе с учителем", True, (0, 0, 0)), "cor": True},
                    {"t": font_1_1.render("возвращаться в школу самим", True, (0, 0, 0)), "cor": False},
                ],
            }
        ]
    },
        {
        "n": font_3.render("улица", True, (255, 255, 255)),
        "g": 0,
        "b": 0,
        "q": [
            {
                "t": font_2.render("Как правильно переходить дорогу?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("по пешеходному переходу", True, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("наискосок", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("с другими людьми", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("бегом", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": [
                    font_2.render("Что делать, если ты заметил", True, (0, 0, 0)),
                    font_2.render("оборванный электрический провод?", True, (0, 0, 0))
                ],
                "an": [
                    {"t": pygame.font.Font(shrift, 23).render("сфотографировать на память", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("перепрыгнуть через него", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("проверить, есть ли ток", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("осторожно обойти", True, (0, 0, 0)), "cor": True},
                ],
            },
            {
                "t": [
                    font_2.render("Если ты гуляешь зимой и с крыши падает", True, (0, 0, 0)),
                    font_2.render("снег или сосульки, что делать?", True, (0, 0, 0))
                ],
                "an": [
                    {"t": font_1.render("прижаться к зданию", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("отойти от здания", True, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("побежать вдоль здания", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("надеть капюшон", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": [
                    font_2.render("Если к тебе на улице подходит незнакомец", True, (0, 0, 0)),
                    font_2.render("и предлагает подвезти, что делать?", True, (0, 0, 0))
                ],
                "an": [
                    {"t": font_1_1.render("вежливо поблагодарить и сесть", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("спросить расценки", True, (0, 0, 0)), "cor": False},
                    {"t": pygame.font.Font(shrift, 21).render("отказаться, уйти к людям и позвонить взрослым", True, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("проучить его как следует", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("Ты потерялся в незнакомом районе. Что делать?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("пойти наугад", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("позвонить родителям", True, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("разжечь сигнальный костёр", True, (0, 0, 0)), "cor": False},
                    {"t": pygame.font.Font(shrift, 18).render("найти высокое место, чтобы осмотреть местность", True, (0, 0, 0)), "cor": False},
                ],
            }
        ]
    },
        {
        "n": font_3.render("город", True, (255, 255, 255)),
        "g": 0,
        "b": 0,
        "q": [
            {
                "t": [
                    font_2.render("По какой причине ночное время суток", True, (0, 0, 0)),
                    font_2.render("считается более опасным?", True, (0, 0, 0))
                ],
                "an": [
                    {"t": pygame.font.Font(shrift, 13).render("ночью люди чаще путают направления и случайно заходят не туда", True, (0, 0, 0)), "cor": False},
                    {"t": pygame.font.Font(shrift, 13).render("ночью воздух тяжелее, и из-за этого труднее бегать при опасности", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_2.render("хуже видимость, меньше людей и труднее получить помощь", True, (0, 0, 0)), "cor": True},
                    {"t": pygame.font.Font(shrift, 14).render("все телефоны ночью заряжаются, некому позвонить за помощью", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": [
                    font_2.render("Если ты идёшь по тёмной улице вечером,", True, (0, 0, 0)),
                    font_2.render("что лучше сделать?", True, (0, 0, 0))
                ],
                "an": [
                    {"t": font_1.render("надеть тёмную одежду", True, (0, 0, 0)), "cor": False},
                    {"t": pygame.font.Font(shrift, 22).render("петь вслух, чтобы отпугивать всех подряд", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("идти, обходя людные места", True, (0, 0, 0)), "cor": False},
                    {"t": pygame.font.Font(shrift, 13).render("идти по освещённой стороне и носить светоотражающие элементы", True, (0, 0, 0)), "cor": True},
                ],
            },
            {
                "t": font_2.render("Что ты будешь делать, встретив уличную собаку?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1_1.render("прысну перцовым баллончиком", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("убегу", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("вызову отлов животных", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("медленно пойду обратно", True, (0, 0, 0)), "cor": True},
                ],
            },
            {
                "t": [
                    font_2.render("без сопровождения взрослого ребёнок может", True, (0, 0, 0)),
                    font_2.render("находиться на улице до...", True, (0, 0, 0))
                ],
                "an": [
                    {"t": font_1.render("до школьного звонка", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("до 22:00", True, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("до 00:00", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("таких правил нет", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("Что делать если тебя ограбили?", True, (0, 0, 0)),
                "an": [
                    {"t": pygame.font.Font(shrift, 13).render("запомнить преступника, уйти в безопасное место и вызвать полицию", True, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("броситься в погоню", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("выложить пост в соцсети", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("кричать оскорбление вслед преступнику", True, (0, 0, 0)), "cor": False},
                ],
            }
        ]
    },
        {
        "n": font_3.render("на природе", True, (255, 255, 255)),
        "g": 0,
        "b": 0,
        "q": [
            {
                "t": font_2.render("Как развести костёр?", True, (0, 0, 0)),
                "an": [
                    {"t": pygame.font.Font(shrift, 15).render("нужно собрать сухих веток и поджечь с подветренной стороны", True, (0, 0, 0)), "cor": False},
                    {"t": pygame.font.Font(shrift, 23).render("надо использовать жидкость для розжига", True, (0, 0, 0)), "cor": False},
                    {"t": pygame.font.Font(shrift, 21).render("предложить вложиться в финансовую пирамиду", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("разводить костры запрещено", True, (0, 0, 0)), "cor": True},
                ],
            },
            {
                "t": font_2.render("Если ты увидел дикое животное, что нужно делать?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("не приближаться", True, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("поймать животное", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("погладить его", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("покормить животное", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("Почему нельзя оставлять мусор в лесу?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1_1.render("он не сочетается с зелёным фоном", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("он вырастет в мусорное дерево", True, (0, 0, 0)), "cor": False},
                    {"t": font_1.render("он может погибнуть", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("он может навредить животным", True, (0, 0, 0)), "cor": True},
                ],
            },
            {
                "t": [
                    font_2.render("Если началась сильная гроза,", True, (0, 0, 0)),
                    font_2.render("а ты оказался далеко в лесу, что лучше сделать?", True, (0, 0, 0))
                ],
                "an": [
                    {"t": font_1.render("встать под дерево", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("присесть на корточки вдали от деревьев", True, (0, 0, 0)), "cor": True},
                    {"t": font_1.render("лечь на землю", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("бежать домой как можно быстрее", True, (0, 0, 0)), "cor": False},
                ],
            },
            {
                "t": font_2.render("Если ты заблудился в лесу, что нужно делать?", True, (0, 0, 0)),
                "an": [
                    {"t": font_1.render("ускорить темп ходьбы", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("залезть на дерево и осмотреться", True, (0, 0, 0)), "cor": False},
                    {"t": font_1_1.render("остановиться и позвонить по номеру 112", True, (0, 0, 0)), "cor": True},
                    {"t": font_1_1.render("начать идти в северном направлении", True, (0, 0, 0)), "cor": False},
                ],
            }
        ]
    }
]


aftor = font_1.render("создатель: Vovan4ek play", True, (255, 255, 255))
versi = font_1.render("версия: 2_2", True, (255, 255, 255))

#уровни
U_lev = [
    [
        pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_0_1.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_0_2.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_0_3.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_0_4.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_0_5.png'))
    ],
    [
        pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_1_1.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_1_2.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_1_3.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_1_4.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_1_5.png'))
    ],
    [
        pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_2_1.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_2_2.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_2_3.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_2_4.png')),
        [
            pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_2_5_0.png')),
            pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_2_5_1.png')),
            pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_2_5_2.png')),
            pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_2_5_3.png')),
            pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_2_5_4.png'))
        ]
    ],
    [
        pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_3_1.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_3_2.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_3_3.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_3_4.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/lev/lev_3_5.png'))
    ]
]
U_pra = [
    [
        pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_0_1.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_0_2.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_0_3.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_0_4.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_0_5.png'))
    ],
    [
        pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_1_1.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_1_2.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_1_3.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_1_4.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_1_5.png'))
    ],
    [
        pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_2_1.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_2_2.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_2_3.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_2_4.png')),
        [
            pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_2_5_0.png')),
            pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_2_5_1.png')),
            pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_2_5_2.png')),
            pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_2_5_3.png')),
            pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_2_5_4.png'))
        ]
    ],
    [
        pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_3_1.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_3_2.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_3_3.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_3_4.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/pra/pra_3_5.png'))
    ]
]
U_dop = [
    [
        pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_0_1.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_0_2.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_0_3.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_0_4.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_0_5.png'))
    ],
    [
        pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_1_1.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_1_2.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_1_3.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_1_4.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_1_5.png'))
    ],
    [
        pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_2_1.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_2_2.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_2_3.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_2_4.png')),
        [
            pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_2_5_0.png')),
            pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_2_5_1.png')),
            pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_2_5_2.png')),
            pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_2_5_3.png')),
            pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_2_5_4.png'))
        ]
    ],
    [
        pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_3_1.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_3_2.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_3_3.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_3_4.png')),
        pygame.image.load(helper.resource_path('Pr/k/U/dop/dop_3_5.png'))
    ]
]



#другие модэли
Con = pygame.image.load(helper.resource_path('Pr/k/Con_.png'))
Con_a_p = pygame.image.load(helper.resource_path('Pr/k/Con_a_p.png'))
Con_b_p = pygame.image.load(helper.resource_path('Pr/k/Con_b_p.png'))
Con_c_p = pygame.image.load(helper.resource_path('Pr/k/Con_c_p.png'))
Con_d_p = pygame.image.load(helper.resource_path('Pr/k/Con_d_p.png'))

K_nocl_p =  pygame.image.load(helper.resource_path('Pr/k/K_nocl.png'))
K_nocl = pygame.image.load(helper.resource_path('Pr/k/K_nocl_p.png'))

Krest = pygame.image.load(helper.resource_path('Pr/k/Krest.png'))
Krest_p = pygame.image.load(helper.resource_path('Pr/k/Krest_p.png'))
buk = pygame.image.load(helper.resource_path('Pr/k/buk.png'))
buk_p = pygame.image.load(helper.resource_path('Pr/k/buk_p.png'))

Ben = [
    pygame.image.load(helper.resource_path('Pr/k/Ben_b.png')),
    pygame.image.load(helper.resource_path('Pr/k/Ben_g.png')),
    pygame.image.load(helper.resource_path('Pr/k/Ben_n.png')),
    pygame.image.load(helper.resource_path('Pr/k/Ben_n_B.png'))
]



le = [
    [
        pygame.image.load(helper.resource_path('Pr/k/le/le_1_1.png')),
        pygame.image.load(helper.resource_path('Pr/k/le/le_1_2.png')),
        pygame.image.load(helper.resource_path('Pr/k/le/le_1_3.png'))
    ],
    [
        pygame.image.load(helper.resource_path('Pr/k/le/le_2_1.png')),
        pygame.image.load(helper.resource_path('Pr/k/le/le_2_2.png')),
        pygame.image.load(helper.resource_path('Pr/k/le/le_2_3.png')),
        pygame.image.load(helper.resource_path('Pr/k/le/le_2_4.png'))
    ],
    [
        pygame.image.load(helper.resource_path('Pr/k/le/le_3_1.png')),
        pygame.image.load(helper.resource_path('Pr/k/le/le_3_2.png')),
        pygame.image.load(helper.resource_path('Pr/k/le/le_3_3.png'))
    ],
    [
        pygame.image.load(helper.resource_path('Pr/k/le/le_4_1.png')),
        pygame.image.load(helper.resource_path('Pr/k/le/le_4_2.png')),
        pygame.image.load(helper.resource_path('Pr/k/le/le_4_3.png')),
        pygame.image.load(helper.resource_path('Pr/k/le/le_4_4.png'))
    ],
    [
        pygame.image.load(helper.resource_path('Pr/k/le/le_5_1.png')),
        pygame.image.load(helper.resource_path('Pr/k/le/le_5_2.png')),
        pygame.image.load(helper.resource_path('Pr/k/le/le_5_3.png')),
        pygame.image.load(helper.resource_path('Pr/k/le/le_5_4.png')),
        pygame.image.load(helper.resource_path('Pr/k/le/le_5_5.png'))
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
X_K_Krest = pygame.Rect(740, 10, 150, 125)
X_exet_k = pygame.Rect(0, 600, 155, 60)
X_exet_L = pygame.Rect(745, 600, 155, 60)

#музыка и звуки

Z_nocl_A = pygame.mixer.Sound(helper.resource_path('Pr/s/Z/0.mp3'))
Z_nocl_n = pygame.mixer.Sound(helper.resource_path('Pr/s/Z/1.mp3'))

#Z_g = pygame.mixer.Sound(helper.resource_path('Pr/s/Z/Z_g.mp3'))
Z_sg = pygame.mixer.Sound(helper.resource_path('Pr/s/Z/Z_g.mp3'))

Z_U = pygame.mixer.Sound(helper.resource_path('Pr/s/Z/1.mp3'))
Z_U_A0 = pygame.mixer.Sound(helper.resource_path('Pr/s/Z/Z_U_A0.mp3'))
Z_U_A1 = pygame.mixer.Sound(helper.resource_path('Pr/s/Z/Z_U_A1.mp3'))


Z_Con = pygame.mixer.Sound(helper.resource_path('Pr/s/Z/0.mp3'))
Z_Con_g = pygame.mixer.Sound(helper.resource_path('Pr/s/Z/Z_Con_g.mp3'))
Z_Con_b = pygame.mixer.Sound(helper.resource_path('Pr/s/Z/Z_Con_b.mp3'))
Z_Krest_A = pygame.mixer.Sound(helper.resource_path('Pr/s/Z/0.mp3'))
Z_Krest_n = pygame.mixer.Sound(helper.resource_path('Pr/s/Z/Z_Krest_n.mp3'))



M = [
    [
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3'))
    ],
    [
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3'))
    ],
    [
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3'))
    ],
    [
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3'))
    ],
    [
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3'))
    ],
    [
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3'))
    ],
    [
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3'))
    ],
    [
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3'))
    ],
    [
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3'))
    ],
    [
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3'))
    ],
    [
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3')),
        pygame.mixer.Sound(helper.resource_path('Pr/s/m/0.mp3'))
    ]
]

#переменные
Log_Fon = F_K
nL_m = 11
nL = 11
nV = 1
Fon = F_N
le_yp = [0, 0, 0, 0, 0,]
U_yp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
lvL_komplit = [3, 2, 2, 2, 2]
test_s = {"nocl": False, "Con": False, "Krest": False, "L": {"1": False, "2": False, "3": False, "4": False, "5": False, "6": False, "7": False, "8": False, "9": False, "10": False,}}
#nE = [[60, 60], [119, -157], [-170, -90], [-125, -15], [60, 0], [45, -210], [50, -460], [-184, -225], [-200, -350], [-190, -500]]
