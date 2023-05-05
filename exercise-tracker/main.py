import requests
from datetime import datetime

APP_ID = "879748e2"
API_KEY = "caf4c4dddf2e248dbd58649fa7d24b37"
NUTRI_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_URL = "https://api.sheety.co/03591896da792d27202bb345fdb595a5/myWorkouts/workouts"
TOKEN = "bhjbd82bdnGTGT@288dh3o"

# Nutri API authentication
headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}

# Get Exercise details
exercise = input("What Exercise Did You Do? ")

# Parameters for Nutri API request
parameters = {
    "query" : exercise,
    "gender": "male",
    "weight_kg" : 90,
    "height_cm" : 184,
    "age" : 26
    }

# Nutri response saved to jason
nutri_response = requests.post(url=NUTRI_URL, json=parameters, headers=headers )
nutri_result = nutri_response.json()

# Required details taken from json
exercise_name = (nutri_result["exercises"][0]["name"])
calories = (nutri_result["exercises"][0]["nf_calories"])
duration = (nutri_result["exercises"][0]["duration_min"])

# print(f"You were {exercise_name} for {duration} mins and burnt {calories} calories")

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

# Google sheet addition parameters
sheet_parameters = {
    "workout" : {
        "date" : date, 
        "time" : time,
        "exercise" : exercise_name.title(),
        "duration" : duration,
        "calories" : calories
    }
}

sheet_header = {

}

# POST exercise to google sheet
sheet_response = requests.post(url=SHEET_URL, json=sheet_parameters, headers=sheet_header)

