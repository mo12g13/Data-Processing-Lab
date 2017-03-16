import folium

map_mn = folium.Map(location=[45, -93.28], zoom_start=13)
folium.Marker([44.9729, -93.2831], popup='MCTC').add_to(map_mn)
map_mn.save('map.html')

map_us = folium.Map(location=[40, -100], zoom_start=4)
map_us.save('US_Map.html')