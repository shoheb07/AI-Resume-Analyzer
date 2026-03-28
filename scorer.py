def calculate_score(matched, total_keywords):
    if total_keywords == 0:
        return 0
    return int((len(matched) / total_keywords) * 100)
