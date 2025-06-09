from stats import *
# stats.py
import sys



def main(): 
    #filepath = '/root/github.com-bootdotdev-bookbot/books/frankenstein.txt'
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]

    book_text = get_book_text(filepath)
    
    words_counted = count_words(book_text)
    #print(f'{words_counted} words found in the document')

    char_counted = count_characters(book_text)
    #print(char_counted)

    formated_counts = format_dict(char_counted)
    #print(formated_counts)
    formated_counts.sort(key=sort_on, reverse=True)
    #print(formated_counts)

    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {filepath}...')
    print('----------- Word Count ----------')
    print(f'Found {words_counted} total words')
    print('---------- Character Count -------')
    for x in formated_counts:
        if x["char"].isalpha() == True:
            print(f'{x["char"]}: {x["num"]}') 


    
main()
