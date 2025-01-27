import pickle
import base64
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a decision tree classifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Save the model as a base64 string
model_bytes = pickle.dumps(model)
model_b64 = base64.b64encode(model_bytes).decode('utf-8')

# Save to JavaScript file
with open('model.js', 'w') as f:
    f.write(f'const MODEL_B64 = "{model_b64}";\n')
    f.write('export { MODEL_B64 };')

print("Model saved as model.js")
