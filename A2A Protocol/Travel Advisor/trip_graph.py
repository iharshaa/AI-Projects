from typing import TypedDict
from langgraph.graph import StateGraph
from agents.planner_agent import planner_agent
from agents.itinerary_agent import itinerary_agent

class TripState(TypedDict, total=False):
    origin: str
    location: str
    days: int
    budget: int
    transport: str
    itinerary_text: str
    final_doc_path: str

builder = StateGraph(TripState)

builder.add_node("Plan", planner_agent)
builder.add_node("Itinerary", itinerary_agent)

builder.set_entry_point("Plan")
builder.add_edge("Plan", "Itinerary")

graph = builder.compile()