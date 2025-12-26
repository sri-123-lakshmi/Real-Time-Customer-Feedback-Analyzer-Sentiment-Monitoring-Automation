from modules.reader import read_txt, read_csv
from modules.sentiment import analyze_sentiment
from modules.categorizer import categorize_feedback
from modules.alerts import log_negative
from modules.report import generate_report
from collections import Counter

feedbacks = []

feedbacks.extend(read_txt("data/feedback_today.txt"))
feedbacks.extend(read_txt("data/chat_logs.txt"))
feedbacks.extend(read_csv("data/email_feedback.csv"))

alert_count = 0
dashboard = Counter()

for f in feedbacks:
    score, sentiment = analyze_sentiment(f["message"])
    category = categorize_feedback(f["message"])

    f["sentiment"] = sentiment
    f["category"] = category

    dashboard[sentiment] += 1
    dashboard[category] += 1

    if sentiment == "Negative":
        if log_negative(f):
            alert_count += 1

generate_report(feedbacks, "output/daily_feedback_report.txt")

print("\n📊 REAL-TIME DASHBOARD")
print("-" * 25)
print("Sentiment Counts:")
print("Positive:", dashboard["Positive"])
print("Neutral:", dashboard["Neutral"])
print("Negative:", dashboard["Negative"])

print("\nComplaint Categories:")
for k in dashboard:
    if k not in ["Positive", "Neutral", "Negative"]:
        print(k, ":", dashboard[k])

print("\n🚨 Alerts Triggered Today:", alert_count)

