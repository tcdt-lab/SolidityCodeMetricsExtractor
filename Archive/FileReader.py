# import csv
# import re
#
#
# def remove_comments_bundled_contracts(file_path, code):
#
#     code_lines_in_list = code.split('\\n')
#     with open(file_path, 'w') as file:
#
#         for code_line in code_lines_in_list:
#             file.write(code_line + '\n')
#
#     with open(file_path, 'r') as file:
#         code = file.read()
#
#     return code
#
#
# def remove_comments_and_whitespaces(file_name):
#
#     # Read the content of the input Solidity file
#     with open(file_name, 'r') as file:
#         code = file.read()
#     if code.split('\n')[0] == '{{':
#         code = remove_comments_bundled_contracts(file_name, code)
#     # Remove single-line comments (//) and inline comments (/* ... */)
#     code = re.sub(r'\/\/.*|\/\*[\s\S]*?\*\/', '', code)
#
#     code = re.sub(r'[^\S\n]+', '', code)
#
#     return code
#
#
# # with open('address_information.csv', 'r') as csv_file:
# #     csv_reader = csv.reader(csv_file)
# #
# #     for row in csv_reader:
# #         remove_comments_and_whitespaces(row)
#
# file_path = "versioned-smart-contracts-master/mainnet/A2Z/0xc6c5ee2c54c79695ebef26f3171e5b96ed74578d/0x0316166fc3ba25085098104cb5ab9902a31c06ae_A2Z_V0.sol"
#
# print(remove_comments_and_whitespaces(file_path))
#
