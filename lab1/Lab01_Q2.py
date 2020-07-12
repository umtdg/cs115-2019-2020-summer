import datetime

current_time = datetime.datetime.now()
# Default year for datetime.strptime is 1900, to fix that year added manually
# to input. This fix is bad practice, however, trying to parse input manually
# is even worse.
exam_date = datetime.datetime.strptime(
    input("Enter exam date (dd/mm): ") + f"/{current_time.year}",
    "%d/%m/%Y"
)

if current_time > exam_date:
    print("Exam finished.")
else:
    # diff = exam_date - current_time # won't give month difference
    month_diff = exam_date.month - current_time.month
    day_diff = exam_date.day - current_time.day
    if month_diff > 0:
        print(f"{month_diff} months until the exam")
    else:
        print(f"{day_diff} days until the exam")
