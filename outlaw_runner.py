import pygame
import random
from sys import exit

def display_time():
    global time_rect, time_font
    time = int(pygame.time.get_ticks() / 1000) - start_time
    time_font = font.render("score: " + str(time), False, "white")
    time_rect = time_font.get_rect(center=(350, 100))
    if game_active:
        screen.blit(time_font, time_rect)
    return time

pygame.init()

background = pygame.image.load("OIG.jpg")
screen = pygame.display.set_mode((700, 700))
title = pygame.display.set_caption("Outlaw runner")
# snake
snake = pygame.image.load("snake.png")
snake_rect = snake.get_rect(midbottom=(700, 650))
# vulture
vulture = pygame.image.load("vulture.png")
vulture_rect = vulture.get_rect(bottomleft=(730, 400))
#dear
deer =pygame.image.load("stand dear1.png")
deer_rect=deer.get_rect(bottomleft=(750,635))
#horse
horse=pygame.image.load("horse stand.png")
horse_rect=horse.get_rect(bottomright=(0,650))
#cowboy
cowboy=pygame.image.load("cowboy.png")
cowboy_rect=cowboy.get_rect(bottomright=(0,650))
#bullet
bullet=pygame.image.load("bullet.png").convert_alpha()
bullet_rect=bullet.get_rect(center=(0,510))
#ballon
ballon=pygame.image.load("ballon.png")
ballon_rect=ballon.get_rect(bottomright=(0,300))
#bomb
bomb=pygame.image.load("bomb.png")
bomb_rect=bomb.get_rect(bottomleft=(350,300))
# player
player_index = 0
player = pygame.image.load("playerfront.png").convert_alpha()
player_jump = pygame.image.load("playerfrontjump.png").convert_alpha()
player_rect = player.get_rect(midbottom=(50, 630))
player_gravity = 0
font = pygame.font.Font("PressStart2P-Regular.ttf", 20)
font2 = pygame.font.Font("PressStart2P-Regular.ttf", 15)
# game over
player_over = pygame.image.load("playerover.png")
player_over_rect = player_over.get_rect(midbottom=(70, 665))
game_over_text = font.render("   GAME OVER   ", False, "black")
game_over_text_rect = game_over_text.get_rect(center=(350, 200))
press = font2.render("press R to play again", False, "white")
press_rect = press.get_rect(midbottom=(350, 600))
#font in phases
font3=pygame.font.Font("PressStart2P-Regular.ttf",60)
def generate_random_sentence():
    sentences = ["cmon, you can do better ",
                 "git gud",
                 "its not even that hard, just kidding"]
    return random.choice(sentences)

# player walking animation
player_walk1 = pygame.image.load("playerfront.png").convert_alpha()
player_walk2 = pygame.image.load("playerfront walking.png").convert_alpha()
player_walk_index = 0
player_walk_timer = pygame.time.get_ticks()
#obstacle
snake_walk1=pygame.image.load("snake.png").convert_alpha()
snake_walk2=pygame.image.load("snakewalking.png").convert_alpha()
vulture_walk1=pygame.image.load("vulture.png").convert_alpha()
vulture_walk2=pygame.image.load("flying vulture.png").convert_alpha()
horse_walk1=pygame.image.load("horse stand.png").convert_alpha()
horse_walk2=pygame.image.load("horse walk.png").convert_alpha()
cowboy_walk1=pygame.image.load("cowboy.png").convert_alpha()
cowboy_walk2=pygame.image.load("cowboy fire.png").convert_alpha()
deer_walk1=pygame.image.load("stand dear1.png").convert_alpha()
deer_walk2=pygame.image.load("walking dear.png").convert_alpha()
deer_walk_index=0
deer_walk_timer=pygame.time.get_ticks()
snake_walk_index=0
snake_walk_timer=pygame.time.get_ticks()
# frame
frame = pygame.time.Clock()
game_active = True
start_time = 0
player_move_right = False
player_move_left = False
player_jumping = False
lose=False
def r1():
    deer_random1=random.randint(1,2)
    return deer_random1
deer_random=r1()
def r():
    horse_random1=random.randint(1,4)
    return horse_random1
horse_random=r()
if horse_random==1:
    cowboy=cowboy_walk1
    bullet_rect.x=450
    horse_speed=6
elif horse_random==2:
    cowboy=cowboy_walk1
    bullet_rect.x=100
    horse_speed=6
