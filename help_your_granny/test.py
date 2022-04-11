import codewars_test as test
from help_your_granny import tour, divvy, to_pairs

test.assert_equals(divvy(2, 1, []), [])
test.assert_equals(divvy(2, 1, ['a']), [])
test.assert_equals(divvy(2, 1, ['a', 'b']), [['a', 'b']])
test.assert_equals(divvy(2, 1, ['a', 'b', 'c']), [['a', 'b'], ['b', 'c']])
test.assert_equals(divvy(2, 1, ['a', 'b', 'c', 'd']), [['a', 'b'], ['b', 'c'], ['c', 'd']])

test.assert_equals(to_pairs(['a', 'b', 'c', 'd']), [('a', 'b'), ('b', 'c'), ('c', 'd')])

friends1 = ["A1", "A2", "A3", "A4", "A5"]
fTowns1 = [["A1", "X1"], ["A2", "X2"], ["A3", "X3"], ["A4", "X4"]]
distTable1 = {"X1": 100.0, "X2": 200.0, "X3": 250.0, "X4": 300.0}
test.assert_equals(tour(friends1, fTowns1, distTable1), 889)
