#!/bin/python3

def is_leap(year):
        
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True

    return False

year = int(input())
print(is_leap(year))
