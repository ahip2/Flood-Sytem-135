import numpy as np
from floodsystem.stationdata import build_station_list
import matplotlib.pyplot as plt
from datetime import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
import datetime
from floodsystem.plot import plot_water_levels


def run():

    stations=build_station_list()

    s=stations_highest_rel_level(stations,5)

    #gets top 5 relative levelled stations

    dt = 2

    for station in s:

        #iterates over each station and plots a graph using dates+levels for each one

        dates, levels = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=dt))

        plot_water_levels(station,dates,levels)

