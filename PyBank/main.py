# Actualize the os and csv modules for data import.  OS modules allow access / control over OS file system.  csv provides functionality to import / read / write csv files.
# Citing sources:  heavily relying on Python Activity 2-8 here.

import os
import csv

# Need to point to our exercise file by creating the new variable
csvpath = os.path.join("Resources","budget_data.csv")
# creating new variable to work with csv file data
with open(csvpath) as csvfile:

    # another new variable
    csvreader = csv.reader(csvfile, delimiter=',')

    # I deactivated this piece of code, appears to simply check that our filepath is working correctly.
    #print(csvreader)

    # We don't want to include the header row of our CSV file when performing calculations /  operations, this code mitigates that.
    # I need to further research *why* this works.
    csv_header = next(csvreader)

    ## handy f-string.  Used this code to confirm I pulled in the file data accurately.  Deactivated.
    #print(f"CSV Header:  {csv_header}")

    #for row in csvreader:
    #    print(row)

    #Need to identify unique month values within the dataset.  Going to create a list object to store these items and then later use the len function to count them.  Found in exercise 3-4.

    #creating new month list object and establishing empty / null value to begin with.
    #creating new list object to capture proft and loss values.
    #need a list to capture month-to-month variance

    months = []
    Profit_Loss_AMT = []
    Profit_month_VAR = []
    #variable to capture change and calculate running +/-
  
    
    
    for row_instance in csvreader:
        months.append(row_instance[0])
        Profit_Loss_AMT.append(int(row_instance[1]))
#cite your sources:  found inspiration for this solution https://github.com/jacobabdel/python-challenge/blob/master/pyBank/main.py and
# Python Activity 3-7
        #Condiitional needed to avoid the first value being deducted from zero, producing inaccurate end value.
        if len(months) >= 2:
            Profit_month_VAR.append((Profit_Loss_AMT[len(Profit_Loss_AMT)-1] - Profit_Loss_AMT[len(Profit_Loss_AMT)-2]))
    
        
    total_months = len(months)
    print(total_months)
    #we have to reduce our month count by one since our count of month changes is less one
    average_month_change = sum(Profit_month_VAR) / int((total_months)-1)
    #print(Profit_month_VAR)
    #print(sum(Profit_month_VAR))
    #print(average_month_change)

    #We're using the index here to identify the corresponding month in our other list.
    Max_Change_Month_Index = Profit_month_VAR.index(max(Profit_month_VAR))
    Max_Change_Month = months[Max_Change_Month_Index]
    Max_Change_Val = max(Profit_month_VAR)
    Min_Change_Month_Index = Profit_month_VAR.index(min(Profit_month_VAR))
    Min_Change_Month = months[Min_Change_Month_Index]
    Min_Change_Val = min(Profit_month_VAR)


    print(f"Financial Analysis")
    print(F"--------------------")
    print(f"Total Months: ",total_months)
    #Cite your sources:  https://www.kite.com/python/answers/how-to-format-a-float-as-currency-in-python#:~:text=format()%20to%20format%20a,format%20the%20float%20as%20currency. & https://mkaz.blog/code/python-string-format-cookbook/
    print(f"Net Profit & Loss: ", "${:,}".format(sum(Profit_Loss_AMT)))
    print(f"Average Month Change: ", "${:,.2f}".format(average_month_change))
    print(f"Greatest Increase in Profits: ", Max_Change_Month, " ", "${:,}".format(Max_Change_Val))
    print(f"Greatest Decrease in Profits: ", Min_Change_Month, " ", "${:,}".format(Min_Change_Val))
    

    #Push results to text file
    #found this solution (i.e., adding the "file=text_file" argument at https://github.com/vimors/BootCamp-Week4-Homework-PyBank/blob/master/main.py)

    output = os.path.join("Analysis","Output.txt")

    with open(output, 'w', newline='') as text_file:

        print(f"Financial Analysis", file = text_file)
        print(F"--------------------", file = text_file)
        print(f"Total Months: ",total_months, file = text_file)
        print(f"Net Profit & Loss: ", "${:,}".format(sum(Profit_Loss_AMT)),file=text_file)
        print(f"Average Month Change: ", "${:,.2f}".format(average_month_change),file=text_file)
        print(f"Greatest Increase in Profits: ", Max_Change_Month, " ", "${:,}".format(Max_Change_Val),file=text_file)
        print(f"Greatest Decrease in Profits: ", Min_Change_Month, " ", "${:,}".format(Min_Change_Val),file=text_file)