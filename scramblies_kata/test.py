import codewars_test as test
from scramblies_kata import scramble

test.assert_equals(scramble('rkqodlw', 'world'), True)
test.assert_equals(scramble('cedewaraaossoqqyt', 'codewars'), True)
test.assert_equals(scramble('katas', 'steak'), False)
test.assert_equals(scramble('scriptjava', 'javascript'), True)
test.assert_equals(scramble('scriptingjava', 'javascript'), True)
