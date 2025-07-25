
#Project Based - LMS - 1
#Scenario: Basic Student Information

#delecation

student_id = 1234

student_name ="harika"
 
Student_age =23

quiz_score =90

assignment_score =95

exam_score =98

student_attendance =93


#avg and total marks

total_marks= quiz_score + assignment_score + exam_score

print(f"total_marks :{total_marks}")

avg_marks= total_marks/ 3

print(f"avg_marks :{avg_marks}")

# relational operators
 
student_passed = avg_marks >= 75
 
print(f"student_passed :{student_passed}")

#increment operator to update:

student_attendance += 1

print(f"student_attendance :{student_attendance}")

#determine award eligibility

student_award= (student_attendance >= 90) and (student_passed)

print(f"student_award :{student_award}")


#display section 

Student_Information_Section=(f"student id:{student_id}, student name:{student_name}, student age:{Student_age}") 

print(Student_Information_Section)