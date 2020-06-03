# reporter.py
import csv
import pandas
import os

#csv_filename = "sales-201710.csv"  # a relative filepath
#csv_filepath=os.path.join("data", csv_filename)


sales = pandas.read_csv("sales-201710.csv")

total_sales = sales["sales price"].sum()

#with open(csv_filename, "r") as csv_file:  # "r" means "open the file for reading"
#    reader = csv.DictReader(csv_filename)  # assuming your CSV has headers
#    # reader = csv.reader(csv_file) # if your CSV doesn't have headers
#    for row in reader:
#        #print(row["date"], row["product"], row["unit price"], row["units sold"], row["sales price"])
#        sales.append(dict(row))

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

print("GENERATING SALES REPORT FOR MONTH OF OCTOBER 2013...")
print("TOTAL SALES: "+to_usd(total_sales))
