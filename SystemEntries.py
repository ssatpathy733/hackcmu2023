# just a bunch of functions to return long strings of text!
import array

class SystemStats:
    def __init__(self, name, distance_km, num_planets, entry):
        self.name = name
        self.distance_km = distance_km
        self.num_planets = num_planets
        self.entry = entry

class System:
    def __init__(self, name, linked_systems, found, color, system_stats):
        self.name = name
        self.linked_systems = linked_systems
        self.found = found
        self.color = color
        self.system_stats = system_stats

def get_index_from_name(name):
    if name == "Proxima Centauri":
        return 0
    if name == "Wolf 359":
        return 1
    if name == "TRAPPIST-1":
        return 2
    if name == "Kepler-62":
        return 3
    if name == "HD 189733b":
        return 4
    if name == "Earth":
        return 5
    return -1
def get_system_entry(system_name):
    if system_name == "Proxima Centauri":
        return "proxima"
    if system_name == "Wolf 359":
        return "wolf"
    if system_name == "TRAPPIST-1":
        return "trappist"
    if system_name == "Kepler-62":
        return "kepler"
    if system_name == "HD 189733b":
        return "glass rain"
    if system_name == "Earth":
        return "earth"
    return system_name + "not found"

def get_distance(from_system, to_system):
    #return 4
    
    index_from = get_index_from_name(getattr(from_system, "name"))
    index_to = get_index_from_name(getattr(to_system, "name"))

    distancesLY = [[0, 5.3, 8, 65, 1200, 4.246],
                [ 8.2, 0, 33, 21, 1.2, 7.795 ],
                [ 50, 8.9, 0, 89, 1.0, 39.46 ],
                [ 1500, 2200, 765, 0, 300, 1207 ],
                [ 70, 23, 88, 12, 0 , 63 ],
                [ 4.246, 7.795, 39.46, 1207, 63, 0 ]]
    
    return distancesLY[index_from, index_to]


systems_stats_dict = {
    "Proxima Centauri": SystemStats("Proxima Centauri", 1000, 1000, get_system_entry("Proxima Centauri")),
    "Wolf 359": SystemStats("Wolf 359", 1000, 1000, get_system_entry("Wolf 359")),
    "TRAPPIST-1": SystemStats("TRAPPIST-1", 1000, 1000, get_system_entry("TRAPPIST-1")),
    "Kepler-62": SystemStats("Kepler-62", 1000, 1000, get_system_entry("Kepler-62")),
    "HD 189733b": SystemStats("HD 189733b", 1000, 1000, get_system_entry("HD 189733b")),
    "Earth": SystemStats("Earth", 1000, 1000, get_system_entry("Earth"))
}

systems_dict = {
    "Proxima Centauri": System("Proxima Centauri", [], False, (102, 102, 153), systems_stats_dict["Proxima Centauri"]), 
    "Wolf 359": System("Wolf 359", [], False, (230, 80, 80), systems_stats_dict["Wolf 359"]), 
    "TRAPPIST-1": System("TRAPPIST-1", [], False, (112, 196, 178), systems_stats_dict["TRAPPIST-1"]), 
    "Kepler-62": System("Kepler-62", [], False, (156, 122, 65), systems_stats_dict["Kepler-62"]), 
    "HD 189733b": System("HD 189733b", [], False, (111, 177, 222), systems_stats_dict["HD 189733b"]), 
    "Earth": System("Earth", [], False, (76, 84, 186), systems_stats_dict["Earth"])
}

