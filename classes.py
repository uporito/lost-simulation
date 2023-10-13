import numpy as np
import random
from manim import *
import constant as C
from utils import mobject_ndarray

class Person :
    """A person romaing the world"""
    name : str
    x : int     # x coordinate
    y : int     # y coordinate

    def __init__(self, name:str) :
        self.name = name
        self.x = np.random.randint(0, C.MAP_WIDTH)
        self.y = np.random.randint(0, C.MAP_HEIGHT)

    def getPosition(self) :
        return (self.x, self.y)
    
    def setPosition(self, x:int, y:int) :
        self.x = x
        self.y = y
    
    def getName(self) :
        return (self.name)
    
class Simulation:
    """An object representing the simulation"""
    ticks : int
    over : bool
    map : list
    players : list[Person]

    def __init__(self, map:np.ndarray, players:list[Person]):
        self.ticks = 0
        self.over = False
        self.map = map
        self.players = players

        for p in players :
            p_name = p.getName()
            x_p, y_p = p.getPosition()[0], p.getPosition()[1]
            self.placePlayerOnMap(p_name, x_p, y_p)

        print("Starting simulation. Tick 0.")
        self.returnMap()

    def returnMap(self):
        print(self.map)
        mmap = mobject_ndarray(self.map, C.MANIM_STEP, BLUE, 15)
        return(mmap)

    def placePlayerOnMap(self, s:str, x:int, y:int):
        self.map[y][x] += s

    def movePlayerOnMap(self, p:Person):

        # make random move
        random_direction = random.choice(list(C.RANDOM_MOVES))
        (x0, y0) = p.getPosition()
        (x_move, y_move) = C.RANDOM_MOVES[random_direction]
        x1, y1 = x0 + x_move, y0 + y_move
        print(f"{p.getName()} went {random_direction}." )

        if (x1 >= C.MAP_WIDTH) :
            print("Max width exceeded.")
            x1 = 0
        elif (y1 >= C.MAP_HEIGHT) :
            print("Max height exceeded.")
            y1 = 0
            
        self.map[y0][x0] = self.map[y0][x0].replace(p.getName(), '')     # removing marker from origin cell
        self.map[y1][x1] += p.getName()               # adding marker to destination cell
        p.setPosition(x1, y1)


    def tick(self) :
        # During a run, each tick, each person makes a random move
        # The 2 find each other if they land on the same cell
        # The simulation ends if the 2 players find each other or MAX_TICKS is reached

        self.ticks += 1
        print(f"---Tick {self.ticks}---")

        if (self.ticks > C.MAX_TICKS) :
            print("Max ticks reached. Simulation ending.")
            return
        
        if (self.over) :
            print("Simulation over.")
            return
        
        for p in self.players :
            self.movePlayerOnMap(p)

        if (self.players[0].getPosition() == self.players[1].getPosition()) :
            print("The players have found each other !")
            self.over = True

        return(self.returnMap())