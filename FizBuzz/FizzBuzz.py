'''
Regras do FizzBuzz

1. Se a posição for múltipla de 3: Fizz
2. Se a posição foi múltipla de 5: Buzz
3. Se a posição for múltipla de 3 e 5: FizBuzz
4. Para qualquer outra posição, fala o próprio número.
'''
from functools import partial

multiple_of = lambda base, num: num % base == 0
multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3)


def robot(pos):
    say = str(pos)

    if multiple_of_3(pos) or multiple_of_5(pos):
        say = 'FizzBuzz'
    elif multiple_of_5(pos):
        say = 'Buzz'
    elif multiple_of_3(pos):
        say = 'Fizz'

    return say

def assert_equal(result, expected):
    from sys import _getframe

    msg = 'Fail: Line {} got {} expecting {}'

    if not result == expected:
        current = _getframe()
        caller = current.f_back
        line_no = caller.f_lineno
        print(msg.format(line_no, result, expected))

if __name__ == '__main__':
    assert_equal(robot(1), '1')
    assert_equal(robot(2), '2')
    assert_equal(robot(4), '4')

    assert_equal(robot(3), 'Fizz')

    assert_equal(robot(6), 'Fizz')
    assert_equal(robot(9), 'Fizz')

    assert_equal(robot(5), 'Buzz')
    assert_equal(robot(10), 'Buzz')
    assert_equal(robot(20), 'Buzz')

    assert_equal(robot(15), 'FizzBuzz')
    assert_equal(robot(30), 'FizzBuzz')
    assert_equal(robot(45), 'FizzBuzz')