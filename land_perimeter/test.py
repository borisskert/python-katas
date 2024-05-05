import codewars_test as test
from land_perimeter import land_perimeter


@test.describe("Basic tests")
def test_group():
    @test.it("Should work for basic tests")
    def test_case():
        test.assert_equals(
            land_perimeter(
                ["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]),
            "Total land perimeter: 60")
        # test.assert_equals(
        #     land_perimeter(
        #         ["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO", "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"]),
        #     "Total land perimeter: 52")
        # test.assert_equals(
        #     land_perimeter(["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"]),
        #     "Total land perimeter: 40")
        # test.assert_equals(
        #     land_perimeter(["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO", "OOOOOXX", "OOOXOXX", "XXXXOXO"]),
        #     "Total land perimeter: 54")
        # test.assert_equals(
        #     land_perimeter(["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"]),
        #     "Total land perimeter: 40")
