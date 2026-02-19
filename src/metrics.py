def compute_accuracy(results):
    return sum(r["is_correct"] for r in results) / len(results)

def compute_overconfidence(results, threshold=0.75):
    return len(
        [r for r in results if (not r["is_correct"]) and r["score"] > threshold]
    ) / len(results)