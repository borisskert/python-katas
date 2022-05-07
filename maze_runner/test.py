import codewars_test as test
from maze_runner import maze_runner

@test.describe('Example Tests')
def example_tests():
    maze = [[1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 3],
            [1, 0, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 2, 1, 0, 1, 0, 1]]

    @test.it("Should return Finish")
    def example_test_case1():
        test.assert_equals(maze_runner(maze, ["N", "N", "N", "N", "N", "E", "E", "E", "E", "E"]), "Finish")
        test.assert_equals(maze_runner(maze, ["N", "N", "N", "N", "N", "E", "E", "S", "S", "E", "E", "N", "N", "E"]),
                           "Finish")
        test.assert_equals(maze_runner(maze, ["N", "N", "N", "N", "N", "E", "E", "E", "E", "E", "W", "W"]), "Finish")

    @test.it("Should return Dead")
    def example_test_case2():
        test.assert_equals(maze_runner(maze, ["N", "N", "N", "W", "W"]), "Dead")
        test.assert_equals(maze_runner(maze, ["N", "N", "N", "N", "N", "E", "E", "S", "S", "S", "S", "S", "S"]), "Dead")

    @test.it("Should return Lost")
    def example_test_case3():
        test.assert_equals(maze_runner(maze, ["N", "E", "E", "E", "E"]), "Lost")
