from collections import namedtuple

Book = namedtuple('Book', ('name', 'Author', 'pages'))
b1 = Book("Quran","Allah",1000)
print(b1)

House = namedtuple('House', ('area', 'type','floor','model'))
h1 = House(900,'individual',1,'3-BHK')
print(h1)

Phone = namedtuple('Phone', ('name', 'model', 'os','price'))
p1 =  Phone("Apple","17 pro max","ios",150000)
p2 =  Phone("Google","Pixel 9","Android",80000)
print(p1)
print(p2)


Bike = namedtuple('Bike',('Name','Model','Price'))
b1 = Bike('Royal Enfield','Meteor-350',300000)
print(b1)

Product = namedtuple('Product', ('country', 'name', 'brand', 'type', 'price'))

products = [

    Product("USA", "Optimus", "Tesla", "Robot", 2000000),
    Product("USA", "Model 3", "Tesla", "Electric Car", 4500000),
    Product("USA", "AWS", "Amazon", "Cloud Platform", 1000),
    Product("USA", "GCP", "Google", "Cloud Platform", 1000),
    Product("USA", "Azure", "Microsoft", "Cloud Platform", 1000),
    Product("USA", "Optimus", "Tesla", "Robot", 2000000),
    Product("USA", "Claude", "Anthropic", "AI Model", 2000),
    Product("USA", "Gemini", "Google", "AI Model", 2000),
    Product("USA", "ChatGPT", "OpenAI", "AI Model", 2000),
    Product("USA", "Figo", "Ford", "Hatchback", 6000000),
    Product("USA", "Xbox Series X", "Microsoft", "Gaming Console", 55000),
    Product("USA", "SQL Server", "Microsoft", "Database", 2000),
    Product("USA", "Banking Services", "Wells Fargo", "Finance", 2000),
    Product("USA", "TPU", "Google", "AI Hardware", 5000),
    Product("USA", "IBM Quantum System One", "IBM", "Quantum Computer", 10000000),
    Product("USA", "Sycamore", "Google", "Quantum Processor", 8000000),
    Product("USA", "Falcon 9", "SpaceX", "Rocket", 500000000),
    Product("USA", "Ensure", "Abbott", "Healthcare Nutrition", 2000),
    Product("USA", "Instagram", "Meta", "Social Media", 0),

    Product("Finland", "Linux", "Linus Torvalds", "Operating System", 0),

    Product("France", "Mistral AI", "Mistral", "AI Model", 2000),
    Product("France", "Handbag", "Louis Vuitton", "Luxury Fashion", 200000),
    Product("France", "Pharmaceuticals", "Sanofi", "Healthcare", 3000),
    Product("France", "Sports Gear", "Decathlon", "Retail", 5000),

    Product("Sweden", "XC90", "Volvo", "Luxury SUV", 9000000),
    Product("Sweden", "Spotify Premium", "Spotify", "Streaming Service", 119),

    Product("Switzerland", "Submariner", "Rolex", "Luxury Watch", 1000000),
    Product("Switzerland", "Reinsurance Services", "Swiss Re", "Insurance", 3000),

    Product("Czech Republic", "Octavia", "Škoda", "Sedan", 2500000),

    Product("UK", "Consulting Services", "Deloitte", "Consulting", 3000),
    Product("UK", "Audit Services", "EY", "Consulting", 3000),
    Product("UK", "Retail Banking", "Lloyds Bank", "Finance", 2000),
    Product("UK", "Audit Services", "EY", "Consulting", 3000),
    Product("UK", "Vaccines", "GSK", "Healthcare", 3000),
    Product("UK", "Pharmaceuticals", "AstraZeneca", "Healthcare", 3000),


    Product("India", "Airdopes 141", "boAt", "Earbuds", 1500),
    Product("India", "450X", "Ather", "Electric Scooter", 150000),
    Product("India", "Vikram Rocket", "Skyroot", "Space Tech", 100000000),
    Product("India", "Zoho CRM", "Zoho", "Software", 1000),
    Product("India", "Freshdesk", "Freshworks", "Software", 2000),
    Product("India", "Attar Perfume", "Adil Quadri", "Perfume", 3000),
    Product("India", "Cloud Hosting", "Utho", "Cloud Platform", 1000),
    Product("India", "IT Services", "Infosys", "Software Services", 2000),
    Product("India", "IT Services", "Wipro", "Software Services", 2000),
    Product("India", "Engineering Services", "Cyient", "Software Services", 2000),
    Product("India", "Covaxin", "Bharat Biotech", "Vaccine", 2000),
    Product("India", "Pharmaceutical Products", "Eden Healthcare", "Healthcare", 2000),
    Product("India", "Pharmaceutical Products", "Lyra Laboratories", "Healthcare", 2000),
    Product("India", "Pharmaceutical Products", "Sygna Pharma", "Healthcare", 2000),
    Product("India", "Scorpio", "Mahindra", "SUV", 1700000),
    Product("India", "Nexon EV", "Tata", "Electric SUV", 1500000),
    Product("India", "Biryani", "Hyderabadi", "Food", 500),


    Product("Iran", "Crude Oil", "NIOC", "Energy", 1000000),
    Product("Iran", "Saffron", "Iran Farms", "Spice", 50000),

    Product("Ireland", "Consulting Services", "Accenture", "Consulting", 3000),

    Product("Japan", "Corolla", "Toyota", "Sedan", 2000000),
    Product("Japan", "Bravia 55", "Sony", "Television", 90000),
    Product("Japan", "PlayStation 5", "Sony", "Gaming Console", 55000),
    Product("Japan", "ASIMO", "Honda", "Humanoid Robot", 2500000),


    Product("South Korea", "Creta", "Hyundai", "SUV", 1500000),
    Product("South Korea", "Seltos", "Kia", "SUV", 1400000),
    Product("South Korea", "Galaxy S24", "Samsung", "Smartphone", 90000),
    Product("South Korea", "Dual Inverter AC", "LG", "Air Conditioner", 45000),

    Product("China", "Seal", "BYD", "Electric Car", 3500000),
    Product("China", "OnePlus 12", "OnePlus", "Smartphone", 65000),
    Product("China", "H1", "Unitree", "Humanoid Robot", 2000000),

    Product("Saudi Arabia", "Ajwa Dates", "Al Madinah", "Food", 3000),

    Product("UAE", "Oud Perfume", "Ajmal", "Perfume", 12000),

    Product("Qatar", "LNG Gas", "QatarEnergy", "Energy", 1000000),

    Product("Turkey", "Turkish Delight", "Hacı Bekir", "Sweet", 1500),


    Product("Germany", "Front Load Washing Machine", "Bosch", "Appliance", 50000),
]

for p in products:
    print(p)