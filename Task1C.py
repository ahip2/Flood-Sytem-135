
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

stations = build_station_list()

Cam_centre= stations_within_radius(stations,(52.2053,0.1218),10)
print(Cam_centre)
