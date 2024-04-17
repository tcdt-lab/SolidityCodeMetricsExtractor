# import csv
# import re
# import os
#
#
# def mccabe_calculator():
#     McCabe_values = list()
#     with open('contracts_information.csv', 'r') as contracts_information:
#         reader = csv.reader(contracts_information)
#         pattern1 = r'\}\s*else\s*\{'  # Regular expression pattern to match '} else {'
#         pattern2 = re.compile(r'\}[\s]*else[\s]*if[\s]*\{')
#         k = 0
#         for row in reader:
#             file_name = 'stemmed_files/' + row[0]
#             if len(row) == 2:
#                 file_name = file_name + '_' + row[1]
#             counter = 1
#             with open(file_name, 'r') as contract_file:
#                 contract_reader = csv.reader(contract_file)
#                 for contract_row in contract_reader:
#                     contract_row = str(contract_row)
#                     if contract_row[2:5] == 'if(' or contract_row[2:6] == 'if (' or contract_row[2:8] == '} if (' or contract_row[2:6] == 'for(' or contract_row[2:7] == 'for (' or contract_row[2:9] == '} for (' or contract_row[2:8] == 'while(' or contract_row[2:9] == 'while (' or contract_row[2:11] == '} while (' or re.search(pattern1, contract_row) or re.search(pattern2, contract_row):
#                         counter += 1
#             McCabe_values.append(counter)
#     return McCabe_values
#
#
# def calculate_mccabe_complexity(file_path):
#     # Remove comments and strings to simplify parsing
#     with open(file_path, 'r') as code_file:
#         code = code_file.read()
#
#     code = re.sub(r'\/\/.*|\/\*[\s\S]*?\*\/|\".*?\"', '', code)
#
#     # Count decision points (if statements, loops, etc.)
#     decision_points = 0
#     decision_keywords = ['if', 'else', 'while', 'for', 'case']
#     for keyword in decision_keywords:
#         decision_points += code.count(keyword)
#
#     # McCabe Cyclomatic Complexity is decision points + 1
#     mccabe_complexity = decision_points + 1
#     return mccabe_complexity
#
#
# def calculate_mccabe(file_path):
#
#     with open(file_path, 'r') as file:
#         code = file.read()
#
#         # Count decision points
#         decision_points = code.count('if(') + code.count('else{') + code.count('for(') + code.count('while(') + code.count('&&') + code.count('||')
#
#         # McCabe's Cyclomatic Complexity
#         mccabe_complexity = decision_points + 1
#         return mccabe_complexity
#
#
# with open('contracts_information.csv', 'r') as contracts_information:
#     reader = csv.reader(contracts_information)
#     for row in reader:
#         file_name = 'contracts_without_comment_and_whitespace/' + row[0]
#         if len(row) == 2:
#             file_name = file_name + '_' + row[1]
#         print(calculate_mccabe(file_name))
