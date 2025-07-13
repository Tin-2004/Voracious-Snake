import pygame
import random

# 初始化Pygame
pygame.init()

# 屏幕尺寸
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

# 标题
pygame.display.set_caption("贪吃蛇小游戏")

# 颜色定义
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# 时钟
clock = pygame.time.Clock()

# 蛇的属性
snake_block = 10
snake_speed = 15

# 字体
font_style = pygame.font.SysFont("simsun", 50)  # 使用宋体支持中文
score_font = pygame.font.SysFont("simsun", 35)  # 使用宋体支持中文

def show_score(score):
    value = score_font.render("您的得分: " + str(score), True, white)
    screen.blit(value, [10, 10])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen_rect = screen.get_rect()
    mesg_rect = mesg.get_rect(center=screen_rect.center)
    screen.blit(mesg, mesg_rect)

def gameLoop():
    global screen
    game_over = False
    game_close = False

    # 蛇的起始位置
    x1 = screen.get_width() / 2
    y1 = screen.get_height() / 2

    x1_change = 0
    y1_change = 0

    # 蛇身
    snake_List = []
    Length_of_snake = 1

    # 食物位置
    foodx = round(random.randrange(0, screen.get_width() - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen.get_height() - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(white)
            message("游戏结束! 按 Q/ESC-退出 或 C/空格-重新开始", red)
            show_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.VIDEORESIZE:
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c or event.key == pygame.K_SPACE:
                        # 重新开始游戏，重置所有变量
                        game_close = False
                        x1 = screen.get_width() / 2
                        y1 = screen.get_height() / 2
                        x1_change = 0
                        y1_change = 0
                        snake_List = []
                        Length_of_snake = 1
                        foodx = round(random.randrange(0, screen.get_width() - snake_block) / 10.0) * 10.0
                        foody = round(random.randrange(0, screen.get_height() - snake_block) / 10.0) * 10.0

        if game_close:
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= screen.get_width() or x1 < 0 or y1 >= screen.get_height() or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for segment in snake_List:
            pygame.draw.rect(screen, blue, [segment[0], segment[1], snake_block, snake_block])
        
        show_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen.get_width() - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, screen.get_height() - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)
    
    return game_over

def main():
    while True:
        game_should_quit = gameLoop()
        if game_should_quit:
            break

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
