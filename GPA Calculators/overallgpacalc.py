#! /usr/bin/env python3

# Bezawit Woldegebriel
# Nov 18, 2014
# Overall GPA calculator


def main():

    courses = open("courses.txt")
    student = open("studentData.txt")
    letgrade = {'A':4.0, 'A-':3.7, 'B+': 3.3, 'B':3.0, 'B-':2.7,
                'C+':2.3, 'C':2.0, 'C-':1.7, 'D+': 1.3, 'D': 1.0,
                'E': 0}
    allcourses = {}
    studtotalgrade = {}
    totalcourses = {}
    studgpa = {}

    for line in courses.readlines():
        course, credit =  line.strip().split(" ")
        allcourses[course] = int(credit)
		
    for line in student.readlines():
        usrname, studcours, studgrade = line.strip().split(" ")
        if usrname in studtotalgrade:
            studtotalgrade[usrname]=studtotalgrade[usrname]+int(letgrade[studgrade])
            totalcourses[usrname]+=1
        else:
            studtotalgrade[usrname]=int(letgrade[studgrade])
            totalcourses[usrname]=1

    for student in studtotalgrade:
        studgpa[student]= '{0:.2f}'.format(studtotalgrade[student]/totalcourses[student])


    print (studgpa)   
    
       
main()
