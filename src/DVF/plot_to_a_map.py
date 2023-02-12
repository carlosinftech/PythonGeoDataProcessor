import folium
import pandas as pd

# Load the data into a pandas dataframe
data = pd.read_csv("data.csv")

# Create a map centered on the mean latitude and longitude of the data
mean_lat = data["latitude"].mean()
mean_lon = data["longitude"].mean()
map = folium.Map(location=[mean_lat, mean_lon], zoom_start=13)

# Add markers for each data point
for lat, lon, label in zip(data["latitude"], data["longitude"], data["label"]):
    folium.Marker([lat, lon], popup=label).add_to(map)

# Save the map to an HTML file
map.save("map.html")