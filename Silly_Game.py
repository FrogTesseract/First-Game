import pygame
from sys import exit

# Essentials
pygame.init()
window = pygame.display.set_mode((400,400))
pygame.display.set_caption('Silly Game - Original')

# Variables
game_active = 0
test_font =  pygame.font.Font("data\\Pixeltype.ttf", 50)

clock = pygame.time.Clock()
enemy_rect = list()

#Sprites

Background = pygame.image.load("data\\Background.jpg").convert_alpha()

Space_strt_surface = test_font.render("Press Space to Start", False , (64,64,64)) # Loads the text - inputs context, Anti Aliasing and uses RGB colour
Space_strt_rect = Space_strt_surface.get_rect(center = (200, 50))

Final_surface = test_font.render("Well Done! ", False , (204, 119, 33)) # Loads the text - inputs context, Anti Aliasing and uses RGB colour
Final_rect = Final_surface.get_rect(center = (200, 150))

Credit_surface = test_font.render("Made By Rohan", False , (204, 119, 33)) # Loads the text - inputs context, Anti Aliasing and uses RGB colour
Credit_rect = Credit_surface.get_rect(center = (200, 250))


player_surface = pygame.image.load("data\\Player_Circle.png").convert_alpha()
player_rect = player_surface.get_rect(center = (200, 10))

finish_surface = pygame.image.load("data\\finish.png").convert_alpha()
finish_rect = player_surface.get_rect(center = (200, 400))

enemy_surface = pygame.image.load("data\\enemy.png").convert_alpha()
enemy_rect.append(enemy_surface.get_rect(center=(200,50)))
enemy_rect.append(enemy_surface.get_rect(center=(200,150)))
enemy_rect.append(enemy_surface.get_rect(center=(200,275)))
enemy_rect.append(enemy_surface.get_rect(center=(200,300)))




#map_surface = pygame.image.load("Map.png").convert_alpha()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mouse.set_pos([200, 10])
                player_rect.center = (200, 10)
                window.blit(player_surface, player_rect)
                game_active = 1


    mouse_pos = pygame.mouse.get_pos()

    #Background
    window.blit(Background, (0,0))


    #Start-Up
    if game_active == 0:
        pygame.mouse.set_pos([200, 10])
        window.blit(Space_strt_surface, Space_strt_rect)



    if game_active == 1:

     # Player
        player_rect.center = mouse_pos
        window.blit(player_surface, player_rect)

    # Enemy

        for i in range(0,4):
            if enemy_rect[i].colliderect(player_rect):
                player_rect.center = (200, 10)
                window.blit(player_surface, player_rect)
                game_active = 0

            if enemy_rect[i].right <=0:
                enemy_rect[i].left = 400

            window.blit(enemy_surface, enemy_rect[i])

        enemy_rect[0].x -= 15
        enemy_rect[1].x -= 15
        enemy_rect[2].x -= 25
        enemy_rect[3].x -= 25

    # Finish

        window.blit(finish_surface, finish_rect)
        if finish_rect.colliderect(player_rect):
            game_active = 2

    if game_active == 2:
        window.blit(Final_surface, Final_rect)
        window.blit(Credit_surface, Credit_rect)

    pygame.display.update()
    clock.tick(60)

