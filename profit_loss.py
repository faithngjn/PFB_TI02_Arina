import csv
from pathlib import Path

# Create a file path to the csv file.
file_path = Path.cwd() / "project_group"/"csv_reports"/"Profits_And_Loss.csv"

# Read the csv file
with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    
    reader = csv.reader(file, delimiter=",")

     # Skip header
    next(reader) 

    # Create an empty list for ProfitRecords
    ProfitRecords = [(int(row[0]), float(row[4])) for row in reader]

# Find the profit difference between all days in data
def calculate_difference(ProfitRecords):
    
    "function determine the difference in net profit"
    
    # List comprehension to calculate the difference for each day
    all_profit_differences = [
        (ProfitRecords[item][0], ProfitRecords[item][1] - ProfitRecords[item - 1][1])
        for item in range(1, len(ProfitRecords))
    ]

    return all_profit_differences

# Call the function to get profit differences
all_profit_differences = calculate_difference(ProfitRecords)

# Find whether net profit is always fluctuating, increasing or decreasing
def calculateExtreme(all_profit_differences):
    "function determine the pattern of net profit and find the data corresponding to the pattern"
    
    # Check if all net profit differences are positive
    if all(value[1] > 0 for value in all_profit_differences):

        # Net profit is increasing
        highest_increment_day, highest_increment_amount = max(all_profit_differences, key=get_second_element)

        print("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

        # Print details of the highest net profit surplus
        print(f"[HIGHEST NET PROFIT SURPLUS] DAY: {highest_increment_day}, AMOUNT: SGD{abs(int(highest_increment_amount))}.")

    # Check to see if all net profit differences are negative
    elif all(value[1] < 0 for value in all_profit_differences):

        # Net profit is decreasing
        lowest_decrement_day, lowest_decrement_amount = min(all_profit_differences, key=get_second_element)

        print("[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN THE PREVIOUS DAY")

        # Print details of the highest net profit deficit
        print(f"[HIGHEST NET PROFIT DEFICIT] DAY: {lowest_decrement_day} AMOUNT: SGD{abs(int(lowest_decrement_amount))}.")

    else:
        # Net profit fluctuates

        # Create lists of deficit days and deficit amounts
        deficit_days = [day for day, amount in all_profit_differences if amount < 0]
        
        deficit_amounts = [amount for day, amount in all_profit_differences if amount < 0]

        # Print details of every net profit deficit
        for value in range(len(deficit_days)):

            # Print
            print(f"[NET PROFIT DEFICIT] DAY: {deficit_days[value]}, AMOUNT: SGD{abs(int(deficit_amounts[value]))}")

        # Sort the top 3 deficits 
        top_3_deficits = sorted(enumerate(deficit_amounts), key=get_second_element, reverse=False)[:3]
        
        for record, (index, deficit_amount) in enumerate(top_3_deficits, start=1):
            
            deficit_day = deficit_days[index]
            
            # Determine the position label for the deficit record
            position = f'{record}TH'
            if record == 1:
                position = "HIGHEST"
            elif record == 2:
                position = "2ND HIGHEST"
            elif record == 3:
                position = "3RD HIGHEST"
            print(f"[{position} NET PROFIT DEFICIT] DAY: {deficit_day} AMOUNT: SGD{abs(int(deficit_amount))}")

# Get the second element of a tuple
def get_second_element(item):
    return item[1]

# Call the function to compute net profit patterns
calculateExtreme(all_profit_differences)

