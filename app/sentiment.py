from transformers import pipeline

# Load sentiment analysis model
classifier = pipeline("sentiment-analysis")

# Get customer message
text = input("Enter customer message: ")

# Predict sentiment
result = classifier(text)

# Extract values
sentiment = result[0]["label"]
confidence = result[0]["score"]

# Display results
print("\n----- Convolyser AI Analysis -----")
print(f"Sentiment : {sentiment}")
print(f"Confidence: {confidence*100:.2f}%")
print("----------------------------------")