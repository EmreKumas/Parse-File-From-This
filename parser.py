import sys
import os.path


def read_file(file_name, parse_by_string, index_of_wanted_part):
    output_list = []

    with open(file_name, 'r') as file:
        for line in file:
            # Read the line and remove the newline character at the end
            line = line.rstrip('\n\r')

            if parse_by_string in line:
                print(line)

    # Close the file...
    file.close()


if __name__ == '__main__':

    # Checking if the program has run with the CORRECT NUMBER of command-line arguments...
    if len(sys.argv) != 4:
        print("You didn't run the program with the CORRECT NUMBER of command-line arguments!")
        print("Usage: python parser.py file_name parse_by_string index_of_wanted_part")
        exit(-1)

    file_name = sys.argv[1]
    parse_by_string = sys.argv[2]
    index_of_wanted_part = sys.argv[3]

    # Check if that file exists...
    if not os.path.isfile(file_name):
        print("Cannot found file with the filename you provided!")
        exit(-1)

    read_file(file_name, parse_by_string, index_of_wanted_part)
