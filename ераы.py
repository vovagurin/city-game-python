import pygame
pygame.init()

# Базовые размеры (виртуальное разрешение)
BASE_WIDTH, BASE_HEIGHT = 800, 600

screen = pygame.display.set_mode((BASE_WIDTH, BASE_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Адаптивное окно")

clock = pygame.time.Clock()

# Загружаем картинку (примерный объект)
image_original = pygame.Surface((200, 150))
image_original.fill((255, 100, 100))

# Позиция объекта в базовых координатах
obj_rect = pygame.Rect(300, 200, 200, 150)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Обновляем окно
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

    # Текущее соотношение масштабирования
    width, height = screen.get_size()
    scale_x = width / BASE_WIDTH
    scale_y = height / BASE_HEIGHT

    # Масштабируем изображение под новый размер
    new_size = (int(obj_rect.width * scale_x), int(obj_rect.height * scale_y))
    scaled_image = pygame.transform.smoothscale(image_original, new_size)

    # Вычисляем новую позицию объекта
    new_pos = (int(obj_rect.x * scale_x), int(obj_rect.y * scale_y))

    # Отрисовка
    screen.fill((30, 30, 30))
    screen.blit(scaled_image, new_pos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()



