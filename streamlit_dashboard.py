# Importieren der benötigten Bibliotheken
import streamlit as st
import pandas as pd
import geopandas as gpd
from PIL import Image   #To use images in the app
import altair as alt    #To add altair visualisations of the data
import pandas as pd   #For simple data manipulation

# Load the favicon and set the page config (so what appears in the tab on your web browser)
im = Image.open("/Users/lionlukasnaumann/Nextcloud/Marketing/Design/Druck/logo/favicon.png")
st.set_page_config(page_title="IoD Deciles across England", layout="wide", page_icon=im)
st.title("Geographical Analysis of the IoD Deciles Across England")

# Example of how to use markdown:
url_link = 'https://www.acui.re/home'
st.markdown(
  f"<div style='text-align: center;'>Taken from the infographic <a href={url_link}> here</a>. </div>",
  unsafe_allow_html=True, #This allows you to use html code!
    )

data = pd.read_csv('/Users/lionlukasnaumann/Downloads/K-2020-AI016-1--AI1601--2023-11-15.csv',delimiter=';')
gdf = gpd.read_file('/Users/lionlukasnaumann/Downloads/dland_destatis.geojson')

geojson_data = gdf.to_json()
geojson_la = '/Users/lionlukasnaumann/Downloads/dland_destatis.geojson'
geodata_la = alt.Data(
  url=geojson_la, format=alt.DataFormat(property="features", type="json")
)
# Create an Altair chart for the GeoJSON data
chart = alt.Chart(geodata_la).mark_geoshape(
    # You can add properties here, like fill color, stroke width, etc.
).properties(
    width=500,  # Adjust the width as needed
    height=300  # Adjust the height as needed
)

# Display the chart in Streamlit
st.altair_chart(chart)