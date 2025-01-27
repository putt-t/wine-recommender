import pickle
import base64
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train Random Forest with many trees
model = RandomForestClassifier(
    n_estimators=1000,          # Number of trees
    max_depth=None,             # Maximum depth of trees
    min_samples_split=2,        # Minimum samples required to split
    min_samples_leaf=1,         # Minimum samples required at leaf node
    bootstrap=True,             # Use bootstrap samples
    random_state=42,            # For reproducibility
    n_jobs=-1                   # Use all available cores
)

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Performance:")
print(f"Accuracy: {accuracy:.4f}")
print("\nDetailed Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Show feature importance
feature_importance = dict(zip(iris.feature_names, model.feature_importances_))
print("\nFeature Importance:")
for feature, importance in sorted(feature_importance.items(), key=lambda x: x[1], reverse=True):
    print(f"{feature}: {importance:.4f}")

# Save the model as a base64 string
model_bytes = pickle.dumps(model)
model_b64 = base64.b64encode(model_bytes).decode('utf-8')

# Save to JavaScript file
with open('model.js', 'w') as f:
    f.write(f'const MODEL_B64 = "{model_b64}";\n')
    f.write('export { MODEL_B64 };')

# Test some predictions
print("\nTesting some predictions:")
test_samples = [
    [4.8, 3.2, 1.1, 0.1],  # Likely setosa
    [5.9, 2.9, 4.3, 1.5],  # Likely versicolor
    [7.2, 3.4, 6.2, 2.4],  # Likely virginica
    [6.0, 3.0, 4.5, 1.8]   # Edge case
]

for sample in test_samples:
    prediction = model.predict([sample])
    probabilities = model.predict_proba([sample])[0]
    print(f"\nInput: {sample}")
    print(f"Predicted class: {iris.target_names[prediction[0]]}")
    print("Class probabilities:")
    for class_name, prob in zip(iris.target_names, probabilities):
        print(f"{class_name}: {prob:.4f}")

print("\nModel saved as model.js")


