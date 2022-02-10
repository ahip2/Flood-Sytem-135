# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from socket import SO_BROADCAST
from unicodedata import name

from sklearn.metrics import nan_euclidean_distances
from floodsystem.station import MonitoringStation
from numpy import number, sqrt
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

    #list of rivers and the number of stations in paired entries
    list=[river_name,num_of_stations]
    N_list=[]

    for i in rivers_with_station(stations):
        station_by_river(i)=num_of_stations
        i=river_name
        list.append(river_name,num_of_stations)
        list.sort(key=lambda x:x[1])
    return list
    #we now have a list of river names and the number of stations
    #sorted in order of number of station
    N_list= list[-N:]
    list[-N]= name1,num1
    if list[river_name]=name1: 
        pass
    elif list[num_of_stations]=num1 :
        N_list.append(river_name,num_of_stations)

return N_list
    