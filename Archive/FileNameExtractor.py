import os
import csv
import numpy as np
all_files = list()

def write_information_into_list(item_path: str):
    all_files.append(item_path.split("/"))
def read_files_in_folder(folder_path):


    # Iterate over all items (files and folders) in the given directory
    for item in os.listdir(folder_path):
        # Construct full path to the item
        item_path = os.path.join(folder_path, item)

        # Check if the item is a directory
        if os.path.isdir(item_path):
            # If it's a directory, recursively call the function
            read_files_in_folder(item_path)
        else:
            write_information_into_list(item_path)


read_files_in_folder("../versioned-smart-contracts-master/mainnet")


print(all_files)
with open("../address_information.csv", mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(all_files)


with open("../contracts_information.csv", mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for i in range(len(all_files)):
        csv_writer.writerow(all_files[i][3:5])
