import streamlit as st
import pandas as pd
 
# Create a sample dataframe
data = pd.DataFrame({
  'Fruits': ['Apples', 'Oranges', 'Bananas', 'Grapes'],
  'Quantity': [15, 25, 35, 45]
})
 
# Create a bar chart
st.bar_chart(data)