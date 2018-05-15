import AppGUI as g

class Controller():
    def __init__(self):
        self.app = g.App()
        self.app.init_display()

    def exit(self):
        pass
    
    def moveDown(self,steps):
        self.app.operate(steps)

    def moveRight(self, steps):
        self.app.operate(steps)

    def setStart(self, x, y):
        pass

    def setEnd(self, x,y):
        pass
    
    def setTraverse(self, startX, startY, endX, endY):
        self.setStart(startX,startY)
        self.setEnd(endX,endY)

    def undoMove(self):
        pass

    def buildMap(self, name): #this name should be set as label for pygame window.
        pass

    def createSolution(self, name):
        pass

    def create_map(self, name):
        pass

    def move_up(self, moves):
        self.app.operate(moves)

    def set_end(self, x,y):
        pass

    def move_left(self, moves):
        self.app.operate(moves)


    def add_solution(self, map, sol):
        pass

    def switch_map(self, map):
        pass

    def add_obstacle(self, map, obj, x, y):
        pass
    
