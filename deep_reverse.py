#!/usr/bin/env python
def is_list(p):
    return isinstance(p, list)

def deep_reverse(input_list):
    reversed_list = input_list[::-1]
    for i in range(0, len(reversed_list)):
        if is_list(reversed_list[i]):
            reversed_list[i] = deep_reverse(reversed_list[i])
    return reversed_list

def test():
    p = [1, [2, 3, [4, [5, 6]]]]
    assert deep_reverse(p) == [[[[6, 5], 4], 3, 2], 1]
    assert p == [1, [2, 3, [4, [5, 6]]]]

    q =  [1, [2,3], 4, [5,6]]
    assert deep_reverse(q) == [ [6,5], 4, [3, 2], 1]
    assert q == [1, [2,3], 4, [5,6]]
    
    print 'test completed'
    
test()