import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days",min_value=1,max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select Data to view",
                     ('Temperature','Sky'))
st.subheader(f"{option} for the next {days} days in {place.title()}")

if place:
    # Get the temperature/sky data
    try:
        filtered_data = get_data(place,days)

        if option == "Temperature":
            temperatures = [diction['main']['temp'] for diction in filtered_data]
            dates = [diction['dt_txt'] for diction in filtered_data]
            # Create a temperature plot
            figure = px.line(x=dates ,y=temperatures ,labels={'x':'Date','y':'Temperature (C)'} )

            st.plotly_chart(figure)
        if option == 'Sky':
            images = {'Clear': "images/clear.png","Clouds": "images/cloud.png",
                    "Rain": "images/rain.png","Snow": "images/snow.png"}
            sky_condtions = [diction['weather'][0]['main'] for diction in filtered_data]
            img_paths = [images[condition] for condition in sky_condtions]
            
            st.image(img_paths, width=111)
    except KeyError:
        st.info("Please Enter a Valid Place")
        st.info(f"{place.title()} is not a Valid Place")
