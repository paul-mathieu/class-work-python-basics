# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import pygame
from Q5Emoticon import Emoticon
from Q5Button import Button

class GeneralConfiguration:
    
    
    #==========================================================================
    # Constructor
    #==========================================================================    
    
    def __init__(self) :
        self.initPygame()
        
        # Parameters for the screen
        self.screenWidth = 1000
        self.screenHeight = 1200 
        
        # Parameters for the emoticons        
        self.emoticonSize = 400
        self.emoticonBorder = 80  
        
        # Parameters for the buttons
        self.buttonWidth = 150
        self.buttonHeight = 80
                
        # Sensors list
        self.sensors = []
        
        self.selectedSensor = 0

        
    #==========================================================================
    # Initializes pygame
    #==========================================================================    
    
    def initPygame(self): 
        #Initialization
        pygame.init()
        # Sets the screen size.
        pygame.display.set_mode((1000,1200))    
        # Sets the timer to check event every 200 ms
        pygame.time.set_timer(pygame.USEREVENT, 200)         
        # Gets pygame screen
        self.screen = pygame.display.get_surface()         
        
  
      
    #==========================================================================
    # Getters 
    #==========================================================================    

    def getScreen(self):
        return self.screen

    def getEmoticonSize(self):
        return self.emoticonSize

    def getEmoticonBorder(self):
        return self.emoticonBorder

    def getButtonWidth(self):
        return self.buttonWidth

    def getButtonHeight(self):
        return self.buttonHeight

    
    def getSensors(self):
        return self.sensors
        
    def getSelectedSensor(self):
        return self.selectedSensor
        
    def getScreenParameters(self):
        return self.screenWidth, self.screenHeight
        
    #==========================================================================
    # Adds a sensor 
    #==========================================================================    

    def addSensor(self, sensor):
        sensor.setGeneralConfiguration(self)
        sensor.setSensorId(len(self.sensors))
        sensor.setEmoticon(Emoticon(sensor))
        sensor.setButton(Button(sensor))
        self.sensors.append(sensor)


 
    #==========================================================================
    # Retrieves the sensor id from a posiiion
    #==========================================================================    

    def positionToSensorId(self, position):
        pass



    #==========================================================================
    # Checks if the display of a new sensor was requested
    #==========================================================================    

    def checkIfSensorChanged(self, eventPosition):
        pass


    
    #==========================================================================
    # Draws on pygame screen   
    #==========================================================================    

    def draw(self):
        
        # Clears the surface
        pygame.display.get_surface().fill([0, 0, 0])

        # Coords of x value for the position of the left corner on x
        buttonWidth = self.buttonWidth
        valX = self.screenWidth / 2 - (len(self.sensors) * buttonWidth) / 2


        
        self.sensors[self.selectedSensor].drawEmoticon()


        
        for sensor in self.sensors:
            
            sensor.drawButton(valX)

            valX += buttonWidth
            
            
    #==========================================================================
    # Displays
    #==========================================================================    

    def display(self):
        
        # Title for the screen
        pygame.display.set_caption("Mesure de la Température")
        
        
        # Draws on the screen surface
        self.draw()
        
        # Updates the display and clears new timer events
        pygame.display.flip()
        pygame.event.clear(pygame.USEREVENT)






#
#Question 5.a) 
#Analyser les fichiers fournis dans le dossier Q5. Dans la fonction main() du fichier
#Q5Main.py, on a ajouté un capteur à l’objet generalConfiguration à l’aide de la méthode
#addSensor(). 
#Expliquer le fonctionnement de cette méthode. 
#Que vaut l’attribut sensors de la classe GeneralConfiguration après cet ajout ?
#
#Cette méthode permet d'ajouter un attribut à la classe generalConfiguration, qui est par
#défaut optionnel. Elle permet ainsi de générer les button et emoticon correspondant, avec
#des valeurs correctes.
#
#L'attribut sensors sera alors une liste ayant pour valeur 
#




