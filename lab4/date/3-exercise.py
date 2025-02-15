from datetime import datetime
now=datetime.now()
new_now=now.replace(microsecond=0)
print("Original datetime:", now)
print("Datetime without microseconds:", new_now)