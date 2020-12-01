# --------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with binary files and error handling in Python
# ChangeLog (Who,When,What):
# JVelazquez,11.29.2020,Created script
# --------------------------------------------------------------- #

import pickle

# Data ---------------------------------------------------------- #
strFileName = 'SavingsTracker.bin'
lstSale = [] # List of Data related to purchase
objFile = None # placeholder object for file
SalePrice = "" # Price you paid
FullPrice = "" # Full retail value of item purchased
Savings = "" # Percent saved

# Processing ---------------------------------------------------- #
def calculate_savings(sale_price, full_price):
    """
    :param sale_price:
    :param full_price:
    :return:
    """
    savings = round(float((full_price - sale_price)/full_price), 3) * 100
    return savings


def add_data_to_list(sale, full, savings, list_of_rows):
    """
    :param sale:
    :param full:
    :param savings:
    :param list_of_rows:
    :return:
    """
    row = {"Sale_Price": sale, "Full_Price": full, "Savings": savings}
    list_of_rows.append(row)
    return list_of_rows, 'Success'

def append_list_to_bin_file(file_name, list):
    """
    :param file_name:
    :param list:
    :return:
    """
    file_name = open("SavingsTracker.bin", "ab")
    pickle.dump(lstSale, file_name)
    file_name.close()

# Presentation/IO -------------------------------------------------- #
def input_new_sale(optional_message = ''):
    """
    :param sale_price:
    :param full_price:
    :return:
    """
    sale = abs(float(input("Enter Sale Price: ")))
    full = abs(float(input("Enter Full Price: ")))
    return sale, full

def display_savings(percent_saved):
    percent_saved = str(Savings)
    print("You saved " + percent_saved + "% on this purchase!")
    print() # add line for looks

def input_cont_or_exit():
    """
    :return:
    """
    choice = str(input("Enter another sale? Press y if yes, any other key to exit: "))
    print() # add line for looks
    return choice

# Main Code Block ----------------------------------------------- #
while(True):
    try:
        SalePrice, FullPrice = input_new_sale() # Get input data
        Savings = (calculate_savings(SalePrice, FullPrice)) # calculate savings
        display_savings(Savings)
        add_data_to_list(SalePrice, FullPrice, Savings, lstSale) # create list object
        append_list_to_bin_file(objFile, lstSale) # append list object to binary file
        strChoice = input_cont_or_exit()
        if strChoice == "y":
          continue
        else:
          break

# Error Handling ------------------------------------------------ #
    except ZeroDivisionError as e:
        print(e)
        print("Cannot divide by zero, please enter non-zero value for second number")
        continue
    except ValueError as e:
        print(e)
        print("Price must be numeric value, please enter numeric value.")



