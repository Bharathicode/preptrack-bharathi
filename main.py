print("=" * 50)
print("              PREPTRACK APPLICATION")
print("=" * 50)

while True:
    student_name = input("Student Name: ")
    if student_name !="":
        break
    else:
        print("Student name cannot be empty")

registration_number = input("Registration Number: ")
graduation_year = int(input("Graduation Year: "))


while True:
    attendance = float(input("Attendance: "))
    if attendance >= 0 and attendance <= 100:
        break
    else:
        print("Attendance must be between 0 and 100")
        

while True:
    project_input = input("Project Completed: ")
    if project_input =="yes":
        project_completed = True
        break
    elif project_input =="no":
        project_completed = False
        break
    else:
        print("Please enter only yes or no")


while True:
    profile_input = input("Profile Verified: ")
    if profile_input == "yes":
        profile_verified = True
        break
    elif profile_input == "no":
        profile_verified = False
        break
    else:
        print("Please enter only yes or no")


total_score = 0

attempted_days = 0
absent_days = 0
passed_days = 0
failed_days = 0

strong_days = 0
satisfactory_days = 0
improvement_days = 0
critical_days = 0

highest_score = 0
highest_score_day = 0

lowest_score = 100
lowest_score_day = 0

first_attempt_found = False

critical_score_found = False
first_critical_day = 0
first_critical_score = 0


for day in range(1, 8):
    while True:
        score = int(input(f"Enter Day {day} score from 0 to 100, "
                "or -1 for absent: "))

        if score == -1 or (score >=0 and score <= 100):
            break
        else:
            print("Please enter only -1 or a score between 0 and 100")

    if score == -1:
        absent_days += 1
        print(f"Day {day} Result: Absent")
        continue

    attempted_days += 1
    total_score += score

    if not first_attempt_found:
        highest_score = score
        highest_score_day = day

        lowest_score = score
        lowest_score_day = day

        first_attempt_found = True
    else:
        if score > highest_score:
            highest_score = score
            highest_score_day = day

        if score < lowest_score:
            lowest_score = score
            lowest_score_day = day

    if score >= 75 and score <=100:
        strong_days += 1
    elif score >= 60 and score <=74:
        satisfactory_days += 1
    elif score >= 40 and score <=59:
        improvement_days += 1
    else:
        critical_days += 1


    if score >= 60 and score <= 100:
        passed_days += 1
    else:
        failed_days += 1


    if score < 40:
        critical_days += 1

        if not critical_score_found:
            critical_score_found = True
            first_critical_day = day
            first_critical_score = score


if attempted_days > 0:
    average_score = total_score / attempted_days
else:
    average_score = 0

graduation_eligible = (graduation_year >= 2025 and graduation_year <= 2027)

attendance_eligible = attendance >= 75
practice_count_eligible = attempted_days >= 6
average_eligible = average_score >= 70
critical_score_clear = not critical_score_found
passed_days_eligible = passed_days >= 4

placement_ready = (
    graduation_eligible
    and attendance_eligible
    and practice_count_eligible
    and average_eligible
    and critical_score_clear
    and passed_days_eligible
    and project_completed
    and profile_verified
)


if attempted_days == 0:
    final_status = "Not Ready for Mock Interview"
    primary_blocker = "No practice attempted"
    next_action = "Practice for at least 6 days"
    
elif critical_score_found:
    final_status = "Not Ready for Mock Interview"
    primary_blocker = "Critical score found"
    next_action = "Improve critical scores to at least 40"

elif attempted_days < 6:
    final_status = "Not Ready for Mock Interview"
    primary_blocker = "Fewer than six attempts"
    next_action = "Practice for at least 6 days"

elif passed_days < 4:
    final_status = "Not Ready for Mock Interview"
    primary_blocker = "Fewer than four passed days"
    next_action = "Pass at least 4 days"

elif average_score < 70:
    final_status = "Not Ready for Mock Interview"
    primary_blocker = "Average below 70"
    next_action = "Improve average score to at least 70"
    
elif attendance < 75:
    final_status = "Not Ready for Mock Interview"
    primary_blocker = "Attendance below 75%"
    next_action = "Improve attendance to at least 75%"

elif graduation_year < 2025 or graduation_year > 2027:
    final_status = "Not Ready for Mock Interview"
    primary_blocker = "Graduation year not eligible"
    next_action = "Ensure graduation year is between 2025 and 2027"
    
elif not project_completed:
    final_status = "Not Ready for Mock Interview"
    primary_blocker = "Project incomplete"
    next_action = "Complete the required project"
    
elif not profile_verified:
    final_status = "Not Ready for Mock Interview"
    primary_blocker = "Profile not verified"
    next_action = "Verify the student profile"

else:
    final_status = "Ready for Mock Interview"
    primary_blocker = "N/A"
    next_action = "N/A"


print()
print("=" * 50)
print("              PREPTRACK REPORT")
print("=" * 50)

print()
print("STUDENT INFORMATION")
print()

print(f"Student Name           : {student_name}")
print(f"Registration Number    : {registration_number}")
print(f"Graduation Year        : {graduation_year}")
print(f"Attendance             : {attendance}%")
print(f"Project Completed      : {project_completed}")
print(f"Profile Verified       : {profile_verified}")

print()
print("PRACTICE SUMMARY")
print()

print(f"Total Practice Days    : 7")
print(f"Attempted Days         : {attempted_days}")
print(f"Absent Days            : {absent_days}")
print(f"Passed Days            : {passed_days}")
print(f"Failed Days            : {failed_days}")

print()
print(f"Strong Days            : {strong_days}")
print(f"Satisfactory Days      : {satisfactory_days}")
print(f"Needs Improvement Days : {improvement_days}")
print(f"Critical Days          : {critical_days}")

print()
print("PERFORMANCE ANALYSIS")
print()

print(f"Total Score            : {total_score}")
print(f"Average Score          : {average_score:.2f}")
if attempted_days > 0:
    print(f"Highest Score          : {highest_score}")
    print(f"Highest Score Day      : Day {highest_score_day}")
    print(f"Lowest Score           : {lowest_score}")
    print(f"Lowest Score Day       : Day {lowest_score_day}")
else:
    print("No practice attempted yet.")
    highest_score = 0
    lowest_score = 0
    highest_score_day = 0
    lowest_score_day = 0

print()
print("CRITICAL SCORE INFORMATION")
print()

if critical_score_found:
    print(f"Critical Score Found   : Yes")
    print(f"First Critical Day     : Day {first_critical_day}")
    print(f"First Critical Score   : {first_critical_score}")
else:
    print(f"Critical Score Found   : No")
    print(f"First Critical Day     : N/A")
    print(f"First Critical Score   : N/A")

print()
print("FINAL DECISION")
print()

print(f"Final Status           : {final_status}")
print(f"Primary Blocker        : {primary_blocker}")
print(f"Next Action            : {next_action}")

print("=" * 50)