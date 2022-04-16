import codewars_test as test
from josephus_survivor import josephus_survivor

test.assert_equals(josephus_survivor(7, 3), 4)
test.assert_equals(josephus_survivor(11, 19), 10)
test.assert_equals(josephus_survivor(1, 300), 1)
test.assert_equals(josephus_survivor(14, 2), 13)
test.assert_equals(josephus_survivor(100, 1), 100)
