# =========================================================
# Project Title: Student Performance & Career Path Predictor
# Name: Priyanshi Varshney
# Reg No: 26BAI10184
# Course: Python Essentials
# =========================================================

DATA_FILE = "student_predictions.txt"


def calculate_prediction(attendance, study_hours, coding_score, projects):
    
    grade_score = (
        (attendance * 0.3)
        + (study_hours * 5 * 0.2)
        + (coding_score * 0.35)
        + (min(projects * 5, 15))
    )
    predicted_score = round(min(grade_score, 100), 2)

    if predicted_score >= 85:
        grade_letter = "A (Excellent)"
    elif predicted_score >= 70:
        grade_letter = "B (Good)"
    elif predicted_score >= 50:
        grade_letter = "C (Average)"
    else:
        grade_letter = "D (Needs Improvement)"

    placement_readiness = (coding_score * 0.5) + (projects * 10 * 0.5)
    if placement_readiness >= 75:
        career_status = "High Chance of Top Tech Placement"
    elif placement_readiness >= 50:
        career_status = "Moderate Placement Readiness"
    else:
        career_status = "Low Readiness - Focus on Core Skills"

    if coding_score >= 80 and projects >= 3:
        suggested_path = "Software Engineering / Data Science"
    elif coding_score >= 60:
        suggested_path = "Web / App Development"
    else:
        suggested_path = "IT Support / Systems Administration"

    return predicted_score, grade_letter, career_status, suggested_path


def save_record(
    name, student_id, score, grade, career_status, suggested_path
):
    
    with open(DATA_FILE, "a") as f:
        f.write(
            f"{student_id} | {name} | {score}% | {grade} | {career_status} | {suggested_path}\n"
        )


def view_all_predictions():
    
    try:
        with open(DATA_FILE, "r") as f:
            lines = f.readlines()
            if not lines:
                print("\n[Info] No prediction records found.")
                return

            print("\n" + "=" * 70)
            print("SAVED PREDICTION RECORDS")
            print("=" * 70)
            for line in lines:
                print(line.strip())
            print("=" * 70 + "\n")
    except FileNotFoundError:
        print("\n[Info] No prediction file found yet. Make a prediction first!")


def add_prediction():
    print("\n--- STUDENT PERFORMANCE PREDICTOR ---")
    name = input("Enter Student Name: ").strip()
    student_id = input("Enter Registration/ID Number: ").strip()

    try:
        attendance = float(input("Enter Attendance Percentage (0-100): "))
        study_hours = float(input("Enter Daily Study Hours (0-12): "))
        coding_score = float(
            input("Enter Programming Assessment Score (0-100): ")
        )
        projects = int(input("Enter Number of Projects Completed: "))
    except ValueError:
        print("\n[Error] Invalid input! Please enter numbers only.")
        return

    score, grade, career_status, suggested_path = calculate_prediction(
        attendance, study_hours, coding_score, projects
    )

    save_record(name, student_id, score, grade, career_status, suggested_path)

    print("\n" + "=" * 45)
    print("        PREDICTION RESULT GENERATED       ")
    print("=" * 45)
    print(f"Predicted Score      : {score}% ({grade})")
    print(f"Placement Status     : {career_status}")
    print(f"Recommended Domain   : {suggested_path}")
    print("=" * 45)
    print("[Success] Prediction record saved successfully!\n")


def main():
    while True:
        print("\n========================================")
        print("  STUDENT PERFORMANCE & CAREER PREDICTOR  ")
        print("==========================================")
        print("1. Predict Student Performance & Career Path")
        print("2. View All Stored Predictions")
        print("3. Exit")

        choice = input("Select an option (1-3): ").strip()
        if choice == "1":
            add_prediction()
        elif choice == "2":
            view_all_predictions()
        elif choice == "3":
            print("\nExiting Predictor Application. Goodbye!")
            break
        else:
            print("[Invalid] Choice invalid. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
