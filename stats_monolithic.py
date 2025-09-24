import os

INPUT_FILE = "./10000-common-passwords.csv"
OUTPUT_FILE = "./statistics.csv"
DELIMITER = ","

def monolithic_data_processor(input_file, output_file, delimiter):
    
    if os.path.exists(output_file):
        os.remove(output_file)
        print(f"Deleted existing file: {output_file}")

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            for line in file:
                elements = line.strip().split(delimiter)
                print(elements)
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")



monolithic_data_processor(INPUT_FILE, OUTPUT_FILE, DELIMITER)