# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from numpy import number, sqrt
from .station import MonitoringStation
from importlib_metadata import import_module
from haversine import haversine, Unit
from .stationdata import build_station_list
from .utils import sorted_by_key
from operator import itemgetter


#empty list
swr=[]


def stations_within_radius (stations, centre, r) :
    #finding stations distance
    for station in stations:
        lat = station.coord[0]
        long = station.coord[1]
        x,y = centre
        dis = haversine(station.coord,centre)
        #if distance is within the radius add to the list
        if -r< dis < r:
            swr.append(station.name)
        else:
            pass
    sorted_swr = sorted(swr)
    return sorted_swr



def stations_by_distance(stations, p):

    station_distances=[] #empty list for station name and dist from p

    for station in stations:
        distance=float(haversine(p,station.coord)) #set distance for each loop as dist from p

        station_distances.append((station.name, distance)) #adds a tuple of a station name and it's distance from p to empty list

    sorted_station_distances = sorted_by_key(station_distances, int(1)) #sorts list based on second item i.e distance not name

    return sorted_station_distances


def rivers_with_station(stations):

    stations=[]

    list_rivers=[]

    for station in stations: #iterates over all the station objects in the given list

        list_rivers.append(station.river) #add each river to the list

    set_rivers=set(list_rivers) #removes duplicate rivers

    return set_rivers

 

def stations_by_river(stations):

    dict_rivers={} #creates empty dictionary

    for station in stations:#iterates over all the station objects in the given list

        if station.river in dict_rivers.keys(): #checks to see if river is already in dictionary
            dict_rivers[station.river].append(station)

        else:
            dict_rivers[station.river]= station #creates new river key if river isn't in dictionary

    return dict_rivers

    
def rivers_by_station_number(stations, N): 

    #empty list
    N_list=[]
    river_list=[]
    #creates a dict with station.river as keys and station objects as values
    rivers_dict = stations_by_river(stations)
    num_of_stations = 0

    for station in stations:
        
        #the send value in each tuple is the number of stations on each river
        num_of_stations = len(rivers_dict[station.river])
        # adds each pair of values to a new list
        river_list.append((station.river,num_of_stations))
        #sorts the list by number of stations smallest to largest
        river_list_sorted = sorted(river_list,key=itemgetter(1))

    print ()

    #creates another list which contains the N largest values of the previous river list
    N_list= river_list_sorted[-N:]
    (name1,num1) = river_list_sorted[-N]
    
    #for all the rivers
    for station.river in river_list_sorted:
        #if the river is 
        if river_list_sorted [0] == name1 :
            pass
        elif river_list_sorted [1] == num1:
            N_list.append((station.river,num_of_stations))
    return N_list
    
