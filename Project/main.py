import pygame, sys
import random,math
from Screen import *
from process import *
# from button import Button

pygame.init()
# screen set up
WIDTH = 1280
HEIGHT = 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")
BG = pygame.image.load("assets/Background.png")
screen = Screen()
process = Process()
Win_Sound = pygame.mixer.Sound("assets/like.mp3")
Lose_Sound = pygame.mixer.Sound("assets/dislike.mp3")
win2_Sound = pygame.mixer.Sound("assets/win2.mp3")
while True:
    if screen.menu:
        win2_Sound.stop()
        screen.Menu(SCREEN)
    if screen.player1:
        SCREEN.fill('white')
        process.imageHM(SCREEN)
        process.keyboard(SCREEN)
        process.Key_word(SCREEN)
    if screen.player2_input_menu:
        SCREEN.fill('white')
        screen.player2_screen(SCREEN)
        start_player2 = screen.player2_screen(SCREEN)
        if not start_player2:
            screen.player2 = True
    if screen.player2:
        SCREEN.fill('white')
        process.imageHM(SCREEN)
        process.keyboard(SCREEN)
        process.Key_word(SCREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if screen.player1:  
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in process.letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            process.guessed.append(ltr)
                            Win_Sound.stop()
                            Lose_Sound.stop()
                            if ltr not in process.word:
                                process.attempt += 1
                                Lose_Sound.play()
                            else:
                               Win_Sound.play()
        if screen.player2_input_menu and not screen.player2:  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    screen.player2_word = screen.player2_word[:-1]
                elif event.unicode.isalpha():
                    screen.player2_word += event.unicode
        if screen.player2: 
            process.word = ''
            process.word += screen.player2_word.upper()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in process.letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            process.guessed.append(ltr)
                            Win_Sound.stop()
                            Lose_Sound.stop()
                            if ltr not in process.word:
                                process.attempt += 1
                                Lose_Sound.play()
                            else:
                               Win_Sound.play()
    win = True
    for letter in process.word:
        if letter not in process.guessed:
            win = False
    if win:
        SCREEN.blit(BG,(0,0))
        message='Congratulation You Won!!!'
        win2_Sound.play()
        screen.Win(SCREEN, process.word, message)
        continue_game = screen.Win(SCREEN, process.word, message)
        if not continue_game:
            process.restart()
            screen.player2_word=''
            screen.menu=True
            screen.player2 = False
    if process.attempt == 6:
        SCREEN.fill('#8B0000')
        message='You Lost the game !!!'
        screen.Win(SCREEN, process.word, message)
        continue_game = screen.Win(SCREEN, process.word, message)
        if not continue_game:
            process.restart()
            screen.player2_word=''
            screen.menu=True
    pygame.display.update()