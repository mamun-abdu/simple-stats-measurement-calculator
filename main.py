import math

def calculate_measurements():
    print("--- Standard Measurement & Statistics Calculator ---")
    # Sample dataset
    data = [15, 22, 34, 45, 22, 67, 89, 22, 45]
    
    # Basic Calculations
    total_sum = sum(data)
    count = len(data)
    mean = total_sum / count
    
    # Sorting for Median
    sorted_data = sorted(data)
    median = sorted_data[count // 2]

    print(f"Dataset: {data}")
    print(f"Total Sum: {total_sum}")
    print(f"Count of Items: {count}")
    print(f"Calculated Mean: {mean:.2f}")
    print(f"Calculated Median: {median}")

if __name__ == "__main__":
    calculate_measurements()
