def calculate_cgpa():
    print("CGPA CALCULATOR")

    subject_count = int(input("Enter the number of subjects: "))

    total_weighted_grade_points = 0.0
    total_credits = 0.0

    for subject_number in range(1, subject_count + 1):
        print(f"\nSubject {subject_number}")
        grade_point = float(input("  Enter grade point (e.g., 10, 9, 8): "))
        credit = float(input("  Enter credit for this subject: "))

        total_weighted_grade_points += grade_point * credit
        total_credits += credit

    if total_credits == 0:
        print("\nTotal credits cannot be zero. Please check your inputs.")
        return

    cgpa = total_weighted_grade_points / total_credits
    percentage = cgpa * 9.5

    print("\nRESULT")
    print(f"Total subjects: {subject_count}")
    print(f"Total credits: {total_credits}")
    print(f"Your CGPA: {cgpa:.2f}")
    print(f"Approx. percentage: {percentage:.2f}%")

if __name__ == "__main__":
    calculate_cgpa()
