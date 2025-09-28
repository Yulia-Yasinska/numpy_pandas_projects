import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

data = pd.read_csv(r"C:\Users\hp\Desktop\проєкт\russia_ukraine_conflict.csv")
print(data.head())

# колонки та типи даних
print(data.info())

# статистика
print(data.describe())

# перевірка на пропуски
print(data.isnull().sum())

# перегляд унікальних значень
print(data['disorder_type'].value_counts())
print(data['source_scale'].value_counts())

data['event_date'] = pd.to_datetime(data['event_date'], errors='coerce')

# групування по місяцях та сумування втрат
monthly_events = data.set_index('event_date')['fatalities'].resample('M').sum()

# побудова графіка
fig, ax = plt.subplots(figsize=(12,6))
ax.plot(monthly_events.index, monthly_events.values, color='red', marker='o')

# форматування осі X: щомісячні підписи
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

plt.xticks(rotation=45)
plt.xlabel("Місяць")
plt.ylabel("Втрати")
plt.title("Втрати по місяцях")
plt.grid(True)
plt.tight_layout()
plt.show()