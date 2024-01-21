#!/bin/python3

#Given the names and grades for each student in a class of N students, 
#store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':

    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    second_lowest_grade = sorted(set(points for _, points in records))[1]

    #print(second_lowest_grade)

    for names in sorted([name for name, points in records if points == second_lowest_grade]):
        print(names)
