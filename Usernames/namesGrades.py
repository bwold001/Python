#! /usr/bin/env python3

# Bezawit Woldegebriel
# Create usernames and process quiz grades


def username(first, last):
    
    first = first.lower()
    last = last.lower()
                   
    firstName = first[0]
    lastName = last[0:4]

    usrname = firstName + lastName + '001'
    return usrname

def convertGrade(grade):
    letgrade = [" ", "D", "C", "B", "A", "F"]
    fingrade = letgrade[grade - 1]
    return fingrade


def main():
    infile = open('grades.txt')

    for line in infile:

        line = line.split()
        firstname = line[0]
        lastname = line[1]
        grades = int(line[-1])

        print(username (firstname, lastname) + " " + convertGrade(grades))

main()
        

