"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""

import os

def extract_values_and_write(directory: str, output_file: str):
    
    values = []

    for filename in os.listdir(directory):
        # print(filename)
        file_path = os.path.join(directory, filename)
        # print(file_path)
        
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                content = f.read().strip()  
                if content: 
                    values.append(content)  

    with open(output_file, 'w') as output:
        output.write(', '.join(values))  
    print(f"Values written to {output_file}")

if __name__ == "__main__":
    extract_values_and_write('/Users/srajuv/Desktop/Python-GD-Assignments/python part 2/files', 'result90.txt')