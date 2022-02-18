
from floodsystem.geo import stations_within_radius
from floodsystem.geo import stations_by_distance
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def test_stations_by_distance():

    stations=build_station_list
    cam_stations_by_dist = stations_by_distance(stations,(52.2053, 0.1218))
    assert cam_stations_by_dist[:10] == [('Cambridge Jesus Lock', 'Cambridge', 0.8402364350834995), ('Bin Brook', 'Cambridge', 2.502274086951454), ("Cambridge Byron's Pool", 'Grantchester', 4.0720438555077125), ('Cambridge Baits Bite', 'Milton', 5.115589516578674), ('Girton', 'Girton', 5.227070345811418), ('Haslingfield Burnt Mill', 'Haslingfield', 7.044388165868453), ('Oakington', 'Oakington', 7.128249171700346), ('Stapleford', 'Stapleford', 7.265694306995238), ('Comberton', 'Comberton', 7.7350743760373675), ('Dernford', 'Great Shelford', 7.993861351711722)]

def test_station_within_radius():

    stations=build_station_list()
    #all stations should be within range of a million km
    million_km = len(stations_within_radius(stations,(52.2053,0.1218),1000000))
    all_stations = len(build_station_list())
    assert all_stations==million_km

def test_rivers_with_station():

    stations=build_station_list
    rivers_sorted=sorted(rivers_with_station(stations)) 
    assert len(rivers_sorted) == 950

def test_stations_by_river():
    
    stations=build_station_list
    rivers_dict=stations_by_river(stations)
    assert len(sorted(rivers_dict)) >0
