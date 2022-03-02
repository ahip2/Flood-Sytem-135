

from click import pass_obj


def stations_level_over_threshold(stations,tol):    

    for station in stations:
        
        over_threshold_list=[] #empty list

        if station.relative_water_level() == None or station.relative_water_level() < tol: #doesn't include stations with water level below threshold
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
