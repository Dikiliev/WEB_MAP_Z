import pygame
import requests
import sys


def get_img(coordinate_, scale_, type_map_='sat'):

    map_params = {
        "ll": f'{coordinate_[0]},{coordinate_[1]}',
        "spn": f'{scale_[0]},{scale_[1]}',
        "l": type_map_,
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

type_maps = ['map', 'sat', 'sat,skl']
type_map = 'map'


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

            elif event.key == pygame.K_1:
                type_map = type_maps[0]
            elif event.key == pygame.K_2:
                type_map = type_maps[1]
            elif event.key == pygame.K_3:
                type_map = type_maps[2]

    get_img(coordinate, (scale, scale), type_map)
    screen.blit(pygame.image.load('map.png'), (0, 0))

    pygame.display.flip()
