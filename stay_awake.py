import pygame
import pyautogui
import os

# Initialize pygame and set up the screen
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Load the alarm sound
alarm_sound = pygame.mixer.Sound('TF001.wav')

# Flag to keep track of whether the button is pressed
button_pressed = False

# Flag to keep track of whether the alarm should play
play_alarm = False

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            button_pressed = True
            play_alarm = False  # Stop playing alarm when the button is pressed
        elif event.type == pygame.MOUSEBUTTONUP:
            button_pressed = False
            play_alarm = True  # Start playing alarm when the button is released

    # If the button is not pressed and the alarm should play, play the alarm on a loop
    if not button_pressed and play_alarm:
        pygame.mixer.Sound.play(alarm_sound, -1)  # -1 means play on a loop

    # If the button is pressed, stop the alarm
    if button_pressed:
        pygame.mixer.Sound.stop(alarm_sound)

    # Draw an exit button
    exit_button = pygame.Rect(10, 10, 100, 50)
    pygame.draw.rect(screen, (0, 0, 255), exit_button)
    font = pygame.font.Font(None, 36)
    text = font.render("Exit", True, (255, 255, 255))
    screen.blit(text, (20, 20))

    # Check for exit button click
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if exit_button.collidepoint(mouse_x, mouse_y):
        if pygame.mouse.get_pressed()[0]:  # Left mouse button pressed
            running = False

    pygame.display.flip()

# Quit pygame and clean up
pygame.quit()
