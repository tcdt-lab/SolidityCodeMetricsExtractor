# from collections import Counter
# import re
# import math
# import csv
#
#
# def read_file_to_string(filename):
#     with open(filename, 'r') as file:
#         file_content = file.read()
#         return file_content
#
#
# def calculate_halstead_volume():
#     halstead_volume_values = list()
#     # Define Solidity operators and operands
#     operators = ['+', '-', '*', '/', '%', '=', '==', '!=', '>', '<', '>=', '<=', '&&', '||', '!', '++', '--', '+=',
#                  '-=', '*=', '/=', '%=', '=>', '->', '.', ':']
#     # Solidity keywords like "function", "if", "else", etc. are considered as operands
#     keywords = ['function', 'modifier', 'event', 'constructor', 'fallback', 'if', 'else', 'for', 'while', 'do',
#                 'return', 'break', 'continue', 'emit', 'throw', 'require', 'assert']
#
#     with open('address_information.csv', 'r') as file_information:
#         reader = csv.reader(file_information)
#         for row in reader:
#             file_name = row[0] + "/" + row[1] + "/" + row[2] + "/" + row[3]
#             if len(row) == 5:
#                 file_name = file_name + "/" + row[4]
#
#             code_content = read_file_to_string(file_name)
#
#             code_content = re.sub(r'\/\/.*|\/\*[\s\S]*?\*\/', '', code_content)
#             # Count the occurrences of operators and operands
#             operator_pattern = '|'.join(map(re.escape, operators))
#             operand_pattern = '|'.join(map(re.escape, keywords))
#             all_pattern = '(' + operator_pattern + '|' + operand_pattern + ')'
#             occurrences = re.findall(all_pattern, code_content)
#
#             # Calculate N and n
#             operator_counts = Counter(occurrences)
#             N = sum(operator_counts.values())
#             n = len(operator_counts)
#             # Calculate Halstead Volume
#             V = N * math.log2(n) if n != 0 else 0
#             halstead_volume_values.append(V)
#     return halstead_volume_values
#
#
# #print(calculate_halstead_volume())
#
