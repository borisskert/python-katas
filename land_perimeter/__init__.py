from functools import reduce


# https://www.codewars.com/kata/5839c48f0cf94640a20001d3/train/python
def land_perimeter(arr):
    land_points = LandPoints.parse(arr)
    return 'Total land perimeter: %s' % land_points.perimeter()


class LandPoints:
    def __init__(self, points):
        self.points = set(points)

    def perimeter(self):
        return reduce(
            lambda acc, point: acc + self.__perimeter_of(point),
            self.points,
            0
        )

    def __perimeter_of(self, point):
        x, y = point
        perimeter = 0

        if (x + 1, y) not in self.points:
            perimeter += 1
        if (x, y + 1) not in self.points:
            perimeter += 1
        if (x - 1, y) not in self.points:
            perimeter += 1
        if (x, y - 1) not in self.points:
            perimeter += 1

        return perimeter

    @staticmethod
    def parse(string_array):
        rows_with_y_indices = zip_with_index(string_array)

        land_points = flat_map(
            lambda row_and_y: LandPoints.__map_row(row_and_y),
            rows_with_y_indices
        )

        return LandPoints(land_points)

    @staticmethod
    def __map_row(row_and_y):
        row, y = row_and_y
        row_as_chars = [char for char in row]
        cells_with_x_indices = zip_with_index(row_as_chars)

        land_points = map(
            lambda cell_and_x: LandPoints.__to_land_point(cell_and_x, y),
            cells_with_x_indices
        )

        return omit_nones(land_points)

    @staticmethod
    def __to_land_point(cell_and_x, y):
        cell, x = cell_and_x

        if cell == 'X':
            return x, y

        return None


def flat_map(func, iterable):
    mapped = map(func, iterable)
    return reduce(lambda result, _list: [*result, *_list], mapped, [])


def zip_with_index(iterable):
    count = len(iterable)
    indices = range(count)

    return zip(iterable, indices)


def omit_nones(iterable):
    return filter(lambda x: x is not None, iterable)
