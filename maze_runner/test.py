import codewars_test as test
from maze_runner import maze_runner, Position, Maze


@test.describe('Maze Runner Tests')
def example_tests():
    maze_array = [[1, 1, 1, 1, 1, 1, 1],
                  [1, 0, 0, 0, 0, 0, 3],
                  [1, 0, 1, 0, 1, 0, 1],
                  [0, 0, 1, 0, 0, 0, 1],
                  [1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 0, 0, 0, 0, 1],
                  [1, 2, 1, 0, 1, 0, 1]]

    @test.it("Should return Finish")
    def example_test_case1():
        test.assert_equals(maze_runner(maze_array, ["N", "N", "N", "N", "N", "E", "E", "E", "E", "E"]), "Finish")
        test.assert_equals(
            maze_runner(maze_array, ["N", "N", "N", "N", "N", "E", "E", "S", "S", "E", "E", "N", "N", "E"]),
            "Finish")
        test.assert_equals(maze_runner(maze_array, ["N", "N", "N", "N", "N", "E", "E", "E", "E", "E", "W", "W"]),
                           "Finish")

    @test.it("Should return Dead")
    def example_test_case2():
        test.assert_equals(maze_runner(maze_array, ["N", "N", "N", "W", "W"]), "Dead")
        test.assert_equals(maze_runner(maze_array, ["N", "N", "N", "N", "N", "E", "E", "S", "S", "S", "S", "S", "S"]),
                           "Dead")

    @test.it("Should return Lost")
    def example_test_case3():
        test.assert_equals(maze_runner(maze_array, ["N", "E", "E", "E", "E"]), "Lost")

    @test.it("Should provide hash and eq methods for Position class")
    def position_tests():
        test.assert_equals(Position(1, 1).__hash__(), Position(1, 1).__hash__())
        test.assert_equals(Position(1, 1).__eq__(Position(1, 1)), True)
        test.assert_equals(Position(1, 1), Position(1, 1))

    @test.it("Should learn how dictionaries work")
    def dictionary_tests():
        my_dict = {}
        my_dict[Position(1, 1)] = 2
        my_dict[Position(2, 3)] = 3
        test.assert_equals(my_dict[Position(1, 1)], 2)
        test.assert_equals(my_dict.get(Position(1, 1), 1), 2)
        test.assert_equals(my_dict.get(Position(1, 2), 1), 1)
        test.assert_equals(my_dict.get(Position(2, 3), 1), 3)

    @test.it("Should create Maze")
    def maze_tests():
        maze = Maze.create_from([[1, 2], [3, 4]])
        test.assert_equals(maze.get(Position(0, 0)), 1)
        test.assert_equals(maze.get(Position(1, 0)), 2)
        test.assert_equals(maze.get(Position(0, 1)), 3)
        test.assert_equals(maze.get(Position(1, 1)), 4)
        test.assert_equals(maze.get(Position(2, 2)), 1)
