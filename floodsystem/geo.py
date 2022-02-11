# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.station import MonitoringStation
from numpy import number, sqrt
from importlib_metadata import import_module
from haversine import haversine, Unit
from .stationdata import build_station_list
from .utils import sorted_by_key


#empty list
swr=[]


def stations_within_radius (stations, centre, r) :
    #finding stations distance
    for station in stations:
        MonitoringStation.coord= (lat,long)
        x,y = centre
        dis = sqrt(((x - lat)**2 )+((y-long)**2))
        #if distance is within the radius add to the list
        if dis < r:
            swr.append(station.name)
        else:
            pass
    return swr

sorted_swr = sorted(swr)
print(sorted_swr)

def rivers_by_station_number(stations, N): 

    from floodsystem.geo import stations_by_river
    #list of rivers and the number of stations in paired entries
    list=[river_name,num_of_stations]
    N_list=[]

    for station.river in rivers_with_station(stations):
        stations_by_river(build_station_list)=num_of_stations
        station.river =river_name
        list.append(river_name,num_of_stations)
        list.sort(key=lambda x:x[1])
    
    #we now have a list of river names and the number of stations
    #sorted in order of number of station
    N_list= list[-N:]
    list[-N]= name1,num1
    if list[name1,num of stations]:
        pass
    elif list[river_name,num1] :
        N_list.append(river_name,num_of_stations)

return N_list

def stations_by_distance(stations, p):

    station_distances=[] #empty list for station name and dist from p

    for station in stations:

        distance=float(haversine(p,station.coord)) #set distance for each loop as dist from p

        station_distances.append((station.name, distance)) #adds a tuple of a station name and it's distance from p to empty list

    sorted_station_distances = sorted_by_key(station_distances, int(1)) #sorts list based on second item i.e distance not name

    return sorted_station_distances

   

 

def rivers_with_station(stations):

    list_rivers=[]

    for station in stations: #iterates over all the station objects in the given list

        list_rivers.append(station.river) #add each river to the list

    set_rivers=set(list_rivers) #removes duplicate rivers

    return set_rivers

 

def stations_by_river(stations):

    dict_rivers={} #creates empty dictionary

    for station in stations:#iterates over all the station objects in the given list

        if station.river in dict_rivers.keys(): #checks to see if river is already in dictionary

            dict_rivers[station.river].append(station.name) #adds new station name if river has already been added as a key

        else:

            dict_rivers[station.river]=[station.name] #creates new river key if river isn't in dictionary

    return dict_rivers
    