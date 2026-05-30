---
title: "Retail Customer Shopping Trends Analysis"
date: 2026-03-09
tags:
  - python
  - sql
  - machine-learning
  - data-analysis
  - linux
  - job-search
  - research
  - projects
  - finance
  - game-design
source: qwen-export
model: qwen3.5-plus
---

# Retail Customer Shopping Trends Analysis

**Date:** 2026-03-09  
**Model:** `qwen3.5-plus`  
**Topics:** [[Python]] · [[SQL]] · [[Machine-Learning]] · [[Data-Analysis]] · [[Linux]] · [[Job-Search]] · [[Research]] · [[Projects]] · [[Finance]] · [[Game-Design]]

---

### 🧑 You

# Step-by-Step Prompts for Retail Customer Shopping Trends Analysis

## Phase 1: Setup & Data Loading
1. **Install required libraries**  
   `pip install pandas numpy matplotlib seaborn jupyter sqlite3`

2. **Download dataset**  
   Get CSV from [Kaggle](https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset  ) and save as `shopping_trends.csv` in your project folder.

3. **Create a new Jupyter Notebook** and import libraries  
   ```python
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   import seaborn as sns
   import sqlite3
   ```

4. **Load the data**  
   ```python
   df = pd.read_csv('shopping_trends.csv')
   ```

5. **Initial inspection**  
   ```python
   print(df.info())
   print(df.head())
   print(df.describe())
   print(df.isnull().sum())
   ```

## Phase 2: EDA & Feature Engineering
6. **Check and remove duplicates**  
   ```python
   print(df.duplicated().sum())
   # df = df.drop_duplicates()  # if duplicates exist
   ```

7. **Examine categorical columns**  
   ```python
   print(df['Category'].unique())
   print(df['Payment Method'].unique())
   print(df['Frequency of Purchases'].unique())
   ```

8. **Create customer value segments**  
   ```python
   high_spend_threshold = df['Purchase Amount (USD)'].quantile(0.75)
   df['Is_High_Spender'] = df['Purchase Amount (USD)'] >= high_spend_threshold

   loyal_threshold = df['Previous Purchases'].quantile(0.75)
   df['Is_Loyal'] = df['Previous Purchases'] >= loyal_threshold

   conditions = [
       (df['Is_High_Spender'] == True) & (df['Is_Loyal'] == True),
       (df['Is_High_Spender'] == True) | (df['Is_Loyal'] == True),
       (df['Is_High_Spender'] == False) & (df['Is_Loyal'] == False)
   ]
   choices = ['Champion', 'Potential', 'At Risk']
   df['Customer_Value_Segment'] = np.select(conditions, choices, default='Other')
   ```

9. **Create visualizations**  
   ```python
   sns.set_style("whitegrid")
   fig, axes = plt.subplots(2, 2, figsize=(14, 10))

   sns.histplot(df['Purchase Amount (USD)'], bins=30, kde=True, ax=axes[0,0])
   axes[0,0].set_title('Distribution of Purchase Amounts')

   category_sales = df.groupby('Category')['Purchase Amount (USD)'].sum().sort_values(ascending=False)
   sns.barplot(x=category_sales.values, y=category_sales.index, ax=axes[0,1], palette='viridis')
   axes[0,1].set_title('Total Sales by Category')

   avg_rating = df.groupby('Category')['Review Rating'].mean().sort_values(ascending=False)
   sns.barplot(x=avg_rating.values, y=avg_rating.index, ax=axes[1,0], palette='magma')
   axes[1,0].set_title('Average Review Rating by Category')

   sns.boxplot(x='Discount Applied', y='Purchase Amount (USD)', data=df, ax=axes[1,1])
   axes[1,1].set_title('Purchase Amount with/without Discount')

   plt.tight_layout()
   plt.savefig('eda_plots.png', dpi=300)
   plt.show()
   ```

