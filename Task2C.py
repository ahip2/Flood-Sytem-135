
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list

def run():
    
    stations=build_station_list
    N=10
    
    print(stations_highest_rel_level(stations,N))
    
if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()