from datetime import datetime, timedelta

# “YYYY-MM-DD HH:MM:SS”.
def display_current_datetime():
    current_date = datetime.now()
    return current_date

# “YYYY-MM-DD”
def calculate_future_date():
    add_days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.date() + timedelta(days=add_days)
    
    return future_date
