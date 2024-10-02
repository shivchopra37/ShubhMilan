
import requests
import csv
import time
import subprocess
import sys

# Function to install requests library
def install_requests():
    try:
        import requests
    except ImportError:
        print("Requests library not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    finally:
        import requests  # Import after installation

install_requests()

# Function to load vendor data from a CSV file
def load_vendor_data(file_path, vendor_type):
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if vendor_type == "printing":
                    data.append({
                        "name": row["name"],
                        "address": row["address"],
                        "contact": row["contact"],
                        "services": row["services"]
                    })
                else:
                    data.append({
                        "name": row["name"],
                        "contact": row["contact"],
                        "address": row["address"],
                        "average_price": row.get("average_price", "N/A")
                    })
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

# Function to get event enhancement suggestions from GPT-4V API
def get_event_suggestions(event_type):
    GPT4V_KEY = "9776e4337cbf451baffbff9a2b452bc3"
    headers = {
        "Content-Type": "application/json",
        "api-key": GPT4V_KEY
    }

    GPT4V_ENDPOINT = "https://tabsonsnct.openai.azure.com/openai/deployments/tabsonsai/chat/completions?api-version=2024-02-15-preview"

    prompt = f"Provide unique and creative ideas to enhance a {event_type} event. Include activities, themes, and other suggestions."
    data = {
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150
    }

    try:
        response = requests.post(GPT4V_ENDPOINT, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        suggestions = response.json().get('choices', [{}])[0].get('message', {}).get('content', '').strip()
        return suggestions
    except Exception as e:
        print(f"Error getting suggestions: {e}")
        return "Sorry, I couldn't fetch suggestions at this time."

# ShubhMilan AI Model
class ShubhMilanAI:
    def __init__(self, venues, decorations, printing, catering):
        self.venues = venues
        self.decorations = decorations
        self.printing = printing
        self.catering = catering

    def greet_user(self):
        print("Hello! I am ShubhMilan, your event planning assistant.")
        time.sleep(2)
        print("I am here to help you plan your event within your budget by suggesting venues, food, decorations, printing, and more.")

    def get_event_details(self):
        event_type = input("What type of event are you planning (e.g., wedding, birthday, corporate)? ").strip().lower()
        location = input("Where do you want to organize the event? ").strip().lower()
        
        while True:
            try:
                budget = float(input("What is your budget for the event? "))
                if budget <= 0:
                    raise ValueError("Budget must be a positive number.")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                attendees = int(input("How many people are you expecting to attend? "))
                if attendees <= 0:
                    raise ValueError("Number of attendees must be a positive integer.")
                break
            except ValueError as e:
                print(e)

        return event_type, location, budget, attendees

    def suggest_event_plan(self, event_type, location, budget, attendees):
        print("\nBased on your inputs, here is a plan for your event:")
        
        # Calculate the budget for each category based on a predefined allocation
        venue_budget = budget * 0.4
        catering_budget = budget * 0.3
        decoration_budget = budget * 0.2
        printing_budget = budget * 0.1

        self.suggest_venues(location, venue_budget)
        self.suggest_decorations(location, decoration_budget)
        self.suggest_catering(location, catering_budget)
        self.suggest_printing(location, printing_budget)

        # Get additional suggestions from the API
        suggestions = get_event_suggestions(event_type)
        print("\nHere are some suggestions to make your event even better:")
        print(suggestions)

    def suggest_venues(self, location, budget):
        print("\nSuggested Venues:")
        filtered_venues = [venue for venue in self.venues if location in venue["address"].lower() and self.price_in_budget(venue["average_price"], budget)]
        if filtered_venues:
            for venue in filtered_venues:
                print(f"• {venue['name']}\n  - Price Range: {venue['average_price']}\n  - Address: {venue['address']}\n  - Contact: {venue['contact']}\n")
        else:
            print(f"No venues available within your budget in {location}.")

    def suggest_decorations(self, location, budget):
        print("\nSuggested Decoration Vendors:")
        filtered_decorations = [decor for decor in self.decorations if self.price_in_budget(decor["average_price"], budget)]
        if filtered_decorations:
            for decor in filtered_decorations:
                print(f"• {decor['name']}\n  - Price Range: {decor['average_price']}\n  - Address: {decor['address']}\n  - Contact: {decor['contact']}\n")
        else:
            print("No decoration vendors available within your budget.")

    def suggest_catering(self, location, budget):
        print("\nSuggested Catering Vendors:")
        filtered_catering = [caterer for caterer in self.catering if self.price_in_budget(caterer["average_price"], budget)]
        if filtered_catering:
            for caterer in filtered_catering:
                print(f"• {caterer['name']}\n  - Price Range: {caterer['average_price']}\n  - Address: {caterer['address']}\n  - Contact: {caterer['contact']}\n")
        else:
            print("No catering vendors available within your budget.")

    def suggest_printing(self, location, budget):
        print("\nSuggested Printing Vendors:")
        filtered_printing = [printer for printer in self.printing if location in printer["address"].lower()]
        if filtered_printing:
            for printer in filtered_printing:
                print(f"• {printer['name']}\n  - Services: {printer['services']}\n  - Address: {printer['address']}\n  - Contact: {printer['contact']}\n")
        else:
            print(f"No printing vendors found in {location}.")

    def price_in_budget(self, price_range, budget):
        if price_range == "N/A":
            return False
        try:
            if "-" in price_range:
                low, high = map(int, price_range.split("-"))
                return low <= budget <= high
            else:
                return int(price_range) <= budget
        except ValueError:
            return False

# Main function to run the AI
def run_shubhmilan():
    # Load vendor data from CSV files
    venues = load_vendor_data('venues.csv', "venue")
    decorations = load_vendor_data('decoration_vendors.csv', "decoration")
    printing = load_vendor_data('printing_vendors.csv', "printing")
    catering = load_vendor_data('catering_vendors.csv', "catering")

    if venues and decorations and printing and catering:
        # Create an instance of ShubhMilan
        shubhmilan = ShubhMilanAI(venues, decorations, printing, catering)

        # Greet the user and ask for details
        shubhmilan.greet_user()
        event_type, location, budget, attendees = shubhmilan.get_event_details()

        # Suggest a plan based on the inputs
        shubhmilan.suggest_event_plan(event_type, location, budget, attendees)
    else:
        print("Unable to load vendor data.")

# Run the AI model
run_shubhmilan()
