from generator import pricestream
from news import request_news
import numpy as np
import pygame
import os
import time
import datetime

# os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'

start_date = datetime.datetime(2024, 1, 1)
next_day_time = time.time() + 1

numberarr = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_PERIOD]
history_arr = []

pygame.init()

display_info = pygame.display.Info()

screen_width = display_info.current_w
screen_height = display_info.current_h

window_size = (screen_width, screen_height)

#hyperparams
S0 = 100
mu = 0.0005
sigma = 0.015
dt = 1/100
new_price = 100
usd_bal = 10000 
stock_bal = 0
shock = 0
tempshock = 0

stock_flag = True
news_flag = False
shock_flag = False
display_news_flag = False

stock_prices = np.array([S0])

width = screen_width
height = screen_height

screen = pygame.display.set_mode(window_size,pygame.NOFRAME)
font = pygame.font.Font("font.ttf",32)
small_font = pygame.font.Font("font.ttf",19)

gliding_text = f"   APPL {round(np.random.uniform(-4,4),2)}%   NVDO {round(np.random.uniform(-4,4),2)}%   TSLO {round(np.random.uniform(-4,4),2)}%   AMZM {round(np.random.uniform(-4,4),2)}%   MCFT {round(np.random.uniform(-4,4),2)}%   GOGL {round(np.random.uniform(-4,4),2)}%  "
gliding_render = font.render(gliding_text, True, (255, 0, 0))
gliding_render2 = font.render(gliding_text, True, (255, 0, 0))

gliding_text_x = width
gliding_text_x2 = width
text_y = height - gliding_render.get_height() - 106

# os.system('cls' if os.name == 'nt' else 'clear')

clock = pygame.time.Clock()

background_image = pygame.image.load("background.png")

image_width, image_height = background_image.get_size()
image_aspect_ratio = image_width / image_height

scaled_width = min(screen_width, int(screen_height * image_aspect_ratio))
scaled_height = min(screen_height, int(screen_width / image_aspect_ratio))

background_image = pygame.transform.scale(background_image, (scaled_width, scaled_height))

image_x = (screen_width-scaled_width) // 2
image_y = (screen_height-scaled_height) // 2

buy_button = pygame.image.load("buy.png")
sell_button = pygame.image.load("sell.png")

buy_button_rect = buy_button.get_rect()
buy_button_rect.topleft = (1330,410)

sell_button_rect = buy_button.get_rect()
sell_button_rect.topleft = (1430,410)

input_box = pygame.Rect(1335,340,175,30)
input_text = ''
input_active = False

x2Flag = False

