# just a bunch of functions to return long strings of text!

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

