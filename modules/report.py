from collections import Counter

def generate_report(feedbacks, output_path):
    sentiment_counts = Counter()
    category_counts = Counter()
    complaints = []

    for f in feedbacks:
        sentiment_counts[f["sentiment"]] += 1
        category_counts[f["category"]] += 1
        if f["sentiment"] == "Negative":
            complaints.append(f["message"])

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("DAILY FEEDBACK REPORT\n")
        f.write("=" * 30 + "\n\n")

        f.write("Sentiment Summary:\n")
        for k, v in sentiment_counts.items():
            f.write(f"{k}: {v}\n")

        f.write("\nMost Common Complaint:\n")
        f.write(category_counts.most_common(1)[0][0] + "\n")

        f.write("\nSample Negative Feedback:\n")
        for c in complaints[:3]:
            f.write(f"- {c}\n")

        f.write("\nSystem Suggestions:\n")
        f.write("- Improve response time\n")
        f.write("- Enhance service quality\n")
        f.write("- Monitor repeated complaints\n")

