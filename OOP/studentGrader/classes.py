import json


class Subject:
    def __init__(self, name, students=[], assignments=[]) -> None:
        self.name = name
        self.students = students
        self.assignments = assignments

    def getAssignments(self, student):
        assignments = []
        for a in self.assignments:
            assignments.append(a)
        #possible that appends reference and cause it to still change
        for a in assignments:
            a.studentGrades = {student.id: a.getStudentGrade(student)}
        return assignments

    def getStudentGrade(self, student):
        avg = 0
        for a in self.assignments:
            avg = avg+a.getStudentGrade(student)
        avg = avg/len(self.assignments)
        return avg

    def getOverallGrade(self):
        avg = 0
        for a in self.assignments:
            avg = avg+a.getMean()
        avg = avg/len(self.assignments)
        return avg

    def addStudent(self, student):
        self.students.append(student)
        for a in self.assignments:
            a.addStudent(student)

    def addAssignment(self, assignment):
        self.assignments.append(assignment)

    def toDict(self):
        result = {}
        result["name"] = self.name
        studentsList = []
        for s in self.students:
            studentsList.append(s.id)
        result["students"] = studentsList
        assignmentDict = {}
        for a in self.assignments:
            assignmentDict[a.name] = a.toDict()
        result["assignments"] = assignmentDict
        return result


class Student:
    def __init__(self, id, gName, fName, subjectEnrolled=[]) -> None:
        self.id = id
        self.givenName = gName
        self.familyName = fName
        self.subjectEnrolled = subjectEnrolled

    def getAssignment(self, subject: Subject):
        assignments = subject.getAssignments(self)
        return assignments

    def showGrades(self):
        grades = {}
        for s in self.subjectEnrolled:
            grades[s.name] = s.getStudentGrade
        print(grades)

    def toDict(self):
        result = {}
        result["id"] = self.id
        result["givenName"] = self.givenName
        result["familyName"] = self.familyName
        subList = []
        for s in self.subjectEnrolled:
            subList.append(s.name)
        result["subjectEnrolled"] = subList
        return result


class Assignment:
    def __init__(self, name, maxMark=100, studentGrades={}) -> None:
        self.name = name
        self.maxMark = maxMark
        self.studentGrades = studentGrades

    def addStudent(self, student):
        self.studentGrades[student.id] = float(input(
            f"Enter student {student.givenName} {student.familyName} grade for assignment {self.name}"))

    def getMean(self):
        avg = 0
        for key in self.studentGrades:
            avg = avg+self.studentGrades[key]
        avg = avg/len(self.studentGrades)
        return avg

    def getRange(self):
        max = 0
        min = self.maxMark
        for key in self.studentGrades:
            if self.studentGrades[key] > max:
                max = self.studentGrades[key]
            if self.studentGrades[key] < min:
                min = self.studentGrades[key]
        return max-min

    def getBelow(self, mark: float):
        result = {}
        for key in self.studentGrades:
            if self.studentGrades[key] < mark:
                result[key] = self.studentGrades[key]
        return result

    def getAbove(self, mark: float):
        result = {}
        for key in self.studentGrades:
            if self.studentGrades[key] > mark:
                result[key] = self.studentGrades[key]
        return result

    def getStudentGrade(self, student):
        return self.studentGrades[student.id]

    def toDict(self):
        result = {}
        result['name'] = self.name
        result['maxMark'] = self.maxMark
        result['studentGrades'] = self.studentGrades
        return result


class StudentGrader:
    def __init__(self) -> None:
        self.students = []
        self.subjects = []

    def addStudent(self, student):
        self.students.append(student)

    def addStudentToSubject(self, student, subject):
        subject.addStudent(student)

    def addAssignment(self, subjectName, assignment):
        for s in self.subjects:
            if s.name == subjectName:
                s.addAssignment(assignment)

    def addSubject(self, subject):
        self.subjects.append(subject)

    def toDict(self):
        result = {}
        stuDict = {}
        for s in self.students:
            stuDict[s.id] = s.toDict()
        result["students"] = stuDict
        subDict = {}
        for s in self.subjects:
            subDict[s.name] = s.toDict()
        result["subjects"] = subDict
        return result

    def readFile(self, filePath):
        with open(filePath) as infile:
            data = json.load(infile)
        studentData = data['students']
        subjectData = data['subjects']
        for id in studentData:
            stuID = studentData[id]['id']
            gName = studentData[id]["givenName"]
            fName = studentData[id]["familyName"]
            # inputted subject enrolled is string not object yet
            SubEnrolled = studentData[id]["subjectEnrolled"]
            student = Student(stuID, gName, fName, SubEnrolled)
            self.students.append(student)
        for s in subjectData:
            subName = subjectData[s]['name']
            stuIDs = subjectData[s]['students']
            students = []
            for id in stuIDs:
                for st in self.students:
                    if st.id == id:
                        students.append(st)
            assignments = subjectData[s]['assignments']
            assignmentObjs=[]
            for a in assignments:
                aName=assignments[a]['name']
                max=assignments[a]['maxMark']
                stuGrades=assignments[a]['studentGrades']
                assignmentObjs.append(Assignment(aName,max,stuGrades))
            sub = Subject(subName, students, assignmentObjs)
            self.subjects.append(sub)
        for st in self.students:
            subs = []
            for s in st.subjectEnrolled:
                for sub in self.subjects:
                    if sub.name == s:
                        subs.append(sub)
            st.subjectEnrolled = subs

    def writeFile(self, filePath):
        dict = self.toDict()
        with open(filePath, "w") as outfile:
            json.dump(dict, outfile)
