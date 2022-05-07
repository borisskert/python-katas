# https://www.codewars.com/kata/58663693b359c4a6560001d6/train/python

import functools

from typing import Dict, Set


def maze_runner(maze, directions):
    grid = Grid.create_from(maze)

    def run(position, _directions):
        if len(_directions) == 0:
            return "Lost"

        [direction, *further_directions] = _directions
        position = position.move(direction)
        field = grid.get(position)

        if field == 1:
            return "Dead"

        if field == 3:
            return "Finish"

        return run(position, further_directions)

    return run(grid.find_start(), directions)


class Position:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == 'N':
            return Position(self.x, self.y + 1)
        if direction == 'S':
            return Position(self.x, self.y - 1)
        if direction == 'E':
            return Position(self.x + 1, self.y)
        if direction == 'W':
            return Position(self.x - 1, self.y + 1)

        return self

    def __eq__(self, other):
        print("__eq__")
        print(self.x)
        print(self.y)
        return str(self.x) == str(other.x) and str(self.y) == str(other.y)

    def __hash__(self) -> int:
        print(hash(str(self.x) + "/" + str(self.y)))
        return hash(str(self.x) + "/" + str(self.y))


class Grid:
    grid: dict[Position, int]

    def __init__(self, grid):
        self.grid = grid

    def find_start(self):
        filtered = filter(Grid.__is_start, self.grid.items())
        [position, _] = list(filtered)[0]

        return position

    def get(self, position):
        field = self.grid.get(position)

        if field is None:
            return 1

        return field

    @staticmethod
    def __is_start(item):
        [_, value] = item

        return value == 2

    @staticmethod
    def create_from(maze):
        indices_y = range(len(maze))

        grid = functools.reduce(
            Grid.__line_into_grid,
            zip(maze, indices_y),
            Dict[Position, Set[int]]
        )

        return Grid(grid)

    @staticmethod
    def __line_into_grid(_grid, line_y):
        [line, y] = line_y
        indices_x = range(len(line))

        return functools.reduce(
            lambda grid, field_x: Grid.__field_into_grid(_grid, field_x, y),
            zip(line, indices_x),
            _grid
        )

    @staticmethod
    def __field_into_grid(_grid, field_x, y):
        [field, x] = field_x
        _grid[Position(x, y)] = field

        return _grid
