##########
#temp.py
##########

########################################################################
# MAIN CLASS FOR BILLIARDS - STYLE CARROM
# Author: Aditya Shekar
# Section H
# 15-112 2017 Fall
# Professor: Kelly Rivers
# Mentor: Kyle Chin
########################################################################

########################################################################
# Welcome! This is the code for a game that is much like carrom (an Indian board
# game), but with a small twist. The gameplay functions under an aspect of
# billiards as well. The player(s) must direct a striker piece towards other 
# carrom pieces in order to sink them into pockets. 
#
# The game makes use of modules native to python such as math and copy, but it also
# makes use of Tkinter 
#
# The core algorithmic aspects of this project involve the creation of a robust physics
# engine to run the game and the creation of various functional AI's against which 
# the player can play. 
#
########################################################################


####################
# Tkinter model from 112 notes
####################

##########################
# Elastic Collision Modeling Equations from Wikipedia
# https://en.wikipedia.org/wiki/Elastic_collision
# Other assistance with respect to understanding the equations
###########################

####################
# Event based animation code from 112 notes
####################


#########################################################
# Pydocs were used for conceptual understanding of the material
#########################################################

#########################################################
#Mouse Wrapper Code and Assistance
#https://stackoverflow.com/questions/22925599/mouse-position-python-tkinter
#Not currently implemented
#Tkinter hit capacity with this feature. Efficiency and speed were prioritized.
#
#########################################################

##########################################################
# Further light conceptual assistance from 
# http://cs231n.github.io/python-numpy-tutorial/#numpy
# https://www.youtube.com/watch?v=-llHYUMH9Dg&t=158s
# https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.linalg.solve.html
# https://www.real-world-physics-problems.com/physics-of-billiards.html
# https://en.wikipedia.org/wiki/Dot_product
##########################################################
# events-example0.py
# Barebones timer, mouse, and keyboard events


#Modules to import
from tkinter import *
import math
import time 
import random
import copy
from classPieces import *


####################################
# customize these functions
####################################

