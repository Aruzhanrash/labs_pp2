from datetime import date,timedelta
today=date.today()
new_date=today-timedelta(days=5)
print("Current time: ", date.today())
print("Substact five days : ",new_date)