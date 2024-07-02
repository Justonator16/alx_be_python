from datetime import datetime, timedelta

# “YYYY-MM-DD HH:MM:SS”.
def display_current_datetime():
    date = datetime.now()
    current_date = date.strftime("%Y-%m-%d %H:%M:%S")
    return current_date

# “YYYY-MM-DD”
def calculate_future_date():
    add_days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=add_days)
    
    return future_date.strftime("%Y-%m-%d")
