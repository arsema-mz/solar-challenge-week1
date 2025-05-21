import matplotlib.pyplot as plt
import streamlit as st

def plot_ghi(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data['DNI'], data['GHI'], label='GHI', color='orange')
    plt.xlabel('DNI')
    plt.ylabel('Global Horizontal Irradiance (GHI)')
    plt.title('GHI VS DNI')
    plt.legend()
    st.pyplot(plt)

def plot_dni(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Tamp'], data['RH'], label='DNI', color='blue')
    plt.xlabel('Tamp')
    plt.ylabel('RH')
    plt.title('Tamp VS RH')
    plt.legend()
    st.pyplot(plt)