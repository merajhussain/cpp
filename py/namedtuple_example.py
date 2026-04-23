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

    Product("France", "Mistral AI", "Mistral", "AI Model", 2000),
    Product("France", "Handbag", "Louis Vuitton", "Luxury Fashion", 200000),

    Product("Sweden", "XC90", "Volvo", "Luxury SUV", 9000000),
    Product("Sweden", "Spotify Premium", "Spotify", "Streaming Service", 119),

    Product("India", "Airdopes 141", "boAt", "Earbuds", 1500),
    Product("India", "450X", "Ather", "Electric Scooter", 150000),
    Product("India", "Vikram Rocket", "Skyroot", "Space Tech", 100000000),
    Product("India", "Zoho CRM", "Zoho", "Software", 1000),
    Product("India", "Freshdesk", "Freshworks", "Software", 2000),
    Product("India", "Attar Perfume", "Adil Quadri", "Perfume", 3000),

    Product("Czech Republic", "Octavia", "Škoda", "Sedan", 2500000),
    Product("Switzerland", "Submariner", "Rolex", "Luxury Watch", 1000000),

    Product("Iran", "Crude Oil", "NIOC", "Energy", 1000000),
    Product("Iran", "Saffron", "Iran Farms", "Spice", 50000),

    Product("Japan", "Corolla", "Toyota", "Sedan", 2000000),
    Product("Japan", "Bravia 55", "Sony", "Television", 90000),


    Product("South Korea", "Creta", "Hyundai", "SUV", 1500000),
    Product("South Korea", "Seltos", "Kia", "SUV", 1400000),
    Product("South Korea", "Galaxy S24", "Samsung", "Smartphone", 90000),
    Product("South Korea", "Dual Inverter AC", "LG", "Air Conditioner", 45000),

    Product("China", "Seal", "BYD", "Electric Car", 3500000),
    Product("China", "OnePlus 12", "OnePlus", "Smartphone", 65000),

    Product("Saudi Arabia", "Ajwa Dates", "Al Madinah", "Food", 3000),

    Product("UAE", "Oud Perfume", "Ajmal", "Perfume", 12000),

    Product("Qatar", "LNG Gas", "QatarEnergy", "Energy", 1000000),

    Product("Turkey", "Turkish Delight", "Hacı Bekir", "Sweet", 1500),
]

for p in products:
    print(p)