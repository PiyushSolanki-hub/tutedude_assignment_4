# tutedude_assignment_4
This repository contains two simple Python scripts demonstrating fundamental file input/output (I/O) operations. The scripts show how to read from, write to, and append data to text files.

Scripts Overview
task1.py
This script demonstrates how to read a text file (sample.txt) and handle potential errors.

It opens and reads sample.txt, printing each line with its corresponding line number.

It includes a try-except block to gracefully handle a FileNotFoundError if sample.txt is not present in the directory.

task2.py
This script is an interactive example of writing, appending, and reading a file (output.txt).

Write ('w'): It first prompts the user for input and writes it to output.txt, overwriting any existing content.

Append ('a'): It then asks for additional text and appends it to the end of the file.

Read ('r'): Finally, it reads the entire updated content of output.txt and prints it to the console.