# Here we set up all the necessary data for game play.
# This includes the pieces, pockets, and player scores.
# It also creates a variable to control gameflow.
def init(data):
    
    #Queen piece
    centerX = data.width/2
    centerY = data.height/2
    queen1 = Queen(centerX, centerY)
    
    #Generic Carrom Men
    centerX = data.width/2
    centerY = data.height/2 - 30
    carrom1 = CarromMan(centerX, centerY, "black")
    
    centerX = data.width/2
    centerY -= 30
    carrom2 = CarromMan(centerX, centerY, "brown")
    
    centerX = data.width/2
    centerY += 90
    carrom3 = CarromMan(centerX, centerY, "brown")
    
    centerX = data.width/2
    centerY += 30
    carrom4 = CarromMan(centerX, centerY, "brown")
    
    
    centerX = data.width/2 + 30
    centerY = data.height/2 - 15
    carrom5 = CarromMan(centerX, centerY, "brown")
    
    centerY -= 30
    carrom6 = CarromMan(centerX, centerY, "black")
    
    centerY += 60
    carrom7 = CarromMan(centerX, centerY, "black")
    
    centerY += 30
    carrom8 = CarromMan(centerX, centerY, "black")
    
    
    
    
    centerX = data.width/2 - 30
    centerY = data.height/2 - 15
    carrom9 = CarromMan(centerX, centerY, "brown")
    
    centerY -= 30
    carrom10 = CarromMan(centerX, centerY, "black")
    
    centerY += 60
    carrom11 = CarromMan(centerX, centerY, "black")
    
    centerY += 30
    carrom12 = CarromMan(centerX, centerY, "black")
    
    centerX = data.width/2 - 60
    centerY = data.height/2
    carrom13 = CarromMan(centerX, centerY, "black")
    
    centerY -= 30
    carrom14 = CarromMan(centerX, centerY, "brown")
    
    centerY += 60
    carrom15 = CarromMan(centerX, centerY, "brown")
    
    centerX = data.width/2 + 60
    centerY = data.height/2
    carrom16 = CarromMan(centerX, centerY, "black")
    
    centerY -= 30
    carrom17 = CarromMan(centerX, centerY, "brown")
    
    centerY += 60
    carrom18 = CarromMan(centerX, centerY, "brown")
    
    #Main Striker
    centerX = data.width/3
    centerY = 8*data.height/10
    mainStriker = Striker(centerX, centerY)
    
    #Pockets
    pock1 = Pocket(20, 20)
    pock2 = Pocket(data.width - 20, 20)
    pock3 = Pocket(20, data.height - 20)
    pock4 = Pocket(data.width - 20, data.height - 20)
    
    #Lists to store them
    data.pieces = []
    data.pockets = []
    
    #Here we append them to the lists as appropriate
    data.pieces.append(queen1)
    data.pieces.append(carrom1)
    data.pieces.append(carrom2)
    data.pieces.append(carrom3)
    data.pieces.append(carrom4)
    data.pieces.append(carrom5)
    data.pieces.append(carrom6)
    data.pieces.append(carrom7)
    data.pieces.append(carrom8)
    data.pieces.append(carrom9)
    data.pieces.append(carrom10)
    data.pieces.append(carrom11)
    data.pieces.append(carrom12)
    data.pieces.append(carrom13)
    data.pieces.append(carrom14)
    data.pieces.append(carrom15)
    data.pieces.append(carrom16)
    data.pieces.append(carrom17)
    data.pieces.append(carrom18)
    data.pieces.append(mainStriker)
    
    data.pockets.append(pock1)
    data.pockets.append(pock2)
    data.pockets.append(pock3)
    data.pockets.append(pock4)
    
    #Define gamestate, gameflow, currentplayer, scores, and a list for shots
    #made
    data.gameState = 0 
    data.currPlayer = "Brown"
    data.switched = False
    data.blackCount = 0
    data.brownCount = 0
    data.shotMade = []
    """
    data.mouseX = 0
    data.mouseY = 0
    
    data.impX = 0 
    data.impY = 0
    """




#Runs the multiplayer for the game
#Uses the currPlayer variable to handle switch offs
#Helper Function
def multiplayer(event, data):
    x = event.x
    y = event.y
    print(x,y)
    for pieceComp in data.pieces:
        if(type(pieceComp) == Striker):
            pieceComp.dy = (y - pieceComp.y)/10
            pieceComp.dx = (x - pieceComp.x)/10
    data.switched = True
    
    

#Runs the easy level, it makes use of random numbers for the AI.
#Helper Function
def easy(event, data):
    if(data.currPlayer == "Black"):
        x = event.x
        y = event.y
        print(x,y)
        for pieceComp in data.pieces:
            if(type(pieceComp) == Striker):
                pieceComp.dy = (y - pieceComp.y)/10
                pieceComp.dx = (x - pieceComp.x)/10
        data.switched = True
        
    #Uses the random module to direct the AI
    elif(data.currPlayer == "Brown"):
        for pieceComp in data.pieces:
            if(type(pieceComp) == Striker):
                pieceComp.dy = random.randint(-25, 25)
                pieceComp.dx = random.randint(-25, 25)
        data.switched = True


#This is the Medium AI separated out
#It makes a general decision in the direction of a piece 
#This is a helper function
def mediumAI(data):
    nearPock = None
    nearPiece = None
    strikerX = None
    strikerY = None
    dist = None
    for pieceComp in data.pieces:
        if(type(pieceComp) == Striker):
            strikerX = pieceComp.x
            strikerY = pieceComp.y
        elif(type(pieceComp) != Striker):
            for pocket in data.pockets:
                if(dist == None):
                    dist = ((pocket.x - pieceComp.x)**2 + (pocket.y - pieceComp.y)**2)**0.5
                    nearPock = pocket
                    nearPiece = pieceComp
                else:
                    temp = ((pocket.x - pieceComp.x)**2 + (pocket.y - pieceComp.y)**2)**0.5
                    if(temp < dist):
                        dist = temp
                        nearPock = pocket
                        nearPiece = pieceComp

    for strikerFind in data.pieces:
        if(type(strikerFind) == Striker):
            strikerFind.dy = (nearPiece.y - strikerY)/10
            strikerFind.dx = (nearPiece.x - strikerX)/10
    data.switched = True

