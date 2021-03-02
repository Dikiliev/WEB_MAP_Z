import pygame
import requests
import sys


def get_img(coordinate, scale):

    map_params = {
        "ll": f'{coordinate[0]},{coordinate[1]}',
        "spn": f'{scale[0]},{scale[1]}',
        "l": "skl",
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"

    response = requests.get(map_api_server, params=map_params)

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)


pygame.init()
screen = pygame.display.set_mode((600, 450))
running = True
clock = pygame.time.Clock()

coordinate = [37.588392, 55.734036]
scale = 0.005

type_map = ['map', 'sat', 'skl']


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                scale -= scale / 2
            elif event.key == pygame.K_PAGEDOWN:
                scale += scale / 2

            elif event.key == pygame.K_UP:
                coordinate[1] += scale / 10
            elif event.key == pygame.K_DOWN:
                coordinate[1] -= scale / 10
            elif event.key == pygame.K_RIGHT:
                coordinate[0] += scale / 10
            elif event.key == pygame.K_LEFT:
                coordinate[0] -= scale / 10

    get_img(coordinate, (scale, scale))
    screen.blit(pygame.image.load('map.png'), (0, 0))

    pygame.display.flip()
