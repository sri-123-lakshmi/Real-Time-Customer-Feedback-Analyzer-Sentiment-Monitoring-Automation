
import logging
from collections import defaultdict

logging.basicConfig(
    filename="logs/negative_alerts.log",
    level=logging.WARNING,
    format="%(asctime)s - %(message)s"
)

customer_complaints = defaultdict(int)

def log_negative(feedback):
    customer_complaints[feedback["customer_id"]] += 1
    urgent = customer_complaints[feedback["customer_id"]] > 1

    message = f"Customer {feedback['customer_id']} | {feedback['message']}"
    if urgent:
        message += " | URGENT REPEATED COMPLAINT"

    logging.warning(message)
    return urgent