#This runs the medium level and makes use of the medium AI
#This is a helper function
def medium(event, data):
    if(data.currPlayer == "Black"):
        x = event.x
        y = event.y
        print(x,y)
        for pieceComp in data.pieces:
            if(type(pieceComp) == Striker):
                pieceComp.dy = (y - pieceComp.y)/10
                pieceComp.dx = (x - pieceComp.x)/10
        data.switched = True

    elif(data.currPlayer == "Brown"):
        mediumAI(data)
        
#This stores a list of tuples of possible piece and pocket pairs for the AI 
#to consider; it does so in the hopes of deducing the best move present. 
#Moves are ranked based on how close they are to the pockets
def possLocations(data):
    nearPock = None
    nearPiece = None
    strikerX = None
    strikerY = None
    dist = None
    strik = None
    potentialMoves = []
    for pieceComp in data.pieces:
        if(type(pieceComp) == Striker):
            strik = pieceComp
            strikerX = pieceComp.x
            strikerY = pieceComp.y
        elif(type(pieceComp) != Striker):
            finalPiece = pieceComp
            for pocket in data.pockets:
                finalPocket = pocket
                if(dist == None):
                    dist = ((pocket.x - pieceComp.x)**2 + (pocket.y - pieceComp.y)**2)**0.5
                    nearPock = pocket
                    nearPiece = pieceComp
                    potentialMoves.append((nearPiece, nearPock))
                else:
                    temp = ((pocket.x - pieceComp.x)**2 + (pocket.y - pieceComp.y)**2)**0.5
                    if(temp < dist):
                        dist = temp
                        nearPock = pocket
                        nearPiece = pieceComp
                        potentialMoves.insert(0, (nearPiece, nearPock))
    return potentialMoves


#Shootengine for advanced AI to predict where to shoot. Note that this is also implemented 
#in another function,  but it is done so intentionally to maintain the flow of the code.
def shootEngine(finalPiece, finalPocket, strikerX, strikerY, strik):
    pockDist = ((finalPocket.x - finalPiece.x)**2 + (finalPocket.y - finalPiece.y)**2)**0.5
    pieceDist = ((finalPiece.x - strikerX)**2 + (finalPiece.y - strikerY)**2)**0.5
    
    pockVec = (finalPocket.x - finalPiece.x, finalPocket.y - finalPiece.y)
    pieceVec = (finalPiece.x - strikerX, finalPiece.y - strikerY)
    
    finVelVec = (pockVec[0]/10, pockVec[1]/10)
    angleTemp = math.atan(finVelVec[1]/finVelVec[0])
    
    if(finVelVec[0] >= 0):
        if(finVelVec[1] >= 0):
            d1 = -(strik.rad + finalPiece.rad)*math.cos(angleTemp)
            d2 = -(strik.rad + finalPiece.rad)*math.sin(angleTemp)
        elif(finVelVec[1] < 0):
            d1 = -(strik.rad + finalPiece.rad)*math.cos(angleTemp)
            d2 = -(strik.rad + finalPiece.rad)*math.sin(angleTemp)
    elif(finVelVec[0] < 0):
        if(finVelVec[1] >= 0):
            d1 = (strik.rad + finalPiece.rad)*math.cos(angleTemp)
            d2 = (strik.rad + finalPiece.rad)*math.sin(angleTemp)
        elif(finVelVec[1] < 0):
            d1 = (strik.rad + finalPiece.rad)*math.cos(angleTemp)
            d2 = (strik.rad + finalPiece.rad)*math.sin(angleTemp)
    
    x = finalPiece.x + d1
    y = finalPiece.y + d2
    return (x,y)

