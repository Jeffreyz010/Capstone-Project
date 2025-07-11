import pandas as pd
import json
import numpy as np

df = pd.read_csv("cad_questions_combined.csv")
df = df.replace({np.nan: None})

def convert_row_to_dict(row):
    return {
        "id": row["id"],
        "question": row["question"],
        "choices": {
            "A": row["opa"],
            "B": row["opb"],
            "C": row["opc"],
            "D": row["opd"]
        },
        "answer": row["cop"],
        "explanation": row["exp"],
        "subject": row["subject_name"],
        "topic": row["topic_name"],
        "type": row["choice_type"]
    }

json_data = [convert_row_to_dict(row) for _, row in df.iterrows()]

with open("cad_questions_combined.json", "w") as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)

print("JSON file has been successfully created: cad_questions.json")