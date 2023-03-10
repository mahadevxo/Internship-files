import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber Pickups in New York City")
DATE_COLUMN = 'date/time'
#DATA_URL = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')
DATA_URL = "uber-raw-data-sep14.csv"

@st.cache(suppress_st_warning= True)
def load_data():
    data = pd.read_csv(DATA_URL)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text("Loading data...")
data = load_data()
data_load_state.text("Loading data...done!")

if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(data)

st.subheader("Number of pickups by hour")
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

hourFil = st.slider("Select hour", 0, 23)
filteredData = data[data[DATE_COLUMN].dt.hour == hourFil]
st.subheader(f"Map of pickups at {hourFil}:00")
st.map(filteredData)