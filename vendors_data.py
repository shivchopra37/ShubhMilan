import csv

# Vendor data
venues = [
    {"name": "AISF Hall", "contact": "+919899182220", "address": "Kalka Devi Marg, National Park, Lajpat Nagar, Delhi 110024", "average_price": "600-800"},
    {"name": "Kamal Banquet", "contact": "011 4672 6660; 098100 18473; 098100 62023", "address": "Lajpat Nagar, Delhi", "average_price": "1000"},
    {"name": "Hotel Mint Oodles", "contact": "9650120207", "address": "Nehru Place, Delhi", "average_price": "800-1000"},
    {"name": "Royal Park Hall", "contact": "011-41639995; 41639910", "address": "Greater Kailash I, Delhi", "average_price": "1400-1500"},
    {"name": "Hotel Ivory 32", "contact": "+91-8470804805", "address": "Greater Kailash I, Delhi", "average_price": "900-1000"},
    {"name": "Kastor International", "contact": "9650120207", "address": "Greater Kailash I, Delhi", "average_price": "850-950"},
    {"name": "Hotel Rockland", "contact": "+919871857779", "address": "Greater Kailash I, Delhi", "average_price": "1200-1400"},
    {"name": "Shabnam Banquet", "contact": "+918802925054", "address": "Kalkaji, Delhi", "average_price": "600-800"},
]

decoration_vendors = [
    {"name": "Jagdish Store", "contact": "011 4229 1100", "address": "39, 40, 41, 43, Ring Road, Lajpat Nagar III, Near Moolchand Hospital, New Delhi", "average_price": "500-5000"},
    {"name": "Elen Blossoms & Greens Limited", "contact": "011 4954 0000; +919152916487", "address": "35 Link Road, New Delhi", "average_price": "300-3000"},
    {"name": "Wedding-e-Khas", "contact": "+919990642522", "address": "", "average_price": "20000-100000"},
    {"name": "The Diamond Weddings", "contact": "+917417368662", "address": "", "average_price": "25000-150000"},
    {"name": "Adamya Planners", "contact": "+919525128899", "address": "", "average_price": "30000-200000"},
    {"name": "Narang Tents", "contact": "+918441 92 8441", "address": "", "average_price": "10000-50000"},
    {"name": "Inder Caterers & Decorators", "contact": "9310999936", "address": "", "average_price": "15000-75000"},
    {"name": "Goonj Weddings", "contact": "+919818335808", "address": "", "average_price": "20000-100000"},
]

printing_vendors = [
    {"name": "Delhi Print & Production", "address": "4 Ram Gidwani Marg, New Delhi, Delhi 110024", "contact": "096507 54660", "services": "Digital Printing, Offset Printing, Flex Printing, Screen Printing, Laser Printing, Corporate Gifting, Event Setup & Fabrication"},
    {"name": "Saiman Prints", "address": "24, Nehru Nagar Market, New Delhi, Delhi, 110065", "contact": "098100 57135", "services": "General printing services"},
    {"name": "Rahul Printers & Publishers", "address": "Lajpat Nagar, Delhi, 110024", "contact": "26901310", "services": "Various printing services"},
    {"name": "Priya Prints", "address": "Lajpat Nagar, Delhi - 110024", "contact": "+91 98765 43219", "services": "Reliable printing services"},
    {"name": "Vani’s Graphics", "address": "Lajpat Nagar, Delhi - 110024", "contact": "+91 98765 43220", "services": "Quality paper printing with various design options"},
]

catering_vendors = [
    {"name": "Homefoodi", "contact": "7669237937; 9582307779; 070426 40064", "address": "Mohan Co-op Industrial Estate, Delhi, 110044", "average_price": "500-1200"},
    {"name": "FNV Caterers", "contact": "+919811221800", "address": "Shop C-118, Lajpat Nagar 1, South Delhi, Delhi 110024", "average_price": "800-1500"},
    {"name": "Ocean Pearl Catering", "contact": "+919819102677", "address": "", "average_price": "1200"},
    {"name": "New Foxnut Catering", "contact": "+91448571725", "address": "", "average_price": "1000"},
    {"name": "Sat-Kartar Catering", "contact": "+919811125098", "address": "", "average_price": "1200"},
]

# Function to write CSV files
def write_csv(filename, data, fieldnames):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Writing CSV files
write_csv('venues.csv', venues, ['name', 'contact', 'address', 'average_price'])
write_csv('decoration_vendors.csv', decoration_vendors, ['name', 'contact', 'address', 'average_price'])
write_csv('printing_vendors.csv', printing_vendors, ['name', 'address', 'contact', 'services'])
write_csv('catering_vendors.csv', catering_vendors, ['name', 'contact', 'address', 'average_price'])

print("CSV files created successfully.")