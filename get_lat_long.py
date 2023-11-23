
import pandas as pd
from geopy.geocoders import Nominatim

# Replace 'YOUR_API_KEY' with your actual API key
geolocator = Nominatim(user_agent="myGeocoder")

# Read the excel file
df = pd.read_excel('conc.xlsx')

# Create empty lists to store the coordinates
coordinates = []

# Iterate over each row in the data
for index, row in df.iterrows():
    # Construct the address string
    address = f"{row['numero']} {row['logradouro']}, {row['municipio']}, {row['uf']}, Brazil"
    
    # Use the Nominatim API to geocode the address
    location = geolocator.geocode(address)
    
    # Check if the geocoding was successful
    if location:
        # Extract the latitude and longitude coordinates
        lat, lng = location.latitude, location.longitude
        
        # Print the address, company name, and company type along with the coordinates
        print(f"Address: {address}")
        print(f"Company Name: {row['Nome']}")
        print(f"Company Type: {row['tipo_cliente']}")
        print(f"Coordinates: Latitude = {lat}, Longitude = {lng}")
        print()
        
        # Append the coordinates to the list
        coordinates.append((lat, lng))
    else:
        print(f"Geocoding failed for address: {address}")

# Print the list of coordinates
print(f"Coordinates List: {coordinates}")
