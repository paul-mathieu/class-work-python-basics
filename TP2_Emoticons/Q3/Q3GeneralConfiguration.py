# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import pygame

class GeneralConfiguration:


    #==========================================================================
    # Constructor
    #==========================================================================    
    def __init__(self) :
        
        self.screenWidth = 1000
        self.screenHeight = 1200
        
        self.initPygame()
        
        # Parameters for the emoticons        
        self.emoticonSize = 500
        self.emoticonBorder = 200 
        
        # Parameters for the buttons
        self.buttonWidth = 150
        self.buttonHeight = 80



    # Initializes pygame
    def initPygame(self): 
        #Initialization
        pygame.init()
        # Sets the screen size.
        pygame.display.set_mode((self.screenWidth, self.screenHeight))    
        # Sets the timer to check event every 200 ms
        pygame.time.set_timer(pygame.USEREVENT, 200)
        # Gets pygame screen
        self.screen = pygame.display.get_surface()         
        
    # Getters
    # Compléter avec les Getters de la question Q1.4

        
    # Draws on pygame screen      
    def draw(self):
        pass




    # Displays   
    def display(self):
        # Draws on the screen surface
        self.draw()
        
        # Updates the displat and clears new timer events
        pygame.display.flip()
        pygame.event.clear(pygame.USEREVENT)
               

