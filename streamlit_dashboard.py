# Importieren der benötigten Bibliotheken
import streamlit as st
import pandas as pd
import geopandas as gpd
from PIL import Image   #To use images in the app
import altair as alt    #To add altair visualisations of the data

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
data.head()

# Pfad zu Ihrer GeoJSON-Datei
geojson_path = 'destatis_geo.shp'

# Laden des GeoJSON mithilfe von Geopandas
gdf = gpd.read_file(geojson_path)
gdf.head()

gdf.to_crs(epsg=4326, inplace=True)

gdf['centroid'] = gdf.geometry.centroid

# Extrahieren der X- und Y-Koordinaten des Centroids
gdf['x'] = gdf.centroid.x
gdf['y'] = gdf.centroid.y

# Optional: Entfernen der Spalte 'centroid', wenn sie nicht benötigt wird
gdf.drop(columns=['centroid'], inplace=True)

url = r'dland_destatis.geojson'

geodata_la = alt.Data(
  url=url, format=alt.DataFormat(property="features", type="json")
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