#This function is used in our theoretical advanced AI to determine whether or not a path is clear
def overlap(x, y, r, data):
    for pieceTest in data.pieces:
        if(type(pieceTest) != Striker):
            if((((pieceTest.x - x)**2 + (pieceTest.y - y)**2)**0.5) <= pieceTest.rad + r):
                return False
    return True
            

#This is the theoretical advanced AI, it currently isn't implemented as it is rather
#punishing on Tkinter with respect to speed and efficiency. However its implementation takes
#advantage of possLocations and refines it to those moves which are open shots for the AI.
#This is done in the hopes that the AI will make a better decision.
def advancedPossLocations(data):
    addBool = True
    potentialMoves = possLocations(data)
    startX = 0
    startY = 0
    pieceX = 0
    pieceY = 0
    strik = None
    finList = []
    oneVal = False
    for pieceComp in data.pieces:
        if(type(pieceComp) == Striker):
            startX = pieceComp.x
            startY = pieceComp.y
            strik = pieceComp
    for testTup in potentialMoves:
        if(oneVal == False):
            finList.append(testTup)
        addBool = True
        tPiece = testTup[0]
        tPocket = testTup[1]
        pos = shootEngine(tPiece, tPocket, startX, startY, strik)
        strik.dx = (pos[0] - strik.x)/10
        strik.dy = (pos[1] - strik.y)/10
        tPiece.dx = (tPocket.x - tPiece.x)/10
        tPiece.dy = (tPocket.y - tPiece.y)/10
        pieceX = tPiece.x
        pieceY = tPiece.y
        pieceRad = tPiece.rad
        strikerRad = strik.rad
        while(startX != pos[0] and startY != pos[1]):
            startX += strik.dx
            startY += strik.dy
            if(overlap(startX, startY, strikerRad, data)):
                addBool = False
        while(pieceX != tPocket.x and pieceY != tPocket.y):
            pieceX += tPiece.dx
            pieceY += tPiece.dy 
            if(overlap(pieceX, pieceY, pieceRad, data)):
                addBool = False
        if(addBool):
            finList.append(testTup)
    return finList 
        
            


