#!/usr/bin/env python
def cellular_automaton(string, pattern_number, generations):
    patterns = {}
    pattern_list = ['xxx', 'xx.', 'x.x', 'x..', '.xx', '.x.', '..x', '...']
    n = len(string)
    
    binary = str(bin(pattern_number)[2:])
    if len(binary) < 8:
        binary = '0' * (8-len(binary)) + binary
    for i in range(8):
        if binary[i] == '1':
            patterns[pattern_list[i]] = 'x'
        else:
            patterns[pattern_list[i]] = '.'
            
    for i in range(generations):
        new_string = ''
        for j in range(n):
            pattern = string[j-1] + string[j] + string[(j+1)%n]
            new_string = new_string + patterns[pattern]
        string = new_string
    return string

 
def test():  
    assert cellular_automaton('.x.x.x.x.', 17, 2) == 'xxxxxxx..'
    assert cellular_automaton('.x.x.x.x.', 249, 3) == '.x..x.x.x'
    assert cellular_automaton('...x....', 125, 1) == 'xx.xxxxx'
    assert cellular_automaton('...x....', 125, 2) == '.xxx....'
    assert cellular_automaton('...x....', 125, 3) == '.x.xxxxx'
    assert cellular_automaton('...x....', 125, 4) == 'xxxx...x'
    assert cellular_automaton('...x....', 125, 5) == '...xxx.x'
    assert cellular_automaton('...x....', 125, 6) == 'xx.x.xxx'
    assert cellular_automaton('...x....', 125, 7) == '.xxxxx..'
    assert cellular_automaton('...x....', 125, 8) == '.x...xxx'
    assert cellular_automaton('...x....', 125, 9) == 'xxxx.x.x'
    assert cellular_automaton('...x....', 125, 10) == '...xxxxx'
    print 'test completed'

test()