#  Sales Data Analysis using Python & Pandas

##  Objective
The goal of this project is to analyze sales data using **Python** and **Pandas** to extract key insights such as:
- Total sales per region
- Most sold products
- Sales trends over time

---

##  Tools & Libraries
- **Python 3**
- **Pandas** — for data manipulation  
- **Matplotlib** & **Seaborn** — for data visualization  
- **Jupyter Notebook / Google Colab** — for running the analysis

---

##  Dataset
**File:** `sales.csv`

| Date | Region | Product | Quantity | Sales |
|------|---------|----------|-----------|--------|
| 2024-01-01 | East | Shoes | 10 | 2500 |
| 2024-01-02 | West | Shirt | 5 | 1200 |
| 2024-01-03 | North | Watch | 7 | 3200 |
| ... | ... | ... | ... | ... |

###  Dataset Description:
- **Date:** Date of sale  
- **Region:** Sales region (East, West, North, South)  
- **Product:** Product category sold  
- **Quantity:** Number of items sold  
- **Sales:** Total sales value in INR  

---

##  Steps Performed
1. **Load the dataset** using `pandas.read_csv()`
2. **Inspect the data** — check for missing values, data types, and summary stats
3. **Group and aggregate data** using `groupby()` and `sum()`
4. **Visualize data** using `matplotlib` and `seaborn`
5. **Interpret insights** like:
   - Highest selling region
   - Most popular product
   - Sales trend over time

---

##  Visualizations
- Bar chart of **Total Sales by Region**
- Bar chart of **Total Sales by Product**
- Line chart of **Daily Sales Trend**

---

##  Sample Insights
- **East Region** had the highest total sales.  
- **Shoes** were the most sold product.  
- Sales showed a steady **upward trend** through January.

---

##  Outcome
By completing this project, you will:
- Learn how to handle CSV files in Python  
- Use `groupby()` and aggregation functions in Pandas  
- Create clear and meaningful visualizations  
- Gain practical experience in data analysis

---

##  Deliverables
- `sales.csv` — dataset  
- `sales_analysis.ipynb` — notebook containing code and charts  
- `README.md` — project documentation

---