#This is the hardAI which makes use of possLocations and makes use of another physics engine.
#to make a shot at a piece with a greater degree of accuracy than the medium level.
#It performs surprisingly well, without overpowering the user.
#This is important as it could otherwise discourage the player from playing the game.
#It is a helper function.
def hardAI(data):
    try:
        #Finds the striker piece.
        potentialMoves = possLocations(data)
        for pieceComp in data.pieces:
            if(type(pieceComp) == Striker):
                strik = pieceComp
                strikerX = pieceComp.x
                strikerY = pieceComp.y
                
        #Checks for valid positioning
        for tuple in potentialMoves:
            tPiece = tuple[0]
            tPocket = tuple[1]
            finalPiece = tPiece
            finalPocket = tPocket
            if(strikerX < tPiece.x and tPiece.x < tPocket.x):
                if(strikerY < tPiece.y and tPiece.y < tPocket.y):
                    finalPiece = tPiece
                    finalPocket = tPocket
                    break
                elif(tPocket.y < tPiece.y and tPiece.y < strikerY):
                    finalPiece = tPiece
                    finalPocket = tPocket
                    break
            elif(tPocket.x < tPiece.x and tPiece.x < strikerX):
                if(strikerY < tPiece.y and tPiece.y < tPocket.y):
                    finalPiece = tPiece
                    finalPocket = tPocket
                    break
                elif(tPocket.y < tPiece.y and tPiece.y < strikerY):
                    finalPiece = tPiece
                    finalPocket = tPocket
                    break
        
        #Checks to find the appropriate spot to shoot
        pockDist = ((finalPocket.x - finalPiece.x)**2 + (finalPocket.y - finalPiece.y)**2)**0.5
        pieceDist = ((finalPiece.x - strikerX)**2 + (finalPiece.y - strikerY)**2)**0.5
        
        pockVec = (finalPocket.x - finalPiece.x, finalPocket.y - finalPiece.y)
        pieceVec = (finalPiece.x - strikerX, finalPiece.y - strikerY)
        
        finVelVec = (pockVec[0]/10, pockVec[1]/10)
        angleTemp = math.atan(finVelVec[1]/finVelVec[0])
        
        if(finVelVec[0] >= 0):
            if(finVelVec[1] >= 0):
                d1 = -(strik.rad + finalPiece.rad)*math.cos(angleTemp)
                d2 = -(strik.rad + finalPiece.rad)*math.sin(angleTemp)
            elif(finVelVec[1] < 0):
                d1 = -(strik.rad + finalPiece.rad)*math.cos(angleTemp)
                d2 = -(strik.rad + finalPiece.rad)*math.sin(angleTemp)
        elif(finVelVec[0] < 0):
            if(finVelVec[1] >= 0):
                d1 = (strik.rad + finalPiece.rad)*math.cos(angleTemp)
                d2 = (strik.rad + finalPiece.rad)*math.sin(angleTemp)
            elif(finVelVec[1] < 0):
                d1 = (strik.rad + finalPiece.rad)*math.cos(angleTemp)
                d2 = (strik.rad + finalPiece.rad)*math.sin(angleTemp)
        
        x = finalPiece.x + d1
        y = finalPiece.y + d2
        
        
        #Makes the shot with an augmented velocity vector to ensure sufficient strength
        for strikerFind in data.pieces:
            if(type(strikerFind) == Striker):
                augmentedDist = (((y - strikerY)/10)**2 + ((x - strikerX)/10)**2)**0.5
                an = math.atan(((y - strikerY)/10)/((x - strikerX)/10))
                augmentedDist += 15
                if(x - strikerX > 0):
                    if(y - strikerY > 0):
                        strikerFind.dx = abs(augmentedDist*math.cos(an))
                        strikerFind.dy = abs(augmentedDist*math.sin(an))
                    else:
                        strikerFind.dx = abs(augmentedDist*math.cos(an))
                        strikerFind.dy = -abs(augmentedDist*math.sin(an))
                else:
                    if(y - strikerY > 0):
                        strikerFind.dx = -abs(augmentedDist*math.cos(an))
                        strikerFind.dy = abs(augmentedDist*math.sin(an))
                    else:
                        strikerFind.dx = -abs(augmentedDist*math.cos(an))
                        strikerFind.dy = -abs(augmentedDist*math.sin(an))
        
        data.switched = True
    except:
        pass
        
#This is the level hard. 
#It runs the level hard.
#It is a helper function. 
def hard(event, data):
    if(data.currPlayer == "Black"):
        x = event.x
        y = event.y
        print(x,y)
        for pieceComp in data.pieces:
            if(type(pieceComp) == Striker):
                pieceComp.dy = (y - pieceComp.y)/10
                pieceComp.dx = (x - pieceComp.x)/10
        data.switched = True
    elif(data.currPlayer == "Brown"):
        hardAI(data)
        
        

#This function handles the mouse pressed event which allows for proper gameplay
#This can occur either between two different players or between the player and the
#AI. There are four possible game states: multiplayer, easy, medium, and hard. 
#There are two players in at any time 'black' and 'brown' who exchange and trade
#turns. The brown is the AI in the easy, medium, and hard levels. 
def mousePressed(event, data):
    #Multiplayer State
    if(data.gameState == 1):
        multiplayer(event, data)
    
    #Easy State
    elif(data.gameState == 2):
        easy(event, data)
    
    #Medium State
    elif(data.gameState == 3):
        medium(event, data)
    
    #Hard State
    elif(data.gameState == 4):
        hard(event, data)
        
