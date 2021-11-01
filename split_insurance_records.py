import csv
import argparse

parser = argparse.ArgumentParser(
    description="Splits a csv file by insurance company, filters duplicate user ids, and sorts by last name (ASC)")
parser.add_argument(
    "file", help="the file to split, filter, and sort, in csv format")
args = parser.parse_args()

# format: {insurance company : [rows]}
seperated_files = {}

header = None

print("Processing " + args.file + " ...")

with open(args.file, 'r') as csv_file_in:
    csv_reader = csv.reader(csv_file_in, delimiter=',')

    # set the header as first row and move the iterator
    header = next(csv_reader, None)

    # split the csv into seperate lists based on the insurance company
    for row in csv_reader:
        insurance_company = row[-1]

        if(insurance_company in seperated_files):
            existing_entries = seperated_files[insurance_company]

            # filter the existing entries by user id and grab the first item in the iterator (if there is one)
            existing_user_entry = next(filter(
                lambda r: r[0] == row[0], existing_entries), None)

            # if user was found with same id, check the version.
            # If less: remove existing and append new
            # If more: keep existing and ignore new
            if(existing_user_entry):
                if(existing_user_entry[2] < row[2]):
                    existing_entries.remove(existing_user_entry)
                else:
                    continue

            existing_entries.append(row)
        else:
            seperated_files[insurance_company] = [row]

for file, rows in seperated_files.items():
 # sort the rows by the last value (presumably last name) in the First name and Last name column before writing
    sorted_list = sorted(
        rows, key=lambda row: row[1].split()[-1], reverse=False)
    filename = file + ".csv"

    print("Creating file: " + filename)

    with open(filename, 'w') as csv_file_out:
        writer = csv.writer(csv_file_out)
        writer.writerow(header)
        writer.writerows(sorted_list)

print("Done.")