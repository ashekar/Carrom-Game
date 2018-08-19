##############################################
# Here we define all of the classes that we will need for our pieces.
# Much of the inheritance is helpful in drawing a distinction between pieces.
# Properties such as radius, mass, color, and position are defined here
# The pieces additionally have methods to draw themselves, and other methods 
# that are important to sets and equalities, etc. etc.
# 
#
#
#
#
# NOTE that here we also defined pockets which are an important aspect of our 
# gameplay as they remove pieces. 
################################################


#This class defines characteristics important to pieces in general including
#position, movement, color, and image(a function to draw them).
class Piece(object):
    def __init__(self, posX, posY):
        self.x = posX
        self.y = posY
        self.dx = 0
        self.dy = 0
        self.color = "orange"
    def draw(self, canvas):
        x = self.x
        y = self.y
        r = self.rad
        canvas.create_oval(x-r, y-r, x+r, y+r, fill = self.color, width = 2)

#This class defines the queen object which is a special carrom piece that is 
#worth three points. It assigns the necessary characteristics.
class Queen(Piece):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.color = "red"
        self.rad = 13
        self.mass = 10
        
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and 
        self.color == other.color and self.rad == other.rad)
    
    def __hash__(self):
        return hash((self.x, self.y, self.color, self.rad))
        
    def __repr(self):
        return "Queen"

#This class defines the Carrom Man piece which is a generic piece worth one point.
#It also assigns the appropriate values wehre necessary.
class CarromMan(Piece):
    def __init__(self, posX, posY, colorType):
        super().__init__(posX, posY)
        self.color = colorType
        if(colorType == "black"):
            self.playerPiece = True
        elif(colorType == "brown"):
            self.playerPiece = False
        self.rad = 13
        self.mass = 10
        
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and 
        self.color == other.color and self.rad == other.rad)
    
    def __hash__(self):
        return hash((self.x, self.y, self.color, self.rad))
    
    def __repr(self):
        return "CarromMan"

#This is our striker piece which the player(s) and AI will control to score points. 
#We assign the necessary properties, and notice here that we make it a little bit bigger
#with respect to both mass and weight.
class Striker(Piece):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.color = "White"
        self.rad = 18
        self.mass = 20
        
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and 
        self.color == other.color and self.rad == other.rad)
    
    def __hash__(self):
        return hash((self.x, self.y, self.color, self.rad))
        
    def __repr(self):
        return "Striker"


#Here we define our pocket class which has many of the same attributes with the exception of movement.
#It also has a draw function which will greatly help us in making the object draw itself.
class Pocket(object):
    def __init__(self, posX, posY):
        self.x = posX
        self.y = posY
        self.rad = 24
        self.color = "navy blue"
        
    def draw(self, canvas):
        x = self.x
        y = self.y
        r = self.rad
        canvas.create_oval(x-r, y-r, x+r, y+r, fill = self.color, width = 2)