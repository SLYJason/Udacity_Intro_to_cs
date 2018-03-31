#!/usr/bin/env python

def shift_n_letters(letter, n):
    n = n%26
    letter_n_order = ord(letter) + n
    if letter_n_order > ord('z'):
        return chr(letter_n_order-ord('z')+ord('a')-1)
    return chr(letter_n_order)
    
def test():
    assert shift_n_letters('s', 1) == 't'
    assert shift_n_letters('s', 2) == 'u'
    assert shift_n_letters('s', 10) == 'c'
    assert shift_n_letters('s', -10) == 'i'
    print 'test completed'

test()