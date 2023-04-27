# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 11:57:08 2023

@author: Santiago Defaz
"""

def isYearLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def daysInMonth(year, month):
    if month == 2:
        if isYearLeap(year):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def dayOfYear(year, month, day):
    if year < 1 or month < 1 or month > 12 or day < 1 or day > daysInMonth(year, month):
        return None
    
    days = 0
    for m in range(1, month):
        days += daysInMonth(year, m)
        
    days += day
    
    return days


print(dayOfYear(2023, 1, 31)) # 366