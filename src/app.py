import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd
from scripts.data_processing import fetch_data
from scripts.visualizations import plot_ghi, plot_dni

# Title of the app
st.title("Solar Data Insights Dashboard")

# Sidebar for user input
st.sidebar.header("User Input Features")

# Slider for selecting date range
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2023-12-31"))

# Button to fetch data
if st.sidebar.button("Fetch Data"):
    data = fetch_data(start_date, end_date)  # Dynamic data fetching
    st.success("Data fetched successfully!")

    # Display data
    st.subheader("Data Preview")
    st.dataframe(data)

    # Plot GHI
    st.subheader("Global Horizontal Irradiance (GHI)")
    plot_ghi(data)

    # Plot DNI
    st.subheader("Direct Normal Irradiance (DNI)")
    plot_dni(data)

# Footer
st.sidebar.text("Developed by Arsema")