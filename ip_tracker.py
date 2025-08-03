import requests
import folium

# Step 3: Ask the user to enter the IP address
ip = input("Enter the IP address to track: ")

# Step 4: Make a request to ipapi.co for geolocation data
url = f"https://ipapi.co/{ip}/json/"
response = requests.get(url)
data = response.json()

# Step 5: Extract and print relevant info
print("\n--- IP Geolocation Info ---")
print(f"IP Address: {data.get('ip')}")
print(f"City: {data.get('city')}")
print(f"Region: {data.get('region')}")
print(f"Country: {data.get('country_name')}")
print(f"Latitude: {data.get('latitude')}")
print(f"Longitude: {data.get('longitude')}")

# Step 6: Generate a location map using folium
map_location = folium.Map(location=[data.get('latitude'), data.get('longitude')], zoom_start=10)
folium.Marker([data.get('latitude'), data.get('longitude')], popup="Target Location").add_to(map_location)

# Step 7: Save the map
map_location.save("ip_location_map.html")
print("\n[+] Map has been saved as ip_location_map.html")
