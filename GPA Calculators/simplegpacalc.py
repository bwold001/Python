#! /usr/bin/env python3

# Bezawit Woldegebriel
# Oct. 23, 2014
# Simple  GPA calculator

def main ():
    
    infile = open('grades.txt','r')
    totcredhrs = 0
    totclasspt = 0


    for line in infile:
        
        letgrade, credit = line.split()
        credit = int(credit)
                        
        if letgrade == 'A':
            qp = 4.0
        if letgrade == 'A-':
            qp = 3.7
        if letgrade == 'B+':
            qp = 3.3
        if letgrade == 'B':
            qp = 3.0
        if letgrade == 'B-':
            qp = 2.7
        if letgrade == 'C+':
            qp = 2.3
        if letgrade == 'C':
            qp = 2.0
        if letgrade == 'C-':
            qp = 1.7
        if letgrade == 'D+':
            qp = 1.3
        if letgrade == 'D':
            qp = 1.0
        if letgrade == 'E':
            qp = 0.0

        classpts = qp * credit
        totcredhrs = credit + totcredhrs
        totclasspt = classpts + totclasspt
        
    gpa = totclasspt/totcredhrs

    print("Overall GPA:", gpa)

main()
