
from pathlib import Path 
import csv

# Create a file path to the csv file.
fp = Path.cwd() / "csv_reports"/"Overheads.csv"

# Read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:

    # Create a CSV reader
    reader = csv.reader(file, delimiter=",")

    next(reader)  # Skip header

    # Create lists for Overhead_data and Overhead_name
    
    # List to store numerical data for overheads
    Overhead_data = []  

    # List to store names of overhead categories
    Overhead_name = [] 

    # Iterate through each row in the CSV file
    for row in reader:

        # Add category name to the list
        Overhead_name.append(row[0])  

        # Add the amounts to the list as a float
        Overhead_data.append(float(row[1])) 

# Find the index of the maximum value in a list
def find_index_of_max_value(first):
    if not first:

        # return none if list is empty
        return None  
    
    # Find the maximum value in the list
    max_value = max(first)  


    # Iterate through the list to find the index of the maximum value
    for index, value in enumerate(first):

        if value == max_value:

            # Return the index when the maximum value is found
            return index  

# Find the greatest overhead
def compute_highest(Overhead_data, Overhead_name):

    "function will find the highest overhead and display the data"
    
    if not Overhead_data:

        print("No data to compute highest overhead.")

        return 

    # Call the find_index_of_max_value function to get the index of the highest value
    category_index = find_index_of_max_value(Overhead_data)

    # Get the name of the category with the highest value
    category_name = Overhead_name[category_index].upper()

    
    return f"[HIGHEST OVERHEAD] {category_name}: {Overhead_data[category_index]}" 

overhead_value = compute_highest(Overhead_data, Overhead_name)


import csv 
from pathlib import Path 
 
# Create a file path to the csv file. 
fp_cash = Path.cwd() /"csv_reports"/ "Cash_On_Hand.csv"
 
# Read the csv file for cash on hand. 
with fp_cash.open(mode="r", encoding="UTF-8", newline="") as file: 
    reader = csv.reader(file, delimiter=",") 
    next(reader)  # Skip header 
 
    # Create an empty list for CashRecords 
    CashRecords = [(int(row[0]), float(row[1])) for row in reader] 
 
# Find the cash difference between all days in data 
def compute_cash_on_hand_difference(CashRecords): 
    "function determine the difference in cash on hands"   
 
    all_cash_differences = [(CashRecords[item][0], CashRecords[item][1] - CashRecords[item - 1][1]) for item in range(1, len(CashRecords))] 
 
    return all_cash_differences 
 
all_cash_differences = compute_cash_on_hand_difference(CashRecords) 
 
# Find whether cash on hand is always fluctuating/increasing/decreasing 
def compute_pattern(all_cash_differences): 
 
    "function determine the pattern of cash on hand and find the data corresponding to the pattern"   
    if all(value[1] > 0 for value in all_cash_differences): 
     
        # Cash-on-hand is always increasing 
        highest_increment_day, highest_increment_amount = max(all_cash_differences, key=get_second_element) 
     
        print("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY") 
     
        print(f"[HIGHEST CASH SURPLUS] DAY: {highest_increment_day}, AMOUNT: SGD{abs(int(highest_increment_amount))}.") 
     
    elif all(value[1] < 0 for value in all_cash_differences): 
     
        # Cash-on-hand is always decreasing 
        lowest_decrement_day, lowest_decrement_amount = min(all_cash_differences, key=get_second_element) 
     
        print("[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY") 
     
        print(f"[HIGHEST CASH DEFICIT] DAY: {lowest_decrement_day} AMOUNT: SGD{abs(int(lowest_decrement_amount))}.") 
    else: 
        # Cash-on-hand fluctuates 
        deficit_days = [day for day, amount in all_cash_differences if amount < 0] 
     
        deficit_amounts = [amount for day, amount in all_cash_differences if amount < 0] 

        COH = []
        for value in range(1, len(deficit_days)): 
         
            COH.append(f"[CASH DEFICIT] DAY: {deficit_days[value]}, AMOUNT: SGD{abs(int(deficit_amounts[value]))}")
 
        # Sort the top 3 deficits 
        top_3_deficits = sorted(enumerate(deficit_amounts), key=get_second_element, reverse=False)[:3]
        top3results = [] 
        for record, (index, deficit_amount) in enumerate(top_3_deficits, start=1): 
            deficit_day = deficit_days[index] 
            position = f'{record}TH' 
            if record == 1: 
                position = "HIGHEST" 
            elif record == 2: 
                position = "2ND HIGHEST" 
            elif record == 3: 
                position = "3RD HIGHEST" 
            top3results.append(f"[{position} CASH DEFICIT] DAY: {deficit_day} AMOUNT: SGD{abs(int(deficit_amount))}")
        return  COH, top3results 
 
 
def get_second_element(item): 
    return item[1] 

coh = compute_pattern(all_cash_differences)


import csv
from pathlib import Path

# Create a file path to the csv file.
file_path = Path.cwd() / "csv_reports"/"Profits_And_Loss.csv"

with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    
    reader = csv.reader(file)

     # Skip header
    next(reader) 

    # Create an empty list for ProfitRecords
    ProfitRecords = [(int(row[0]), float(row[4])) for row in reader]

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

        PL = []

        # Print details of every net profit deficit
        for value in range(len(deficit_days)):

            # Print
            PL.append(f"[NET PROFIT DEFICIT] DAY: {deficit_days[value]}, AMOUNT: SGD{abs(int(deficit_amounts[value]))}")

        # Sort the top 3 deficits 
        top_3_deficits = sorted(enumerate(deficit_amounts), key=get_second_element, reverse=False)[:3]
        top3amounts = []
        for record, (number, deficit_amount) in enumerate(top_3_deficits, start=1):
            
            deficit_day = deficit_days[number]
            
            # Determine the position label for the deficit record
            position = f'{record}TH'
            if record == 1:
                position = "HIGHEST"
            elif record == 2:
                position = "2ND HIGHEST"
            elif record == 3:
                position = "3RD HIGHEST"
            top3amounts.append(f"[{position} NET PROFIT DEFICIT] DAY: {deficit_day} AMOUNT: SGD{abs(int(deficit_amount))}")
        return PL, top3amounts
# Get the second element of a tuple
def get_second_element(item):
    return item[1]

# Call the function to compute net profit patterns
PL = calculateExtreme(all_profit_differences)

# with open('summary_report.txt', mode='w') as file:
    
#     file.write(str(overhead_value))
#     file.write(str(coh) + "\n")
#     file.write((str(PL)))
   

with open('summary_report.txt', mode='w') as file:
    
    # Write overhead value to a new line
    file.write(str(overhead_value) + "\n")

    # Write each item in COH list to a new line
    for item in coh[0]:
        file.write(str(item) + "\n")

    # Write each item in top3results list to a new line
    for item in coh[1]:
        file.write(str(item) + "\n")

    # Write each item in PL list to a new line
    for item in PL[0]:
        file.write(str(item) + "\n")

    # Write each item in top3amounts list to a new line
    for item in PL[1]:
        file.write(str(item) + "\n")




