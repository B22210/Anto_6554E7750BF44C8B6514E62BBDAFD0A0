class student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_student(student_list):
  # sort the list of student in descending order of CGPA
  sorted_students = sorted(student_list,
                          key=lambda student: student.cgpa,
                          reverse=True)
  return sorted_students

students = [
  student("joy","b22213",1.8),
  student("gilbert","b22233",4.5),
  student("anto","b22210",8.4),
  student("kingston","b22245",6.3),
  student("christo","b22232",9.6),
]

sorted_students = sort_student(students)
for student in sorted_students:
  print("Name : {} ,Roll Number : {}, CGPA : {}".format(student.name,student.roll_number,student.cgpa))