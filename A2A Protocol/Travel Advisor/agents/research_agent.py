from typing import Dict
from utils.gemini_client import call_gemini

def research_agent(state: Dict) -> Dict:
    location = state["location"]
    days = state["days"]

    prompt = f"""
    I'm planning a {days}-day trip to {location}. Suggest the top 5–7 cities or places worth visiting.
    Only return the names of the cities in order.
    """

    output = call_gemini(prompt)
    cities = [line.strip("-•123. ") for line in output.splitlines() if line.strip()]
    state["research_places"] = cities
    return state
