import pandas as pd
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="omkarmahalkar45",
    database="newdb1"
)

cursor = conn.cursor()

df = pd.read_csv(r"C:\Users\Omkar\Downloads\indian_ecommerce_pricing_revenue_growth_36_months.csv")
print("Head")
print(df.head())

print("Describe")
print(df.describe())

print("Info")
print(df.info())

print("Checking for null values")
print(df.isnull().sum())

print("lowercase columns")
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
print(df.columns)

labels = ['Young Adult', 'Adult', 'Middle Aged', 'Senior']
df['age_group'] = pd.qcut(df['customer_age'], q=4, labels = labels)

print(df.info())
print(df.head())


print("Connected Successfully!")
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:omkarmahalkar45@localhost/newdb1")

df.to_sql("ecommerce_data", con=engine, if_exists="replace", index=False)

print("Data inserted successfully!")