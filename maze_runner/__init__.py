# https://www.codewars.com/kata/58663693b359c4a6560001d6/train/python
import functools
from enum import IntEnum


def maze_runner(maze, directions):
    maze = Maze.create_from(maze)

    def run(position, _directions):
        if len(_directions) == 0:
            return "Lost"

        [direction, *further_directions] = _directions
        position = position.move(direction)
        field = maze.get(position)

        if field == Field.WALL:
            return "Dead"

        if field == Field.FINISH:
            return "Finish"

        return run(position, further_directions)

    return run(maze.find_start(), directions)


class Position:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == 'N':
            return Position(self.x, self.y - 1)
        if direction == 'S':
            return Position(self.x, self.y + 1)
        if direction == 'E':
            return Position(self.x + 1, self.y)
        if direction == 'W':
            return Position(self.x - 1, self.y)

        return self

    def str(self):
        return str(self)

    def __eq__(self, other):
        return str(self.x) == str(other.x) and str(self.y) == str(other.y)

    def __hash__(self) -> int:
        return hash(str(self.x) + "/" + str(self.y))

    def __str__(self) -> str:
        return "Position(" + str(self.x) + "/" + str(self.y) + ")"


class Field(IntEnum):
    SAFE = 0
    WALL = 1
    START = 2
    FINISH = 3


class Maze:
    grid: {}

    def __init__(self, grid):
        self.grid = grid

    def find_start(self):
        filtered = filter(Maze.__is_start, self.grid.items())
        [position, _] = list(filtered)[0]

        return position

    def get(self, position):
        field = self.grid.get(position, Field.WALL)

        return field

    @staticmethod
    def __is_start(item):
        [_, value] = item

        return value == Field.START

    @staticmethod
    def create_from(maze):
        indices_y = range(len(maze))

        grid = functools.reduce(
            Maze.__line_into_grid,
            zip(maze, indices_y),
            {}
        )

        return Maze(grid)

    @staticmethod
    def __line_into_grid(_grid, line_y):
        [line, y] = line_y
        indices_x = range(len(line))

        return functools.reduce(
            lambda grid, value_x: Maze.__field_into_grid(_grid, value_x, y),
            zip(line, indices_x),
            _grid
        )

    @staticmethod
    def __field_into_grid(_grid, value_x, y):
        [value, x] = value_x
        _grid[Position(x, y)] = value

        return _grid
