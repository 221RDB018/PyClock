import pygame
import math
import time
import sys

# Set window size and create it
width, height = 600, 600
screen = pygame.display.set_mode((width, height))  # initialize a window for display
pygame.display.set_caption('Analog Clock')  # set the current window caption

# Initialize pygame
pygame.init()  # initialize all imported pygame modules

# Colors
grey = (19, 51, 76)
orange = (253, 95, 0)
blue = (0, 87, 146)
white = (246, 246, 233)

# Clock face settings
center_x = int(width / 2)  # clock face center coordinate
center_y = int(height / 2)
radius = 225

# Clock hands length
hour_length = int(radius * 0.4)
minute_length = int(radius * 0.6)
second_length = int(radius * 0.8)

# Font settings
font = pygame.font.SysFont('Arial', int(radius * 0.1))  # hour marks font
font_speed = pygame.font.SysFont('Arial', int(radius * 0.07))  # display fonts
font_text = pygame.font.SysFont('Arial', int(radius * 0.1))


# Define hour marks

# returns x coordinate of hour marks
def x_coord(length, angle):  # length from center to the clock numbers
    return center_x + length * math.cos(angle * math.pi / 180)  # (to radians)


# returns y coordinate of hour marks
def y_coord(length, angle):
    return center_y - length * math.sin(angle * math.pi / 180)


# Angle and animation speed
angle = 0  # top of the clock
clock_speed = 6 * 0.1  # 6 degrees per second, * 0.1 , because time.sleep(0.1) for smooth animation

# Clock main loop
while True:
    for event in pygame.event.get():  # pygame.event.get() - gets events from the queue
        if event.type == pygame.QUIT:  # when the x is pressed
            pygame.quit()  # deactivates Python library
            sys.exit()  # terminates the program
        if event.type == pygame.KEYDOWN:  # when the keyboard buttons are pressed
            if event.key == pygame.K_RIGHT:  # ->
                clock_speed += 1  # increase the clock speed
            if event.key == pygame.K_LEFT:  # <-
                clock_speed -= 1
            if event.key == pygame.K_r:  # "R" resets the clock to 00:00 and speed to 6 degrees per second
                angle = 0
                clock_speed = 6 * 0.1

    # Fill the background color
    screen.fill(grey)

    # Draw clock face
    pygame.draw.circle(screen, white, (center_x, center_y), radius, 2)  # surface, color, center, radius, width
    pygame.draw.circle(screen, white, (center_x, center_y), 7, 1)  # small circle in the moddle

    # Draw hour marks
    a = 60  # initial angle
    for i in range(1, 13):  # 13 not included
        number = font.render(str(i), True, white)  # text, antialias, color
        screen.blit(number, (
        x_coord(radius - 30, a) - 5, y_coord(radius - 30, a) - 9))  # draw hour marks   blit(source, dest())
        a = a - 30  # distance between hour marks in degrees

    # Create clock face
    a = 90
    for i in range(60):
        x1 = x_coord(radius, a)  # start of the line
        y1 = y_coord(radius, a)
        if a % 30 == 0:  # draw longer lines for each hour
            x2 = x_coord(radius - 15, a)  # end of the line(line's height)
            y2 = y_coord(radius - 15, a)
        else:
            x2 = x_coord(radius - 10, a)
            y2 = y_coord(radius - 10, a)
        pygame.draw.line(screen, white, [x1, y1], [x2, y2])
        a += 6  # 360 /60 - 6  lines for ach second

    # Update clock hands
    angle += clock_speed
    hour_x = center_x + hour_length * math.sin(angle * math.pi / 180 / 3600)  # x = x0 + r * cos(a)
    hour_y = center_y - hour_length * math.cos(angle * math.pi / 180 / 3600)  # 3600 seconds in 1 hour
    minute_x = center_x + minute_length * math.sin(angle * math.pi / 180 / 60)  # 60 seconds in 1 minute
    minute_y = center_y - minute_length * math.cos(angle * math.pi / 180 / 60)
    second_x = center_x + second_length * math.sin(angle * math.pi / 180)
    second_y = center_y - second_length * math.cos(angle * math.pi / 180)

    # Draw clock hands
    pygame.draw.line(screen, blue, (center_x, center_y), (minute_x, minute_y),
                     4)  # surface, color, start_pos, end_pos, width
    pygame.draw.line(screen, orange, (center_x, center_y), (hour_x, hour_y), 6)
    pygame.draw.line(screen, white, (center_x, center_y), (second_x, second_y), 2)

    # for text on the screen
    c = round(clock_speed * 10, 0)
    speed_text = font_speed.render('Speed: ' + str(c) + ' degrees per second', True,
                                   white)  # clock speed   render(text, antialias, color)
    text_text = font_text.render('Use the <- -> arrows to change the clock speed', True, white)  # text
    screen.blit(speed_text, (width - 190, 520))  # draws text    blit(source, dest())
    r_text = font_text.render('Press "R" to reset the clock', True, white)
    screen.blit(r_text, (width - 400, 40))
    screen.blit(text_text, (width - 480, 20))

    # Update the screen
    pygame.display.update()
    # Pause for a while
    time.sleep(0.1)

