# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from cProfile import label
from tkinter import Y
from numpy import sqrt
from sqlalchemy import lateral
from zmq import PUSH
from floodsystem.stationdata import build_station_list

#emply list
swr=[]

def stations_within_radius (centre, r) :
    #list of stations
    stations = build_station_list
    #finding stations distance
    for station in stations:
        station.coord == long, lat
        x,y = centre
        dis = sqrt(((x - long)**2 )+((y-lat)**2))
        #if distance is within the radius add to the list
        if dis < r:
            swr.append(station.name)
    return swr

sorted_swr = sorted(swr)
print(sorted_swr)

PUSH