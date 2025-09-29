import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\hp\Desktop\numpy_pandas_projects\russia_losses_equipment.csv")

# конвертація дати
data['date'] = pd.to_datetime(data['date'], errors='coerce')

# заповнення пропусків
data = data.fillna(0)

print(data.columns.tolist())
categories = [
    'tank', 'APC', 'field artillery', 'MRL',
    'military auto', 'fuel tank', 'drone',
    'naval ship', 'anti-aircraft warfare',
    'special equipment', 'mobile SRBM system',
    'vehicles and fuel tanks', 'cruise missiles',
    'submarines'
]

total_losses = data[categories].iloc[-1]

# будуємо гістограму
total_losses.sort_values(ascending=False).plot(
    kind='bar', figsize=(12,6), color='tomato'
)
plt.title("Сумарні втрати РФ по категоріях техніки")
plt.ylabel("Кількість одиниць")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


