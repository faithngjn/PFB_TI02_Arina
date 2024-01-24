from pathlib import Path
import csv

file_path = Path.cwd() /"project_group"/"csv_reports"/ "Profits_And_Loss.csv"

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

    #variable is created to store previous days 
    previousDay_Netprofit = 0

    for data in Profit_and_loss_data:
        day = int(data[0])
        netProfit = float(data[4])
        
        # ensure calculation starts from day 11 onwards
        if day > 10 and netProfit < previousDay_Netprofit:

            deficit = previousDay_Netprofit - netProfit

            # append day and deficit to the list
            net_profit_deficit.append({day: deficit})

        #set new previous day
        previousDay_Netprofit = netProfit

    return net_profit_deficit

# calculate and print the top three net profit deficits and all deficits.
def calculateExtreme(net_profit_deficit):

    # the use of lambda to take a single argument and 
    # returns the first value of the dictionary (the net profit deficit)



    # reverse parameter is used to sort the list in descending order 
    # (from highest to lowest)

    # get the top three elements from the sorted list
    top_3_deficits = sorted(net_profit_deficit, key=lambda x: list(x.values())[0], reverse=True)[:3]

    
    for deficit in net_profit_deficit:
        
        # .key() variable to contain day as the key and the net profit deficit as the value
        # create a list to extract first value [0]
        print(f'[NET PROFIT DEFICIT]: DAY: {list(deficit.keys())} AMOUNT: SGD{abs(int(list(deficit.values())[0]))}')

 
    #  i is a variable used in a for loop with the enumerate function

    # get both the index and value of each item in an iterable object (top_3_deficits)
    
    # the for loop iterates over the top_3_deficits list 
    # assign the index of each item to i and the item itself to deficit
    for i, deficit in enumerate(top_3_deficits):
        print(f'[{i+1}ST HIGHEST DEFICIT] DAY: {list(deficit.keys())} AMOUNT: SGD{abs(int(list(deficit.values())[0]))}')


# Calculate the net profit deficit
net_profit_deficit = calculateDifference(Profit_and_loss_data)

# Print the results
calculateExtreme(net_profit_deficit)