## Phase 3: Business Impact Analysis – Churn & Revenue Loss
10. **Create churn risk score**  
    ```python
    df['Churn_Risk_Score'] = 0
    df.loc[df['Review Rating'] < 3.0, 'Churn_Risk_Score'] += 3
    df.loc[(df['Review Rating'] >= 3.0) & (df['Review Rating'] < 4.0), 'Churn_Risk_Score'] += 1
    df.loc[df['Subscription Status'] == 'No', 'Churn_Risk_Score'] += 2

    high_risk_freq = ['Annually', 'Every 3 Months']
    medium_risk_freq = ['Quarterly']
    df.loc[df['Frequency of Purchases'].isin(high_risk_freq), 'Churn_Risk_Score'] += 3
    df.loc[df['Frequency of Purchases'].isin(medium_risk_freq), 'Churn_Risk_Score'] += 1
    ```

11. **Normalize risk score**  
    ```python
    max_score = df['Churn_Risk_Score'].max()
    df['Churn_Risk_Normalized'] = (df['Churn_Risk_Score'] / max_score) * 10
    ```

12. **Define risk categories**  
    ```python
    risk_conditions = [
        (df['Churn_Risk_Normalized'] >= 7),
        (df['Churn_Risk_Normalized'] >= 4) & (df['Churn_Risk_Normalized'] < 7),
        (df['Churn_Risk_Normalized'] < 4)
    ]
    risk_labels = ['High Risk', 'Medium Risk', 'Low Risk']
    df['Churn_Risk_Category'] = np.select(risk_conditions, risk_labels, default='Medium Risk')
    ```

13. **Assign churn probabilities**  
    ```python
    risk_prob_map = {'High Risk': 0.7, 'Medium Risk': 0.3, 'Low Risk': 0.05}
    df['Churn_Probability'] = df['Churn_Risk_Category'].map(risk_prob_map)
    ```

14. **Calculate potential revenue loss**  
    ```python
    df['Potential_Revenue_Loss'] = df['Purchase Amount (USD)'] * df['Churn_Probability']
    total_potential_loss = df['Potential_Revenue_Loss'].sum()
    print(f"Total Potential Revenue Loss: ${total_potential_loss:,.2f}")
    ```

15. **Visualize loss by risk category**  
    ```python
    plt.figure(figsize=(10,6))
    loss_by_risk = df.groupby('Churn_Risk_Category')['Potential_Revenue_Loss'].sum()
    sns.barplot(x=loss_by_risk.index, y=loss_by_risk.values, palette=['red', 'orange', 'green'])
    plt.title('Total Potential Revenue Loss by Churn Risk Category')
    plt.ylabel('Potential Loss (USD)')
    plt.xlabel('Churn Risk')
    plt.tight_layout()
    plt.savefig('revenue_loss_by_risk.png')
    plt.show()
    ```

## Phase 4: Load Data into SQL Database
16. **Save enhanced data to CSV**  
    ```python
    df.to_csv('shopping_trends_enhanced.csv', index=False)
    ```

17. **Connect to SQLite database**  
    ```python
    conn = sqlite3.connect('retail_analytics.db')
    ```

18. **Load DataFrame into SQL table**  
    ```python
    df.to_sql('customer_shopping', conn, if_exists='replace', index=False)
    ```

19. **Verify data load**  
    ```python
    pd.read_sql_query("SELECT * FROM customer_shopping LIMIT 5;", conn)
    ```

