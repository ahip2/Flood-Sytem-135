
def stations_level_over_threshold(stations,tol):    

    for station in stations:
        

        over_threshold_list=[] #empty list

        if type == float and station.relative_water_level() >= tol:
                over_threshold_list.append((station.name,station.relative_water_level))
    
    sorted_ot_list = over_threshold_list.sort(key=lambda a: a[1],reverse=True)
    
    return sorted_ot_list

def stations_highest_rel_level(stations,N):
    
    N_highest_level_list=[]
    sorted_ot_list = stations_level_over_threshold(stations,0) #information about relative water level about any level within relative range
    N_highest_level_list = sorted_ot_list[:N] #only the highest N values returned as a list of tuples
    return N_highest_level_list


from floodsystem.utils import sorted_by_key    
from floodsystem.stationdata import update_water_levels

def stations_high_rel_level(stations,N):

    """calculates relative water level compared to its typical range, returns 'N' highest"""

    relative_levels=[]

    #creates an empty list

    update_water_levels(stations)

    for station in stations:

        if station.typical_range != None and station.typical_range_consistent and station.latest_level !=None :

            #only counts stations with consistent data

            relative_level=station.latest_level-station.typical_range[1]

            #finds difference between current station level and typical upper range

            relative_levels.append((station,relative_level))

            #adds station and its relative level as a tuple to a list

    sorted_relative_levels= sorted_by_key(relative_levels, int(1),reverse=True)

    #sorts list based on relative level, in reverse (to make list descending)

    station_only=[]

    #creates empty list for just stations

    for tuple in sorted_relative_levels[0:N]:

        #iterates over first 'N' tuples in list of (station,relative level)

        station_only.append(tuple[0])

    #adds station terms of sorted list to a new list

    return station_only