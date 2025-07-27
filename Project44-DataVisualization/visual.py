import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [1200, 1500, 1700, 1600, 1800, 2100]
}
df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="Month", y="Sales", marker="o", linewidth=2.5, color="mediumblue")
plt.title("Monthly Sales Trend", fontsize=14, weight="bold")
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales (USD)", fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
sns.barplot(data=df, x="Month", y="Sales", palette="coolwarm")
plt.title("Monthly Sales Report", fontsize=14, weight="bold")
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales (USD)", fontsize=12)
for index, value in enumerate(df["Sales"]):
    plt.text(index, value + 50, f"${value}", ha='center', fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()

