import streamlit as st
import base64
import os
from trip_graph import graph

st.set_page_config(page_title="AI Trip Planner", layout="centered")
st.title("🧭 AI Trip Planner")

with st.form("trip_form"):
    origin = st.text_input("From", "Hyderabad")
    destination = st.text_input("To", "Goa")
    days = st.number_input("Trip Duration (Days)", min_value=1, value=4)
    budget = st.number_input("Budget (INR)", min_value=1000, value=25000)

    transport = st.selectbox(
        "Choose your preferred transport mode",
        ["Flight", "Train", "Bus", "Car"]
    )

    submitted = st.form_submit_button("🚀 Plan My Trip")

if submitted:
    with st.spinner("Gemini agents are crafting your custom itinerary..."):
        input_data = {
            "origin": origin,
            "location": destination,
            "days": days,
            "budget": budget,
            "transport": transport
        }

        try:
            result = graph.invoke(input_data)
        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.stop()

        st.success("✅ Your trip plan is ready!")

        # 📝 Show itinerary text if available
        if "itinerary_text" in result:
            st.markdown("### 📄 Day-wise Itinerary")
            st.markdown(result["itinerary_text"])

        # 📥 Download DOCX
        docx_path = result.get("final_doc_path")
        if docx_path and os.path.exists(docx_path):
            with open(docx_path, "rb") as file:
                b64 = base64.b64encode(file.read()).decode()
                docx_name = os.path.basename(docx_path)
                href = f'<a href="data:application/octet-stream;base64,{b64}" download="{docx_name}">📥 Download Itinerary (DOCX)</a>'
                st.markdown(href, unsafe_allow_html=True)
        else:
            st.warning("⚠️ Itinerary document not found.")
