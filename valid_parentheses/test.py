import codewars_test as test
from valid_parentheses import valid_parentheses

@test.describe("Sample Tests")
def tests():
    @test.it("Sample tests")
    def sample_tests():
        test.assert_equals(valid_parentheses("  ("),False, "should work for '  ('")
        test.assert_equals(valid_parentheses(")test"),False, "should work for ')test'")
        test.assert_equals(valid_parentheses(""),True, "should work for ''")
        test.assert_equals(valid_parentheses("hi())("),False, "should work for 'hi())('")
        test.assert_equals(valid_parentheses("hi(hi)()"),True, "should work for 'hi(hi)()'")
