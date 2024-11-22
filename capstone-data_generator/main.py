import os
import argparse
import configparser
from faker import Faker
import multiprocessing
from datetime import datetime
import json
import random

# Initialize Faker for generating random data
fake = Faker()

# Function to generate random data based on schema
def generate_random_data(schema, lines):
    data = []
    for _ in range(lines):
        row = {}
        for key, value in schema.items():
            if value.startswith("int:rand"):
                start, end = map(int, value.split(":")[1][5:-1].split(","))
                row[key] = random.randint(start, end)
            elif value == "timestamp":
                row[key] = datetime.now().isoformat()
            elif value == "str:rand":
                row[key] = fake.name()
            elif value.startswith("["):
                choices = json.loads(value.replace("'", '"'))
                row[key] = random.choice(choices)
        data.append(row)
    return data

# Function to write data to a file
def write_file(path, data):
    with open(path, 'w') as f:
        for row in data:
            f.write(json.dumps(row) + "\n")

# Function to handle file generation with multiprocessing
def generate_files(output_dir, file_name, file_prefix, data_schema, lines, index):
    file_path = os.path.join(output_dir, f"{file_prefix}_{file_name}_{index}.json")
    print(f"Generating file: {file_path}")
    schema = json.loads(data_schema)
    data = generate_random_data(schema, lines)
    write_file(file_path, data)

# Load configuration and parse command-line arguments
def load_config():
    config = configparser.ConfigParser()
    config.read('config/default.ini')
    return config['DEFAULT']

def main():
    # Load default configuration from default.ini
    config = load_config()

    # Setup argparse for command-line arguments
    parser = argparse.ArgumentParser(description="Data file generator")
    parser.add_argument("--file_count", type=int, default=config.getint('files_count'),
                        help="Number of files to generate")
    parser.add_argument("--file_name", type=str, default=config['file_name'],
                        help="Base file name")
    parser.add_argument("--prefix", type=str, default=config['file_prefix'],
                        help="Prefix for the file name")
    parser.add_argument("--path_to_save", type=str, default=config['path_to_save_files'],
                        help="Path where files will be saved")
    parser.add_argument("--multiprocessing", type=int, default=config.getint('multiprocessing'),
                        help="Number of processes to use")
    parser.add_argument("--data_lines", type=int, default=config.getint('data_lines'),
                        help="Number of lines of data per file")
    parser.add_argument("--data_schema", type=str, required=True,
                        help="Data schema for generating random data")

    args = parser.parse_args()

    # Create the output directory if it doesn't exist
    if not os.path.exists(args.path_to_save):
        os.makedirs(args.path_to_save)

    # Use multiprocessing to generate files
    processes = []
    for i in range(args.file_count):
        p = multiprocessing.Process(target=generate_files,
                                    args=(args.path_to_save, args.file_name, args.prefix,
                                          args.data_schema, args.data_lines, i))
        processes.append(p)
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()

    print("All files generated successfully!")

if __name__ == "__main__":
    main()
