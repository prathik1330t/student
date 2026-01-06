def show_grade_criteria():
    print("\n--- Grade Criteria ---")
    print("90 - 100 : Grade S")
    print("80 - 89  : Grade A")
    print("65 - 79  : Grade B")
    print("50 - 64  : Grade C")
    print("40 - 49  : Grade D")
    print("Below 40 : Grade F")
    print("----------------------")


def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3


def calculate_grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


def main():
    show_grade_criteria()

    print("\n--- Enter Student Details ---")
    name = input("Enter Student Name: ")
    department = input("Enter Department: ")
    semester = input("Enter Semester: ")

    print("\n--- Enter Marks ---")
    m1 = float(input("Enter Subject 1 Marks: "))
    m2 = float(input("Enter Subject 2 Marks: "))
    m3 = float(input("Enter Subject 3 Marks: "))

    avg = calculate_average(m1, m2, m3)
    grade = calculate_grade(avg)

    print("\n--- Student Result ---")
    print(f"Name       : {name}")
    print(f"Department : {department}")
    print(f"Semester   : {semester}")
    print(f"Average    : {avg}")
    print(f"Grade      : {grade}")


if __name__ == "__main__":
    main()