## Phase 5: Answer Business Questions with SQL
20. **Run the following queries using `pd.read_sql_query()` and print results**  

    **Query 1: Most profitable customer segments**  
    ```sql
    SELECT 
        Customer_Value_Segment,
        COUNT(*) as Customer_Count,
        ROUND(AVG("Purchase Amount (USD)"), 2) as Avg_Purchase,
        ROUND(SUM("Purchase Amount (USD)"), 2) as Total_Revenue
    FROM customer_shopping
    GROUP BY Customer_Value_Segment
    ORDER BY Total_Revenue DESC;
    ```

    **Query 2: Revenue at risk by category and risk level**  
    ```sql
    SELECT 
        Category,
        Churn_Risk_Category,
        COUNT(*) as Customer_Count,
        ROUND(SUM("Purchase Amount (USD)"), 2) as Current_Revenue,
        ROUND(SUM(Potential_Revenue_Loss), 2) as At_Risk_Revenue
    FROM customer_shopping
    WHERE Churn_Risk_Category IN ('High Risk', 'Medium Risk')
    GROUP BY Category, Churn_Risk_Category
    ORDER BY At_Risk_Revenue DESC;
    ```

    **Query 3: Impact of discounts and promo codes**  
    ```sql
    SELECT 
        "Discount Applied",
        "Promo Code Used",
        COUNT(*) as Transaction_Count,
        ROUND(AVG("Purchase Amount (USD)"), 2) as Avg_Spend,
        ROUND(AVG("Review Rating"), 2) as Avg_Rating
    FROM customer_shopping
    GROUP BY "Discount Applied", "Promo Code Used"
    ORDER BY Avg_Spend DESC;
    ```

    **Query 4: Locations with highest % of high-risk customers**  
    ```sql
    SELECT 
        Location,
        COUNT(*) as Total_Customers,
        SUM(CASE WHEN Churn_Risk_Category = 'High Risk' THEN 1 ELSE 0 END) as High_Risk_Count,
        ROUND(100.0 * SUM(CASE WHEN Churn_Risk_Category = 'High Risk' THEN 1 ELSE 0 END) / COUNT(*), 2) as High_Risk_Percentage,
        ROUND(SUM(Potential_Revenue_Loss), 2) as Total_At_Risk_Revenue
    FROM customer_shopping
    GROUP BY Location
    HAVING Total_Customers > 10
    ORDER BY High_Risk_Percentage DESC
    LIMIT 10;
    ```

    **Query 5: Seasonal revenue with churn risk overlay**  
    ```sql
    SELECT 
        Season,
        Churn_Risk_Category,
        COUNT(*) as Transactions,
        ROUND(SUM("Purchase Amount (USD)"), 2) as Revenue,
        ROUND(AVG("Review Rating"), 2) as Avg_Rating
    FROM customer_shopping
    GROUP BY Season, Churn_Risk_Category
    ORDER BY 
        CASE Season
            WHEN 'Spring' THEN 1
            WHEN 'Summer' THEN 2
            WHEN 'Fall' THEN 3
            WHEN 'Winter' THEN 4
            ELSE 5
        END, Revenue DESC;
    ```

## Phase 6: Build Power BI Dashboard
21. **Connect Power BI to data source**  
    - Open Power BI Desktop → Get Data → SQLite database (or import CSV).

22. **Create DAX measures**  
    - `Total Revenue = SUM(customer_shopping[Purchase Amount (USD)])`  
    - `At Risk Revenue = SUM(customer_shopping[Potential_Revenue_Loss])`  
    - `Avg Churn Risk = AVERAGE(customer_shopping[Churn_Risk_Normalized])`  
    - `High Risk Customers = CALCULATE(COUNTROWS(customer_shopping), customer_shopping[Churn_Risk_Category] = "High Risk")`

23. **Design dashboard pages**  
    - **Page 1 – Executive Summary**: KPI cards (Revenue, At-Risk Revenue, Avg Rating), donut chart of revenue by segment, bar chart of revenue by category, line chart (seasonal trend if available).  
    - **Page 2 – Churn & Risk Analysis**: Gauge of avg churn risk, stacked bar of risk category by subscription status, table of high-risk customers, map of high-risk locations.  
    - **Page 3 – Product & Promotion Performance**: Scatter plot (rating vs. spend by category), matrix of avg spend by category and season, clustered bar of discount/promo impact.

24. **Add interactivity and polish**  
    - Add slicers for `Category`, `Season`, `Location`, `Gender`.  
    - Apply a consistent color theme (red=high risk, green=low risk).  
    - Include titles, logos, and explanatory text.

## Phase 7: Document and Share
25. **Create GitHub repository**  
    - Add `README.md` with: project objective, business problem, data source, tools used, key insights, and screenshots of dashboard.  
    - Upload: Python script (`.ipynb` or `.py`), SQL queries file (`.sql`), Power BI file (`.pbix`).

26. **Share on LinkedIn / X**  
    - Write a post focusing on business impact (e.g., "Identified $XXX,XXX potential revenue loss from high-risk customers and built an interactive dashboard to track it.")  
    - Include screenshots and link to GitHub.

---
