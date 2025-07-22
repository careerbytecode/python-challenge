import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

months = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
sales = np.array([200, 220, 250, 270, 300, 320])

model = LinearRegression()
model.fit(months, sales)

future_months = np.array([7, 8, 9]).reshape(-1, 1)
predicted_sales = model.predict(future_months)

for month, prediction in zip(future_months.flatten(), predicted_sales):
    print(f"Predicted sales for month {month}: ${int(prediction)}")

plt.scatter(months, sales, color='blue', label='Actual Sales')
plt.plot(np.vstack((months, future_months)), model.predict(np.vstack((months, future_months))), color='green', label='Regression Line')
plt.scatter(future_months, predicted_sales, color='red', label='Predicted Sales')
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Sales Forecast with Linear Regression")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
