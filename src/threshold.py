import numpy as np

def threshold_analysis(results, thresholds):
    scores = np.array([r["score"] for r in results])
    correctness = np.array([1 if r["is_correct"] else 0 for r in results])

    acc_list = []
    coverage_list = []

    for t in thresholds:
        mask = scores >= t
        if mask.any():
            acc_list.append(correctness[mask].mean())
            coverage_list.append(mask.mean())
        else:
            acc_list.append(0)
            coverage_list.append(0)

    return acc_list, coverage_list
