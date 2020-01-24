# Parse-File-From-This

A simple parser for any text file. Just give the input file, define what you want and get the corresponding output...

## Usage

`python parser.py file_name parse_by_string index_of_wanted_part`

- file_name : the file you want to parse
- parse_by_string : define any text that you want to get in that line
- index_of_wanted_part : each word in the line corresponds to some index, define which word you want by typing the index

## Example Input

<br/>

![img](https://i.ibb.co/7Q45WV5/parser-input.jpg)

For this example, we have the output of the work done by the genetic algorithm. We have 100 different solutions and 100 different average fitness values. But we want to get all average fitness values and plot it in somewhere else. How we do we get it? Yes, by using this parser.

Lets define the parameters...

- file_name : solution_030.txt_100_100_0.5_0.001.txt
- parse_by_string : Average
- index_of_wanted_part : 4

Since I want the numbers that are defined for average fitness values, my parse_by_string will be 'Average'. And, I want the numbers that are indexed at 4(0 is the 'Average', 1 is the 'solution', etc.).

## Example Output

After we run the parser with these parameters, we get the following output text file:

`python parser.py solution_030.txt_100_100_0.5_0.001.txt Average 4`

![img](https://i.ibb.co/5W45DRW/parser-output.jpg)
