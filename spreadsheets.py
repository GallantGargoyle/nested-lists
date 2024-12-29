import csv
import sys

def read_csv(file_path):
    contents = []
    with open(file_path, 'r', encoding='latin-1') as csv_file:
        csvreader = csv.reader(csv_file)
        next(csvreader)
        for row in csvreader:
            contents.append(row)
        return contents

if __name__ == "__main__":
    # Check if the spreadsheet file was passed in
    if len(sys.argv) > 1:   
        contents = read_csv(sys.argv[1])
    else:
        print("Needs a spreadsheet file")
