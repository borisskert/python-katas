import codewars_test as test
from second_variation_on_caesar_cipher import encode_str
from second_variation_on_caesar_cipher import decode


@test.describe('Second Variation on Caesar Cipher Tests')
def fixed_tests():
    def testing_code(strng, shift, exp):
        actual = encode_str(strng, shift)
        test.assert_equals(actual, exp)

    def testing_decode(arr, exp):
        actual = decode(arr)
        test.assert_equals(actual, exp)

    @test.it('Basic Tests testing encode')
    def tests1():
        u = "I should have known that you would have a perfect answer for me!!!"
        v = ["ijJ tipvme ibw", "f lopxo uibu z", "pv xpvme ibwf ", "b qfsgfdu botx", "fs gps nf!!!"]
        testing_code(u, 1, v)
        v = ['ikK ujqwnf jcx', 'g mpqyp vjcv a', 'qw yqwnf jcxg ', 'c rgthgev cpuy', 'gt hqt og!!!']
        testing_code(u, 28, v)

        u = "abcdefghjuty12"
        v = ['abbc', 'defg', 'hikv', 'uz12']
        testing_code(u, 1, v)
        v = ['aeef', 'ghij', 'klny', 'xc12']
        testing_code(u, 30, v)

    @test.it('Basic Tests testing decode')
    def tests2():
        u = "O CAPTAIN! my Captain! our fearful trip is done;"
        v = ["opP DBQUBJ", "O! nz Dbqu", "bjo! pvs g", "fbsgvm usj", "q jt epof;"]
        testing_decode(v, u)
        v = ['owW KIXBIQ', 'V! ug Kixb', 'iqv! wcz n', 'miznct bzq', 'x qa lwvm;']
        testing_decode(v, u)

        u = "Exult, O shores, and ring, O bells! But I, with mournful tread, Walk the deck my Captain lies, Fallen cold and dead. "
        v = ["efFyvmu, P tipsft, boe s", "joh, P cfmmt! Cvu J, xju", "i npvsogvm usfbe, Xbml u",
             "if efdl nz Dbqubjo mjft,", " Gbmmfo dpme boe efbe. "]
        testing_decode(v, u)
