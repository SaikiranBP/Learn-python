"""
This is a program which has a list named with list_with_colours.
This list contains items in the format of city-area-color.
This program produces output city-area-color,1 if the city-area appears for the first time,
and city-area-color,0 if the city-area appeared previously.
"""
list_with_colours = ["glb-gnsh-red", "glb-vjnr-green", "glb-gnsh-yellow", "glb-vjnr-brown",
                     "blr-gnsh-red", "blr-vjnr-blue", "blr-gnsh-blue", "blr-vjnr-red"]
list_without_colours = []

for name in list_with_colours:
    city_area = name.rsplit('-', 1)
    if city_area[0] not in list_without_colours:
        print(name + ',' + 'True')
    elif city_area[0] in list_without_colours:
        print(name + ',' + 'False')
    list_without_colours.append(city_area[0])
