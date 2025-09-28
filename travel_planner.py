import streamlit as st
import google.generativeai as genai

# -------------------------------
# 🔑 Configure Gemini API
# -------------------------------
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# 🎨 Custom CSS for background
# -------------------------------
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: 
        linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
        url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    color: white; /* makes default text white for visibility */
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0); /* transparent header */
}

[data-testid="stToolbar"] {
    right: 2rem;
}

h1, h2, h3, h4, h5, h6, label, .stMarkdown, .stTextInput, .stSelectbox, .stNumberInput, .stTextArea {
    color: white !important; /* force text to be readable */
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)



# Choose the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

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


