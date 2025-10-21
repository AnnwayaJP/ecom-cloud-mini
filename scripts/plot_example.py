import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/cleaned_dataset.csv')


agg = df.groupby('category')['amount'].sum().sort_values()


ax = agg.plot(kind='bar', title='Spending by Category')
ax.set_xlabel('Category')
ax.set_ylabel('Total Amount')
plt.tight_layout()
plt.savefig('report/category_spending.png')
print("Saved plot to report/category_spending.png")
plt.show()
