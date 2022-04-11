import codewars_test as test
from simple_pig_latin import pig_it

test.assert_equals(pig_it('Pig latin is cool'), 'igPay atinlay siay oolcay')
test.assert_equals(pig_it('This is my string'), 'hisTay siay ymay tringsay')
test.assert_equals(pig_it('O tempora o mores !'), 'Oay emporatay oay oresmay !')
test.assert_equals(pig_it('Quis custodiet ipsos custodes ?'), 'uisQay ustodietcay psosiay ustodescay ?')
