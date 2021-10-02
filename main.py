import pyxel
from random import randint

class PlayField:
    def __init__(self):
        self.removeQueue =[]

    def generate(self):
        self.playField = [ [ randint(4,9) for i in range(17) ] for j in range(17) ]
    
    def draw(self):
        for row in range(16):
            for column in range(16):
                #pyxel.circ(row*8+3, column*8+3, 3, self.playField[row][column])  
                pyxel.rect(row*8, column*8,7,7, self.playField[row][column])
    
    def check_if_gameover(self):
        col=0
        alone=True
        for row in range(16):
            for column in range(16):
                col=self.playField[row][column]
                if col !=0:
                    #print("tjekker")
                    if self.playField[row][column-1] == col and column-1 !=-1:
                        alone=False
                    if self.playField[row][column+1] == col and column+1 !=16:
                        alone=False
                    if self.playField[row+1][column] == col and row+1 !=16:
                        alone=False
                    if self.playField[row-1][column] == col and row-1 !=-1:
                        alone=False
        if alone==True:
            #pyxel.play(1, 0, loop=False)
            return False
        

    def remove(self, row, column, col):
        alone=True
        if self.playField[row][column-1] == col and column-1 !=-1:
            alone=False
        if self.playField[row][column+1] == col and column+1 !=16:
            alone=False
        if self.playField[row+1][column] == col and row+1 !=16:
            alone=False
        if self.playField[row-1][column] == col and row-1 !=-1:
            alone=False

        if col==0 or alone==True:
            #pyxel.play(1, 0, loop=False)
            return False
        self.removeQueue.append([row, column])
        self.recurse(row, column, col)

    def recurse(self, row, column, col):    

        self.removeQueue.pop()
        if self.playField[row][column-1] == col and column-1 !=-1:
            self.removeQueue.append([row, column-1]) #** EAST
        if self.playField[row][column+1] == col and column+1 !=16:
            self.removeQueue.append([row, column+1]) #** WEST
        if self.playField[row+1][column] == col and row+1 !=16:
            self.removeQueue.append([row+1, column]) #** NORTH
        if self.playField[row-1][column] == col and row-1 !=-1:
            self.removeQueue.append([row-1, column]) #** SOUTH
        self.playField[row][column] = 0
        
        if self.removeQueue !=[]:    
            self.recurse(self.removeQueue[len(self.removeQueue)-1][0], 
                         self.removeQueue[len(self.removeQueue)-1][1],col)  
        else:
            print("Done")
            self.check_if_gameover()
            
                
    def fall(self):
        clearedRow=False
        for row in range(16):
            for column in range(15):
                if self.playField[row][column+1]==0 and self.playField[row][column] !=0:
                    self.playField[row][column+1]=self.playField[row][column]
                    self.playField[row][column]=0
                    #pyxel.play(1, 2, loop=False)
                  
class App:
    def __init__(self):
        pyxel.init(128, 128)
        #pyxel.load("assets/sound.pyxres")
        pyxel.mouse(True)

        self.pf = PlayField()
        self.pf.generate()
        pyxel.run(self.update, self.draw)
        
    def update(self):
        self.pf.fall()
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.pf.remove(int(pyxel.mouse_x/8),int(pyxel.mouse_y/8),self.pf.playField[int(pyxel.mouse_x/8)][int(pyxel.mouse_y/8)])       
        

    def draw(self):
        pyxel.cls(0)
        self.pf.draw()
        #pyxel.text(0,0,str(int(pyxel.mouse_y/8))+"/"+str(int(pyxel.mouse_x/8)),1)
        pyxel.circb(int(pyxel.mouse_x/8)*8+3, int(pyxel.mouse_y/8)*8+3, 3, 15)
        
App()