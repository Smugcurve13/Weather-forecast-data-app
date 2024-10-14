import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place: ")
days = st.slider("Forecast Days",min_value=1,max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select Data to view",
                     ('Temperature','Sky'))

st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates = ['2020','2029','2069']
    temps = [99,69,54]
    temps = [days * i for i in temps ]
    return dates , temps


d,t = get_data(days)

figure = px.line(x=d ,y=t ,labels={'x':'Date','y':'Temperature (C)'} )
st.plotly_chart(figure)