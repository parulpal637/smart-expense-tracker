import matplotlib.pyplot as plt
from db import category_data

def pie_chart():
    data = category_data()

    if not data:
        return

    labels = [i[0] for i in data]
    values = [i[1] for i in data]

    plt.figure(figsize=(6,6))
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Expense Distribution")
    plt.show()


def bar_chart():
    data = category_data()

    if not data:
        return

    labels = [i[0] for i in data]
    values = [i[1] for i in data]

    plt.bar(labels, values)
    plt.title("Category-wise Expenses")
    plt.show()