import csv
import folium

mammoth_color = {
    'Mammuthus columbi': 'green',
    'Mammuthus primigenius': 'blue',
    'Mammuthus hayi': 'purple',
    'Mammuthus exilis': 'red',
    'Mammuthus': 'orange'

}
# Using folium api to set location of latitude
mammoth_map = folium.Map(location=[40, -100], zoom_start=4, tiles='Stamen Terrain')
with open('mammoth_data.csv', 'r') as mammoth_csv:
    reader = csv.reader(mammoth_csv, quoting=csv.QUOTE_NONNUMERIC)
    reader.__next__()
    for line in reader:
        try:

            lat = line[3]
            lon = line[4]

            marker_text = '{} found in {}. {}. {}.'.format(line[0],line[6],line[5], line[7])
            if line[1]:
                marker_text += '{} {}'.format(line[1], line[2])
            print(lat, lon, marker_text)
            color = mammoth_color[line[0]]
            marker = folium.Marker([lat, lon], popup=marker_text, icon=folium.Icon(color=color))
            marker.add_to(mammoth_map)

        except IndexError:
            continue

mammoth_map.save('mammoth_map.html')