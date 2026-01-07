import sys


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


def get_input(prompt, default=None):
    try:
        return input(prompt)
    except EOFError:
        return default


def main():
    show_grade_criteria()

    print("\n--- Enter Student Details ---")

    # CLI arguments for Jenkins / Docker
    if len(sys.argv) == 7:
        _, name, department, semester, m1, m2, m3 = sys.argv
        m1, m2, m3 = float(m1), float(m2), float(m3)
    else:
        name = get_input("Enter Student Name: ", "Prathik")
        department = get_input("Enter Department: ", "BCA")
        semester = get_input("Enter Semester: ", "III")

        print("\n--- Enter Marks ---")
        m1 = float(get_input("Enter Subject 1 Marks: ", 85))
        m2 = float(get_input("Enter Subject 2 Marks: ", 90))
        m3 = float(get_input("Enter Subject 3 Marks: ", 95))

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
