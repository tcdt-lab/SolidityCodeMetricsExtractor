import csv
import numpy as np

# SLOC_values = list()
#
# def SLOC_calculator():
#     with open('address_information.csv', 'r') as address_file:
#         csv_reader = csv.reader(address_file)
#
#         for row in csv_reader:
#             file_name = "contracts_without_comment_and_whitespace/" + row[3]
#             if len(row) == 5:
#                 file_name = file_name + "_" + row[4]
#             counter = 0
#             with open(file_name, 'r') as contract_file:
#                 contract_reader = contract_file.readlines()
#                 for contract_row in contract_reader:
#                     if contract_row != '\n':
#                         counter += 1
#                 SLOC_values.append(counter)
#     return SLOC_values


#values = np.array(SLOC_calculator())

# Load the existing CSV file into a NumPy array
#existing_data = np.genfromtxt('output.csv', delimiter=',')

# Create a new column of values
#new_column = np.array(values)

# Stack the existing data and the new column horizontally
#updated_data = np.column_stack((existing_data, new_column))

# Save the updated data to a new CSV file
#np.savetxt('output.csv', updated_data, delimiter=',', fmt='%d')
