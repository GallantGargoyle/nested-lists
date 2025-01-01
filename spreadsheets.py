import csv
import sys

#function to handle opening and reading csv file
def read_csv(file_path):
    contents = []
    with open(file_path, 'r', encoding='latin-1') as csv_file:
        csvreader = csv.reader(csv_file)
        next(csvreader)
        for row in csvreader:
            contents.append(row)
        return contents

#function to handle sortby command
def sortby_command(command, contents):
    column_to_sort = int(command[len('sortby '):])
    contents.sort(key = lambda x: float(x[column_to_sort]))
    

#function to handle print command
def print_command(command, contents):
    rows_to_print = int(command.split()[-1])
    for row in contents:
        if rows_to_print <= 0:
            break
        print(", ".join(row))
        rows_to_print -= 1

#function to handle add command
def add_command(command, contents):
    new_row = command[len('add '):]
    line = next(csv.reader([new_row]))
    contents.append(line)


#function to handle user commands
def user_input(contents):
    boolean_guard = True
    
    while boolean_guard:
        #getting user input
        command = input("Enter command: ")

        #if-else ladder dealing with different commands
        if command.startswith("exit"):
            boolean_guard = False
        elif command.startswith("add"):
            add_command(command, contents)
        elif command.startswith("sortby"):
            sortby_command(command, contents)
        elif command.startswith("print"):
            print_command(command, contents)
        else:
            print("Invalid command: " + command)


if __name__ == "__main__":
    # Check if the spreadsheet file was passed in
    if len(sys.argv) > 1:   
        contents = read_csv(sys.argv[1])
        user_input(contents)
    else:
        print("Needs a spreadsheet file")
