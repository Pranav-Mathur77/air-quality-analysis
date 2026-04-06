# ==========================================
# 🌍 Air Quality Data Analysis Project
# Delhi Focus + Mumbai Comparison (Advanced)
# ==========================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import calendar
from sklearn.linear_model import LinearRegression


# ==========================================
# 1. Load Dataset
# ==========================================
df = pd.read_csv("city_day.csv")

print("Dataset Shape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())


# ==========================================
# 2. Data Cleaning
# ==========================================
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df = df.dropna(subset=['AQI'])

print("\nShape after cleaning:", df.shape)


# ==========================================
# 3. Delhi Data Preparation
# ==========================================
delhi_df = df[df['City'] == 'Delhi'].copy()
delhi_df = delhi_df.sort_values(by='Date').reset_index(drop=True)

delhi_df['Year'] = delhi_df['Date'].dt.year
delhi_df['Month'] = delhi_df['Date'].dt.month


# ==========================================
# 4. Monthly AQI Analysis (Delhi)
# ==========================================
monthly_aqi = delhi_df.groupby('Month')['AQI'].mean()
monthly_aqi.index = monthly_aqi.index.map(lambda x: calendar.month_name[x])

monthly_aqi.plot(kind='bar')
plt.title("Monthly Average AQI in Delhi (2015–2020)")
plt.xlabel("Month")
plt.ylabel("Average AQI")
plt.xticks(rotation=45)
plt.show()


# ==========================================
# 5. Rolling Trend (Delhi)
# ==========================================
delhi_df['Rolling_AQI'] = delhi_df['AQI'].rolling(window=30).mean()

plt.figure(figsize=(12,5))
plt.plot(delhi_df['Date'], delhi_df['AQI'], label='Actual AQI', alpha=0.4)
plt.plot(delhi_df['Date'], delhi_df['Rolling_AQI'], label='30-Day Avg', linewidth=2)

plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

plt.title("AQI Trend in Delhi (2015–2020)")
plt.xlabel("Year")
plt.ylabel("AQI")
plt.legend()
plt.show()


# ==========================================
# 6. Mumbai Analysis (Basic)
# ==========================================
mumbai_df = df[df['City'] == 'Mumbai']

mumbai_monthly = mumbai_df.groupby(mumbai_df['Date'].dt.month)['AQI'].mean()
mumbai_monthly.index = mumbai_monthly.index.map(lambda x: calendar.month_name[x])

mumbai_monthly.plot(kind='bar')
plt.title("Monthly AQI in Mumbai")
plt.xlabel("Month")
plt.ylabel("AQI")
plt.xticks(rotation=45)
plt.show()


# ==========================================
# 7. City Comparison
# ==========================================
city_aqi = df[df['City'].isin(['Delhi', 'Mumbai'])].groupby('City')['AQI'].mean()

plt.figure(figsize=(8,5))
ax = city_aqi.plot(kind='bar')

for i, value in enumerate(city_aqi):
    plt.text(i, value + 5, f"{round(value,1)}", ha='center', fontweight='bold')

plt.title("Average AQI Comparison: Delhi vs Mumbai (2015–2020)")
plt.xlabel("City")
plt.ylabel("Average AQI")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# ==========================================
# 8. AQI Category Classification
# ==========================================
def classify_aqi(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Satisfactory"
    elif aqi <= 200:
        return "Moderate"
    elif aqi <= 300:
        return "Poor"
    elif aqi <= 400:
        return "Very Poor"
    else:
        return "Severe"

df['AQI_Category'] = df['AQI'].apply(classify_aqi)

aqi_counts = df['AQI_Category'].value_counts()

aqi_counts.plot(kind='bar')
plt.title("AQI Category Distribution (India)")
plt.xlabel("AQI Category")
plt.ylabel("Number of Days")
plt.show()


# ==========================================
# 9. Linear Trend Model (Delhi)
# ==========================================
delhi_df['Days'] = (delhi_df['Date'] - delhi_df['Date'].min()).dt.days

X = delhi_df[['Days']]
y = delhi_df['AQI']

model = LinearRegression()
model.fit(X, y)

trend = model.predict(X)

print("\nSlope (Trend):", model.coef_[0])

plt.plot(delhi_df['Date'], delhi_df['AQI'], label="Actual", alpha=0.4)
plt.plot(delhi_df['Date'], trend, label="Trend Line", linestyle='--')

plt.title("AQI Trend Line in Delhi")
plt.xlabel("Date")
plt.ylabel("AQI")
plt.legend()
plt.show()


# ==========================================
# 10. Advanced Analysis
# ==========================================

# Year-wise trend
yearly_aqi = delhi_df.groupby('Year')['AQI'].mean()

yearly_aqi.plot(marker='o')
plt.title("Year-wise AQI Trend in Delhi")
plt.xlabel("Year")
plt.ylabel("AQI")
plt.grid()
plt.show()


# Heatmap
pivot_table = delhi_df.pivot_table(values='AQI', index='Month', columns='Year', aggfunc='mean')

plt.imshow(pivot_table, aspect='auto')
plt.colorbar(label='AQI')

plt.title("AQI Heatmap (Month vs Year)")
plt.xlabel("Year")
plt.ylabel("Month")

plt.yticks(range(12), range(1,13))
plt.xticks(range(len(pivot_table.columns)), pivot_table.columns, rotation=45)
plt.show()


# Top polluted days
top_pollution = delhi_df.sort_values(by='AQI', ascending=False).head(10)
print("\nTop 10 Most Polluted Days:\n", top_pollution[['Date', 'AQI']])


# AQI percentage
aqi_percent = (aqi_counts / aqi_counts.sum()) * 100
print("\nAQI Category Percentage:\n", aqi_percent)


# Correlation
corr = df[['PM2.5','PM10','NO2','SO2','CO','O3','AQI']].corr()
print("\nCorrelation Matrix:\n", corr)


# Season-wise analysis
delhi_df['Season'] = delhi_df['Month'].apply(
    lambda x: 'Winter' if x in [11,12,1] else
              'Summer' if x in [4,5,6] else
              'Monsoon' if x in [7,8,9] else
              'Post-Monsoon'
)

season_aqi = delhi_df.groupby('Season')['AQI'].mean()

season_aqi.plot(kind='bar')
plt.title("Season-wise AQI in Delhi")
plt.show()


# ==========================================
# 11. Export Report
# ==========================================
delhi_df.to_excel("Delhi_AQI_Final_Report.xlsx", index=False)

print("\n✅ Project Completed Successfully!")