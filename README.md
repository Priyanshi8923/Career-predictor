# Student Performance & Career Path Predictor

A simple command-line Python application that predicts a student's academic performance grade and suggests a suitable career path based on attendance, study habits, coding assessment score, and completed projects. All predictions are saved to a local text file for future reference.

## Project Details

| Field | Value |
|---|---|
| Project Title | Student Performance & Career Path Predictor |
| Name | Priyanshi Varshney |
| Registration No. | 26BAI10184 |
| Course | Python Essentials |

## Features

- Predicts a numeric performance score (0–100) from four inputs
- Assigns a letter grade (A/B/C/D) based on the predicted score
- Estimates placement readiness (High / Moderate / Low)
- Suggests a career/domain path (Software Engineering, Web/App Dev, or IT Support)
- Saves every prediction to a persistent text file (`student_predictions.txt`)
- Lets you view all previously saved predictions at any time
- Simple menu-driven interface that runs in a loop until you exit

## Requirements

- Python 3.x (no external libraries needed — uses only the built-in `input`, `open`, etc.)

## File Structure

```
project-folder/
│
├── student_predictor.py      # Main program file (your script)
└── student_predictions.txt   # Auto-created; stores saved predictions
```

## How to Run

### Step 1: Save the script
Save the code in a file named, for example, `student_predictor.py`.

### Step 2: Open a terminal
Navigate to the folder containing the script:
```bash
cd path/to/project-folder
```

### Step 3: Run the program
```bash
python student_predictor.py
```
(On some systems you may need `python3` instead of `python`.)

### Step 4: Use the menu
You'll see a menu with three options:
```
1. Predict Student Performance & Career Path
2. View All Stored Predictions
3. Exit
```
Type `1`, `2`, or `3` and press Enter.

## Step-by-Step Usage Guide

### Option 1 — Predict Student Performance & Career Path
1. Select `1` from the main menu.
2. Enter the student's **Name**.
3. Enter the **Registration/ID Number**.
4. Enter **Attendance Percentage** (a number between 0 and 100).
5. Enter **Daily Study Hours** (a number between 0 and 12).
6. Enter **Programming Assessment Score** (a number between 0 and 100).
7. Enter the **Number of Projects Completed** (a whole number).
8. The program calculates and displays:
   - Predicted Score (%) and Grade (A/B/C/D)
   - Placement Status (High / Moderate / Low readiness)
   - Recommended Domain (career path suggestion)
9. The result is automatically appended to `student_predictions.txt`.

If you type a non-numeric value for attendance, study hours, score, or projects, the program shows an error and cancels that entry — no invalid record is saved.

### Option 2 — View All Stored Predictions
1. Select `2` from the main menu.
2. The program reads `student_predictions.txt` and prints every saved record in the format:
   ```
   RegNo | Name | Score% | Grade | Career Status | Suggested Path
   ```
3. If no file exists yet (no predictions made), it tells you that instead of crashing.

### Option 3 — Exit
Select `3` to close the program.

## How the Prediction Logic Works

### 1. Predicted Score
```
grade_score = (attendance × 0.3)
            + (study_hours × 5 × 0.2)
            + (coding_score × 0.35)
            + min(projects × 5, 15)
```
The result is capped at 100 and rounded to 2 decimal places.

### 2. Grade Letter
| Score Range | Grade |
|---|---|
| 85 – 100 | A (Excellent) |
| 70 – 84 | B (Good) |
| 50 – 69 | C (Average) |
| Below 50 | D (Needs Improvement) |

### 3. Placement Readiness
```
placement_readiness = (coding_score × 0.5) + (projects × 10 × 0.5)
```
| Readiness Score | Status |
|---|---|
| ≥ 75 | High Chance of Top Tech Placement |
| 50 – 74 | Moderate Placement Readiness |
| Below 50 | Low Readiness – Focus on Core Skills |

### 4. Suggested Career Path
| Condition | Suggested Path |
|---|---|
| coding_score ≥ 80 **and** projects ≥ 3 | Software Engineering / Data Science |
| coding_score ≥ 60 | Web / App Development |
| Otherwise | IT Support / Systems Administration |

## Data Storage Format

Each saved record is a single line in `student_predictions.txt`, pipe-separated:
```
26BAI10184 | Priyanshi Varshney | 87.5% | A (Excellent) | High Chance of Top Tech Placement | Software Engineering / Data Science
```

## Example Run

```
========================================
  STUDENT PERFORMANCE & CAREER PREDICTOR
==========================================
1. Predict Student Performance & Career Path
2. View All Stored Predictions
3. Exit
Select an option (1-3): 1

--- STUDENT PERFORMANCE PREDICTOR ---
Enter Student Name: Priyanshi Varshney
Enter Registration/ID Number: 26BAI10184
Enter Attendance Percentage (0-100): 92
Enter Daily Study Hours (0-12): 4
Enter Programming Assessment Score (0-100): 85
Enter Number of Projects Completed: 3

=============================================
        PREDICTION RESULT GENERATED
=============================================
Predicted Score      : 90.55% (A (Excellent))
Placement Status     : High Chance of Top Tech Placement
Recommended Domain   : Software Engineering / Data Science
=============================================
[Success] Prediction record saved successfully!
```

## Notes & Possible Improvements
- Currently, all records are appended without checking for duplicate Registration IDs.
- Input validation only catches type errors, not out-of-range values (e.g., attendance > 100).
- Could be extended with a CSV export, GUI, or graph of performance trends.
