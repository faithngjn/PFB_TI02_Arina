import csv 
from pathlib import Path 
 
# Create a file path to the csv file. 
fp_cash = Path.cwd() /"project_group"/"csv_reports"/ "Cash_On_Hand.csv"
 
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
 
        for value in range(len(deficit_days)): 
         
            print(f"[CASH DEFICIT] DAY: {deficit_days[value]}, AMOUNT: SGD{abs(int(deficit_amounts[value]))}") 
 
        # Sort the top 3 deficits 
        top_3_deficits = sorted(enumerate(deficit_amounts), key=get_second_element, reverse=False)[:3] 
        for record, (index, deficit_amount) in enumerate(top_3_deficits, start=1): 
            deficit_day = deficit_days[index] 
            position = f'{record}TH' 
            if record == 1: 
                position = "HIGHEST" 
            elif record == 2: 
                position = "2ND HIGHEST" 
            elif record == 3: 
                position = "3RD HIGHEST" 
            print(f"[{position} CASH DEFICIT] DAY: {deficit_day} AMOUNT: SGD{abs(int(deficit_amount))}") 
 
 
def get_second_element(item): 
    return item[1] 
 
compute_pattern(all_cash_differences)
