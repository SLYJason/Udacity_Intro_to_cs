#!/usr/bin/env python
def triangle(n):
    result = [] 
    current = [1]
    for i in range(0, n):
        result.append(current)
        current = make_next_row(current)
    return result
    

def make_next_row(current):
    prev = 0
    next_row = []
    for i in current:
        next_row.append(prev + i)
        prev = i
    next_row.append(prev)
    return next_row

def test():
    assert triangle(0) == []
    assert triangle(1) == [[1]]
    assert triangle(2) == [[1], [1, 1]]
    assert triangle(3) == [[1], [1, 1], [1, 2, 1]]
    assert triangle(6) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    print 'test completed'
    
test()