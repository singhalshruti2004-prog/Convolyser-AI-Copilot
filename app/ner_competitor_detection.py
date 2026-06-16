from transformers import pipeline

ner = pipeline(
    "ner",
    model="dslim/bert-base-NER",
    aggregation_strategy="simple"
)

text = input("Enter customer message: ")

entities = ner(text)

organizations = []

for entity in entities:
    if entity["entity_group"] == "ORG":
        organizations.append(entity["word"])

print("\nOrganizations Found:\n")

if organizations:
    for org in organizations:
        print(org)
else:
    print("No organization found.")