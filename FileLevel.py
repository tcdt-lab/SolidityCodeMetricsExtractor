import os
import re
import math
from collections import Counter
import csv
import matplotlib.pyplot as plt
from NumberOfVersions import Versions


class FileLevel(object):

    def __init__(self,file_path):
        self.file_path = file_path

    def remove_comments_bundled_contracts(self, file_path, code):

        code_lines_in_list = code.split('\\n')
        with open(file_path, 'w') as file:
            for code_line in code_lines_in_list:
                file.write(code_line + '\n')

        with open(file_path, 'r') as file:
            code = file.read()

        return code

    def remove_comments_and_whitespaces(self, code):

        # Read the content of the input Solidity file
        if code.split('\n')[0] == '{{':
            code = self.remove_comments_bundled_contracts(file_path, code)
        # Remove single-line comments (//) and inline comments (/* ... */)
        code = re.sub(r'\/\/.*|\/\*[\s\S]*?\*\/', '', code)

        code = re.sub(r'[^\S\n]+', '', code)

        return code

    def sloc(self):
        with open(file_path, 'r') as contract_file:
            code = contract_file.read()
            code = self.remove_comments_and_whitespaces(code)
        with open(file_path, 'w') as contract_file:
            contract_file.write(code)
        counter = 0
        with open(file_path, 'r') as contract_file:
            line = contract_file.readline()
            while line:
                counter += 1
                if line.strip()[:2] in ['//', '/*']:
                    counter -= 1
                if '/*' in line and line.strip()[:2] != '//':
                    while '*/' not in line:
                        line = contract_file.readline()
                if line.strip() == '':
                    counter -= 1
                line = contract_file.readline()
        return counter

    def hv(self):

        # Define Solidity operators and operands
        operators = ['+', '-', '*', '/', '%', '=', '==', '!=', '>', '<', '>=', '<=', '&&', '||', '!', '++', '--', '+=',
                     '-=', '*=', '/=', '%=', '=>', '->', '.', ':']
        # Solidity keywords like "function", "if", "else", etc. are considered as operands
        keywords = ['function', 'modifier', 'event', 'constructor', 'fallback', 'if', 'else', 'for', 'while', 'do',
                    'return', 'break', 'continue', 'emit', 'throw', 'require', 'assert']

        with open(file_path, 'r') as file:
            code = file.read()

        code = re.sub(r'\/\/.*|\/\*[\s\S]*?\*\/', '', code)
        # Count the occurrences of operators and operands
        operator_pattern = '|'.join(map(re.escape, operators))
        operand_pattern = '|'.join(map(re.escape, keywords))
        all_pattern = '(' + operator_pattern + '|' + operand_pattern + ')'
        occurrences = re.findall(all_pattern, code)

        # Calculate N and n
        operator_counts = Counter(occurrences)
        N = sum(operator_counts.values())
        n = len(operator_counts)
        # Calculate Halstead Volume
        V = N * math.log2(n) if n != 0 else 0
        if V == 0:
            return 1

        return V

    def mccabe(self):

        with open(self.file_path, 'r') as file:
            code = file.read()
        code = self.remove_comments_and_whitespaces(code)

        decision_points = code.count('if(') + code.count('else{') + code.count('for(') + code.count(
            'while(') + code.count('&&') + code.count('||')

        mccabe_complexity = decision_points + 1
        return mccabe_complexity

    def mi(self):
        sloc = self.sloc()
        cc = self.mccabe()
        hv = self.hv()
        mi = 171 - 5.2 * math.log(hv) - 0.23 * math.log(cc) - 16.2 * math.log(sloc)
        return mi


if __name__ == '__main__':
    obj = Versions()
    contract_names = list()
    data = obj.numberOfRevisions()
    plot_data = dict(dict())
    for key, value in data.items():
        if value == 10:
            contract_names.append(key)
    for contract_name in contract_names:
        plot_data[contract_name] = {}
    with open('results_class_level_with_versions.csv', 'r') as result:
        rows = csv.reader(result)

        for row in rows:
            if row[0] in contract_names:
                plot_data[row[0]][row[1]] = row[5]


    # for i in plot_data.keys():
    #     print(len(plot_data[i]))

    plot_data.pop('HelloERC20')
    plot_data.pop('TOKEN')

    print(plot_data)


    # with open('address_information.csv', 'r') as file:
    #     contracts = csv.reader(file)
    #     with open('results_class_level_with_versions.csv', 'w') as result:
    #         writer = csv.writer(result)
    #         for row in contracts:
    #             file_path = row[0] + '/' + row[1] + '/' + row[2] + '/' + row[3]
    #             if len(row) == 5:
    #                 file_path = file_path + '/' + row[4]
    #             contract_name = file_path.split('_')[-2]
    #             contract_version = file_path.split('_')[-1].split('.')[0]
    #             method_obj = FileLevel(file_path)
    #             sloc = method_obj.sloc()
    #             mccabe = method_obj.mccabe()
    #             hv = method_obj.hv()
    #             mi = method_obj.mi()
    #             writer.writerow([contract_name, contract_version, sloc,mccabe,hv,mi])

