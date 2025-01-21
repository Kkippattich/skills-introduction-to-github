
import requests
import json
import folium

m = folium.Map(tiles="cartodbpositron")

f = open("D:\\Мышино\\учебач\\Своё\\Взлом пентагона\\проекты\\Новая папка\\OSMB-b37fec0aeac1f17f04f76d15d431b791f8280685.geojson", "r")
geojson_data = json.load(f)

text = 'Test'
circle_lat = 60
circle_lon = 10


folium.GeoJson(geojson_data, name="ЯНАО").add_to(m)

folium.Circle([circle_lat, circle_lon], 150000, fill=True).add_child(folium.Popup('My name is Circle')).add_to(m)
folium.map.Marker(
    [circle_lat + 0.5, circle_lon - 1.6],
    icon=folium.DivIcon(
        icon_size=(150,36),
        icon_anchor=(0,0),
        html='<div style="font-size: 24pt">%s</div>' % text,
        )
    ).add_to(m)
folium.LayerControl().add_to(m)


m.save("index.html")

f.close()