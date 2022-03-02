import numpy as np
import matplotlib.pyplot as plt
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

    dt = 2

    for station in s:

        #iterates over each station and plots a graph using dates+levels for each one

        dates, levels = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=dt))

        plot_water_levels(station,dates,levels)

def polyfit(dates, levels, p):
   y=poly, d0 = polyfit(dates, levels, 4)
   x = np.linspace(0, 2, 10)


# Using shifted x values, find coefficient of best-fit
# polynomial f(x) of degree 4
p_coeff = np.polyfit(x - x[0], y, 4)

# Convert coefficient into a polynomial that can be evaluated
# e.g. poly(0.3)
poly = np.poly1d(p_coeff)

# Plot original data points
plt.plot(x, y, '.')

# Plot polynomial fit at 30 points along interval (note that polynomial
# is evaluated using the shift x)
x1 = np.linspace(x[0], x[-1], 30)
plt.plot(x1, poly(x1 - x[0]))

# Display plot
plt.show()
