from collections import namedtuple



Product = namedtuple('Product', ('country', 'name', 'brand', 'type', 'price'))


# Country-wise Product Dataset (Full, Unmodified)
products =[

# Global
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
Product("USA", "Innerwear & Apparel", "Jockey", "Clothing", 2000),
Product("USA", "Harvard Medical School", "Harvard", "Medical College", 0),
Product("USA", "Harvard Business School", "Harvard", "B-School", 0),
Product("USA", "Stanford Graduate School of Business", "Stanford", "B-School", 0),
Product("USA", "USC School of Cinematic Arts", "USC", "Film Institute", 0),
Product("USA", "American Film Institute", "AFI", "Film Institute", 0),
Product("USA", "Harvard Law School", "Harvard", "Law College", 0),
Product("USA", "Yale Law School", "Yale", "Law College", 0),
Product("USA", "Interactive Coding Courses", "Educative", "EdTech", 2000),
Product("USA", "Frontend Playground", "CodePen", "Developer Tool", 0),
Product("USA", "DSA Courses", "AlgoExpert", "EdTech", 2000),
Product("USA", "Online Courses", "Udemy", "EdTech", 2000),
Product("USA", "Online Courses", "Coursera", "EdTech", 2000),

# Finland
Product("Finland", "Linux", "Linus Torvalds", "Operating System", 0),



# France
Product("France", "Mistral AI", "Mistral", "AI Model", 2000),
Product("France", "Handbag", "Louis Vuitton", "Luxury Fashion", 200000),
Product("France", "Pharmaceuticals", "Sanofi", "Healthcare", 3000),
Product("France", "Sports Gear", "Decathlon", "Retail", 5000),
Product("France", "Sorbonne University", "Sorbonne", "University", 0),
Product("France", "Sorbonne Medical School", "Sorbonne", "Medical College", 0),
Product("France", "INSEAD", "INSEAD", "B-School", 0),
Product("France", "La Fémis", "Femis", "Film Institute", 0),

# Sweden
Product("Sweden", "XC90", "Volvo", "Luxury SUV", 9000000),
Product("Sweden", "Spotify Premium", "Spotify", "Streaming Service", 119),
Product("Sweden", "KTH Royal Institute of Technology", "KTH", "University", 0),
Product("Sweden", "Karolinska Institute", "Karolinska", "Medical College", 0),
Product("Sweden", "Stockholm School of Economics", "SSE", "B-School", 0),
Product("Sweden", "Stockholm University of the Arts", "SKH", "Film Institute", 0),


# Czech Republic
Product("Czech Republic", "Octavia", "Škoda", "Sedan", 2500000),
Product("Czech Republic", "IntelliJ IDEA", "JetBrains", "IDE", 0),
Product("Czech Republic", "Charles University", "Charles University", "University", 0),
Product("Czech Republic", "Charles University Faculty of Medicine", "Charles", "Medical College", 0),
Product("Czech Republic", "University of Economics Prague", "VSE", "B-School", 0),
Product("Czech Republic", "FAMU", "FAMU", "Film Institute", 0),

# Switzerland
Product("Switzerland", "Submariner", "Rolex", "Luxury Watch", 1000000),
Product("Switzerland", "Reinsurance Services", "Swiss Re", "Insurance", 3000),
Product("Switzerland", "University of Zurich Faculty of Medicine", "UZH", "Medical College", 0),


# UK
Product("UK", "Consulting Services", "Deloitte", "Consulting", 3000),
Product("UK", "Audit Services", "EY", "Consulting", 3000),
Product("UK", "Retail Banking", "Lloyds Bank", "Finance", 2000),
Product("UK", "Audit Services", "EY", "Consulting", 3000),
Product("UK", "Vaccines", "GSK", "Healthcare", 3000),
Product("UK", "Pharmaceuticals", "AstraZeneca", "Healthcare", 3000),
Product("UK", "Enterprise Software", "Micro Focus (OpenText)", "Software", 5000),
Product("UK", "University of Oxford", "Oxford", "University", 0),
Product("UK", "University of Oxford Medical School", "Oxford", "Medical College", 0),
Product("UK", "London Business School", "LBS", "B-School", 0),
Product("UK", "National Film and Television School", "NFTS", "Film Institute", 0),
Product("UK", "Oxford Faculty of Law", "Oxford", "Law College", 0),


# Italy
Product("Italy", "Sunglasses", "Ray-Ban", "Eyewear", 5000),

#Spanish
Product("Spain", "Olive Oil", "Extra Virgin", "Food", 1200),

# India
Product("India", "Tadipatri", "Anantapur", "Town", 0),
Product("India", "Proddatur", "Kadapa", "Town", 0),
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
Product("India", "Yogi Vemana University", "Kadapa", "University", 0),
Product("India", "IIT Kadapa", "IIT", "Engineering Institute (Future)", 0),
Product("India", "RIMS Kadapa", "RIMS", "Medical College", 0),
Product("India", "Cosmetics", "Sugar Cosmetics", "Beauty", 1000),
Product("India", "Pharmaceutical Products", "Panm Labs", "Pharma", 2000),
Product("India", "Eyewear", "Lenskart", "Retail", 3000),
Product("India", "Jewelry", "Palmonas", "Fashion", 2000),
Product("India", "Gold & Diamond Jewelry", "Malabar", "Jewelry", 50000),
Product("India", "Gold & Diamond Jewelry", "Kalyan Jewellers", "Jewelry", 50000),
Product("India", "Gold Jewelry", "Lalitha Jewellery", "Jewelry", 50000),
Product("India", "Gold & Diamond Jewelry", "Joyalukkas", "Jewelry", 50000),
Product("India", "Gold Jewelry", "Khazana Jewellery", "Jewelry", 50000),
Product("India", "AIIMS Delhi", "AIIMS", "Medical College", 0),
Product("India", "Osmania University & Medical College Hyderabad", "Osmania", "University & Medical College", 0),
Product("India", "IIM Ahmedabad", "IIM", "B-School", 0),
Product("India", "FTII Pune", "FTII", "Film Institute", 0),
Product("India", "Ramanaidu Film School Hyderabad", "Ramanaidu", "Film Institute", 0),
Product("India", "MGR Film Institute Chennai", "MGR", "Film Institute", 0),
Product("India", "Interview Preparation", "Interview Ready", "EdTech", 2000),
Product("India", "Career Upskilling", "Take U Forward", "EdTech", 2000),
Product("India", "Programming Courses", "Chai aur Code", "EdTech", 2000),
Product("India", "Math & Logic Learning", "Log2Base2", "EdTech", 2000),
Product("India", "DSA & Interview Prep", "LearnYard", "EdTech", 2000),
Product("India", "YSR Sports School Kadapa", "YSR Sports School", "Sports School", 0),
Product("India", "Anantapur Sports Village", "RF Youth Sports", "Sports Academy", 0),

# Russia
Product("Russia", "Kaspersky", "Kaspersky", "Cybersecurity", 2000),


# Canada
Product("Canada", "Enterprise Information Management", "OpenText", "Enterprise Software", 5000),
Product("Canada", "University of Toronto Faculty of Medicine", "Toronto", "Medical College", 0),

# Iran
Product("Iran", "Crude Oil", "NIOC", "Energy", 1000000),
Product("Iran", "Saffron", "Iran Farms", "Spice", 50000),
Product("Iran", "University of Tehran", "Tehran", "University", 0),
Product("Iran", "Sharif University of Technology", "Sharif", "University", 0),

# Iraq
Product("Iraq", "University of Baghdad", "Baghdad", "University", 0),

# Ireland
Product("Ireland", "Consulting Services", "Accenture", "Consulting", 3000),


# Japan
Product("Japan", "Corolla", "Toyota", "Sedan", 2000000),
Product("Japan", "Bravia 55", "Sony", "Television", 90000),
Product("Japan", "PlayStation 5", "Sony", "Gaming Console", 55000),
Product("Japan", "ASIMO", "Honda", "Humanoid Robot", 2500000),
Product("Japan", "University of Tokyo", "UTokyo", "University", 0),
Product("Japan", "University of Tokyo Faculty of Medicine", "UTokyo", "Medical College", 0),


# China
Product("China", "Seal", "BYD", "Electric Car", 3500000),
Product("China", "OnePlus 12", "OnePlus", "Smartphone", 65000),
Product("China", "H1", "Unitree", "Humanoid Robot", 2000000),
Product("China", "Tsinghua University", "Tsinghua", "University", 0),
Product("China", "Peking University Health Science Center", "Peking", "Medical College", 0),
Product("China", "CEIBS", "CEIBS", "B-School", 0),
Product("China", "Beijing Film Academy", "BFA", "Film Institute", 0),

# Qatar
Product("Qatar", "LNG Gas", "QatarEnergy", "Energy", 1000000),

# Saudi Arabia
Product("Saudi Arabia", "Ajwa Dates", "Al Madinah", "Food", 3000),
Product("Saudi Arabia", "King Saud University", "KSU", "University", 0),
Product("Saudi Arabia", "Islamic University of Madinah", "IUM", "University", 0),
Product("Saudi Arabia", "King Saud University College of Medicine", "KSU", "Medical College", 0),
Product("Saudi Arabia", "Prince Mohammed Bin Salman College", "MBSC", "B-School", 0),
Product("Saudi Arabia", "Effat University Film School", "Effat", "Film Institute", 0),

# UAE
Product("UAE", "Oud Perfume", "Ajmal", "Perfume", 12000),
Product("UAE", "Fashion Retail", "Max", "Clothing", 2000),

# Singapore
Product("Singapore", "NUS Faculty of Law", "NUS", "Law College", 0),
Product("Singapore", "DevOps Learning", "KodeKloud", "EdTech", 2000),

# South Korea
Product("South Korea", "Creta", "Hyundai", "SUV", 1500000),
Product("South Korea", "Seltos", "Kia", "SUV", 1400000),
Product("South Korea", "Galaxy S24", "Samsung", "Smartphone", 90000),
Product("South Korea", "Dual Inverter AC", "LG", "Air Conditioner", 45000),

# Turkey
Product("Turkey", "Turkish Delight", "Hacı Bekir", "Sweet", 1500),
Product("Turkey", "Restaurant Chain", "CZN Burak", "Food Chain", 3000),

#Portugal
Product("Portugal", "Cristiano Ronaldo", "Football", "Athlete", 0),

# Germany
Product("Germany", "Front Load Washing Machine", "Bosch", "Appliance", 50000),
Product("Germany", "G-Class (G-Wagon)", "Mercedes-Benz", "Luxury SUV", 30000000)

]

for p in products:
    print(p)