"""Print basic summary statistics for a small list of numbers."""

from collections import Counter


def median(values):
    """Middle value of the sorted data; the average of the two middle values when the count is even."""
    ordered = sorted(values)
    n = len(ordered)
    mid = n // 2
    if n % 2 == 1:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2


def modes(values):
    """Every value that appears the most times."""
    counts = Counter(values)
    top = max(counts.values())
    return sorted(v for v, c in counts.items() if c == top)


def calculate_measurements(data):
    print("--- Standard Measurement & Statistics Calculator ---")

    total_sum = sum(data)
    count = len(data)
    mean = total_sum / count

    print(f"Dataset: {data}")
    print(f"Total Sum: {total_sum}")
    print(f"Count of Items: {count}")
    print(f"Calculated Mean: {mean:.2f}")
    print(f"Calculated Median: {median(data)}")
    print(f"Mode(s): {', '.join(str(m) for m in modes(data))}")
    print(f"Range: {max(data) - min(data)} (min {min(data)}, max {max(data)})")


if __name__ == "__main__":
    # Sample dataset. Change these numbers to try your own.
    sample = [15, 22, 34, 45, 22, 67, 89, 22, 45]
    calculate_measurements(sample)
