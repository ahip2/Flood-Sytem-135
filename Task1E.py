from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list



def run():
    stations = build_station_list()
    N=9
    print(rivers_by_station_number(stations,N))

if __name__ == "__main__":
    run()
