from collections import namedtuple



Product = namedtuple('Product', ('country', 'name', 'brand', 'type', 'price'))


products = [


    Product("Global", "Quran", "Islam", "Religious Book", 0),
    Product("Global", "Bhagavad Gita", "Hinduism", "Religious Book", 0),
    Product("Global", "Vedas", "Hinduism", "Religious Book", 0),
    Product("Global", "Guru Granth Sahib", "Sikhism", "Religious Book", 0),
    Product("Global", "Bible", "Christianity", "Religious Book", 0),
    Product("Global", "Torah", "Judaism", "Religious Book", 0),
    Product("Global", "Tripitaka", "Buddhism", "Religious Book", 0),
    Product("Global", "Avesta", "Zoroastrianism", "Religious Book", 0),
    Product("Global", "Tao Te Ching", "Taoism", "Religious Book", 0),
    Product("Global", "Analects", "Confucianism", "Religious Book", 0),



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
    Product("USA", "Visual Studio", "Microsoft", "IDE", 0),
    Product("USA", "vi", "Unix", "Text Editor", 0),
    Product("USA", "VS Code", "Microsoft", "Code Editor", 0),
    Product("USA", "SecureAnywhere", "Webroot (OpenText)", "Antivirus", 2000),
    Product("USA", "MIT", "Massachusetts Institute of Technology", "University", 0),
    Product("USA", "Harvard University", "Harvard", "University", 0),
    Product("USA", "Stanford University", "Stanford", "University", 0),
    Product("USA", "iPhone 17 Pro Max", "Apple", "iOS", 150000),
    Product("USA", "Pixel 9", "Google", "Android", 80000),

    Product("Finland", "Linux", "Linus Torvalds", "Operating System", 0),

    Product("France", "Mistral AI", "Mistral", "AI Model", 2000),
    Product("France", "Handbag", "Louis Vuitton", "Luxury Fashion", 200000),
    Product("France", "Pharmaceuticals", "Sanofi", "Healthcare", 3000),
    Product("France", "Sports Gear", "Decathlon", "Retail", 5000),
    Product("France", "Sorbonne University", "Sorbonne", "University", 0),


    Product("Sweden", "XC90", "Volvo", "Luxury SUV", 9000000),
    Product("Sweden", "Spotify Premium", "Spotify", "Streaming Service", 119),
    Product("Sweden", "KTH Royal Institute of Technology", "KTH", "University", 0),

    Product("Switzerland", "Submariner", "Rolex", "Luxury Watch", 1000000),
    Product("Switzerland", "Reinsurance Services", "Swiss Re", "Insurance", 3000),

    Product("Czech Republic", "Octavia", "Škoda", "Sedan", 2500000),
    Product("Czech Republic", "IntelliJ IDEA", "JetBrains", "IDE", 0),
    Product("Czech Republic", "Charles University", "Charles University", "University", 0),

    Product("UK", "Consulting Services", "Deloitte", "Consulting", 3000),
    Product("UK", "Audit Services", "EY", "Consulting", 3000),
    Product("UK", "Retail Banking", "Lloyds Bank", "Finance", 2000),
    Product("UK", "Audit Services", "EY", "Consulting", 3000),
    Product("UK", "Vaccines", "GSK", "Healthcare", 3000),
    Product("UK", "Pharmaceuticals", "AstraZeneca", "Healthcare", 3000),
    Product("UK", "Enterprise Software", "Micro Focus (OpenText)", "Software", 5000),
    Product("UK", "University of Oxford", "Oxford", "University", 0),


    Product("Canada", "Enterprise Information Management", "OpenText", "Enterprise Software", 5000),

    Product("India", "Airdopes 141", "boAt", "Earbuds", 1500),
    Product("India", "450X", "Ather", "Electric Scooter", 150000),
    Product("India", "Vikram Rocket", "Skyroot", "Space Tech", 100000000),
    Product("India", "Zoho CRM", "Zoho", "Software", 1000),
    Product("India", "Freshdesk", "Freshworks", "Software", 2000),
    Product("India", "Attar Perfume", "Adil Quadri", "Perfume", 3000),
    Product("India", "Cloud Hosting", "Utho", "Cloud Platform", 1000),
    Product("India", "IT Services", "Infosys", "Software Services", 2000),
    Product("India", "IT Services", "Wipro", "Software Services", 2000),
    Product("India", "Engineering & IT Services", "Cyient", "Software Services", 2000),
    Product("India", "Covaxin", "Bharat Biotech", "Vaccine", 2000),
    Product("India", "Pharmaceutical Products", "Eden Healthcare", "Healthcare", 2000),
    Product("India", "Pharmaceutical Products", "Lyra Laboratories", "Healthcare", 2000),
    Product("India", "Pharmaceutical Products", "Sygna Pharma", "Healthcare", 2000),
    Product("India", "Scorpio", "Mahindra", "SUV", 1700000),
    Product("India", "Nexon EV", "Tata", "Electric SUV", 1500000),
    Product("India", "Biryani", "Hyderabadi", "Food", 500),
    Product("India", "IISc Bangalore", "Indian Institute of Science", "University", 0),
    Product("India", "III Hyderabad", "Indian Institute of Technology Hyderabad", "University", 0),
    Product("India", "IIT Madras", "Indian Institute of Technology Madras", "University", 0),
    Product("India", "IIIT Kurnool", "Indian Institute of Information Technology Kurnool", "University", 0),
    Product("India", "IIT Tirupati", "Indian Institute of Technology Tirupati", "University", 0),
    Product("India", "IIT Delhi", "Indian Institute of Technology Delhi", "University", 0),
    Product("India", "900 sqft House", "Individual", "3-BHK", 6000000),
    Product("India", "Meteor-350", "Royal Enfield", "Bike", 300000),


    Product("Russia", "Kaspersky", "Kaspersky", "Cybersecurity", 2000),


    Product("Iran", "Crude Oil", "NIOC", "Energy", 1000000),
    Product("Iran", "Saffron", "Iran Farms", "Spice", 50000),

    Product("Ireland", "Consulting Services", "Accenture", "Consulting", 3000),

    Product("Japan", "Corolla", "Toyota", "Sedan", 2000000),
    Product("Japan", "Bravia 55", "Sony", "Television", 90000),
    Product("Japan", "PlayStation 5", "Sony", "Gaming Console", 55000),
    Product("Japan", "ASIMO", "Honda", "Humanoid Robot", 2500000),
    Product("Japan", "University of Tokyo", "UTokyo", "University", 0),


    Product("South Korea", "Creta", "Hyundai", "SUV", 1500000),
    Product("South Korea", "Seltos", "Kia", "SUV", 1400000),
    Product("South Korea", "Galaxy S24", "Samsung", "Smartphone", 90000),
    Product("South Korea", "Dual Inverter AC", "LG", "Air Conditioner", 45000),

    Product("China", "Seal", "BYD", "Electric Car", 3500000),
    Product("China", "OnePlus 12", "OnePlus", "Smartphone", 65000),
    Product("China", "H1", "Unitree", "Humanoid Robot", 2000000),
    Product("China", "Tsinghua University", "Tsinghua", "University", 0),

    Product("Saudi Arabia", "Ajwa Dates", "Al Madinah", "Food", 3000),
    Product("Saudi Arabia", "King Saud University", "KSU", "University", 0),
    Product("Saudi Arabia", "Islamic University of Madinah", "IUM", "University", 0),

    Product("UAE", "Oud Perfume", "Ajmal", "Perfume", 12000),

    Product("Qatar", "LNG Gas", "QatarEnergy", "Energy", 1000000),

    Product("Turkey", "Turkish Delight", "Hacı Bekir", "Sweet", 1500),








    Product("Germany", "Front Load Washing Machine", "Bosch", "Appliance", 50000),


]

for p in products:
    print(p)


