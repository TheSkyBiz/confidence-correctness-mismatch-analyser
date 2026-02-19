import numpy as np

def compute_ece(results, n_bins=10):
    scores = np.array([min(max(r["score"], 0), 1) for r in results])
    correctness = np.array([1 if r["is_correct"] else 0 for r in results])

    bins = np.linspace(0, 1, n_bins + 1)
    binids = np.digitize(scores, bins) - 1

    ece = 0.0

    for i in range(n_bins):
        mask = binids == i
        if np.any(mask):
            bin_acc = correctness[mask].mean()
            bin_conf = scores[mask].mean()
            ece += np.abs(bin_acc - bin_conf) * (mask.sum() / len(scores))

    return ece