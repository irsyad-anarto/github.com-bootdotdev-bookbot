def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_characters(text):
    lowercase_text = text.lower()
    counts = {}
    for char in lowercase_text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def get_book_text(filepath):
    with open(filepath) as f:
    # do something with f (the file) here# f is a file object
        file_contents = f.read()

    return file_contents

def format_dict(input_dict):
    formatted_dict = []
    for key, value in input_dict.items():
        temp_dict = {"char" : key, "num" : value}
        formatted_dict.append(temp_dict)
    return formatted_dict

def sort_on(dict):
    return dict["num"]


