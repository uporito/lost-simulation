import numpy as np
from manim import *
import constant as C
from classes import Person, Simulation

# def main() :

#     # There is a map, constituted of cells
#     map = np.empty((C.MAP_HEIGHT, C.MAP_WIDTH), dtype='U25')

#     # There are 2 people, P1 and P2
#     Tom = Person("Tom")
#     Lucy = Person("Lucy")

#     # Initializing the simulation
#     sim = Simulation(map, players=[Tom, Lucy])

#     # During a run, each tick, each person makes a random move
#     # The 2 find each other if they land on the same cell
#     # A run can end in FOUND or NOT FOUND

#     mmap1 = sim.tick()
#     mmap2 = sim.tick()
#     mmap3 = sim.tick()
#     mmap4 = sim.tick()
#     mmap5 = sim.tick()

class Map(Scene) :
    def construct(self) :
        # There is a map, constituted of cells
        map = np.empty((C.MAP_HEIGHT, C.MAP_WIDTH), dtype='U25')

        # There are 2 people, P1 and P2
        Tom = Person("Tom")
        Lucy = Person("Lucy")

        # Initializing the simulation
        sim = Simulation(map, players=[Tom, Lucy])

        # During a run, each tick, each person makes a random move
        # The 2 find each other if they land on the same cell
        # A run can end in FOUND or NOT FOUND

        mmap1 = sim.tick()
        mmap2 = sim.tick()
        mmap3 = sim.tick()
        mmap4 = sim.tick()
        mmap5 = sim.tick()

        self.play(Succession(
            Create(mmap1),
            FadeOut(mmap1),
            Wait(4),
            Create(mmap2),
            FadeOut(mmap2),
            Wait(4),
            Create(mmap3),
            FadeOut(mmap3),
            Wait(4),
            Create(mmap4),
            FadeOut(mmap4)
        ))


# if (__name__ == "__main__") :
#     main()