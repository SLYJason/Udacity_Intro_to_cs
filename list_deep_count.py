#!/usr/bin/env python
def is_list(p):
    return isinstance(p, list)
    
def deep_count(p):
    for e in p:
        if is_list(e):
            return len(p) + deep_count(e)
    return len(p)

#sol_2
#def deep_count(p):
#    sum = 0
#    for e in p:
#        sum = sum + 1
#        if is_list(e):
#            sum = sum + deep_count(e)
#    return sum
    
def test():
    assert deep_count([1, 2, 3]) == 3
    assert deep_count([1, [], 3]) == 3
    assert deep_count([1, [1, 2, [3, 4]]]) == 7
    assert deep_count([[[[[[[[1, 2, 3]]]]]]]]) == 10
    print 'test completed'

test()