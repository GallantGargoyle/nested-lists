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

def user_input():
    boolean_guard = True
    while boolean_guard:
        #getting user input
        command = input("Enter command: ")

        #if-else ladder dealing with different commands
        if command.startswith("exit"):
            boolean_guard = False
        elif command.startswith("add"):
            continue
        elif command.startswith("sortby"):
            continue
        elif command.startswith("print"):
            continue
        else:
            print("Invalid command: " + command)

if __name__ == "__main__":
    # Check if the spreadsheet file was passed in
    if len(sys.argv) > 1:   
        contents = read_csv(sys.argv[1])
        user_input()
    else:
        print("Needs a spreadsheet file")
