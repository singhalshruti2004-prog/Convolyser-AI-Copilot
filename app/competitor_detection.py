competitors = [
    "airtel",
    "jio",
    "vodafone",
    "vi",
    "bsnl"
]

text = input("Enter customer message: ")

text = text.lower()

found = []

for competitor in competitors:
    if competitor in text:
        found.append(competitor)

if found:
    print("Competitor Mentioned:")
    for company in found:
        print(company.title())
else:
    print("No competitor mentioned.")