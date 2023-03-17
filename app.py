import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import requests
def getYearWise(city):
    city_year=temp_data.groupby(["City","Year"])["AvgTemperature"].mean()
    return city_year[city]

def getMonthWise(city,year):
    city_year=temp_data.groupby(["City","Year","Month"])["AvgTemperature"].mean()
    return city_year[city][year]


# url = 'http://localhost:3000/data' 
# response = requests.get(url)
# json_data = response.json()
# temp_data = pd.DataFrame(json_data)

temp_data=pd.read_csv('./Saif/city_temperature.csv')
cityList = temp_data['City'].unique()
st.title('CITY WISE TEMPRATURE VISUALISATION')
def plotYearWise(sample):
    fig, ax = plt.subplots()
    sample.plot(ax=ax)
    # Set the title and axis labels
    plt.title('Average Temperatures Over the Years')
    plt.xlabel('Years')
    plt.ylabel('Temperature (°F)')
    # Show the plot
    st.pyplot(fig)

def plotMonthWise(sample):
    fig, ax = plt.subplots()
    sample.plot(ax=ax)
    # Set the title and axis labels
    plt.title('Average Temperatures Over Months')
    plt.xlabel('Months')
    plt.ylabel('Temperature (°F)')
    # Show the plot
    st.pyplot(fig)

cityOption= st.selectbox('Select City',cityList)
typeOption=st.selectbox('How do you want the data?',['Year Wise',"Month Wise"])
if typeOption=='Month Wise':
    sample=(getYearWise(cityOption))
    yearList=list(sample.index)
    yearOption=st.selectbox('Select Year',yearList)
    

#yearOption=st.selectbox('Select Year',)
if st.button('VISUALISE'):
    if typeOption=='Year Wise':
        data=getYearWise(cityOption)
        plotYearWise(data)
    else:
        data=getMonthWise(cityOption,yearOption)
        plotMonthWise(data)    

