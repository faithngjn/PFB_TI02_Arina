from pathlib import Path
import csv

file_path = Path.cwd() /"project_group"/"csv_reports"/"Profits_And_Loss.csv"

# Read the data from the file into a list
with file_path.open(mode="r") as file:
    reader = csv.reader(file)

    # skip header
    next(reader)

    # create an empty list to net profit data  
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

    # Iterate through each row of profit and loss data
    for data in Profit_and_loss_data:

        # Extract the day number and net profit values
        day = int(data[0])
        netProfit = float(data[4])

        # Ensure calculation starts from day 11 onwards
        if day > 10 and netProfit < previousDay_Netprofit:

            # Calculate deficit
            deficit = previousDay_Netprofit - netProfit

            # Append day and deficit to the list
            net_profit_deficit.append({day: deficit})

        # Set new previous day
        previousDay_Netprofit = netProfit

    return net_profit_deficit

# Define a function to extract the first value
def sort_deficits(item):
    
    # Get the first value from the item 
    # Take the first element of the list
    return list(item.values())[0]

# calculate and print the top three net profit deficits and all deficits
def calculateExtreme(net_profit_deficit):

    # Sort the list using the function
    # Sort in descending order (highest deficits first)
    sorted_deficits = sorted(net_profit_deficit, key=sort_deficits, reverse=True)

   
    for deficit in sorted_deficits:
        
        # Extract the day key from the deficit dictionary as a list
        day = list(deficit.keys())[0]
        
        # Extract the amount, ensure it's an integer, and convert it to absolute value
        amount = abs(int(list(deficit.values())[0]))

        print(f'[NET PROFIT DEFICIT]: DAY: {day} AMOUNT: SGD{amount}')


    # Assign a position to each of the top three deficits
    # Positions should start from 1 onwards
    for record, deficit in enumerate(sorted_deficits[:3], start=1):

        # Extract the day and amount from the deficit dictionary
        day = list(deficit.keys())[0]

        # Get the deficit amount as a positive integer
        # [0] retrieves the very first key in the list
        amount = abs(int(list(deficit.values())[0]))

        # Position label is assigned based on the record number
        if record == 1:
            position = "HIGHEST"
        elif record == 2:
            position = "2ND"
        elif record == 3:
            position = "3RD"
        else:
            position = f'{record}TH'

        #Print position, day, and amount
        print(f'[{position} NET PROFIT DEFICIT] DAY: {day} AMOUNT: SGD{amount}')


# Calculate the net profit deficit
net_profit_deficit = calculateDifference(Profit_and_loss_data)

# Print the results
calculateExtreme(net_profit_deficit)

