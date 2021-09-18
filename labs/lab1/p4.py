Cha = {"A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7,
       "C+": 2.4, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0, "F": 0.0}
credit = 0
gpa = 0
while True:
    grade = input().split(", ")
    if((grade[0] in Cha) and (grade[1].isnumeric() and int(grade[1]) > 0)):
        credit += int(grade[1])
        gpa += Cha[grade[0]]*int(grade[1])
        print("Current GPA: {:.2f}".format(gpa/credit))

    elif(grade[0] == "exit"):
        print("Your GPA: {:.2f}.".format(gpa/credit))
        print("Program ends.")
        break
    else:
        print("Wrong input!")
