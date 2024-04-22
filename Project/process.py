import pygame
import sys
import random
from Screen import *
pygame.init()
width = 1280
height = 720
RADIUS = 30
GAP = 20
# fonts
LETTER_FONT = pygame.font.SysFont('ARIAL BLACK', 40)
WORD_FONT = pygame.font.SysFont('ARIAL BLACK', 60)
class Process():
    def __init__(self):
        # images for hangman
        self.images = []
        for i in range(7):
            image = pygame.image.load("hangman" + str(i) + ".png")
            bigger_img = pygame.transform.scale(image, (image.get_width() * 1.8, image.get_height() * 1.8))
            self.images.append(bigger_img)

        # keyboard letter and the setup
        self.letters = []
        self.startx = round((width - (RADIUS * 2 + GAP) * 13) / 2)
        self.starty =500
        A = 65
        for i in range(26):
            x = self.startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
            y = self.starty + ((i // 13) * (GAP + RADIUS * 2))
            self.letters.append([x, y, chr(A + i), True])
        self.attempt = 0
        self.words = ["AFGHANISTAN", "ALBANIA", "ALGERIA", "ANDORRA", "ANGOLA", "ARGENTINA", "ARMENIA", "AUSTRALIA", "AUSTRIA", "AZERBAIJAN", "BAHAMAS", "BAHRAIN", "BANGLADESH", "BARBADOS", "BELARUS", "BELGIUM", "BELIZE", "BENIN", "BHUTAN", "BOLIVIA", "BOTSWANA", "BRAZIL", "BRUNEI", "BULGARIA", "BURKINAFASO", "BURUNDI", "CAMBODIA", "CAMEROON", "CANADA", "CHAD", "CHILE", "CHINA", "COLOMBIA", "COMOROS", "CONGO", "CROATIA", "CUBA", "CYPRUS", "DENMARK", "DJIBOUTI", "DOMINICA", "ECUADOR", "EGYPT", "ESTONIA", "ETHIOPIA", "FIJI", "FINLAND", "FRANCE", "GABON", "GAMBIA", "GEORGIA", "GERMANY", "GHANA", "GREECE", "GRENADA", "GUATEMALA", "GUINEA", "GUYANA", "HAITI", "HONDURAS", "HUNGARY", "ICELAND", "INDIA", "INDONESIA", "IRAN", "IRAQ", "IRELAND", "ISRAEL", "ITALY", "JAMAICA", "JAPAN", "JORDAN", "KAZAKHSTAN", "KENYA", "KIRIBATI", "KOSOVO", "KUWAIT", "KYRGYZSTAN", "LAOS", "LATVIA", "LEBANON", "LESOTHO", "LIBERIA", "LIBYA", "LIECHTENSTEIN", "LITHUANIA", "LUXEMBOURG", "MACEDONIA", "MADAGASCAR", "MALAWI", "MALAYSIA", "MALDIVES", "MALI", "MALTA", "MARSHALLISLANDS", "MAURITANIA", "MAURITIUS", "MEXICO", "MICRONESIA", "MOLDOVA", "MONACO", "MONGOLIA", "MONTENEGRO", "MOROCCO", "MOZAMBIQUE", "MYANMAR", "NAMIBIA", "NAURU", "NEPAL", "NETHERLANDS", "NEWZEALAND", "NICARAGUA", "NIGER", "NIGERIA", "NORTHKOREA", "NORWAY", "OMAN", "PAKISTAN", "PALAU", "PALESTINE", "PANAMA", "PAPUANEWGUINEA", "PARAGUAY", "PERU", "PHILIPPINES", "POLAND", "PORTUGAL", "QATAR", "ROMANIA", "RUSSIA", "RWANDA", "SAMOA", "SANMARINO", "SAOTOMEANDPRINCIPE", "SAUDIARABIA", "SENEGAL", "SERBIA", "SEYCHELLES", "SIERRALEONE", "SINGAPORE", "SLOVAKIA", "SLOVENIA", "SOMALIA", "SOUTHAFRICA", "SOUTHKOREA", "SOUTHSUDAN", "SPAIN", "SRILANKA", "SUDAN", "SURINAME", "SWAZILAND", "SWEDEN", "SWITZERLAND", "SYRIA", "TAIWAN", "TAJIKISTAN", "TANZANIA", "THAILAND", "TOGO", "TONGA", "TRINIDADANDTOBAGO", "TUNISIA", "TURKEY", "TURKMENISTAN", "TUVALU", "UGANDA", "UKRAINE", "UNITEDARABEMIRATES", "UNITEDKINGDOM", "UNITEDSTATES", "URUGUAY", "UZBEKISTAN", "VANUATU", "VATICANCITY", "VENEZUELA", "VIETNAM", "YEMEN", "ZAMBIA", "ZIMBABWE"]
        self.word = random.choice(self.words)
        self.guessed = []

    def imageHM(self,screen):
        # upload the images of hangman
        self.screen=screen
        screen.blit(self.images[self.attempt], (90, 50))

    def keyboard(self,screen):
        # upload the keyboard key
        for letter in self.letters:
            x, y, ltr, visible = letter
            if visible:
                pygame.draw.circle(screen, (0,0,0), (x, y), RADIUS, 3)
                text = LETTER_FONT.render(ltr, 1, (0,0,0))
                screen.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
    
    def Key_word(self,screen):
        display_word = ""
        for letter in self.word:
            if letter in self.guessed:
                display_word += letter + " "
            else:
                display_word += "_ "
        text = WORD_FONT.render(display_word, 1, (0,0,0))
        screen.blit(text, (500, 200))
        pygame.display.update()

    def restart(self):
        self.attempt = 0
        self.word = random.choice(self.words)
        self.guessed = []
        for i in range(26):
            self.letters[i][3]=True