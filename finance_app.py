import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import streamlit as st

# Assuming 'finance_data.db' is already created and populated from the previous code

# Connecting to the database
conn = sqlite3.connect('finance_data.db')

# Streamlit app
st.title("Financial Data Dashboard")

# Sidebar for navigation/filters
st.sidebar.header("Filters")
selected_year = st.sidebar.selectbox("Select Year", pd.read_sql_query("SELECT DISTINCT year FROM finance_data", conn)['year'].unique())

# Queries with filtering
segment_profit = pd.read_sql_query(f"""
SELECT segment, SUM(CAST(REPLACE(_profit_, '$', '') AS DECIMAL(10,2))) AS total_profit
FROM finance_data
WHERE year = {selected_year}
GROUP BY segment
""", conn)

sales = pd.read_sql_query(f"""
SELECT segment, SUM(CAST(REPLACE(_sales_, '$', '') AS DECIMAL(10,2))) AS total_sales
FROM finance_data
WHERE year = {selected_year}
GROUP BY segment
""", conn)


# Displaying data and charts
st.subheader("Segment-wise Profit")
st.bar_chart(segment_profit.set_index('segment'))

st.subheader("Segment-wise Sales")
st.bar_chart(sales.set_index('segment'))

# ... (rest of your Streamlit code to display other charts and data)

# Example for yearly profit (replace with your actual data)
yearly_profit = pd.read_sql_query(f"""
SELECT year, SUM(CAST(REPLACE(_profit_, '$', '') AS DECIMAL(10,2))) AS total_profit
FROM finance_data
GROUP BY year
""", conn)
st.subheader("Yearly Profit")
st.line_chart(yearly_profit.set_index('year'))

# Close the connection
conn.close()lose()
