import csv
from pathlib import Path
hi = print("testing")
# Create a file path to the csv file.
fp = Path.cwd() / "project_group"/"csv_reports"/"Cash_On_Hand.csv"

# Read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file, delimiter=",")
    next(reader) # Skip header

    # Create an empty list for CashRecords
    CashRecords = []

    # Append cash-on-hand data into CashRecords list
    for row in reader:
        # Get the cash
        # and append to the deliveryRecords list
        CashRecords.append((int(row[0]), float(row[1])))

# Find the cash difference between all days in data
def compute_cash_on_hand_difference(CashRecords):
    "function determine the difference in cash on hands"  
    all_cash_differences = []
    for item in range(1, len(CashRecords)):
        cash_difference = CashRecords[item][1] - CashRecords[item - 1][1]
        all_cash_differences.append((CashRecords[item][0], cash_difference))
    return all_cash_differences

all_cash_differences = compute_cash_on_hand_difference(CashRecords)

# Find whether cash on hand is always fluctuating/increasing/decreasing
def compute_pattern(all_cash_differences):
    "function determine the pattern of cash on hand and find the data corresponding to the pattern"  
    for value in range(1, len(all_cash_differences)):
        if all(value[1] > 0 for value in all_cash_differences):
        # Cash-on-hand is always increasing
            highest_increment_day = all_cash_differences[all_cash_differences.index(max(all_cash_differences))][0]
            highest_increment_amount = max(all_cash_differences)[1]
            print("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
            print(f"[HIGHEST CASH SURPLUS] DAY: {highest_increment_day}, AMOUNT: SGD{abs(int(highest_increment_amount))}.")
    for value in range(1, len(all_cash_differences)):
        if all(value[1] < 0 for value in all_cash_differences):
        # Cash-on-hand is always decreasing
            lowest_decrement_day = all_cash_differences[all_cash_differences.index(min(all_cash_differences))][0]
            lowest_decrement_amount = min(all_cash_differences)[1]
            print("[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY")
            print(f"[HIGHEST CASH DEFICIT] DAY: {lowest_decrement_day} AMOUNT: SGD{abs(int(lowest_decrement_amount))}.")
    else:
        # Cash-on-hand fluctuates
        # Create empty list for all deficits and their days
        deficit_days = []
        deficit_amounts = []
        for value in range(1, len(all_cash_differences)):
            if all_cash_differences[value][1] < 0:
                deficit_days.append(value)
                deficit_amounts.append(all_cash_differences[value][1])
    for value in range(len(deficit_days)):
        print(f"[CASH DEFICIT] DAY: {all_cash_differences[deficit_days[value]][0]}, AMOUNT: SGD{abs(int(all_cash_differences[deficit_days[value]][1]))}")
    # create list of sorted top 3 from deficit_days and deficit_amounts using zip which is from external research
    top_3_deficits = sorted(zip(deficit_amounts, deficit_days))[:3]
    print(f"[HIGHEST CASH DEFICIT] DAY:{all_cash_differences[top_3_deficits[0][1]][0]} AMOUNT: SGD{abs(int(top_3_deficits[0][0]))} ")
    print(f"[2ND HIGHEST CASH DEFICIT] DAY:{all_cash_differences[top_3_deficits[1][1]][0]} AMOUNT: SGD{abs(int(top_3_deficits[1][0]))} ")
    print(f"[3RD HIGHEST CASH DEFICIT] DAY:{all_cash_differences[top_3_deficits[2][1]][0]} AMOUNT: SGD{abs(int(top_3_deficits[2][0]))} ")

compute_pattern(all_cash_differences)
