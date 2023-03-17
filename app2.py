import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

def tempCo2Plot1(country, data):
    fig, ax = plt.subplots()
    df = data[data['Country'] == country]
    plt.plot(df['Year'], df['AvgTemperature'], label='Average Temperature')
    plt.plot(df['Year'], df['Co2 Value'], label='CO2 Value')

    # Add axis labels and title
    plt.xlabel('Year')
    plt.ylabel('Average Temperature / CO2 Value')
    plt.title('Average Temperature and CO2 Values for ' + country + ' over the Years')
    
    # Add a legend
    plt.legend()
    
    # Display the plot
    st.pyplot(fig)



def tempCo2Plot(country, data):
    fig, ax1 = plt.subplots()

    # Plot temperature on primary y-axis
    df = data[data['Country'] == country]
    ax1.plot(df['Year'], df['AvgTemperature'], label='Average Temperature', color='blue')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Average Temperature (°F)', color='blue')
    ax1.tick_params('y', colors='blue')

    # Create secondary y-axis for CO2 values
    ax2 = ax1.twinx()

    # Plot CO2 values on secondary y-axis
    ax2.plot(df['Year'], df['Co2 Value'], label='CO2 Value', color='green')
    ax2.set_ylabel('CO2 Value (ppm)', color='green')
    ax2.tick_params('y', colors='green')

    # Set title and legend
    plt.title('Average Temperature and CO2 Values for ' + country + ' over the Years')
    plt.legend()

    # Display the plot
    st.pyplot(fig)




merged_df=pd.read_csv('merged_df.csv')
countryList = merged_df['Country'].unique()
st.title('TEMPRATURE VS CO2 EMMISSION FOR DIFFERENT COUNTRIES')

countryOption= st.selectbox('Select Country',countryList)
if st.button('VISUALISE'):
    tempCo2Plot(countryOption,merged_df)