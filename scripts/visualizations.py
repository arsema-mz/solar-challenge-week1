import matplotlib.pyplot as plt
import streamlit as st

def plot_ghi(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['GHI'], label='GHI', color='orange')
    plt.xlabel('Date')
    plt.ylabel('Global Horizontal Irradiance (GHI)')
    plt.title('GHI Over Time')
    plt.legend()
    st.pyplot(plt)

def plot_dni(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['DNI'], label='DNI', color='blue')
    plt.xlabel('Date')
    plt.ylabel('Direct Normal Irradiance (DNI)')
    plt.title('DNI Over Time')
    plt.legend()
    st.pyplot(plt)