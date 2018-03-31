#!/usr/bin/env python
def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    assert not dateIsBefore(y2, m2, d2, y1, m1, d1)
    days = 0
    while dateIsBefore(y1, m1, d1, y2, m2, d2):
        days += 1
        y1, m1, d1 = nextDay(y1, m1, d1)
    return days
    
def dateIsBefore(y1, m1, d1, y2, m2, d2):
    if y1<y2:
        return True
    if y1==y2:
        if m1<m2:
            return True
        if m1==m2:
            return d1<d2
    return False
    
def nextDay(year, month, day):
    if day<daysInMonth(year, month):
        return year, month, day+1
    else:
        if month == 12:
            return year+1, 1, 1
        else:
            return year, month+1, 1
    
def daysInMonth(year, month):
    if month==2:
        if isLeapYear(year):
            return 29
        return 28
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    return 31
    
def isLeapYear(year):
    if year%4 == 0:
        if year%400 == 0:
            return True
        if year%100 == 0:
            return False
        return True
    return False
    
def test():
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 1) == 0
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 2) == 1
    assert nextDay(2013, 1, 1) == (2013, 1, 2)
    assert nextDay(2013, 4, 30) == (2013, 5, 1)
    assert nextDay(2012, 12, 31) == (2013, 1, 1)
    assert nextDay(2013, 2, 28) == (2013, 3, 1)
    assert daysBetweenDates(2013, 1, 1, 2014, 1, 1) == 365  

    # added tests for leap years
    assert nextDay (2012, 2, 28) == (2012, 2, 29)
    assert daysBetweenDates(2012, 1, 1, 2013, 1, 1) == 366      
    print 'Tests Completed'

test()