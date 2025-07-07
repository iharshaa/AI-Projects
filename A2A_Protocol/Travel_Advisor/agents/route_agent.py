from urllib.parse import quote
from typing import Dict, List, Tuple
from geopy.geocoders import Nominatim
import time

def generate_route_map_link(places: List[str]) -> str:
    if len(places) < 2:
        return "Not enough locations to generate route."
    base = "https://www.google.com/maps/dir/"
    path = "/".join(quote(place.strip()) for place in places)
    return base + path

def get_coordinates(places: List[str]) -> List[Tuple[float, float, str]]:
    geolocator = Nominatim(user_agent="trip-planner")
    coordinates = []
    for place in places:
        try:
            location = geolocator.geocode(place, timeout=10)
            if location:
                coordinates.append((location.latitude, location.longitude, place))
            else:
                coordinates.append((0.0, 0.0, place))  # fallback
            time.sleep(1)
        except:
            coordinates.append((0.0, 0.0, place))
    return coordinates

def route_agent(state: Dict) -> Dict:
    itinerary = state.get("itinerary", {})
    daywise_locations = []

    for day, info in itinerary.items():
        location = info.get("location")
        if location and location not in daywise_locations:
            daywise_locations.append(location)

    state["route_sequence"] = daywise_locations
    state["route_map_url"] = generate_route_map_link(daywise_locations)
    state["route_coordinates"] = get_coordinates(daywise_locations)

    return state
