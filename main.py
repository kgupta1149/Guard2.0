import joblib

_model = None
_vectorizer = None

def load_artifacts():
    """
    Lazy-load model/vectorizer so importing this module doesn't require
    local .pkl files (important for unit tests and CI).
    """
    global _model, _vectorizer
    if _model is None or _vectorizer is None:
        _model = joblib.load("phish_model.pkl")
        _vectorizer = joblib.load("vectorizer.pkl")
    return _model, _vectorizer

def scan_url(url, model_obj=None, vectorizer_obj=None):
    # Use injected fakes for unit tests; otherwise lazy-load real artifacts
    if model_obj is None or vectorizer_obj is None:
        model_obj, vectorizer_obj = load_artifacts()

    url_vector = vectorizer_obj.transform([url])
    prediction = model_obj.predict(url_vector)
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
