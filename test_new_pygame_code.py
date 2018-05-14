from pygame.locals import *
import pygame
import numpy as np


class Player:
    #Current X and Y with respect to the grid
    def __init__(self, current_x, current_y, maze_matrix):
        self.speed = 5
        self.current_x = current_x
        self.current_y = current_y
        self.w = 70
        #Current X and Y with respect to the screen
        self.x = self.w * self.current_x
        self.y = self.w * self.current_y
        self.matrix_row = maze_matrix.shape[0]
        self.matrix_column = maze_matrix.shape[1]
        self.maze_matrix = maze_matrix

    def moveRight(self):
        if((self.current_x + 1) == self.matrix_column):
            print(self.current_y)
            return "CANNOT MOVE"
        elif(self.maze_matrix[self.current_y, self.current_x + 1]):
            return "OBSTACULE"
        else:
            position_x = self.w * (self.current_x + 1)
            while(self.x != position_x):
                print("WHILE" + str(self.current_y))
                self.x += self.speed
            self.current_x += 1  


    def moveLeft(self):
        if((self.current_x - 1) == -1 or self.maze_matrix[self.current_y, self.current_x - 1]):
            return "CANNOT MOVE"
        position_x = self.w * (self.current_x - 1)
        while(self.x != position_x):
            self.x -= self.speed
        self.current_x -= 1  

    def moveUp(self):
        if((self.current_y - 1) == -1 or self.maze_matrix[self.current_y - 1, self.current_x]):
            return "CANNOT MOVE"
        position_y = self.w * (self.current_y - 1)
        while(self.y != position_y):
            self.y -= self.speed
        self.current_y -= 1 

    def moveDown(self):
        print("MOVE DOWN " + str(self.current_x))
        if((self.current_y + 1) == self.matrix_row or self.maze_matrix[self.current_y + 1, self.current_x]):
            return "CANNOT MOVE"
        position_y = self.w * (self.current_y + 1)
        while(self.y != position_y):
            print("MOVE DOWN inside while " + str(self.current_y))
            self.y += self.speed
        self.current_y += 1 


class Grid:
    def __init__(self):
        self.M = 10 #Columns
        self.N = 8 #Rows
        # self.maze = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        #              1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
        #              1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
        #              1, 0, 1, 1, 1, 1, 1, 1, 0, 1,
        #              1, 0, 1, 0, 0, 0, 0, 0, 0, 1,
        #              1, 0, 1, 0, 1, 1, 1, 1, 0, 1,
        #              1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
        #              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]
        self.maze = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]
        self.w = 70
        self.x = 0
        self.y = 0
        self.dimensions = 10
        self.image = pygame.image.load("Images/tree_sized.png")
        self.image = pygame.transform.rotozoom(self.image, 0, 0.8)
        self.grid = [[1] * self.dimensions for n in range(self.dimensions)]
        self.maze_matrix = np.array(self.maze).reshape(8,10)
        print(type(self.maze_matrix))
        

    def draw(self, display_surf):
        for row in range(self.N):
            for column in range(self.M):
                if(self.maze_matrix[row,column]):
                    display_surf.blit(self.image,(self.w * row, self.w * column))
                    


class App:

    windowWidth = 800
    windowHeight = 600
    player = 0
    clock = pygame.time.Clock()

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.grid = Grid()
        self.player = Player(0,0, self.grid.maze_matrix)
        self.Background = None
        self.images_dict = {
            'RIGHT': [],
            'LEFT': [],
            'UP': [],
            'DOWN': []
        }
        self.counter = 0


    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('PUZZOLVE')
        self._running = True
        self.Background = pygame.image.load("Images/grass-pattern.png").convert()
        self.images_dict['DOWN'].append(pygame.image.load("Images/ironman_front.png"))
        self.images_dict['DOWN'].append(pygame.image.load("Images/ironman_front1.png"))
        self.images_dict['DOWN'].append(pygame.image.load("Images/ironman_front2.png"))
        self.images_dict['LEFT'].append(pygame.image.load("Images/ironman_left.png"))
        self.images_dict['LEFT'].append(pygame.image.load("Images/ironman_left1.png"))
        self.images_dict['LEFT'].append(pygame.image.load("Images/ironman_left2.png"))
        self.images_dict['UP'].append(pygame.image.load("Images/ironman_back.png"))
        self.images_dict['UP'].append(pygame.image.load("Images/ironman_back1.png"))
        self.images_dict['UP'].append(pygame.image.load("Images/ironman_back2.png"))
        self.images_dict['RIGHT'].append(pygame.image.load("Images/ironman_right.png"))
        self.images_dict['RIGHT'].append(pygame.image.load("Images/ironman_right1.png"))
        self.images_dict['RIGHT'].append(pygame.image.load("Images/ironman_right2.png"))
        self._image_surf = self.images_dict['DOWN'][0]
        self._image_surf = pygame.transform.rotozoom(self._image_surf, 0, 1.5)
        self._block_surf = pygame.image.load("Images/tree_sized.png")

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def switch_image(self, direction, index):
        if direction == "RIGHT":
            self._image_surf = self.images_dict['RIGHT'][index]

        if direction == "LEFT":
            self._image_surf = self.images_dict['LEFT'][index]

        if direction == "DOWN":
            self._image_surf = self.images_dict['DOWN'][index]

        if direction == "UP":
            self._image_surf = self.images_dict['UP'][index]

        self._image_surf = pygame.transform.rotozoom(self._image_surf, 0, 1.5)

    def on_render(self):
        self._display_surf.blit(self.Background, (0, 0))
        self._display_surf.blit(self._image_surf, (self.player.x, self.player.y))
        self.grid.draw(self._display_surf)
        pygame.display.update()


    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    self._running = False

            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.switch_image("RIGHT", self.counter)
                self.counter = (self.counter + 1) % len(self.images_dict['RIGHT'])
                self.player.moveRight()

            if (keys[K_LEFT]):
                self.switch_image("LEFT", self.counter)
                self.counter = (self.counter + 1) % len(self.images_dict['LEFT'])
                self.player.moveLeft()

            if (keys[K_UP]):
                self.switch_image("UP", self.counter)
                self.counter = (self.counter + 1) % len(self.images_dict['UP'])
                self.player.moveUp()

            if (keys[K_DOWN]):
                self.switch_image("DOWN", self.counter)
                self.counter = (self.counter + 1) % len(self.images_dict['DOWN'])
                self.player.moveDown()

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()
            self.clock.tick(15)
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
