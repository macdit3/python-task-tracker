# daily_todo_list_tracker.py
'''
The daily ToDo List tracker program helps users to track daily tasks and 
rewards them with encouraging messages based on their progress.
'''

# Prompt the user for their full name
full_name = input("Enter your full name: ")

# Initialize tasks
total_tasks = 5
completed_tasks = 0

# Check daily progress
# Task 1
task1_status = input("Did you complete your 30 minutes gym exercise? (yes/no): ")
if task1_status.lower() == 'yes':
    completed_tasks += 1

# Task 2
task2_status = input("Did you have breakfast this morning? (yes/no): ")
if task2_status.lower() == 'yes':
    completed_tasks += 1

# Task 3
task3_status = input("Did you complete your homework & study? (yes/no): ")
if task3_status.lower() == 'yes':
    completed_tasks += 1

# Task 4
task4_status = input("Did you have a healthy launch this afternoon? (yes/no): ")
if task4_status.lower() == 'yes':
    completed_tasks += 1

# Task 3
task5_status = input("Did you have a healthy dinner this evening? (yes/no): ")
if task5_status.lower() == 'yes':
    completed_tasks += 1


# Calculate progress
progress_percentage = (completed_tasks / total_tasks) * 100

# Provide feedback
if progress_percentage == 100:
    print(f"Amazing job {full_name}! You've completed all tasks!")
elif progress_percentage >= 50:
    print(f"Keep going {full_name}! You're more than halfway there!")
else:
    print(f"You can do it {full_name}! Every step counts!")