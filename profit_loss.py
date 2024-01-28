from pathlib import Path
import csv

# Create a file path to the csv file.
file_path = Path.cwd() /"project_group"/"csv_reports"/ "Profits_And_Loss.csv"

# Read the csv file.
with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)

    # skip header
    next(reader)

    # create an empty list for net profit data  
    Profit_and_loss_data = []

    # each line returns each row as a list
    for line in reader:
        Profit_and_loss_data.append(line)

# calculate both the profits and losses that occur
def calculateDifference(Profit_and_loss_data):

    # create empty list to store all net profit deficits and respective days 
    net_profit_deficit = []

    # variable is created to store previous days 
    previousDay_Netprofit = 0

    # Initialize surplus as an empty dictionary
    surplus = {}

    # Iterate through each row of profit and loss data
    for data in Profit_and_loss_data:

        # Extract the day number and net profit values
        day = int(data[0])

        netProfit = float(data[4])

        # Ensure calculation starts from day 11 onwards
        if day > 10:

            if netProfit < previousDay_Netprofit:

                # Calculate deficit
                deficit = previousDay_Netprofit - netProfit

                # Append day and deficit to list
                net_profit_deficit.append({day: deficit})

            elif netProfit > previousDay_Netprofit:

                # Calculate surplus
                surplus[day] = netProfit - previousDay_Netprofit

            # Set new previous day
            previousDay_Netprofit = netProfit

    return net_profit_deficit, surplus

# Define a function to extract the first value
def sort_deficits_by_day(item):

    # Get the first value from the item 
    # Take the first element of the list
    return list(item.keys())[0]

def sort_deficits_by_amount(item):

    # Get the first value from the item 
    # Take the first element of the list
    return list(item.values())[0]

def calculateExtreme(net_profit_deficit, surplus):


    # Check if there are only deficits
    # Identify whether each day's profit is lower than the previous day 
    if net_profit_deficit and not surplus:

        print('[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN THE PREVIOUS DAY')

        # Find the highest net profit deficit
        highest_deficit_day = max(net_profit_deficit, key=sort_deficits_by_amount)
        
        # Extracts the amount of the highest deficit
        highest_deficit_amount = abs(list(highest_deficit_day.values())[0])

        # Print highest net profit deficit
        print(f'[HIGHEST NET PROFIT DEFICIT] DAY: {list(highest_deficit_day.keys())[0]} AMOUNT: SGD{highest_deficit_amount}')

    # Check if there are only surpluses
    elif surplus and not net_profit_deficit:

        print('[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')

        # Print the highest net profit surplus
        highest_surplus_day = max(surplus, key=surplus.get)

        # Print highest net profit surplus
        print(f'[HIGHEST NET PROFIT SURPLUS] DAY: {highest_surplus_day} AMOUNT: SGD{surplus[highest_surplus_day]}')

    # If there are both deficits and surpluses
    else:
        print('[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN THE PREVIOUS DAY')

        # Print all net profit deficits sorted by day
        sorted_deficits_by_day = sorted(net_profit_deficit, key=sort_deficits_by_day)

        # Iterate through each deficit
        for deficit in sorted_deficits_by_day:

            # Extract the day from the current deficit dictionary
            day = list(deficit.keys())[0]

            # Extract the deficit amount from the deficit dictionary
            amount = abs(int(list(deficit.values())[0]))

            print(f'[NET PROFIT DEFICIT] DAY: {day} AMOUNT: SGD{amount}')

        # Print the top three net profit deficits sorted by amount
        sorted_deficits_by_amount = sorted(net_profit_deficit, key=sort_deficits_by_amount, reverse=True)
        
        # Iterate through the top three deficits sorted by amount
        for record, deficit in enumerate(sorted_deficits_by_amount[:3], start=1):

            day = list(deficit.keys())[0]

            amount = abs(int(list(deficit.values())[0]))

           
            position = f'{record}TH'
            if record == 1:
                position = "HIGHEST"
            elif record == 2:
                position = "2ND HIGHEST"
            elif record == 3:
                position = "3RD HIGHEST"

            print(f'[{position} NET PROFIT DEFICIT] DAY: {day} AMOUNT: SGD{amount}')

        # Print the highest net profit surplus
        highest_surplus_day = max(surplus, key=surplus.get)

        print(f'[HIGHEST NET PROFIT SURPLUS] DAY: {highest_surplus_day} AMOUNT: SGD{surplus[highest_surplus_day]}')

# Calculate the net profit deficit
net_profit_deficit, surplus = calculateDifference(Profit_and_loss_data)

# Print the results
calculateExtreme(net_profit_deficit, surplus)
