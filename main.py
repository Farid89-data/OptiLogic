# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Generate synthetic data using NumPy
np.random.seed(42)  # Set a seed for reproducibility
num_samples = 500

# Generate random data for a company's sales
days = np.arange(1, num_samples + 1)
sales = np.random.normal(loc=200, scale=50, size=num_samples)  # Normal distribution
ad_spend = np.random.uniform(low=50, high=300, size=num_samples)  # Uniform distribution
promotion_flag = np.random.choice([0, 1], size=num_samples, p=[0.7, 0.3])  # 30% chance of promotion

# Step 2: Create a DataFrame using Pandas
data = pd.DataFrame({
    'Day': days,
    'Sales': sales,
    'AdSpend': ad_spend,
    'Promotion': promotion_flag
})

# Add a column for adjusted sales (sales slightly boosted by promotions)
data['AdjustedSales'] = data['Sales'] + data['Promotion'] * 20

# Step 3: Perform some analysis
# Describe the dataset
print("Dataset Summary:")
print(data.describe())

# Calculate the correlation between AdSpend and AdjustedSales
correlation = data['AdSpend'].corr(data['AdjustedSales'])
print(f"\nCorrelation between AdSpend and AdjustedSales: {correlation:.2f}")

# Step 4: Visualize the data with Matplotlib
# Scatter plot of AdSpend vs AdjustedSales
plt.figure(figsize=(10, 6))
plt.scatter(data['AdSpend'], data['AdjustedSales'], alpha=0.6, c=data['Promotion'], cmap='viridis', edgecolor='k')
plt.colorbar(label='Promotion (0=No, 1=Yes)')
plt.title('Ad Spend vs Adjusted Sales', fontsize=16)
plt.xlabel('Ad Spend ($)', fontsize=12)
plt.ylabel('Adjusted Sales ($)', fontsize=12)
plt.grid(True)
plt.show()

# Time-series plot of sales and adjusted sales over time
plt.figure(figsize=(12, 6))
plt.plot(data['Day'], data['Sales'], label='Sales', alpha=0.7)
plt.plot(data['Day'], data['AdjustedSales'], label='Adjusted Sales', alpha=0.9, linestyle='--')
plt.title('Sales and Adjusted Sales Over Time', fontsize=16)
plt.xlabel('Day', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

# Bar plot: Average sales with and without promotion
avg_sales = data.groupby('Promotion')['AdjustedSales'].mean()
plt.figure(figsize=(8, 5))
avg_sales.plot(kind='bar', color=['blue', 'green'], alpha=0.8)
plt.title('Average Adjusted Sales with and without Promotion', fontsize=16)
plt.xlabel('Promotion (0=No, 1=Yes)', fontsize=12)
plt.ylabel('Average Adjusted Sales ($)', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()