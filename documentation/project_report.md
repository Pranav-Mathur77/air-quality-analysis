# 🌍 Air Quality Data Analysis & Pollution Trend Modelling (India)
### Delhi Focus + Mumbai Comparison | 2015–2020

**Author:** Malik  
**Degree:** M.E. Environmental Engineering, MBM University Jodhpur  
**Tools:** Python, Pandas, NumPy, Matplotlib, Scikit-learn

---

## 1. Introduction

Air pollution is one of the most critical environmental challenges in India. The Air Quality Index (AQI) is a standardised measure used by CPCB to communicate daily air quality levels and their potential health impacts.

This project analyses real-world air quality data from Indian cities using Python. Delhi is the primary case study, with Mumbai for comparison, covering the period 2015–2020.

---

## 2. Objectives

- Analyse AQI trends over time for Delhi
- Identify seasonal and monthly pollution patterns
- Compare air quality between Delhi and Mumbai
- Classify AQI into standard health categories
- Apply rolling average smoothing for trend modelling
- Build a linear regression model to determine pollution trend direction

---

## 3. Dataset

| Attribute | Details |
|---|---|
| Source | Kaggle / CPCB India |
| File | city_day.csv |
| Total Records (raw) | 29,531 |
| After Cleaning | 24,850 |
| Delhi Records | 1,999 |
| Mumbai Records | 775 |
| Time Period | 2015–2020 |
| Columns | 16 |

---

## 4. Tools Used

| Library | Purpose |
|---|---|
| Python 3.13 | Core language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Visualisation |
| Scikit-learn | Linear regression |
| OpenPyXL | Excel export |

---

## 5. Key Results

### Monthly AQI – Delhi
- Most polluted month: **November (AQI: 402)**
- Least polluted month: **August (AQI: 134)**
- Winter months (Nov–Jan) consistently highest
- Monsoon months (Jul–Aug) consistently lowest

### City Comparison
- **Delhi Avg AQI: 259.5** (Poor category)
- **Mumbai Avg AQI: 105.4** (Moderate category)
- Delhi is **146.3% more polluted** than Mumbai

### Linear Trend
- Slope: **-0.057** → AQI slowly decreasing (slight improvement)

### AQI Category Distribution
| Category | % of Days |
|---|---|
| Good | 5.40% |
| Satisfactory | 33.09% |
| Moderate | 35.53% |
| Poor | 11.19% |
| Very Poor | 9.40% |
| Severe | 5.38% |

---

## 6. Graphs

| File | Description |
|---|---|
| monthly_aqi_delhi.png | Monthly average AQI – Delhi |
| trend_delhi.png | Actual vs 30-day rolling average |
| mumbai_monthly.png | Monthly average AQI – Mumbai |
| city_comparison.png | Delhi vs Mumbai comparison |
| aqi_distribution.png | AQI category distribution |
| linear_trend_delhi.png | Linear regression trend line |
| yearly_trend.png | Year-wise AQI trend |
| heatmap.png | Month × Year AQI heatmap |
| season_analysis.png | Season-wise AQI |

---

## 7. Conclusion

This project demonstrates Python-based data analytics applied to real environmental data. Delhi's AQI of 259.5 places it in the Poor category while Mumbai's coastal location helps maintain a moderate 105.4. A slight improvement trend is observed but pollution levels remain dangerously high, especially in winter months.

---

## 8. References

- CPCB India: cpcb.nic.in
- Kaggle Dataset: kaggle.com/datasets/rohanrao/air-quality-data-in-india
- Pandas: pandas.pydata.org
