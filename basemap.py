import folium
import pandas as pd

fdir = r"...\tiyatro.csv"
data = pd.read_csv(fdir, sep=";")
sahne = list(data["THEATER_NAME"])
lat = list(data["LATITUDE"])
lon = list(data["LONGITUDE"])

map = folium.Map(location=[41.0082, 28.9784],zoom_start=12)

fg = folium.FeatureGroup(name="My Map")

for shn,lt,ln in zip(sahne,lat,lon):
    fg.add_child(folium.Marker(location=[lt,ln],
                                popup=shn, 
                                icon=folium.Icon(color="blue")))

map.add_child(fg)

map.save("city_theaters.html")