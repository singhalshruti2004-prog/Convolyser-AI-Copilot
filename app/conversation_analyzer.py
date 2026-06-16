from transformers import pipeline
classifier = pipeline("sentiment-analysis")
competitors=["airtel","jio","vodafone","vi","bsnl"]
text=input("enter customer message:")
result=classifier(text)
sentiment=result[0]["label"]
confidence=result[0]["score"]
text_lower=text.lower()
found=[]
for competitor in competitors:
    if competitor in text_lower:
        found.appnd(competitor)
print("\n----- Convolyser AI Analysis -----")
print(f"Sentiment : {sentiment}")
print(f"Confidence: {confidence*100:.2f}%")
if found:
    for company in found:
        print(company.title())
else:    print("No competitor mentioned.")
print("----------------------------------")