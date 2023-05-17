import pandas as pd

data = pd.read_csv('class134(1).csv')

name = data['name'].to_list()
distance = data['distance'].to_list()
mass = data['mass'].to_list()
radius = data['radius'].to_list()
gravity = data['gravity'].to_list()

planet_list = []
for i in range(20):
    planet_data = {
        'name':name[i],
        'distance':distance[i],
        'mass':mass[i],
        'radius':radius[i],
        'gravity':gravity[i]
    }
    planet_list.append(planet_data)

data = planet_list
print(data)