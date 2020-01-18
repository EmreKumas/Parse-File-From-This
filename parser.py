import sys
import os


def read_file(file_name, parse_by_string, index_of_wanted_part):
    output_list = []

    with open(file_name, 'r') as file:
        for line in file:
            # Read the line and remove the newline character at the end
            line = line.rstrip('\n\r')

            # If the desired string is in this line, we split it and put it in output_list with index provided...
            if parse_by_string in line:
                line = line.split()
                output_list.append(line[index_of_wanted_part])

    # Close the file...
    file.close()

    return output_list


def write_to_file(file_name, output_list):
    output_file_name = "parsed_" + file_name
    file = open(output_file_name, 'w')

    for element in output_list:
        file.write("{}\n".format(element))

    # Lastly, we will delete the last line from the file, because it's empty.
    file.seek(file.tell() - 2, os.SEEK_SET)
    file.truncate()

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

    output_list = read_file(file_name, parse_by_string, int(index_of_wanted_part))
    write_to_file(file_name, output_list)
