def gradingStudents(grades):
    # Write your code here
    newGrades=[]
    for i in grades:
        if i<38:
            newGrades.append(i)
        else :
            y=i%5
            if y>=3:
                newGrades.append(i+(5-y))
            else :
                newGrades.append(i)
    return newGrades  
