# PrepTrack — Placement Preparation Performance Analyzer

## Project Overview

PrepTrack is a Python console application designed to assess and track students' readiness for placement mock interviews. The application collects student profile information (such as name, registration number, graduation year, attendance percentage, project completion status, and profile verification) alongside daily scores across a 7-day practice period. It performs detailed performance analysis by calculating average scores, classifying performance levels, identifying highest/lowest daily results, and detecting critical score thresholds (scores below 40). Finally, it displays a comprehensive PrepTrack Performance Report evaluating placement readiness, highlighting any primary blockers, and recommending immediate next steps.

---

## Features Implemented

- **Student-Profile Input**: Captures student details including name, registration number, graduation year, attendance, project completion, and profile verification status.
- **Attendance Validation**: Validates that student attendance percentages fall strictly between 0% and 100%.
- **Yes-or-No Input Validation**: Robust boolean input validation ensuring users enter only `'yes'` or `'no'` for project completion and profile verification status.
- **Seven-Day Practice Processing**: Iteratively collects score entries (0–100) or absence indicators (`-1`) for 7 consecutive practice days.
- **Score Classification**: Categorizes daily attempted scores into Strong (75–100), Satisfactory (60–74), Needs Improvement (40–59), and Critical (<40).
- **Passed and Failed Counting**: Counts passed days (scores ≥ 60) and failed days (scores < 60 or absences) across the 7-day tracking period.
- **Highest and Lowest Score Detection**: Dynamically identifies the student's highest and lowest scores along with the specific days on which they occurred.
- **Critical-Score Detection**: Flags scores below 40 as critical and captures the day and score of the first critical performance instance.
- **Average Calculation**: Calculates the exact average score across all attempted practice days.
- **Placement-Readiness Evaluation**: Evaluates overall eligibility for mock interviews against criteria including graduation year (2025–2027), attendance (≥75%), practice attempt count (≥6 days), average score (≥70), passed days (≥4), zero critical scores, project completion, and profile verification.

---

## Python Concepts Used

- **Variables & Primitive Data Types**: Managed strings (`str`), integers (`int`), floats (`float`), and booleans (`bool`) for student data and metrics.
- **Input & Output Handling**: Used `input()` for dynamic CLI prompts, `print()` statements for report layout, and `f-strings` with format specifiers (e.g., `:.2f`).
- **Control Flow & Selection Statements**: Utilized conditional logic (`if`, `elif`, `else`) to handle score ranges, eligibility checks, and blocker determination.
- **Loops & Iteration**: 
  - `while True` loops for robust input validation.
  - `for day in range(1, 8)` loop to iterate through the 7 practice days.
- **Loop Control Statements**: Employed `break` to exit validation loops upon receiving valid input and `continue` to skip calculations for absent days.
- **Logical & Relational Operators**: Applied relational (`>=`, `<=`, `<`, `>`) and logical (`and`, `or`, `not`) operators to combine multi-variable eligibility rules.
- **Counters, Accumulators & State Flags**: Tracked performance using accumulators (`total_score`), counters (`attempted_days`, `passed_days`, `critical_days`), and boolean tracking flags (`first_attempt_found`, `critical_score_found`).

---

## How to Run

To run the application, open your terminal or command prompt in the project directory and execute:

```bash
python main.py
```

Depending on your system configuration (e.g., macOS/Linux or systems with multiple Python installations):

```bash
python3 main.py
```

---

## Test-Result Summary

The application was thoroughly verified across multiple edge cases and test scenarios:

| Test Case | Inputs / Conditions Tested | Expected Status | Actual Outcome | Status |
| :--- | :--- | :--- | :--- | :--- |
| **1. Fully Eligible Student** | Attendance: 85%, Graduation: 2026, Project: yes, Profile: yes, Scores: [80, 85, 90, 75, 70, 88, 92] | Ready for Mock Interview | Final Status: Ready for Mock Interview | PASSED |
| **2. Low Attendance Blocker** | Attendance: 70%, Scores: [80, 80, 80, 80, 80, 80, 80] | Not Ready for Mock Interview | Primary Blocker: Attendance below 75% | PASSED |
| **3. Critical Score Blocker** | Scores: [85, 90, 35, 80, 85, 90, 80] | Not Ready for Mock Interview | Primary Blocker: Critical score found (Day 3: 35) | PASSED |
| **4. High Absence Count** | 3 days absent (-1), 4 days attempted | Not Ready for Mock Interview | Primary Blocker: Fewer than six attempts | PASSED |
| **5. Input Validation** | Empty name, negative attendance, non-yes/no answers, out-of-range scores | Re-prompt until valid input | Handled gracefully without crashes | PASSED |

---

## Individual Contribution

- **Name**: Bharathi
- **Repository URL**: https://github.com/Bharathicode/preptrack-bharathi
- **My main contribution**: Designed and implemented the complete core logic for `PrepTrack` in `main.py`, covering user input collection, input validation loops, daily score evaluation over a 7-day period, statistical calculations, placement readiness checks, and structured report output formatting.

- **Features I implemented**:
  - Student profile data collection and multi-stage input validation (`while True` loops).
  - 7-day score iteration with support for score bounds checking (0–100) and absence recording (`-1`).
  - Score classification logic (Strong, Satisfactory, Needs Improvement, Critical).
  - Dynamic tracking of highest score, lowest score, and first critical score occurrence.
  - Multi-condition placement readiness evaluation engine and primary blocker identification.
  - User-friendly terminal output layout for the final PrepTrack Report.

- **Python concepts I used**:
  - Loops (`while`, `for ... in range()`) and control statements (`break`, `continue`).
  - Conditionals (`if`, `elif`, `else`) with nested and compound logical conditions (`and`, `or`, `not`).
  - Variables, type conversion (`int()`, `float()`), boolean flags, and numeric accumulators.
  - Standard I/O with formatted f-strings (`:.2f`).

- **Most difficult logic**: Designing the dynamic tracking mechanism for highest and lowest scores during the 7-day loop while accounting for optional absent days (`-1`), ensuring that initialization only occurs on the `first_attempt_found` rather than hardcoding static array indices or initial zero values that could corrupt lowest score detection.

- **Problem I faced**: When a student scored below 40, initial logic was incrementing critical days count twice and failing to properly preserve the *first* critical day metadata when subsequent low scores occurred.

- **How I solved it**: Standardized the critical score tracking using an explicit boolean flag (`critical_score_found`). On the first occurrence of a score < 40, the flag sets to `True` and locks in `first_critical_day` and `first_critical_score` without overwriting them on subsequent critical days.

---

## Code Review Completed

- **Reviewer**: 
- **Review Date**: 
- **Review Status**: 
- **Summary**: 

---

## Feedback Received

Reviewed By:

Feedback Received:

Was the Feedback Valid? Yes / No

Change Made:

Commit Message Used:

---

