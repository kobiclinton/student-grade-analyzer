def calculate_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def calculate_statistics(scores):
    total = sum(scores)
    average = total / len(scores)
    highest = max(scores)
    lowest = min(scores)

    return total, average, highest, lowest


def calculate_status(average):
    if average >= 50:
        return "PASS"
    else:
        return "FAIL"


def save_result(name, courses, scores, total, average, highest, lowest, grade, status):
    with open("results.txt", "a") as file:
        file.write("\n===== STUDENT RESULT =====\n")
        file.write(f"Student: {name}\n")

        for i in range(len(courses)):
            course_grade = calculate_grade(scores[i])
            file.write(f"{courses[i]}: {scores[i]} → {course_grade}\n")

        file.write(f"Total: {total}\n")
        file.write(f"Average: {average:.2f}\n")
        file.write(f"Highest: {highest:.2f}\n")
        file.write(f"Lowest: {lowest:.2f}\n")
        file.write(f"Grade: {grade}\n")
        file.write(f"Status: {status}\n")


def analyze_student():
    print("\n===== ANALYZE STUDENT =====")

    name = input("Enter student name: ")

    courses = []
    scores = []

    while True:
        try:
            num_courses = int(input("Enter number of courses: "))

            if num_courses > 0:
                break
            else:
                print("Please enter at least 1 course.")

        except ValueError:
            print("Please enter a valid number.")

    for i in range(num_courses):
        course = input(f"Enter course {i + 1}: ")
        courses.append(course)

        while True:
            try:
                score = float(input(f"Enter score for {course}: "))

                if 0 <= score <= 100:
                    break
                else:
                    print("Score must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid score.")

        scores.append(score)

    print("\n====== COURSES AND SCORES ======")

    for i in range(len(courses)):
        print(f"{courses[i]}: {scores[i]}")

    print("\n====== COURSE RESULTS ======")

    for i in range(len(courses)):
        score = scores[i]
        grade = calculate_grade(score)

        print(f"{courses[i]}: {score} → {grade}")

    total, average, highest, lowest = calculate_statistics(scores)

    grade = calculate_grade(average)
    status = calculate_status(average)

    print("\n===== RESULT =====")

    print(f"Student: {name}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Highest: {highest:.2f}")
    print(f"Lowest: {lowest:.2f}")
    print(f"Grade: {grade}")
    print(f"Status: {status}")

    save_result(
        name,
        courses,
        scores,
        total,
        average,
        highest,
        lowest,
        grade,
        status
    )

    print("Result saved successfully!")


def view_results():
    try:
        with open("results.txt", "r") as file:
            results = file.read()

        if results.strip():
            print("\n===== SAVED RESULTS =====")
            print(results)
        else:
            print("\nNo saved results yet.")

    except FileNotFoundError:
        print("\nNo saved results yet.")


def search_student():
    name = input("Enter student name to search: ")

    try:
        with open("results.txt", "r") as file:
            results = file.read()

        records = results.split("===== STUDENT RESULT =====")

        found = False

        for record in records:
            if f"Student: {name}" in record:
                print("\n===== SEARCH RESULT =====")
                print("===== STUDENT RESULT =====")
                print(record.strip())
                found = True

        if not found:
            print(f"\nNo result found for {name}.")

    except FileNotFoundError:
        print("\nNo saved results yet.")


def delete_student():
    name = input("Enter student name to delete: ")

    try:
        with open("results.txt", "r") as file:
            results = file.read()

        records = results.split("===== STUDENT RESULT =====")

        new_records = []
        deleted = False

        for record in records:
            if f"Student: {name}" in record:
                deleted = True
            else:
                new_records.append(record)

        if deleted:
            with open("results.txt", "w") as file:
                file.write("===== STUDENT RESULT =====".join(new_records))

            print(f"\nResults for {name} deleted successfully!")
        else:
            print(f"\nNo result found for {name}.")

    except FileNotFoundError:
        print("\nNo saved results yet.")


def edit_student():
    name = input("Enter student name to edit: ")

    try:
        with open("results.txt", "r") as file:
            results = file.read()

        records = results.split("===== STUDENT RESULT =====")

        found = False

        for i in range(len(records)):
            if f"Student: {name}" in records[i]:

                print("\n===== STUDENT FOUND =====")
                print(records[i].strip())

                new_course = input("Enter new course name: ")

                while True:
                    try:
                        new_score = float(input("Enter new score: "))

                        if 0 <= new_score <= 100:
                            break
                        else:
                            print("Score must be between 0 and 100.")

                    except ValueError:
                        print("Please enter a valid score.")

                new_grade = calculate_grade(new_score)
                new_status = calculate_status(new_score)

                records[i] = f"""
Student: {name}
{new_course}: {new_score} → {new_grade}
Total: {new_score}
Average: {new_score:.2f}
Highest: {new_score:.2f}
Lowest: {new_score:.2f}
Grade: {new_grade}
Status: {new_status}
"""

                found = True
                break

        if found:
            with open("results.txt", "w") as file:
                file.write("===== STUDENT RESULT =====".join(records))

            print(f"\nResult for {name} updated successfully!")

        else:
            print(f"\nNo result found for {name}.")

    except FileNotFoundError:
        print("\nNo saved results yet.")


def main():
    while True:
        print("\n===== STUDENT GRADE ANALYZER =====")
        print("1. Analyze Student")
        print("2. View Saved Results")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Edit Student")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            analyze_student()

        elif choice == "2":
            view_results()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            edit_student()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, 5, or 6.")


main()
