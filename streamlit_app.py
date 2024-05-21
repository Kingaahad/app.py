
import streamlit as st
import pandas as pd
import numpy as np

DATA_URL= ("C:\Users\Kingaahad\Desktop\home/Motor_Vehicle_Collisions_-_Crashes.csv"
)
st.title("Motor Vehicle Collisions in New York City")
st.markdown("This application is a Streamlit dashboard that can be used "
"to analyze motor vehicle collisions in NYC🗽💥🚗")


def load_data(nrows):
  data = pd.read_csv(DATA_URL, nrows=nrows, parse_date=[['CRASH_DATE', 'CRASH_TIME']])
  data.dropna(subset=['LATITUDE','LONGITUDE'], inplace=True)
  lowercase= lambda x: str(x).lower()
  data.rename(lowercase, axis= 'columns', inplace= True)
  data.rename(columns={'crash_date_crash_time': 'date/time'}, inplace= True)
  return data
  
data=load_data(100000)
st.header("Where are the most people injured in NYC")
injured_people= st.slider("Numbers of persons injured in vehicle collisions",0,19)
st.map(data.query("injured_persons>= @injured_people")[["latitude","longitude"]].dropna(how="any"))

