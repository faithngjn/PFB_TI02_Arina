import csv
from pathlib import Path

# Create a file path to the csv file.
fp = Path.cwd() /"project_group"/"csv_reports"/ "Overheads.csv"

# Read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file, delimiter=",")
    next(reader) # Skip header

    # Create an empty list for Overhead_data
    Overhead_data = []
    Overhead_name = []
    # Append cash-on-hand data into Overhead_data list
    for row in reader:
        # Get the cash
        # and append to the deliveryRecords list
        Overhead_data.append(float(row[1]))
        Overhead_name.append(row[0])

#Find the greatest overhead
def compute_highest(Overhead_data, Overhead_name):
    "function will find the highest overhead and display the data"
    highest_overhead = max(Overhead_data)
    category_index = Overhead_data.index(highest_overhead)
    category_name = Overhead_name[category_index].upper()
    print(f"[HIGHEST OVERHEAD] {category_name}: {highest_overhead}")

compute_highest(Overhead_data, Overhead_name)
