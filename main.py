import sys
from stats import print_report  

def main():
    # check for proper tool usage
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        num_words, char_list = print_report(sys.argv[1])

        print(
            f'''
            ============ BOOKBOT ============
            Analyzing book found at books/frankenstein.txt...
            ----------- Word Count-----------
            Found {num_words} total words
            -------- Character Counts -------
            {char_list}
            ============= END ===============
        ''')

main()
