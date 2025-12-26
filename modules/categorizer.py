def categorize_feedback(message):
    msg = message.lower()

    if any(word in msg for word in ["delay", "late", "shipping"]):
        return "Delivery Delay"
    elif any(word in msg for word in ["bill", "charge", "payment"]):
        return "Billing Problem"
    elif any(word in msg for word in ["app", "website", "login", "error"]):
        return "App/Website Issue"
    elif any(word in msg for word in ["service", "support", "staff"]):
        return "Service Issue"
    elif any(word in msg for word in ["thank", "love", "great"]):
        return "General Appreciation"
    else:
        return "Other"
