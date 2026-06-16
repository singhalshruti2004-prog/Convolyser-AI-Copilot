from transformers import pipeline

print("Loading AI model...")

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

print("Model loaded!")

text = input("Enter customer message: ")

candidate_labels = [
    "Network Issue",
    "Billing Issue",
    "Support Issue",
    "App Issue",
    "Technical Issue"
]

result = classifier(
    text,
    candidate_labels
)

print("\nRoot Cause Predictions:\n")

for label, score in zip(
    result["labels"],
    result["scores"]
):
    print(
        f"{label}: {score*100:.2f}%"
    ) 