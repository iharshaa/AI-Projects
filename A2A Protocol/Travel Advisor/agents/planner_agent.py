from utils.gemini_client import call_gemini

def planner_agent(state: dict) -> dict:
    origin = state.get("origin", "")
    location = state.get("location", "")
    days = state.get("days", 4)
    transport = state.get("transport", "Flight")
    budget = state.get("budget", 30000)

    prompt = f"""
You are a travel agent helping plan a {days}-day trip from {origin} to {location}.
The user will be traveling by {transport}, with an overall budget of ₹{budget}.

Generate a detailed, day-wise itinerary including:
- Welcome intro with total budget
- Bullet-point activities for each day
- Highlight arrival/departure info
- Estimate approximate cost for each day (like: ₹5,000/day)
- Break down budget into:
    • Travel / Local transport
    • Food
    • Stay
    • Attractions

Format:
Day 1: Title
- 🗒️ Activity 1
- 🍽️ Food spot
- 🏞️ Visit location
- 💰 Estimated cost: ₹X (transport ₹Y, food ₹Z...)

Respond in natural language. Keep tone friendly and helpful.
"""

    output = call_gemini(prompt)
    state["itinerary_text"] = output
    return state
