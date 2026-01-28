# grade_eval.py
# spring 2026
# Prof. Lehman
#
# Demonstrates Functions, If Statements
# Code determines grade percent, letter grade, and checks minimum requirements for major
#


def grade_percentage(attendance: float, exams: float, assignments: float) -> float:
    """
    attendance worth 10%
    exams worth 50%
    assignments worth 40%

    returns: float (overall course percentage)
    """
    # TODO: calculate and return the weighted percentage
    return 0.0


def letter_grade(percent: float) -> str:
    """
    returns: str

    Letter grade rules:
    A: 90–100
    B: 80–89
    C: 70–79
    D: 60–69
    F: below 60
    """
    # TODO: determine and return "A", "B", "C", "D", or "F"
    return "?"


def minimum_grade(grade: str, category: str, major: str) -> bool:
    """
    returns: bool

    Determines if grade meets minimum for major and core requirements

    Rules:
    - If course category is "major", then grade must be "C" or higher
    - If course category is "core", then grade must be "D" or higher
    - If major is nursing or ota, ALL courses require "C" or higher
    """

    result = False

    # TODO: set result to True or False based on grade, category, and major

    return result


def detailed_report(a: float,
                            e: float,
                            s: float,
                            p: float,
                            g: str) -> None:
    """
    returns: None

    Prints a formatted course evaluation report.

    a = attendance
    e = exams
    s = assignments
    p = percentage
    g = letter grade
    """

    print()
    print("Course Evaluation")
    print("-----------------")
    print(f"Attendance:  {a}")
    print(f"Exams:       {e}")
    print(f"Assignments: {s}")
    print()
    print(f"Final percentage: {p:.2f}%")
    print(f"Final letter grade: {g}")
    print()


# --------------------
# main program
# --------------------

if __name__ == "__main__":
    
    #---------------------
    # --- INPUT ----------
    #---------------------
    attendance = 95

    exams = 89

    assignments = 92

    major = "CS"        # try: "cs", "nursing", "ota"

    category = "major"  # "major" or "core"


    #---------------------
    # --- PROCESSING -----
    #---------------------

    percent = grade_percentage(attendance, exams, assignments)

    grade = letter_grade(percent)


    #--------------------
    # --- OUTPUT --------
    #--------------------

    detailed_report(attendance, exams, assignments, percent, grade)

    if minimum_grade(grade, category, major) == True:
        print("The grade meets the minimum requirement.")
    else:
        print("The grade does NOT meet the minimum requirement.")