#This functions mans the flow of the game
#It controls one state to another, and allows the player to start, and restart 
#the game with different levels, etc.
#There are five states.
def keyPressed(event, data):
    if(event.keysym == "s" and data.gameState == 0):
        init(data)
        data.gameState = 1
        data.currPlayer = "Black"
    elif(event.keysym == "e" and data.gameState == 0):
        init(data)
        data.gameState = 2
        data.currPlayer = "Black"
    elif(event.keysym == "m" and data.gameState == 0):
        init(data)
        data.gameState = 3
        data.currPlayer = "Black"
    elif(event.keysym == "h" and data.gameState == 0):
        init(data)
        data.gameState = 4
        data.currPlayer = "Black"
    elif(event.keysym == "r" and (data.gameState == 10 or 
    data.gameState == 1 or data.gameState == 2 or data.gameState == 3 or data.gameState == 4)):
        init(data)
        data.gameState = 0

"""
#Stack Overflow Assistance
def moveMouse(event, data):
    data.mouseX = event.x
    data.mouseY = event.y
"""

#This checks for board stasis
#It is important in timer fired
def boardStasis(data):
    for piece in data.pieces:
        if(piece.dx != 0 or piece.dy != 0):
            return False
    return True

# This function basically controls the entire aesthetic aspect of gameplay.
# It has the core physics engine for collision modeling, and runs the frictional modeling for all pieces.
# It runs the corner and wall bouncing.
# It also runs all of the score tallying, and it switches players as appropriate.
def timerFired(data):
    try:
        #Checks for board stasis, and swithces players if so.
        if(boardStasis(data) == True and data.switched):
            if(len(data.madeShot) == len(data.pieces)):
                if(data.currPlayer == "Black"):
                    data.currPlayer = "Brown"
                elif(data.currPlayer == "Brown"):
                    data.currPlayer = "Black"
            data.switched = False
        if(boardStasis(data) == True):
            data.madeShot = copy.deepcopy(data.pieces)
            
        #Collsions against the walls. 
        for pieceComp in data.pieces:
            if (pieceComp.x + pieceComp.rad >= data.width - 6):
                pieceComp.x -= 5
                pieceComp.dx = -pieceComp.dx
            elif(pieceComp.x - pieceComp.rad <= 6):
                pieceComp.x += 5
                pieceComp.dx = -pieceComp.dx
            if (pieceComp.y + pieceComp.rad >= data.height - 6):
                pieceComp.y -= 5
                pieceComp.dy = -pieceComp.dy
            elif(pieceComp.y - pieceComp.rad <= 6):
                pieceComp.y += 5
                pieceComp.dy = -pieceComp.dy
            pieceComp.x += pieceComp.dx
            pieceComp.y += pieceComp.dy 
            
            #Checks if the pieces have been sunk into the pockets. 
            #Removes them if so, tallies the points as appropriate.
            #Assigns them to the correct person, etc. etc.
            for pocket in data.pockets:
                if(((pieceComp.x - pocket.x)**2 + 
                    (pieceComp.y - pocket.y)**2)**0.5 <= pocket.rad):
                    if(isinstance(pieceComp, Queen)):
                        if(data.currPlayer == "Black"):
                            data.blackCount += 3
                        elif(data.currPlayer == "Brown"):
                            data.brownCount += 3
                        data.pieces.remove(pieceComp)
                    elif(isinstance(pieceComp, CarromMan)):
                        if(data.currPlayer == "Black"):
                            data.blackCount += 1
                        elif(data.currPlayer == "Brown"):
                            data.brownCount += 1
                        data.pieces.remove(pieceComp)
                    elif(isinstance(pieceComp, Striker)):
                        if(data.currPlayer == "Black"):
                            data.blackCount -= 1
                        elif(data.currPlayer == "Brown"):
                            data.brownCount -= 1
                        pieceComp.x = data.width/2
                        pieceComp.y = 8*data.height/10
                        pieceComp.dx = 0
                        pieceComp.dy = 0 
    
            #Frictional modeling for all pieces as all time goes on, and their
            #velocities diminish.
            angle = 0
            if(pieceComp.dy == 0 and pieceComp.dx == 0):
                pass
            elif(pieceComp.dx == 0 and pieceComp.dy != 0):
                if(pieceComp.dy > 0):
                    angle = math.pi/2
                else:
                    angle = -math.pi/2
            else:
                angle = math.atan(pieceComp.dy/pieceComp.dx)
                
            velMag = ((pieceComp.dx)**2 + (pieceComp.dy)**2)**0.5
            if(velMag - 1 > 0):
                velMag -= 1
            else:
                velMag = 0 
                
            if(pieceComp.dx > 0):
                if(pieceComp.dy > 0):
                    pieceComp.dx = velMag*math.cos(angle)
                    pieceComp.dy = velMag*math.sin(angle)
                elif(pieceComp.dy < 0):
                    pieceComp.dx = velMag*math.cos(angle)
                    pieceComp.dy = velMag*math.sin(angle)
            elif(pieceComp.dx < 0):
                if(pieceComp.dy > 0):
                    pieceComp.dx = -velMag*math.cos(angle)
                    pieceComp.dy = -velMag*math.sin(angle)
                elif(pieceComp.dy < 0):
                    pieceComp.dx = -velMag*math.cos(angle)
                    pieceComp.dy = -velMag*math.sin(angle)
    
    
        #Core Physics Engine.
        #Collision Modeling.
        #Checks to see if there is any overlap between pieces. 
        #Utilizes vector equations as necessary to calculate the elastic collision.
        #Ensures proper collision. 
        hitSet = set()
        for mainPiece in data.pieces:
            for pieceTest in data.pieces:
                if(mainPiece != pieceTest and mainPiece not in hitSet):
                    if(((pieceTest.x - mainPiece.x)**2 + (pieceTest.y -
                        mainPiece.y)**2)**0.5 <= (pieceTest.rad + mainPiece.rad)):
                            
                            
                            x = [mainPiece.x, mainPiece.y]
                            y = [pieceTest.x, pieceTest.y]
                            v1 = [mainPiece.dx, mainPiece.dy]
                            v2 = [pieceTest.dx, pieceTest.dy]
                            m1 = mainPiece.mass
                            m2 = pieceTest.mass
                            
                            vel = [v1[0] - v2[0], v1[1] - v2[1]]
                            d = [x[0] - y[0], x[1] - y[1]]
                            dot = vel[0] * d[0] + vel[1] * d[1]
                            dist = ((d[0])**2 + (d[1])**2)
                            mult = dot/dist * (-2*m2/(m1 + m2))
                            d[0] = mult*d[0]
                            d[1] = mult*d[1]
                            finalMain = [v1[0] + d[0], v1[1] + d[1]]
                            mainPiece.dx = finalMain[0]
                            mainPiece.dy = finalMain[1]
                            
                            vel = [v2[0] - v1[0], v2[1] - v1[1]]
                            d = [y[0] - x[0], y[1] - x[1]]
                            dot = vel[0] * d[0] + vel[1] * d[1]
                            dist = ((d[0])**2 + (d[1])**2)
                            mult = dot/dist * (-2*m1/(m1 + m2))
                            d[0] = mult*d[0]
                            d[1] = mult*d[1]
                            finalMain = [v2[0] + d[0], v2[1] + d[1]]
                            pieceTest.dx = finalMain[0]
                            pieceTest.dy = finalMain[1]
                            
                            mainPiece.x += mainPiece.dx
                            mainPiece.y += mainPiece.dy
                            pieceTest.x += pieceTest.dx
                            pieceTest.y += pieceTest.dy 
    
                            
                            hitSet.add(pieceTest)
        
                            
        #Ends game if there are no pieces left other than the striker.
        if(len(data.pieces) == 1):
            data.gameState = 10
    except:
        pass
        
