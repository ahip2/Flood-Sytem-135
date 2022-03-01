from floodsystem.stationdata import build_station_list

from floodsystem.utils import sorted_by_key

from floodsystem.stationdata import update_water_levels

import matplotlib.pyplot as plt

from datetime import datetime

from floodsystem.datafetcher import fetch_measure_levels

import datetime

from floodsystem.flood import plot_water_levels, stations_highest_rel_level

from floodsystem.datafetcher import fetch_measure_levels

from floodsystem.stationdata import build_station_list

import datetime


def run():

    stations=build_station_list()

    s=stations_highest_rel_level(stations,5)

    #gets top 5 relative levelled stations

    dt = 10

    for station in s:

        #iterates over each station and plots a graph using dates+levels for each one

        dates, levels = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=dt))

        plot_water_levels(station,dates,levels)


if __name__ == "__main__":

    print("*** Task 2E: CUED Part IA Flood Warning System ***")

def plot_water_levels(station, dates, levels):

 

    t =dates

    level = levels

    # Plot

    plt.plot(t, level)

    plt.xlabel('date')

    plt.ylabel('water level (m)')

    plt.xticks(rotation=45);

    plt.title("Station {}".format(station))

 

    # Display plot

    plt.tight_layout()  # This makes sure plot does not cut off date labels

    if station.typical_range != None:

            plt.axhline(station.typical_range[0], color='r') # lower level

            plt.axhline(station.typical_range[1], color='r') # upper level

    plt.show()