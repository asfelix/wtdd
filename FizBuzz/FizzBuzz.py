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

    if multiple_of_3(pos) and multiple_of_5(pos):
        say = 'FizzBuzz'
    elif multiple_of_5(pos):
        say = 'Buzz'
    elif multiple_of_3(pos):
        say = 'Fizz'

    return say

if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'Fizz'
    assert robot(6) == 'Fizz'
    assert robot(9) == 'Fizz'

    assert robot(5) == 'Buzz'
    assert robot(10) == 'Buzz'
    assert robot(20) == 'Buzz'

    assert robot(15) == 'FizzBuzz'
    assert robot(30) == 'FizzBuzz'
    assert robot(45) == 'FizzBuzz'