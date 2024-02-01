import csv
from pathlib import Path

# Create a file path to the csv file.
fp = Path.cwd() / "project_group"/"csv_reports"/"Overheads.csv"

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

    # Print 
    print(f"[HIGHEST OVERHEAD] {category_name}: {Overhead_data[category_index]}")

compute_highest(Overhead_data, Overhead_name)
