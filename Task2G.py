from floodsystem.flood import highest_risk

from floodsystem.stationdata import build_station_list

 

def run():

    """Requirements for Task 2G"""

    stations= build_station_list()

    for s in highest_risk(stations,dt=3,N=10,y=3):

        print(s)

    #takes really long

 

if __name__ == "__main__":

    print("*** Task 2G: CUED Part IA Flood Warning System ***")

    run()