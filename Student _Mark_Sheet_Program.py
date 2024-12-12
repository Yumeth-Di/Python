def calculate_total_and_position(science_marks, maths_marks):

    total_marks = science_marks + maths_marks
    return total_marks, None  

def main():
    student_data = []
    for i in range(5):
        science_marks = int(input(f"Enter science marks for student {i+1}: "))
        maths_marks = int(input(f"Enter maths marks for student {i+1}: "))
        total_marks, _ = calculate_total_and_position(science_marks, maths_marks)
        student_data.append((total_marks, i+1))

    student_data.sort(reverse=True)

    for i, (total_marks, student_id) in enumerate(student_data):
        position = i + 1
        print(f"Student {student_id}:Total Marks = {total_marks},Position = {position}")
main()
