task = input("Enter your task: ")
match_priority = input("Priority (high/medium/low): ")
time= input("Is it time-bound? (yes/no): ")

if match_priority == "high":
    print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
elif match_priority == "low":
    print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
elif match_priority == "medium":
    print(f"Note: '{task}' is a medium priority task. Consider completing it after a high priority.")
else:
    print("Invalid level please use (high/medium/low)")
    