def get_num_words(filepath):
    # open a file and set it to a variable
    with open(filepath) as b:
        character_counts = {}
        book_text = b.read()
        book_data = book_text.lower().split()
        word_count = len(book_data)

        for word in book_data:
            for character in word:
                if character not in character_counts:
                    character_counts[character] = 1
                else:
                    character_counts[character] += 1
    return word_count, character_counts

def print_report(filepath):
    num_words, char_list = get_num_words(filepath)
    counts_dict = []
    counts_list = []

    for char in char_list:
        if char.isalpha():
            char_dict = {'char': char, 'count': char_list[char]}
            counts_dict.append(char_dict)

    def sort_on(items):
        return items["count"]
    
    counts_dict.sort(reverse=True, key=sort_on)

    for item in counts_dict:
        counts_list.append(f"{item['char']}: {item['count']}")

    return num_words, counts_list
        
