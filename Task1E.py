from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

stations = build_station_list()
N=9

def run():
    print(rivers_by_station_number(stations,N))

if __name__ == "__main__":
    run()
