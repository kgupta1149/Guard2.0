import joblib

# Load saved model and vectorizer
model = joblib.load("phish_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def scan_url(url,model=model, vectorizer=vectorizer):
    # Turn input into a format the model understands
    url_vector = vectorizer.transform([url])
    prediction = model.predict(url_vector)
    return "⚠️ Phishing" if prediction[0] == 1 else "✅ Safe"

def main():
    print("🛡️  AutoPhishGuard - Smart URL Scanner")
    while True:
        url = input("🔗 Enter a URL (or type 'exit' to quit): ")
        if url.lower() == "exit":
            break
        result = scan_url(url)
        print("🔍 Result:", result)
        print()

if __name__ == "__main__":
    main()