#Start Screen of the game
def startScreen(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "light blue", width = 40)
    canvas.create_text(data.width/2, 1*data.height/10, text = "BILLIARDS - STYLE CARROM", font = "arial 32")
    canvas.create_text(data.width/2, 2*data.height/10, text = "Welcome to the Carrom Game.", font = "arial 24")
    canvas.create_text(data.width/2, 3*data.height/10, text = "Press 'E, M, H' to play against different levels of the computer", font = "arial 24")
    canvas.create_text(data.width/2, 4*data.height/10, text = "Or press 'S' to play multiplayer", font = "arial 24")
    canvas.create_text(data.width/2, 5*data.height/10, text = "Turns alternate between the brown and black player.", font = "arial 18")
    canvas.create_text(data.width/2, 6*data.height/10, text = "Moves can be made by clicking in the direction you wish the white striker piece to move.", font = "arial 18")
    canvas.create_text(data.width/2, 7*data.height/10, text = "Points tally according to how many carrom men you land in the pockets. Red - 3, Others - 1", font = "arial 18")
    canvas.create_text(data.width/2, 8*data.height/10, text = "The black player starts, and you will be the black player if you play against the AI", font = "arial 18")
    canvas.create_text(data.width/2, 9*data.height/10, text = "Have fun and enjoy the game!", font = "arial 18")
    
