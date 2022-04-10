import codewars_test as test
from maximum_subarray_sum import max_sequence

test.describe("Tests")
test.it('should work on an empty array')
test.assert_equals(max_sequence([]), 0)
test.it('should work on the example')
test.assert_equals(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
