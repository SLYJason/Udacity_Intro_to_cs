#!/usr/bin/env python
#coding=utf8
def remove_tags(string):
    start = string.find('<')
    while start != -1:
        end = string.find('>', start)
        string = string[:start] + ' ' + string[end+1:]
        start = string.find('<')
    return string.split()

def test():
    assert remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''') == ['Title','This','is','a','link','.']
    assert remove_tags('''<table cellpadding='3'>
                   <tr><td>Hello</td><td>World!</td></tr>
                   </table>''') == ['Hello','World!']
    assert remove_tags("<hello><goodbye>") == []
    assert remove_tags("This is plain text.") == ['This', 'is', 'plain', 'text.']
    print 'test completed'

test()