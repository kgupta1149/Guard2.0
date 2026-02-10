import pandas as pnd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
data = pnd.read_csv("dataset.csv")

# Split into inputs (X) and targets (y)
X = data["url"]             # URLs as input
y = data["label"]           # Labels (0 = safe, 1 = phishing)

# Convert URLs to number vectors
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Split into training/testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42)

# Create and train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict and evaluate accuracy
y_pred = model.predict(X_test)
print("✅ Model accuracy:", accuracy_score(y_test, y_pred))

# Save the model + vectorizer
joblib.dump(model, "phish_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

# 🔴 You can't use this line yet — it's missing "new_url_vector"
# loaded_model = joblib.load("phish_model.pkl")
# result = loaded_model.predict(new_url_vector)


