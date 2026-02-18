
class CheckCancerProbability(object):
    """description of class"""


import json
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# -----------------------------
# 1. Generate Synthetic Dataset
# -----------------------------

np.random.seed(42)

n_samples = 1000

microplastic = np.random.uniform(0, 100, n_samples)
pm25 = np.random.uniform(0, 150, n_samples)
inflammation = np.random.uniform(0, 100, n_samples)
years = np.random.uniform(0, 40, n_samples)

risk_score = (
    0.04 * microplastic +
    0.03 * pm25 +
    0.05 * inflammation +
    0.02 * years
)

probability = 1 / (1 + np.exp(-risk_score + 5))
labels = (probability > 0.5).astype(int)

data = pd.DataFrame({
    "microplastic": microplastic,
    "pm25": pm25,
    "inflammation": inflammation,
    "years": years,
    "label": labels
})

# -----------------------------
# 2. Train Logistic Regression
# -----------------------------

X = data[["microplastic", "pm25", "inflammation", "years"]]
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy:.2f}")


# -----------------------------
# 3. Lambda Handler
# -----------------------------

def CheckCancerProbability(input_array):
    # input_array: [microplastic, pm25, inflammation, years]
    input_data = np.array([[float(input_array[0]),
                            float(input_array[1]),
                            float(input_array[2]),
                            float(input_array[3])]])
    probability = model.predict_proba(input_data)[0][1]
    return {
        "simulated_probability": round(float(probability), 4),
        "model_accuracy": round(float(accuracy), 2),
        "disclaimer": "Model trained on synthetic research data. Not a medical diagnosis."
    }