elif horse_random==3:
    cowboy=pygame.transform.flip(cowboy_walk1,True,False)
    bullet_rect.x=300
    horse_speed=6
    horse_rect.x=704
    cowboy_rect.x=704
elif horse_random==4:
    cowboy=cowboy_walk1
    bullet_rect.right=500
    horse_speed=6
    horse_rect.x=704
    cowboy_rect.x=704
#ballon
bomb_list=[]
for v in range(5):
    bomb_rect.x=random.randint(20,700)
    bomb_list.append(bomb_rect.x)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 630:
                    if 96<display_time()<137:
                        player = player_jump
                        player_gravity = -30
                        player_jumping = True
                    else:
                        player = player_jump
                        player_gravity = -25
                        player_jumping = True
                if event.key == pygame.K_RIGHT:
                    player_move_right = True
                if event.key == pygame.K_LEFT:
                    player_move_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player_move_right = False
                    player_walk_index = 0  # Reset walking animation index
                    player = [player_walk1, player_walk2][player_walk_index]
                if event.key == pygame.K_LEFT:
                    player_move_left = False
                    player_walk_index = 0  # Reset walking animation index
                    player = [player_walk1, player_walk2][player_walk_index]

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    start_time = int(pygame.time.get_ticks() / 1000)
                    game_active = True
                    lose=False
                    player_gravity = 0  # Reset player gravity
                    if horse_random==1:
                         bullet_rect.x=450
                         horse_rect.left=700
                         cowboy_rect.left=700
                    if horse_random==2:
                        bullet_rect.x=100
                        horse_rect.left=700
                        cowboy_rect.left=700
                    if horse_random==3:
                        bullet_rect.x=300
                        horse_rect.right=0
                        cowboy_rect.right=0
                    if horse_random==4:
                        bullet_rect.x=650
                        horse_rect.right=0
                        cowboy_rect.right=0
                    snake_rect.left = 704
                    vulture_rect.left = 730
                    deer_rect.left =750
                    player_rect.x = 50
                    player_rect.y = 630
                    player=pygame.image.load("playerfront.png").convert_alpha()
                    player_move_right = False
                    player_move_left = False

    if game_active:
        # player
        player_gravity += 1
        player_rect.y += player_gravity

        # switch back to original image when on the floor
        if player_rect.bottom >= 630:
            player_rect.bottom = 630
            player_jumping = False
            player = [player_walk1, player_walk2][player_walk_index]

        # player walking animation moving right
        if player_move_right and not player_jumping:
            player_current_time = pygame.time.get_ticks()
            if player_current_time - player_walk_timer > 100:  # Change image every 100 milliseconds
                player_walk_timer = player_current_time
                player_walk_index = (player_walk_index + 1) % 2
            player = [player_walk1, player_walk2][player_walk_index]
        #animations
        snake_current_time=pygame.time.get_ticks()
        if snake_current_time-snake_walk_timer >500:
            snake_walk_timer=snake_current_time
            snake_walk_index=(snake_walk_index+1)%2
        deer_current_time=pygame.time.get_ticks()
        if deer_current_time-deer_walk_timer>200:
            deer_walk_timer=deer_current_time
            deer_walk_index=(deer_walk_index+1)%2
        snake=[snake_walk1,snake_walk2][snake_walk_index]
        vulture=[vulture_walk1,vulture_walk2][snake_walk_index]
        deer=[deer_walk1,deer_walk2][deer_walk_index]
        horse=[horse_walk1,horse_walk2][deer_walk_index]

        # player walking animation moving left
        if player_move_left and not player_jumping:
            current_time = pygame.time.get_ticks()
            if current_time - player_walk_timer > 100:  # Change image every 100 milliseconds
                player_walk_timer = current_time
                player_walk_index = (player_walk_index + 1) % 2
            player = pygame.transform.flip([player_walk1, player_walk2][player_walk_index], True, False)
        screen.blit(background, (0, 0))
        screen.blit(player, player_rect)
        display_time()
        if display_time() <12:
            snake_rect.x += -3
            if snake_rect.right < 0:
                snake_rect.left = 700
            screen.blit(snake, snake_rect)
        elif 11<display_time()<15:
            snake_rect.x += -3
            screen.blit(snake, snake_rect)
        elif 15<=display_time() <=17:
            phase_2=font3.render("PHASE 2",False,(150,22,21))
            phase_2_rect=phase_2.get_rect(center=(350,350))
            screen.blit(phase_2,phase_2_rect)
        elif 18 <= display_time() <35:
            snake_rect.x += -4
            if snake_rect.right < 0:
                snake_rect.left = 700
            vulture_rect.x += -2
            if vulture_rect.right < 0:
                 vulture_rect.left = 700
            screen.blit(vulture, vulture_rect)
            screen.blit(snake, snake_rect)
        elif 34<display_time()<39:
            vulture_rect.x +=-2
            snake_rect.x += -4
            screen.blit(snake, snake_rect)
            screen.blit(vulture,vulture_rect)
        elif 38 < display_time() < 42:
            phase_3 = font3.render("PHASE 3", False, (150, 22, 21))
            phase_3_rect = phase_3.get_rect(center=(350, 350))
            screen.blit(phase_3, phase_3_rect)
        elif 41 < display_time() < 63:
            if deer_random == 1:
                deer_rect.x -= 5
                if deer_rect.right < 0:# Change this condition to check if right edge is less than 0
                    deer_random = r1()
                    deer_rect.left = 700
            else:
                deer=pygame.transform.flip(deer,True,False)
                deer_rect.x += 5
                if deer_rect.left > 700:  # Change this condition to check if left edge is greater than 700
                    deer_rect.right = 0# Set right edge to 0
                    deer_random = r1()

            screen.blit(deer, deer_rect)
        elif 62 < display_time() < 68:
            if deer_random==1:
                deer_rect.x += -5
            else:
                deer=pygame.transform.flip(deer,True,False)
                deer_rect.x += 5
            screen.blit(deer, deer_rect)
        elif 67 <= display_time()<= 70:
            phase_3 = font3.render("PHASE 4", False, (150, 22, 21))
            phase_3_rect = phase_3.get_rect(center=(350, 300))
            screen.blit(phase_3, phase_3_rect)
        elif 71 <= display_time() <90:
            vulture_rect.x += -2
            if vulture_rect.right < 0:
                vulture_rect.left = 700
            screen.blit(vulture, vulture_rect)
            if deer_random == 1:
                deer_rect.x -= 5
                if deer_rect.right < 0:  # Change this condition to check if right edge is less than 0
                    deer_random = r1()
                    deer_rect.left = 700
            else:
                deer = pygame.transform.flip(deer, True, False)
                deer_rect.x += 5
                if deer_rect.left > 700:  # Change this condition to check if left edge is greater than 700
                    deer_rect.right = 0  # Set right edge to 0
                    deer_random = r1()
            screen.blit(vulture, vulture_rect)
            screen.blit(deer, deer_rect)
        elif 89 <display_time() <93:
            vulture_rect.x +=-2
            if deer_random==1:
                deer_rect.x += -5
            else:
                deer=pygame.transform.flip(deer,True,False)
                deer_rect.x += 5
            screen.blit(deer, deer_rect)
            screen.blit(vulture,vulture_rect)
        elif 92 <display_time()<95:
            phase_4=font3.render("Phase 5",False,(150, 22, 21))
            phase_4_rect=phase_4.get_rect(center=(350,350))
            screen.blit(phase_4,phase_4_rect)
        else:
            if horse_random == 1:
                horse_rect.x += horse_speed
                cowboy_rect.x += horse_speed
                if horse_rect.x > 400:
                        horse_speed=0
                        horse = horse_walk1
                        cowboy = cowboy_walk2
                        if 0 < horse_rect.x < 700:
                            screen.blit(bullet, bullet_rect)
                            bullet_rect.x += -5
                        else:
                            bullet_rect.x += -20
                        if bullet_rect.x < 0:
                            horse=[horse_walk1,horse_walk2][deer_walk_index]
                            cowboy= cowboy_walk1
                            horse_speed=6

                if horse_rect.left > 700:
                        horse_rect.right = 0
                        cowboy_rect.right = 0
                        bullet_rect.x=450
                        horse_random=r()
                        if horse_random == 1:
                            cowboy = cowboy_walk1
                            bullet_rect.x = 450
                            horse_speed = 6
                        elif horse_random == 2:
                            cowboy = cowboy_walk1
                            bullet_rect.x = 100
                            horse_speed = 6
                        elif horse_random == 3:
                            cowboy = pygame.transform.flip(cowboy_walk1, True, False)
                            bullet_rect.x = 300
                            horse_speed = 6
                            horse_rect.x = 704
                            cowboy_rect.x = 704
                        elif horse_random == 4:
                            cowboy = cowboy_walk1
                            bullet_rect.right = 500
                            horse_speed = 6
                            horse_rect.x = 704
                            cowboy_rect.x = 704
                screen.blit(cowboy, cowboy_rect)
                screen.blit(horse, horse_rect)
            elif horse_random==2:
                    horse_rect.x += horse_speed
                    cowboy_rect.x += horse_speed
                    if horse_rect.x > 50:
                        horse_speed = 0
                        horse = horse_walk1
                        cowboy = pygame.transform.flip(cowboy_walk2,True,False)
                        bullet = pygame.transform.flip(bullet, True, False)
                        if 0 < horse_rect.x < 700:
                            screen.blit(bullet, bullet_rect)
                            bullet_rect.x += 5
                        else:
                            bullet_rect.x += 20
                        if bullet_rect.x > 700:
                            horse = [horse_walk1, horse_walk2][deer_walk_index]
                            cowboy = cowboy_walk1
                            horse_speed = 6
                    if horse_rect.left > 700:
                        horse_rect.right = 0
                        cowboy_rect.right = 0
                        bullet_rect.x = 100
                        horse_random = r()
                        if horse_random == 1:
                            cowboy = cowboy_walk1
                            bullet_rect.x = 450
                            horse_speed = 6
                        elif horse_random == 2:
                            cowboy = cowboy_walk1
                            bullet_rect.x = 100
                            horse_speed = 6
                        elif horse_random == 3:
                            cowboy = pygame.transform.flip(cowboy_walk1, True, False)
                            bullet_rect.x = 300
                            horse_speed = 6
                            horse_rect.x = 704
                            cowboy_rect.x = 704
                        elif horse_random == 4:
                            cowboy = cowboy_walk1
                            bullet_rect.right = 500
                            horse_speed = 6
                            horse_rect.x = 704
                            cowboy_rect.x = 704
                    screen.blit(horse, horse_rect)
                    screen.blit(cowboy, cowboy_rect)
            elif horse_random == 3:
                cowboy=pygame.transform.flip(cowboy_walk1,True,False)
                horse =[pygame.transform.flip(horse_walk1, True, False), pygame.transform.flip(horse_walk2, True, False)][deer_walk_index].convert_alpha()
                horse_rect.x += -horse_speed
                cowboy_rect.x += -horse_speed
                if horse_rect.right < 300:
                    horse_speed = 0
                    horse = horse_walk1
                    cowboy = pygame.transform.flip(cowboy_walk2, True, False)
                    bullet=pygame.transform.flip(bullet,True,False)
                    if 0 < horse_rect.x < 700:
                        screen.blit(bullet, bullet_rect)
                        bullet_rect.x += 5
                    else:
                        bullet_rect.x+=20
                    if bullet_rect.x > 700:
                        horse = [pygame.transform.flip(horse_walk1,True,False), pygame.transform.flip(horse_walk2,True,False)][deer_walk_index]
                        cowboy=pygame.transform.flip(cowboy_walk1,True,False)

                        horse_speed = 6
                if horse_rect.right < 0:
                    horse_rect.left = 700
                    cowboy_rect.left = 700
                    bullet_rect.x = 300
                    horse_random = r()
                    if horse_random == 1:
                        cowboy = cowboy_walk1
                        bullet_rect.x = 450
                        horse_speed = 6
                    elif horse_random == 2:
                        cowboy = cowboy_walk1
                        bullet_rect.x = 100
                        horse_speed = 6
                    elif horse_random == 3:
                        cowboy = pygame.transform.flip(cowboy_walk1, True, False)
                        bullet_rect.x = 300
                        horse_speed = 6
                        horse_rect.x = 704
                        cowboy_rect.x = 704
                    elif horse_random == 4:
                        cowboy = cowboy_walk1
                        bullet_rect.right = 500
                        horse_speed = 6
                        horse_rect.x = 704
                        cowboy_rect.x = 704


                screen.blit(horse, horse_rect)
                screen.blit(cowboy, cowboy_rect)

            elif horse_random == 4:
                cowboy=pygame.transform.flip(cowboy_walk1,True,False)
                horse =[pygame.transform.flip(horse_walk1, True, False), pygame.transform.flip(horse_walk2, True, False)][deer_walk_index].convert_alpha()
                horse_rect.x += -horse_speed
                cowboy_rect.x += -horse_speed
                if horse_rect.right < 650:
                    horse_speed = 0
                    horse = pygame.transform.flip(horse_walk1,True,False)
                    cowboy = cowboy_walk2
                    if 0 < horse_rect.x < 700:
                        screen.blit(bullet, bullet_rect)
                        bullet_rect.x -= 5
                    else:
                        bullet_rect.x-=20
                    if bullet_rect.x < 0:
                        horse = [pygame.transform.flip(horse_walk1,True,False), pygame.transform.flip(horse_walk2,True,False)][deer_walk_index]
                        cowboy=pygame.transform.flip(cowboy_walk1,True,False)

                        horse_speed = 6
                if horse_rect.right < 0:
                    horse_rect.left = 700
                    cowboy_rect.left = 700
                    bullet_rect.right = 500
                    horse_random = r()
                    if horse_random == 1:
                        cowboy = cowboy_walk1
                        bullet_rect.x = 450
                        horse_speed = 6
                    elif horse_random == 2:
                        cowboy = cowboy_walk1
                        bullet_rect.x = 100
                        horse_speed = 6
                    elif horse_random == 3:
                        cowboy = pygame.transform.flip(cowboy_walk1, True, False)
                        bullet_rect.x = 300
                        horse_speed = 6
                        horse_rect.x = 704
                        cowboy_rect.x = 704
                    elif horse_random == 4:
                        cowboy = cowboy_walk1
                        bullet_rect.right = 500
                        horse_speed = 6
                        horse_rect.x = 704
                        cowboy_rect.x = 704

                screen.blit(horse, horse_rect)
                screen.blit(cowboy, cowboy_rect)
        # else:
        #     phase_5 = font3.render("PHASE 6", False, (150, 22, 21))
        #     phase_5_rect = phase_5.get_rect(center=(350, 350))
        #     screen.blit(phase_5, phase_5_rect)
        # elif 141 <display_time()<170:
        #     ballon_rect.x+=3
        #     if ballon_rect.left>700:
        #         ballon_rect.right=0
        #     screen.blit(ballon,ballon_rect)
        #     for i in bomb_list:
        #         bomb_rect.x=i
        #         if bomb_rect.x<=ballon_rect.x+90:
        #             ballon_rect.x-=3
        #             bomb_rect.y+=5
        #             if bomb_rect.y>=582:
        #                 bomb_rect.y=582
        #             if bomb_rect.y==582:
        #                 ballon_rect.x+=3
        #             screen.blit(bomb,bomb_rect)
            screen.blit(time_font, time_rect)
        if  player_rect.colliderect(horse_rect) or player_rect.colliderect(cowboy_rect) or player_rect.colliderect(deer_rect) or player_rect.colliderect(snake_rect)  or player_rect.colliderect(
                vulture_rect) or player_rect.left >= 700 or player_rect.right <= 0:
            lose=True
        if player_rect.colliderect(bullet_rect) and bullet_rect.x !=450 and horse_random==1 and 0<horse_rect.x<700:
            lose=True
        if player_rect.colliderect(bullet_rect) and bullet_rect.x !=100 and horse_random==2 and 0<horse_rect.x<700:
            lose=True
        if player_rect.colliderect(bullet_rect) and bullet_rect.x !=300 and horse_random==3 and 0<horse_rect.x<700:
            lose=True
        if player_rect.colliderect(bullet_rect) and bullet_rect.x !=650 and horse_random==4 and 0<horse_rect.x<700:
            lose=True


        if lose:
            game_active = False
            screen.blit(background, (0, 0))
            screen.blit(player_over, player_over_rect)
            screen.blit(game_over_text, game_over_text_rect)
            screen.blit(press, press_rect)
            random_sentence = generate_random_sentence()
            sentence_text = font2.render(random_sentence, False, "white")
            sentence_rect = sentence_text.get_rect(center=(350, 500))
            screen.blit(sentence_text, sentence_rect)
            Final_score = font2.render("your Final score: " + str(display_time()), False, "black")
            Final_score_rect = Final_score.get_rect(center=(350, 300))
            screen.blit(Final_score, Final_score_rect)
            pygame.draw.rect(screen, (0, 0, 0), (
                sentence_rect.x - 10, sentence_rect.y - 10, sentence_rect.width + 50, sentence_rect.height + 50))
            screen.blit(sentence_text, sentence_rect)

        if player_move_right:
            player_rect.x += 4
        if player_move_left:
            player_rect.x -= 4

    pygame.display.update()
    frame.tick(60)
