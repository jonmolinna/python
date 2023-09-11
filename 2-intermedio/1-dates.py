# Date
from datetime import datetime, time, date, timedelta

now = datetime.now()
print(now.year)
print(now.month)
print(now.day)

timestamp = now.timestamp()
print(timestamp)

# Creando una fecha
year_2024 = datetime(2024, 1, 1)
print(year_2024.year)
print(year_2024.month)
print(year_2024.day)
print(year_2024.timestamp())

# Metodo Time
current_time = time(21, 6, 0)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Metodo Date
currente_date = date(2023, 9, 11)
print(currente_date.year)
print(currente_date.month)
print(currente_date.day)

# Metodo TimeDelta
star_delta = timedelta(200, 100, 100, weeks=10)
end_delta = timedelta(300, 100, 100, weeks=13)
print(end_delta - star_delta)
