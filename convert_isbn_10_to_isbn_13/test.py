import codewars_test as test
from convert_isbn_10_to_isbn_13 import isbn_converter


@test.describe("Fixed tests")
def tests():
    @test.it("Basic Test Cases")
    def test_isbn_converter():
        test.assert_equals(isbn_converter("1-85326-158-0"), "978-1-85326-158-9")
        test.assert_equals(isbn_converter("0-14-143951-3"), "978-0-14-143951-8")
        test.assert_equals(isbn_converter("0-02-346450-X"), "978-0-02-346450-8")
        test.assert_equals(isbn_converter("963-14-2164-3"), "978-963-14-2164-4")
        test.assert_equals(isbn_converter("1-7982-0894-6"), "978-1-7982-0894-6")
        test.assert_equals(isbn_converter("276-326-440-9"), "978-276-326-440-0")
