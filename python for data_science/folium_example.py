import folium
from IPython.display import HTML

def display(m, height=300):
    """Takes a folium instance and embed HTML."""
    m._build_map()
    srcdoc = m.HTML.replace('"', '&quot;')
    embed = HTML('<iframe srcdoc="{0}" '
                 'style="width: 100%; height: {1}px; '
                 'border: none"></iframe>'.format(srcdoc, height))
    return embed


# map = folium.Map(location=[37.76, -122.45])
# map.simple_marker([37.76, -122.45])
# display(map)

map_osm = folium.Map(location=[37.76, -122.45])
folium.Marker([37.76, -122.45]).add_to(map_osm)
map_osm.save('spst.html')
#	display(map_osm)