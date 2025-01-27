import pandas as pd
import json

data_loc = "../data/XWines_Slim_1K_wines.csv"
df = pd.read_csv(data_loc)

columns_of_interest = ["Country", "Acidity", "Body", "Harmonize", "ABV", "Grapes", "Elaborate", "Type", "WineName"]
df = df[columns_of_interest]

df = df.drop_duplicates()

form_data = {}

categorical_columns = ["Country", "Grapes", "Type", "Harmonize", "Elaborate", "WineName"]
for col in categorical_columns:
    form_data[col] = df[col].dropna().unique().tolist()

numeric_columns = ["Acidity", "Body", "ABV"]
for col in numeric_columns:
    form_data[col] = {
        "min": df[col].min(),
        "max": df[col].max(),
        "step": 0.1
    }

with open("form_data.json", "w") as f:
    json.dump(form_data, f)
