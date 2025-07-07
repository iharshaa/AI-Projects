import os
from dotenv import load_dotenv

# Load Gemini API Key
load_dotenv()

# Import agents
from agents.research_agent import research_agent
from agents.planner_agent import planner_agent
from agents.budget_agent import budget_agent
from agents.route_agent import route_agent
from agents.itinerary_agent import itinerary_agent

# Sample test input
test_state = {
    "origin": "Delhi",
    "location": "Japan",
    "days": 5,
    "budget": 80000
}

# ✅ Step 1: Research Agent
test_state = research_agent(test_state)

# ✅ Step 2: Planner Agent (requires research_places)
test_state = planner_agent(test_state)
print("🗓️ Itinerary:", test_state["itinerary"])
# ✅ Step 3: Budget Agent (requires itinerary)
test_state = budget_agent(test_state)

# ✅ Step 4: Route Agent (requires itinerary)
test_state = route_agent(test_state)

# ✅ Step 5: Itinerary Agent (requires budget_plan + route_map_url)
test_state = itinerary_agent(test_state)

# ✅ View Final Output
print("\n🧪 Test Output:\n")
for k, v in test_state.items():
    print(f"{k}: {v if k != 'final_doc_path' else '[DOCX saved at outputs/]'}")
