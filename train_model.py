import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from utils import clean_text

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "sample_data", "demo_cyber_data.csv"))

print("Loading CSV from:", CSV_PATH)

df = pd.read_csv(CSV_PATH)
df["clean"] = df["text"].apply(clean_text)

X = df["clean"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipe = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=500))
])

pipe.fit(X_train, y_train)

MODEL_PATH = os.path.join(BASE_DIR, "cyber_pipeline.joblib")
joblib.dump(pipe, MODEL_PATH)

print("\nModel training complete!")
print("Saved model at:", MODEL_PATH)
