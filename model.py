"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from typing import List
from random import random
import constants
from math import sin, cos, pi


__author__ = ""  # TODO


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = 0

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
        
    def tick(self):
        self.location.x += self.direction.x
        self.location.y += self.direction.y

    def color(self) -> str:
        """Return the color representation of a cell."""
        return "black"


class Model:
    """The state of the simulation."""

    population: List[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float):
        """Initialize the cells with random locations and directions."""
        self.population = []
        for _ in range(constants.CELL_COUNT):
            self.population.append(Cell(self.random_location(), self.random_direction(constants.CELL_SPEED)))
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for c in self.population:
            c.tick()
            self.enforce_bounds(c)

    def random_location(self) -> Point:
        """Generate a random location."""
        rand_x = random() * constants.BOUNDS_WIDTH - (constants.BOUNDS_WIDTH / 2)
        rand_y = random() * constants.BOUNDS_HEIGHT - (constants.BOUNDS_HEIGHT / 2)
        return Point(rand_x, rand_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle = 2.0 * pi * random()
        x_speed = cos(random_angle) * speed
        y_speed = sin(random_angle) * speed
        return Point(x_speed, y_speed)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1
            
            

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        return False