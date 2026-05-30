---
title: "Retail Shopping Trends Analysis"
date: 2026-03-09
tags:
  - python
  - sql
  - machine-learning
  - data-analysis
  - linux
  - obsidian
  - geopolitics
  - research
source: qwen-export
model: qwen3.5-plus
---

# Retail Shopping Trends Analysis

**Date:** 2026-03-09  
**Model:** `qwen3.5-plus`  
**Topics:** [[Python]] · [[SQL]] · [[Machine-Learning]] · [[Data-Analysis]] · [[Linux]] · [[Obsidian]] · [[Geopolitics]] · [[Research]]

---

### 🧑 You

pip install pandas numpy matplotlib seaborn jupyter sqlite3 powerbi-visuals-tools

---

### 🧑 You

# Phase 1: Setup & Data Loading

# Import essential libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import warnings
from datetime import datetime
warnings.filterwarnings('ignore')

# Set style for visualizations
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("🚀 Retail Customer Shopping Trends Analysis - Start")
print(f"📅 Analysis Date: {datetime.now().strftime('%d-%m-%Y')}")

---

### 🧑 You

pip install pandas numpy matplotlib seaborn jupyter sqlite3 powerbi-visuals-tools
# Phase 1: Setup & Data Loading

# Import essential libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import warnings
from datetime import datetime
warnings.filterwarnings('ignore')

# Set style for visualizations
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("🚀 Retail Customer Shopping Trends Analysis - Start")
print(f"📅 Analysis Date: {datetime.now().strftime('%d-%m-%Y')}")

---

### 🧑 You

# Generate realistic retail dataset (3,900 rows as per Kaggle dataset)
np.random.seed(42)

def generate_retail_data():
    # Customer demographics
    customer_ids = range(1, 3901)
    ages = np.random.randint(18, 65, 3900)
    genders = np.random.choice(['Male', 'Female'], 3900, p=[0.52, 0.48])
    
    # Customer segments
    segments = np.random.choice(['Loyal', 'Potential', 'At-Risk', 'Lost'], 
                               3900, p=[0.45, 0.25, 0.20, 0.10])
    
    # Purchase behavior (in INR)
    purchase_amounts = np.random.exponential(2000, 3900) + 500
    purchase_frequencies = np.random.poisson(3, 3900) + 1
    
    # Indian payment methods
    payment_methods = np.random.choice(['Credit Card', 'Debit Card', 'UPI', 'Cash', 'Paytm', 'PhonePe'], 
                                     3900, p=[0.25, 0.20, 0.35, 0.08, 0.08, 0.04])
    
    # Product categories
    categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books', 
                  'Beauty', 'Food', 'Toys', 'Automotive', 'Health']
    categories = np.random.choice(categories, 3900)
    
    # Discount usage
    used_discounts = np.random.choice([0, 1], 3900, p=[0.35, 0.65])
    
    # Shipping preferences
    shipping = np.random.choice(['Standard', 'Express', 'Same-Day'], 3900, p=[0.60, 0.30, 0.10])
    
    # Time of purchase (months)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    purchase_month = np.random.choice(months, 3900)
    
    # Create DataFrame
    data = pd.DataFrame({
        'CustomerID': customer_ids,
        'Age': ages,
        'Gender': genders,
        'CustomerSegment': segments,
        'PurchaseAmount': purchase_amounts,
        'PurchaseFrequency': purchase_frequencies,
        'PaymentMethod': payment_methods,
        'ProductCategory': categories,
        'UsedDiscount': used_discounts,
        'ShippingPreference': shipping,
        'PurchaseMonth': purchase_month
    })
    
    return data

# Generate and save dataset
print("📊 Generating retail dataset...")
retail_data = generate_retail_data()
retail_data.to_csv('retail_customer_data.csv', index=False)
print(f"✅ Dataset generated with {len(retail_data)} records")# Load the dataset
df = pd.read_csv('retail_customer_data.csv')

print("\n🔍 Dataset Overview:")
print(f"\n📋 Dataset Shape: {df.shape}")
print(f"\n📊 Data Information:")
df.info()

print("\n📈 First 5 Rows:")
print(df.head())

print("\n📝 Statistical Summary:")
print(df.describe())

print("\n❓ Missing Values:")
print(df.isnull().sum())

print("\n🎯 Unique Values in Categorical Columns:")
print(f"CustomerSegment: {df['CustomerSegment'].unique()}")
print(f"PaymentMethod: {df['PaymentMethod'].unique()}")
print(f"ProductCategory: {df['ProductCategory'].unique()}")
print(f"ShippingPreference: {df['ShippingPreference'].unique()}")

---

### 🧑 You

print(f"\n🔄 Duplicate Records: {df.duplicated().sum()}")
# df = df.drop_duplicates()  # if duplicates exist
# Create customer value segments
print("\n💰 Creating Customer Value Segments...")

high_spend_threshold = df['PurchaseAmount'].quantile(0.75)
df['Is_High_Spender'] = df['PurchaseAmount'] >= high_spend_threshold

loyal_threshold = df['PurchaseFrequency'].quantile(0.75)
df['Is_Loyal'] = df['PurchaseFrequency'] >= loyal_threshold

# Create RFM-style customer segments based on Indian retail context
conditions = [
    (df['Is_High_Spender'] == True) & (df['Is_Loyal'] == True),
    (df['Is_High_Spender'] == True) | (df['Is_Loyal'] == True),
    (df['Is_High_Spender'] == False) & (df['Is_Loyal'] == False),
    (df['Is_Loyal'] == True) & (df['Is_High_Spender'] == False),
    (df['Is_Loyal'] == False) & (df['Is_High_Spender'] == True)
]
choices = ['Champion', 'Potential', 'At Risk', 'Loyal Regular', 'Occasional Buyer']
df['Customer_Value_Segment'] = np.select(conditions, choices, default='New Customer')

print("✅ Customer segments created:")
print(df['Customer_Value_Segment'].value_counts())

---
