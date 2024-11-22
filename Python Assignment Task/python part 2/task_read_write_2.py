"""
Use function 'generate_words' to generate random words.
Write them to a new file encoded in UTF-8. Separator - '\n'.
Write second file encoded in CP1252, reverse words order. Separator - ','.

Example:
    Input: ['abc', 'def', 'xyz']

    Output:
        file1.txt (content: "abc\ndef\nxyz", encoding: UTF-8)
        file2.txt (content: "xyz,def,abc", encoding: CP1252)
"""


def generate_words(n=20):
    import string
    import random

    words = []
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words

def write_files(words):
    
    with open('file_task_4_1.txt', 'w', encoding='utf-8') as file1:
        file1.write('\n'.join(words))
    
    
    reversed_words = words[::-1]

    
    with open('file_task_4_2.txt', 'w', encoding='cp1252') as file2:
        file2.write(','.join(reversed_words))

# Example usage
words = generate_words(20)
write_files(words)
