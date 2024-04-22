import pygame
import sys
from process import *
pygame.init()
width = 1280
height = 720

font = pygame.font.Font("assets/font.ttf", 75)
font2 = pygame.font.Font("assets/font.ttf", 40)
BG = pygame.image.load("assets/Background.png")
process = Process()

class Screen():
    def __init__(self):
        self.menu = True
        self.player2_input_menu = False
        self.player1 = False
        self.player2 = False
        self.player2_word = ''
        self.Quit_btn = font.render('Quit',True,'black')
        self.Quit_btn_rect = self.Quit_btn.get_rect(center=(640, 550))
        if self.player1:
            process.word = process.word
    def Menu(self,screen):
        self.screen = screen
        pos = pygame.mouse.get_pos()
        screen.blit(BG,(0,0))
        Hangman = font.render('Hangman', True, '#4793AF')
        Hangman_rect = Hangman.get_rect(center=(640, 100))
        player1 = font.render('1 Player',True,'#DD5746')
        player1_rect = player1.get_rect(center=(640, 250))
        player2 = font.render('2 Players',True,'#DD5746')
        player2_rect = player2.get_rect(center=(640, 400))
        if player1_rect.collidepoint(pos):
            player1 = font.render('1 Player',True,'blue')
            if pygame.mouse.get_pressed()[0]:
                self.menu = False
                self.player1 = True
        if player2_rect.collidepoint(pos):
            player2 = font.render('2 Players',True,'blue')
            if pygame.mouse.get_pressed()[0]:
                self.menu = False
                self.player2_input_menu =True
        if self.Quit_btn_rect.collidepoint(pos):
            self.Quit_btn = font.render('Quit',True,'red')
            if pygame.mouse.get_pressed()[0]:
                sys.exit()
        else:
            self.Quit_btn = font.render('Quit',True,'#8B322C')
        screen.blit(Hangman,Hangman_rect)
        screen.blit(player1,player1_rect)
        screen.blit(player2,player2_rect)
        screen.blit(self.Quit_btn,self.Quit_btn_rect)
        pygame.display.update()
    def player2_screen(self,screen):
        Player_key = font.render(self.player2_word.upper(), True, 'black')
        Box_Input = pygame.Rect(200, 300, 800, 100)
        pos = pygame.mouse.get_pos()
        EnterBTN = font.render('Enter',True,'black')
        Enter_Promt = font2.render('Enter Your Word',True,'black')
        EnterBTN_rect = EnterBTN.get_rect(center=(1050, 550))
        if EnterBTN_rect.collidepoint(pos) and not self.player1:
            EnterBTN = font.render('Enter',True,'green')
            if pygame.mouse.get_pressed()[0]:
                process.word = pygame.display.flip()
                return False
        else:
            self.EnterBTN = font.render('Enter',True,'black')
        pygame.draw.rect(screen,(173, 216, 230),Box_Input,2)
        screen.blit(Enter_Promt,(200,250))
        screen.blit(Player_key,(Box_Input.x+5,Box_Input.y+10))
        screen.blit(EnterBTN,EnterBTN_rect)
        return True
    def Win(self,screen,Theword,message):
        self.player1 = False
        self.player2 = False
        self.player2_input_menu = False
        pos = pygame.mouse.get_pos()
        win_message = font2.render(message, True, '#4793AF')
        win_message2 = font2.render('Your word is '+ Theword, True, '#4793AF')
        Back_btn = font.render('Back',True,'#DD5746')
        Back_btn_rect = Back_btn.get_rect(center=(1100, 550))
        if self.Quit_btn_rect.collidepoint(pos):
            self.Quit_btn = font.render('Quit',True,'red')
            if pygame.mouse.get_pressed()[0]:
                sys.exit()
        else:
            self.Quit_btn = font.render('Quit',True,'#DD5746')
        if Back_btn_rect.collidepoint(pos) and not self.player1:
            Back_btn = font.render('Back',True,'green')
            if pygame.mouse.get_pressed()[0]:
                return False
        else:
            self.Back_btn = font.render('Back',True,'#DD5746')
        screen.blit(win_message,(200, 100))
        screen.blit(win_message2,(width/4, 250))
        screen.blit(Back_btn,Back_btn_rect)
        screen.blit(self.Quit_btn,self.Quit_btn_rect)
        pygame.display.update()
        return True
    