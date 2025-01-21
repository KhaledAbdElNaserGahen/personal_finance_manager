# app/services/data_visualization.py

import matplotlib.pyplot as plt
import pandas as pd

def visualize_expenses():
    from ..models.database import get_transactions
    transactions = get_transactions()
    df = pd.DataFrame(transactions, columns=["amount", "category", "description", "date"])
    plt.figure(figsize=(10, 6))
    df.groupby('category').sum().plot(kind='bar', legend=False)
    plt.title('Total Expenses by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.show()