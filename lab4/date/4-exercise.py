from datetime import datetime, timedelta
now = datetime.now()
yesterday = now - timedelta(days=1)
tomorrow = now + timedelta(days=1)
yesterday_seconds = yesterday.timestamp()
tomorrow_seconds = tomorrow.timestamp()
print(tomorrow_seconds - yesterday_seconds)
