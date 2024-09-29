import csv
import time

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
        budget = float(input("What is your budget for the event? "))
        attendees = int(input("How many people are you expecting to attend? "))
        return event_type, location, budget, attendees

    def suggest_event_plan(self, event_type, location, budget, attendees):
        print("\nBased on your inputs, here is a plan for your event:")

        # Suggest venues, decorations, printing, and catering services
        self.suggest_venues(location, budget)
        self.suggest_decorations(location, budget)
        self.suggest_catering(location, budget)
        self.suggest_printing(location)

        print("\nThank you for using ShubhMilan! We hope your event goes smoothly.")

    def suggest_venues(self, location, budget):
        print("\nSuggested Venues:")
        filtered_venues = [venue for venue in self.venues if location in venue["address"].lower() and self.price_in_budget(venue["average_price"], budget)]
        if filtered_venues:
            for venue in filtered_venues:
                print(f"- {venue['name']}, Price Range: {venue['average_price']}, Address: {venue['address']}, Contact: {venue['contact']}")
        else:
            print(f"No venues available within your budget in {location}.")

    def suggest_decorations(self, location, budget):
        print("\nSuggested Decoration Vendors:")
        filtered_decorations = [decor for decor in self.decorations if self.price_in_budget(decor["average_price"], budget)]
        if filtered_decorations:
            for decor in filtered_decorations:
                print(f"- {decor['name']}, Price Range: {decor['average_price']}, Address: {decor['address']}, Contact: {decor['contact']}")
        else:
            print("No decoration vendors available within your budget.")

    def suggest_catering(self, location, budget):
        print("\nSuggested Catering Vendors:")
        filtered_catering = [caterer for caterer in self.catering if self.price_in_budget(caterer["average_price"], budget)]
        if filtered_catering:
            for caterer in filtered_catering:
                print(f"- {caterer['name']}, Price Range: {caterer['average_price']}, Address: {caterer['address']}, Contact: {caterer['contact']}")
        else:
            print("No catering vendors available within your budget.")

    def suggest_printing(self, location):
        print("\nSuggested Printing Vendors:")
        filtered_printing = [printer for printer in self.printing if location in printer["address"].lower()]
        if filtered_printing:
            for printer in filtered_printing:
                print(f"- {printer['name']}, Services: {printer['services']}, Address: {printer['address']}, Contact: {printer['contact']}")
        else:
            print(f"No printing vendors found in {location}.")

    def price_in_budget(self, price_range, budget):
        if "-" in price_range:
            low, high = map(int, price_range.split("-"))
            return low <= budget <= high
        else:
            return int(price_range) <= budget

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
