#!/usr/bin/env python
def split_string(source,splitlist):
    result = []
    letter = ''
    for ch in source:
        if ch not in splitlist:
            letter += ch
        else:
            if letter != '':
                result.append(letter)
                letter = ''
    if letter != '':
        result.append(letter)
    return result

def split_string_ans(source,splitlist):
    output = []
    atsplit = True
    for char in source:
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                output[-1] += char
    return output
    
def test():
    out = split_string_ans("This is a test-of the,string separation-code!"," ,!-")
    assert out == ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

    out = split_string_ans("After  the flood   ...  all the colors came out.", " .")
    assert out == ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

    out = split_string_ans("First Name,Last Name,Street Address,City,State,Zip Code",",")
    assert out == ['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
    print "test completed"

test()