

def stations_level_over_threshold(stations,tol):    

    for station in stations:
        
        over_threshold_list=[] #empty list

        if station.relative_water_level() == None: #doesn't include empty water level entries
            pass 
        elif station.relative_water_level() < tol: #doesn't include stations with water level below threshold
            pass
        else: 
            over_threshold_list.append(station.name,station.relative_water_level)
    
    sorted_ot_list = over_threshold_list.sort(key=lambda a: a[1],reverse=True)
    
    return sorted_ot_list

def stations_highest_rel_level(stations,N):
    
    N_highest_level_list=[]
    sorted_ot_list = stations_level_over_threshold(stations,0) #information about relative water level about any level within relative range
    N_highest_level_list = sorted_ot_list[:N] #only the highest N values returned as a list of tuples
    return N_highest_level_list


import matplotlib.pyplot as plt
from datetime import datetime

t = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1),
     datetime(2017, 1, 2), datetime(2017, 1, 3), datetime(2017, 1, 4),
     datetime(2017, 1, 5)]
level = [0.2, 0.7, 0.95, 0.92, 1.02, 0.91, 0.64]

# Plot
plt.plot(t, level)

# Add axis labels, rotate date labels and add plot title
plt.xlabel('date')
plt.ylabel('water level (m)')
plt.xticks(rotation=45);
plt.title("Station A")

# Display plot
plt.tight_layout()  # This makes sure plot does not cut off date labels

plt.show()

def plot_water_levels(station, dates, levels):

 

    t =dates

    level = levels

    # Plot

    plt.plot(t, level)

   

 

    # Add axis labels, rotate date labels and add plot title

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