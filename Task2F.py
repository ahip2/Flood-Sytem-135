import numpy as np
from floodsystem.stationdata import build_station_list, update_water_levels
import matplotlib.pyplot as plt
from datetime import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_high_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.analysis import polyfit

def run():

    stations=build_station_list()

    update_water_levels(stations)
    
    s=stations_high_rel_level(stations,5)

    #gets top 5 relative levelled stations

    dt = 2
    p=4 
    for station in s:

        #iterates over each station and plots a graph using dates+levels for each one
        print (station)

        dates, levels = fetch_measure_levels(station[0].measure_id,dt=datetime.timedelta(days=dt))

        plot_water_levels(station[0],dates,levels)
        polyfit(dates,levels,p)
        

if __name__ == "__main__":

    print("*** Task 2F: CUED Part IA Flood Warning System ***")

    run()

