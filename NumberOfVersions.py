import csv


class Versions:

    def numberOfRevisions(self):
        number_of_revisions = dict()
        with open('contracts_information.csv', 'r') as file_information:
            reader = csv.reader(file_information)
            for row in reader:
                file_name = row[-1]
                file_split = file_name.split('_')
                if file_split[-2] not in number_of_revisions.keys():
                    number_of_revisions[file_split[-2]] = 1
                else:
                    number_of_revisions[file_split[-2]] += 1
        return number_of_revisions

    def write_to_file(self):

        # Open a CSV file in write mode
        with open('number_of_versions', 'w', newline='') as csvfile:
            # Create a CSV writer object
            csv_writer = csv.writer(csvfile)

            data = self.numberOfRevisions()

            # Iterate over the dictionary
            for key, value in data.items():
                csv_writer.writerow([key, value])


obj = Versions()

data = obj.numberOfRevisions()

counter = 0

for key, value in data.items():
    if value == 10:
        counter += 1
print(counter)
