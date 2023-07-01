#  a GPA Calculator for AAST CCIT Students, the program will output the Overall GPA, Each Semester GPA and the overall grade based on the courses registered
student_mark=[]
ct=0
s=0.0
sm=0.0
n=int(input("number of terms:"))
for i in range(n):
    c=int(input("numper of courses:"))
    ct+=c
    def GradeToMarks(c):
        sum=0.0
        for j in range(c):
            grade=str(input("enter grade:"))
            if grade =="A+":
               m=4
            elif grade=="A":
                 m=3.83
            elif grade =="A-":
                m=3.66
            elif grade =="B+":
                 m=3.33
            elif grade =="B":            
                 m=3.00
            elif grade =="B-":
                 m=2.66
            elif grade =="C+":
                m=2.33
            elif grade =="c":
                m=2.00
            elif grade =="c-":
                m=1.66
            elif grade =="D+":
                m=1.33
            elif grade =="D":
                m=1.00
            else:
                m=0.0
            sum +=m*3
        return sum
    sm=GradeToMarks(c)
    GPA=(sm/(c*3))
    s +=sm
    print ("SEMESTER GPA:",GPA)
GPA_TOTAL=s/(ct*3)
print (("TOTAL GPA :"),GPA_TOTAL)
if 3.6<=GPA_TOTAL<=4:
    print ("GRADE:","EXCELLENT")
elif 3<=GPA_TOTAL<=3.6:
    print("GRADE:","VERY GOOD")
elif 2.6<=GPA_TOTAL<=3:
    print("GRADE:","GOOD")
elif 2.0<=GPA_TOTAL<=2.6:
    print ("GRADE:","PASS")
else:
    print("GRADE:","FAIL")                