#! /usr/bin/env python3

# Bezawit Woldegebriel
# Sept. 30, 2014
# Create usernames by using def function and getting input from user



def username(first, last):
    
    first = first.lower()
    last = last.lower()
                   
    firstName = first[0]
    lastName = last[0:4]

    usrname = firstName + lastName + '001'
    return usrname
      
    #username(first, last)

def convertGrade(grade):
    letgrade = [" ", "D", "C", "B", "A", "F"]
    fingrade = letgrade[grade - 1]
    return fingrade

    #convertGrade(grade)


def main():
    infile = open('grades22.txt')

    for line in infile:

        line = line.split()
        firstname = line[0]
        lastname = line[1]
        grades = int(line[-1])

        print(username (firstname, lastname) + " " + convertGrade(grades))

main()
        

