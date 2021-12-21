from posixpath import dirname
import classes
import json
import os

def test():
    grader = classes.StudentGrader()
    math = classes.Subject("Math", [], [])
    cs = classes.Subject("Computer Science", [], [])
    econ = classes.Subject("Economics", [], [])
    grader.addSubject(math)
    grader.addSubject(cs)
    grader.addSubject(econ)
    s1 = classes.Student(1, "Preston", "Ku", [cs, math])
    s2 = classes.Student(2, "Aaron","Wang", [cs, math, econ])
    s3 = classes.Student(3, "Rebecca","Chen", [cs])
    grader.addStudent(s1)
    grader.addStudent(s2)
    grader.addStudent(s3)
    grader.addAssignment("Computer Science",classes.Assignment("Student Grader",100,{}))
    grader.addStudentToSubject(s1,cs)
    grader.addStudentToSubject(s1,math)
    grader.addStudentToSubject(s2,cs)
    grader.addStudentToSubject(s2,math)
    grader.addStudentToSubject(s2,econ)
    grader.addStudentToSubject(s3,cs)

    dict=grader.toDict()
    print(json.dumps(dict,sort_keys=True,indent=4))

def main():
    grader = classes.StudentGrader()
    grader.readFile("C:/Users/user/Documents/GitHub/AaronIBCS2023/OOP/studentGrader/out.json")

if __name__ == "__main__":
    main()
    #test()