#Game Screen of the game
def gameScreen(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "tan")
    #canvas.create_line(data.width/2, 0, data.width/2, data.height, fill = "black", width = 10)
    #canvas.create_line(0, data.height/2, data.width, data.height/2, fill = "black", width = 10)
    #canvas.create_oval(200, 200, 600, 600, fill = "dark red", width = 10)
    #canvas.create_oval(250, 250, 550, 550, fill = "tan", width = 10)
    for elem in data.pieces:
        if(type(elem) == Striker):
            sX = elem.x
            sY = elem.y
        elem.draw(canvas)
    for pocket in data.pockets:
        pocket.draw(canvas)
    canvas.create_text(150, 100, text = str(data.currPlayer), font = "arial 28", fill = "navy blue")
    canvas.create_text(150, 130, text = "Current Player: " + str(data.currPlayer), font = "arial 16")
    canvas.create_text(150, 150, text = "Brown Count: " + str(data.brownCount), font = "arial 16")
    canvas.create_text(150, 170, text = "Black Count: " + str(data.blackCount), font = "arial 16")
    """
    if(data.gameState == 1  or data.currPlayer == "Black"):
        canvas.create_line(sX, sY, data.mouseX, data.mouseY, width = 5, fill = "dark green")
    """
    
#End Screen of the game
def endScreen(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "dark green", width = 50)
    if(data.brownCount > data.blackCount):
        canvas.create_text(data.width/2, data.height/2, text = "Brown won!", font = "arial 34")
    elif(data.brownCount < data.blackCount):
        canvas.create_text(data.width/2, data.height/2, text = "Black won!", font = "arial 34")
    elif(data.brownCount == data.blackCount):
        canvas.create_text(data.width/2, data.height/2, text = "It's a tie!", font = "arial 34")
    canvas.create_text(data.width/2, 7*data.height/10, text = "Brown Count: " + str(data.brownCount), font = "arial 34")
    canvas.create_text(data.width/2, 8*data.height/10, text = "Black Count: " + str(data.blackCount), font = "arial 34")
    canvas.create_text(data.width/2, 9*data.height/10, text = "Press 'R' to play again!", font = "arial 34")

#Redraws the game as necessary.
def redrawAll(canvas, data):
    if(data.gameState == 0):
        startScreen(canvas, data)
    elif(data.gameState != 10):
        gameScreen(canvas, data)
    if(data.gameState == 10):
        endScreen(canvas, data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    
    ######################################
    #Assistance from stack overflow
    ######################################
    def moveWrapper(event, canvas, data):
        moveMouse(event, data)
        redrawAllWrapper(canvas, data)
    
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 5 # milliseconds
    data.pieces = []
    data.gameState = 0
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    """
    #Stackoverflow
    root.bind("<Motion>", lambda event:
                            moveWrapper(event, canvas, data))
    """
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(800, 800)