import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# генеруємо дані
n_students = 50
subjects = ['Math', 'Physics', 'History', 'English']
grades = np.random.randint(50, 101, size=(n_students, len(subjects)))

# створюємо DataFrame
df = pd.DataFrame(grades, columns=subjects)
df['Student_ID'] = [f'Student_{i+1}' for i in range(n_students)]
df = df.set_index('Student_ID')

# Статистика по предметах
for subject in subjects:
    print(f"--- {subject} ---")
    print("Середнє:", np.mean(df[subject]))
    print("Медіана:", np.median(df[subject]))
    print("Стандартне відхилення:", np.std(df[subject]))
    print("25-й та 75-й перцентиль:", np.percentile(df[subject], [25,75]))
    print()

# Візуалізація розподілу оцінок по предмету
plt.figure(figsize=(12,6))
plt.hist(df['Math'], bins=10, color='skyblue', edgecolor='black')
plt.title("Розподіл оцінок з математики")
plt.xlabel("Оцінка")
plt.ylabel("Кількість студентів")
plt.show()
