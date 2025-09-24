import os

INPUT_FILE = "./10000-common-passwords.csv"
OUTPUT_FILE = "./statistics.csv"
DELIMITER = ","


def delete_existing_output_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Deleted existing file: {filename}")


def process_and_print_lines(input_filename, delimiter):
    try:
        with open(input_filename, "r", encoding="utf-8") as file:
            for line in file:
                elements = line.strip().split(delimiter)
                print(elements)
    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")


delete_existing_output_file(OUTPUT_FILE)
process_and_print_lines(INPUT_FILE, DELIMITER)