done = False
#game instance
running = True
while running:

    screen.blit(background_image,(image_x, image_y))
    
    usd_render = small_font.render(str(round(usd_bal,2)), True, (0,0,0))
    stock_render = small_font.render(str(round(stock_bal,2)), True, (0,0,0))
    screen.blit(usd_render,(865,631))
    screen.blit(stock_render,(865,680))

    gliding_text_x -= 2

    if x2Flag:
        gliding_text_x2 -= 2

    if gliding_text_x < 0:
        x2Flag = True
    if gliding_text_x + gliding_render.get_width() < 0:
        gliding_text_x = width
    if gliding_text_x2 + gliding_render2.get_width() < 0:
        gliding_text_x2 = width

    if stock_flag:
        start_time = time.time()
        next_price_change_time = start_time + np.random.uniform(0,0.4)
        stock_flag = False
    
    if time.time() > next_price_change_time:
        new_price = pricestream(new_price,mu,sigma,dt)
        stock_prices = np.append(stock_prices, new_price)
        if stock_prices[-1] >= stock_prices[-2]:
            price_text = font.render(f"{new_price}", True, (116, 208, 164))
        else:
            price_text = font.render(f"{new_price}", True, (206, 90, 86))
        stock_flag = True

    if not news_flag and not shock_flag:
        news_start_time = time.time()
        next_news_time = news_start_time + np.random.randint(12,17)
        news_flag = True

    if news_flag and time.time() > next_news_time-np.random.randint(3,7):
        if shock == 0:
            shock = request_news()
        display_news_flag = True

    
    if display_news_flag:
        max_width = 450
        try:
            words = shock[2].split()
        except:
            words = tempshock[2].split()
        lines = []
        current_line = ''
        for word in words:
            test_line = current_line + word + ' '
            if small_font.size(test_line)[0] < max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + ' '
        lines.append(current_line)

        line_height = small_font.get_linesize()
        total_height = len(lines) * line_height

        y = 150
        for line in lines:
            rendered_line = small_font.render(line, True, (0, 0, 0))
            screen.blit(rendered_line, (20, y))
            y += line_height
        
        try:
            words = shock[3].split()
        except:
            words = tempshock[3].split()
        lines = []
        current_line = ''
        for word in words:
            test_line = current_line + word + ' '
            if small_font.size(test_line)[0] < max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + ' '
        lines.append(current_line)

        line_height = small_font.get_linesize()
        total_height = len(lines) * line_height

        y = 240
        for line in lines:
            rendered_line = small_font.render(line, True, (0, 0, 0))
            screen.blit(rendered_line, (20, y))
            y += line_height
    
    if news_flag and time.time() > next_news_time:
        mu += shock[0]
        tempshock = shock
        # print(mu)
        end_shock = time.time() + shock[1]
        shock = 0
        shock_flag = True
        news_flag = False
        
        
    if shock_flag and time.time() > end_shock:
        mu -= tempshock[0]
        # print(mu)
        shock_flag = False
        
    try:
        screen.blit(price_text, (width-172,height-252))
    except:
        continue

    screen.blit(gliding_render, (gliding_text_x, text_y))
    screen.blit(gliding_render2, (gliding_text_x2, text_y))

    arr = stock_prices[-70:]
    candle_width = 10
    yframe = max(arr) - min(arr)
    
    for i in range(len(arr)):
            try:
                if arr[i+1] >= arr[i]:
                    pygame.draw.rect(screen, (116, 208, 164), pygame.Rect(523+i*candle_width, 200+400*(max(arr)-arr[i+1])/yframe, candle_width, 400*(arr[i+1]-arr[i])/yframe))
                else:
                    pygame.draw.rect(screen, (206, 90, 86), pygame.Rect(523+i*candle_width, 200+400*(max(arr)-arr[i])/yframe, candle_width, 400*(arr[i]-arr[i+1])/yframe))
            except:
                pass

    mouse_pos = pygame.mouse.get_pos()

    screen.blit(buy_button, buy_button_rect)
    screen.blit(sell_button, sell_button_rect)

    if input_active:
        pygame.draw.rect(screen, (180,180,180), input_box)
        try:
            helper_render = small_font.render(f'USD: {round(new_price*float(input_text),2)}', True, (0,0,0))
            screen.blit(helper_render,(1335,313))
            helper_render2 = small_font.render(f'fees: {round(new_price*float(input_text)*0.02,2)}', True, (0,0,0))
            screen.blit(helper_render2,(1335,293))
        except:
            pass

    else:
        pygame.draw.rect(screen, (160,160,160), input_box)
        
    input_surface = small_font.render(input_text, True, (0,0,0))
    screen.blit(input_surface, (input_box.x + 5, input_box.y + 5))


    if buy_button_rect.collidepoint(mouse_pos):
        # Darken the button
        button_darkened = pygame.Surface(buy_button.get_size())
        button_darkened.fill((0,0,0))
        button_darkened.set_alpha(40)  # Adjust transparency to darken the button
        screen.blit(button_darkened, buy_button_rect)
    
    if sell_button_rect.collidepoint(mouse_pos):
        # Darken the button
        button_darkened = pygame.Surface(buy_button.get_size())
        button_darkened.fill((0,0,0))
        button_darkened.set_alpha(40)  # Adjust transparency to darken the button
        screen.blit(button_darkened, sell_button_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_text != '':
                if buy_button_rect.collidepoint(event.pos):
                    if new_price*float(input_text) <= usd_bal:
                        usd_bal -= new_price*float(input_text)
                        stock_bal += float(input_text)*0.995
                        history_arr.insert(0,f'BUY {input_text} @ {new_price} for {round(new_price*float(input_text),2)}, fees: {round(new_price*float(input_text)*0.005,2)}')
                        input_text = ''    
                if sell_button_rect.collidepoint(event.pos):
                        if float(input_text) <= stock_bal:
                            usd_bal += new_price*float(input_text)*0.995
                            stock_bal -= float(input_text)
                            history_arr.insert(0,f'SELL {input_text} @ {new_price} for {round(new_price*float(input_text),2)}, fees: {round(new_price*float(input_text)*0.005,2)}')
                            input_text = ''
            if input_box.collidepoint(event.pos):
                input_active = True
            else:
                input_active = False

        if event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_BACKSPACE:
                    try:
                        input_text = input_text[:-1]
                    except:
                        continue
                elif event.key == pygame.K_PERIOD and '.' not in input_text:
                    input_text += event.unicode
                else:
                    if event.key != pygame.K_SPACE and len(input_text) < 13 and event.key in numberarr and event.key != pygame.K_PERIOD:
                        input_text += event.unicode

    for i, item in enumerate(history_arr[:6]):
        history_text = small_font.render(item, True, (0, 0, 0))
        screen.blit(history_text, (30, 520+i * 30))

    if start_date < datetime.datetime(2025, 1, 1):
        if time.time() > next_day_time:
            start_date += datetime.timedelta(days=1)
            next_day_time = time.time() + 1
    else:
        done = True

    time_text = small_font.render(str(start_date.strftime("%d-%m-%Y")), True, (0, 0, 0))
    screen.blit(time_text, (1147, 665))

    if done:
        total_val = usd_bal + stock_bal * new_price
        target_val = 100*new_price
        ending = pygame.image.load("ending.png")
        ending_rect = ending.get_rect()
        ending_x = (width - ending_rect.width) // 2
        ending_y = (height - ending_rect.height) // 2
        screen.blit(ending,(ending_x,ending_y))
        total_val_render = small_font.render(str(round(total_val,2)), True, (0, 0, 0))
        screen.blit(total_val_render, (705, 270))
        target_val = small_font.render(str(target_val), True, (0, 0, 0))
        screen.blit(target_val, (705, 360))
        pygame.display.flip()

    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()