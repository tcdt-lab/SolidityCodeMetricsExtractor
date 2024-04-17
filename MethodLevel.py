import csv
import re
import math
from collections import Counter


class MethodLevel:

    def __init__(self,file_path):
        self.file_path = file_path

    def extract_functions(self):
        function_body = str()
        with open(self.file_path, 'r') as file:
            line = file.readline()
            while line:
                line = file.readline()
                if 'function' in line:
                    #print(line)
                    counter = line.count('{') - line.count('}')
                    while counter != 0 and line:
                        if line.strip() != '\n':
                            function_body += line
                        counter = counter + line.count('{') - line.count('}')
                        line = file.readline()
        function_list = function_body.split('function')
        final_list = list()
        function_body = ''
        for function in function_list:
            function_lines = function.split('\n')
            for function_line in function_lines:
                if function_line.strip() != '':
                    function_body += function_line + '\n'
            final_list.append(function_body)
            function_body = ''
        for function in final_list:
            if function == '':
                final_list.remove(function)
        return final_list

    def sloc(self):
        functions = self.extract_functions()
        sloc_values = list()
        for function in functions:
            counter = 0
            function_lines = function.split('\n')
            for function_line in function_lines:
                if function_line.strip() != "":
                    counter += 1
            sloc_values.append(counter)
        return sloc_values

    def mccabe(self):
        functions = self.extract_functions()
        mccabe_values = list()
        for function in functions:
            counter = function.count('if(') + function.count('else{') + function.count('for(') + function.count(
                'while(') + function.count('&&') + function.count('||') + 1

            mccabe_values.append(counter)
        return mccabe_values

    def hv(self):
        functions = self.extract_functions()
        hv_values = list()
        # Define Solidity operators and operands
        operators = ['+', '-', '*', '/', '%', '=', '==', '!=', '>', '<', '>=', '<=', '&&', '||', '!', '++', '--', '+=',
                     '-=', '*=', '/=', '%=', '=>', '->', '.', ':']
        # Solidity keywords like "function", "if", "else", etc. are considered as operands
        keywords = ['function', 'modifier', 'event', 'constructor', 'fallback', 'if', 'else', 'for', 'while', 'do',
                    'return', 'break', 'continue', 'emit', 'throw', 'require', 'assert']

        for function in functions:

            # Count the occurrences of operators and operands
            operator_pattern = '|'.join(map(re.escape, operators))
            operand_pattern = '|'.join(map(re.escape, keywords))
            all_pattern = '(' + operator_pattern + '|' + operand_pattern + ')'
            occurrences = re.findall(all_pattern, function)

            # Calculate N and n
            operator_counts = Counter(occurrences)
            N = sum(operator_counts.values())
            n = len(operator_counts)
            # Calculate Halstead Volume
            V = N * math.log2(n) if n != 0 else 0
            if V == 0:
                V = 1
            hv_values.append(V)

        return hv_values

    def mi(self):
        mi_values = list()
        sloc = self.sloc()
        cc = self.mccabe()
        hv = self.hv()
        for i in range(len(sloc)):
            mi = 171 - 5.2 * math.log(hv[i]) - 0.23 * math.log(cc[i]) - 16.2 * math.log(sloc[i])
            mi_values.append(mi)
        return mi_values


if __name__ == '__main__':
    with open('address_information.csv', 'r') as file:
        contracts = csv.reader(file)
        with open('results_method_level.csv', 'w') as result:
            writer = csv.writer(result)
            for row in contracts:
                address = row[0] + '/' + row[1] + '/' + row[2] + '/' + row[3]
                if len(row) == 5:
                    address = address + '/' + row[4]
                method_obj = MethodLevel(address)
                functions = method_obj.extract_functions()
                sloc = method_obj.sloc()
                mccabe = method_obj.mccabe()
                hv = method_obj.hv()
                mi = method_obj.mi()
                for i in range(len(functions)):
                    # writer.writerow([address.split('/')[-1],functions[i], sloc[i],mccabe[i],hv[i],mi[i]])
                    writer.writerow([sloc[i],mccabe[i],hv[i],mi[i]])


