import streamlit as st
import google.generativeai as genai

# -------------------------------
# 🔑 Configure Gemini API
# -------------------------------
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Choose the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# -------------------------------
# 🎨 Streamlit UI
# -------------------------------
st.set_page_config(page_title="AI Travel Planner", page_icon="🗺️")
st.title("🗺️ AI Travel Planner")
st.write("Plan your perfect trip with AI ✈️")

# User Inputs
destination = st.text_input("Enter your destination (e.g., Paris, Tokyo)")
days = st.number_input("Number of days", min_value=1, max_value=30, value=5)
budget = st.selectbox("Choose your budget", ["Low", "Medium", "Luxury"])
preferences = st.text_area("Your interests (e.g., food, museums, adventure)")

# Generate button
if st.button("Generate Plan"):
    if destination:
        with st.spinner("Planning your trip..."):
            # -------------------------------
            # 📩 Create Prompt for Gemini
            # -------------------------------
            prompt = f"""
            You are a professional travel planner AI.
            Create a detailed day-by-day itinerary for {days} days in {destination}.
            Budget: {budget}.
            Traveler preferences: {preferences}.
            
            Include:
            - Morning, afternoon, and evening activities
            - Local food recommendations
            - Approximate cost estimates
            """

            # -------------------------------
            # 🤖 Gemini Response
            # -------------------------------
            response = model.generate_content(prompt)

            # -------------------------------
            # 📄 Show Output
            # -------------------------------
            st.subheader("✨ Your Travel Plan Is Here ✨")
            st.write(response.text)
    else:
        st.warning("Please enter a destination first!")
