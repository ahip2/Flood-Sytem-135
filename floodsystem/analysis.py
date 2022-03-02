
import numpy as np
import matplotlib.pyplot as plt
from floodsystem.flood import plot_water_levels, stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
import datetime

def polyfit(dates, levels, p):
    y = levels
    x = plt.dates.date2num(dates)
    # Using shifted x values, find coefficient of best-fit
    p_coeff = np.polyfit(x - x[0], y, p)

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
