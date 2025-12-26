import csv
from datetime import datetime

def read_txt(file_path):
    feedbacks = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or "|" not in line:
                continue  

            parts = line.split("|", 2)
            if len(parts) != 3:
                continue  

            timestamp, customer_id, message = parts

            feedbacks.append({
                "timestamp": timestamp,
                "customer_id": customer_id,
                "message": message
            })
    return feedbacks


def read_csv(file_path):
    feedbacks = []
    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            feedbacks.append({
                "timestamp": row["timestamp"],
                "customer_id": row["customer_id"],
                "message": row["message"]
            })
    return feedbacks

