# 🗺️ AI Travel  Planner

An AI-powered travel itinerary planner built with **Streamlit** and **Google Gemini API**.  
It generates detailed day-by-day itineraries based on destination, budget, number of days, and user preferences.

---

## 🚀 Features
- Day-wise travel plans (Morning, Afternoon, Evening activities)
- Budget customization (Low, Medium, Luxury)
- Local food recommendations
- Cost estimates
- Simple and clean Streamlit UI

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit**
- **Google Generative AI (Gemini API)**

---

## 📂 Project Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/travel_planner.git
cd travel_planner
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Add your Gemini API Key
Replace `YOUR_GEMINI_API_KEY` in `travel_planner.py` with your actual API key.  
Or set it as an environment variable:

```bash
export GOOGLE_API_KEY="your_api_key_here"   # Linux/Mac
set GOOGLE_API_KEY="your_api_key_here"      # Windows
```

### 5️⃣ Run the App
```bash
streamlit run travel_planner.py
```

---

## 📸 Demo Screenshot
*(Add a screenshot of your app UI here)*

---

## 📋 Example Prompt
Input:
```
Destination: Paris
Days: 5
Budget: Medium
Preferences: Food, Museums, Adventure
```

Output (sample):
```
Day 1:
- Morning: Eiffel Tower visit (€25)
- Afternoon: Seine River Cruise (€15)
- Evening: Dinner at Le Bouillon (€30)
```

---

## 📜 License
This project is licensed under the MIT License - feel free to use and modify.

---
