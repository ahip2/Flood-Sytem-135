

# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


from sklearn.manifold import trustworthiness
from sqlalchemy import false, true


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        NoneType= type(None)
        """Checks that the typical range of the high/low flood level are formatted correctly"""
        if type(self.typical_range)== NoneType: #checks if value is 'missing'
            return false
        elif self.typical_range[0]<= self.typical_range[1]:
            #checks that higher is more than lower level
            return true
        else:
            return false

def inconsistent_typical_range_stations(stations):
    """Creates a list of any station where the typical range is formatted incorrectly, or no data is provided"""
    inconsistent_stations=[] #creates an empty list
    for station in stations:
        if MonitoringStation.typical_range_consistent(station)== False: #uses above function to check whether range values are consistent
            inconsistent_stations.append(station.name)
    return inconsistent_stations

