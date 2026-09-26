students = []
n = int(input("Enter the number of student:"))
def input_student():
    id = int(input("Student id:"))
    name = input("Student name:")
    Dob = (input("Student DoB:"))

    return{
        "id": id,
        "name": name,
        "DoB": Dob
    }
for i in range(n):
        print(f"\nStudent {i + 1}")
        student = input_student()
        students.append(student)

courses = []
m = int(input("Enter the number of course:"))
def input_course():
    code = input("Course code:")
    name = input("Course name:")
    return{
        "code": code,
        "name": name
    }
for i in range(m):
        print(f"\nCourse {i + 1}")
        course = input_course()
        courses.append(course)

marks56 = []
a = int(input("Enter the number of mark:"))
def input_mark():
    student_id = int(input("Student id:"))
    course_code = input("Course code:")
    score = float(input("Score:"))
    return{
        "student_id": student_id,
        "course_code": course_code,
        "score": score
    }
for i in range(a):
    print(f"\nMark {i + 1}")
    mark = input_mark()
    marks.append(mark)