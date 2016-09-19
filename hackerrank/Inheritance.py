class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        total = (sum(i for i in scores)) // len(scores)
        print (total , len(scores))
        if total < 40:
            return "T"
        elif total >= 40 and total < 55:
            return "D"
        elif total >= 55 and total < 70:
            return "P"
        elif total >= 70 and total < 80:
            return "A"
        elif total >= 80 and total < 90:
            return "E"
        elif total >= 90 and total <= 100:
            return "O"

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())