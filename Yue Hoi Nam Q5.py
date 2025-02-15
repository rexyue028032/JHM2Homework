import pandas as pd
import matplotlib.pyplot as plt
data = {
  'Months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'sep', 'Oct', 'Nov', 'Dec'], 
  'Sales': [380, 400, 660, 800, 900, 1200, 1600, 2200, 1500, 1100, 600, 250]
}
df = pd.DataFrame(data)
filename = 'sales.csv'
data = pd.read_csv('sales.csv')
print(df)
months = data['Month']
sales = data['Sales']
plt.figure(figsize=(10,6))
plt.bar(months, sales, color='green', width=0.5)
plt.title('Bar Chart of Ice-cream Sales')
plt.xlabel('Month')
plt.ylabel('Sales (in thousand dollars)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()