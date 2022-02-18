
from floodsystem.geo import stations_within_radius
from floodsystem.geo import stations_by_distance
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def test_stations_by_distance():

    stations=build_station_list()
    cam_stations_by_dist = stations_by_distance(stations,(52.2053, 0.1218))
    assert cam_stations_by_dist[:1] == [('Cambridge Jesus Lock', 0.840237595667494)]
    

def test_station_within_radius():

    stations=build_station_list()
    #all stations should be within range of a million km
    million_km = len(stations_within_radius(stations,(52.2053,0.1218),1000000))
    all_stations = len(build_station_list())
    assert all_stations==million_km

def test_rivers_with_station():

    stations=build_station_list()
    rivers_sorted=sorted(rivers_with_station(stations)) 
    assert (len(rivers_sorted)) >= 0

def test_stations_by_river():
    
    stations=build_station_list()
    rivers_dict=stations_by_river(stations)
    assert len(sorted(rivers_dict)) >=0

def test_rivers_by_station_number():

    stations = build_station_list()
    rivers_by_station_number(stations,1000000)
    assert len(rivers_by_station_number(stations,10)) >10

test_stations_by_distance()
test_station_within_radius()
test_rivers_with_station()
test_stations_by_river()
test_rivers_by_station_number()
