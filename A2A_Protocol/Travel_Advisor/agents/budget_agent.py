from typing import Dict
from utils.gemini_client import call_gemini

def budget_agent(state: Dict) -> Dict:
    itinerary = state.get("itinerary", {})
    budget = state.get("budget", 50000)

    locations = [info["location"] for info in itinerary.values() if "location" in info]

    prompt = f"""
    Help me allocate a ₹{budget} budget across this {len(locations)}-day trip to the following places: {', '.join(locations)}.
    
    Break the budget into:
    - Transport
    - Accommodation
    - Food
    - Entry Fees / Attractions
    - Miscellaneous

    Return a simple bullet-point format or dictionary-like structure.
    """

    output = call_gemini(prompt)
    state["budget_plan"] = output
    return state
