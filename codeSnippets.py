                        """
                        while(((pieceTest.x - mainPiece.x)**2 + (pieceTest.y - mainPiece.y)**2)**0.5 <= (pieceTest.rad + mainPiece.rad)):
                            mainPiece.x += mainPiece.dx
                            mainPiece.y += mainPiece.dy
                            pieceTest.x += pieceTest.dx
                            pieceTest.y += pieceTest.dy 
                        """
                
                
                        """
                        
                        mainXVal = mainPiece.x
                        mainYVal = mainPiece.y
                        testXVal = pieceTest.x
                        testYVal = pieceTest.y
                        
                        if(testXVal >= mainXVal):
                            if(testYVal >= mainYVal):
                                diffX = testXVal - mainXVal 
                                diffY = -(testYVal - mainYVal)
                            elif(testYVal < mainYVal):
                                diffX = testXVal - mainXVal 
                                diffY = (testYVal - mainYVal)
                        elif(testXVal < mainXVal):
                            if(testYVal >= mainYVal):
                                diffX = mainXVal - testXVal
                                diffY = -(testYVal - mainYVal)
                            elif(testYVal < mainYVal):
                                diffX = mainXVal - testXVal
                                diffY = (testYVal - mainYVal)
                        if(diffY == 0):
                            pass
                        if(mainPiece.dx == 0):
                            pass
                        if(pieceTest.dx == 0):
                            pass
                        
                        phi = math.atan(diffX/diffY)
                        v1 = ((mainPiece.dx)**2 + (mainPiece.dy)**2)**0.5
                        v2 = ((pieceTest.dx)**2 + (pieceTest.dy)**2)**0.5
                        thet1 = math.atan(-mainPiece.dy/mainPiece.dx)
                        thet2 = math.atan(-pieceTest.dy/pieceTest.dx)
                        m1 = mainPiece.mass
                        m2 = pieceTest.mass
                        
                        finV1X = (((v1*math.cos(thet1 - phi)*(m1 - m2) 
                        + 2*m2*v2*math.cos(thet2 - phi))/(m1 + m2))*math.cos(phi) 
                        + v1*math.sin(thet1 - phi)*math.cos(phi + math.pi/2))
                        
                        finV1Y = (((v1*math.cos(thet1 - phi)*(m1 - m2) 
                        + 2*m2*v2*math.cos(thet2 - phi))/(m1 + m2))*math.sin(phi) 
                        + v1*math.sin(thet1 - phi)*math.sin(phi + math.pi/2))
                        
                        finV2X = (((v2*math.cos(thet2 - phi)*(m2 - m1) 
                        + 2*m1*v1*math.cos(thet1 - phi))/(m2 + m1))*math.cos(phi) 
                        + v2*math.sin(thet2 - phi)*math.cos(phi + math.pi/2))
                        
                        finV2Y = (((v2*math.cos(thet2 - phi)*(m2 - m1) 
                        + 2*m1*v1*math.cos(thet1 - phi))/(m2 + m1))*math.sin(phi) 
                        + v2*math.sin(thet2 - phi)*math.sin(phi + math.pi/2))
                        
                        mainPiece.dx = finV1X
                        mainPiece.dy = finV1Y
                        pieceTest.dx = finV2X
                        pieceTest.dy = finV2Y
                        
                        break 
                        
                        if(pieceTest not in hitDict):
                            hitDict[pieceTest] = set()
                        hitDict[pieceTest].add(mainPiece)
                        
                        """
                        
        """
        if(pieceComp.dx < 0):
            pieceComp.dx += 0.5
        elif(pieceComp.dx > 0):
            pieceComp.dx -= 0.5
        elif(pieceComp.dx == 0):
            pieceComp.dx = 0
        if(pieceComp.dy < 0):
            pieceComp.dy += 0.5
        elif(pieceComp.dy > 0):
            pieceComp.dy -= 0.5
        elif(pieceComp.dy == 0):
            pieceComp.dy = 0
        """
        
        
        """
        if(data.currPlayer == "Black"):
            data.currPlayer = "Brown"
        elif(data.currPlayer == "Brown"):
            data.currPlayer = "Black"
        """
        
        
        
        """
        denom = math.abs(pieceComp.dx * pieceComp.dy)
        if(denom != 0):
            if(denom > 0):
                if(pieceComp.dx > 0):
                    pieceComp.dx -= pieceComp.dx/denom
                elif(pieceComp.dx < 0):
                    pieceComp.dx -= pieceComp.dx/denom
                pieceComp.dx -= pieceComp.dx/denom
                pieceComp.dy -= pieceComp.dy/denom
            else:
                pieceComp.dx += pieceComp.dx/denom
                pieceComp.dy += pieceComp.dy/denom 
        """
        """
        if(data.currPlayer == "Black"):
            data.currPlayer = "Brown"
        elif(data.currPlayer == "Brown"):
            data.currPlayer = "Black"
        """
        
        
        """
                    strikerFind.dx = outX
                    strikerFind.dy = outY
                    
                    strikerFind.dx = 2*XTEST
                    strikerFind.dy = 2*YTEST
        """
        
    """
            dist = ((d1)**2 + (d2)**2)**0.5
            mC = (2*strik.mass)/(finalPiece.mass + strik.mass)
            
            coeff1 = d1*d1/dist**2
            coeff2 = d1*d2/dist**2
            coeff3 = d2*d2/dist**2
            
            firstX = mC*coeff1
            firstY = mC*coeff2
            
            scndX = mC*coeff2
            scndY = mC*coeff3
            
            eqs = np.array([[firstX, firstY], [scndX, scndY]])
            sols = np.array([finVelVec[0], finVelVec[1]])
            try:
                ans = np.linalg.solve(eqs, sols)
            except:
                ans = [1, 1]
            #print(ans)
            
            dot = pieceVec[0]*pockVec[0] + pieceVec[1]*pockVec[1]
            theta = math.acos(dot/(pockDist*pieceDist))
            speed = ((finVelVec[0])**2 + (finVelVec[1])**2)**0.5
            r1 = strik.rad
            r2 = finalPiece.rad
            m1 = strik.mass
            m2 = finalPiece.mass
            d = pieceDist
            
            dConst = (m2*speed)/(m1*math.cos(theta))
            tempX = math.cos(math.asin((r1 + r2)/d*math.sin(theta)))
            tempY = (r1 + r2)/d*math.sin(theta)

            outX = dConst * tempX
            outY = dConst * tempY
            print(outX, outY)
            
            
            fC = pieceVec[0]*m2*speed/(pieceDist*m1*math.cos(theta))
            sC = -pieceVec[1]*m2*speed/(pieceDist*m1*math.cos(theta))
            
            XTEST = fC*tempX - sC*tempY
            YTEST = fC*tempY + sC*tempX
            
            print(XTEST)
            print(YTEST)
    """
    
    
    
#The player must shoot from
# wherever the piece ended up from the last player's turn. There is a red piece
# that is worth three points and all other pieces are worth one point each. The
# striker piece is white and all the pockets are navy blue. The player also has
# the option to play against different levels of AI